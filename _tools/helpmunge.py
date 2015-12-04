"""
helpmunge

munge captured Pleiades help files into something jekyll can handle
"""

import argparse
import difflib
from functools import wraps
import logging
import os
import sys
import traceback

import dateutil.parser as dateparser
import regex as re
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

DEFAULTLOGLEVEL = logging.WARNING
RX_HEADING = re.compile(r'^#\s+(.*)$')
RX_REVISION = re.compile(r'^\s+\*\s+Edited by \[(.+)\]\((.+)\) on (.+)\s*$')

def arglogger(func):
    """
    decorator to log argument calls to functions
    """
    @wraps(func)
    def inner(*args, **kwargs): 
        logger = logging.getLogger(func.__name__)
        logger.debug("called with arguments: %s, %s" % (args, kwargs))
        return func(*args, **kwargs) 
    return inner    


def get_yamlfm(f):
    """ 
    get jekyll-style yaml front matter from a file object
    h/t: http://stackoverflow.com/a/25816324
    """
    pointer = f.tell()
    if f.readline() != '---\n':
        f.seek(pointer)
        return ''
    readline = iter(f.readline, '')
    readline = iter(readline.__next__, '---\n')
    return ''.join(readline)

def get_title(lines: list):
    logger = logging.getLogger(sys._getframe().f_code.co_name)

    try:
        heading = [line for line in lines if line.startswith('# ')][0]
    except IndexError:
        raise RuntimeError("Failure parsing initial heading")
        return None
    else:
        title = RX_HEADING.match(heading.strip()).group(1)
        logger.debug("got heading: '{0}'".format(heading))
        return heading, title

def make_permalink(source: str):
    if os.path.sep in source:
        parts = os.path.basename(source)
    else:
        parts = source
    parts = parts.lower().split('.')
    parts = '-'.join(parts[:-1]).split()
    return '-'.join(parts)

def get_creators_and_contributors(lines: list):
    return "Mutt and Jeff"

def get_dates(lines: list):
    logger = logging.getLogger(sys._getframe().f_code.co_name)
    line = [line for line in lines if line.startswith("Last modified ")][0]
    modified = line[14:].strip()
    logger.debug(modified)
    modified = dateparser.parse(modified).strftime("%Y-%m-%d")
    if '\nHistory\n' in ''.join(lines):
        line = [line for line in lines if RX_REVISION.match(line) is not None][-1]
        created = RX_REVISION.match(line).group(3)
        created = dateparser.parse(created).strftime("%Y-%m-%d")
    else:
        created = None
    return created, modified

def get_tags(lines: list):
    return None

def main (args):
    """
    main functions
    """
    logger = logging.getLogger(sys._getframe().f_code.co_name)

    for fn in args.filenames:
        logger.debug("processing {0}".format(fn))

        # get file content
        with open(fn, 'r') as f:
            front_matter = get_yamlfm(f)
            text_raw = f.readlines()
        if front_matter != '':
            logger.warning(
                "YAML frontmatter already found in {0}; skipping".format(fn)
                )
        else:
            text_cooked = text_raw

            # generate front matter for jekyll
            try:
                heading, title = get_title(text_cooked)
            except RuntimeError as err:
                logger.error("{0} from {1}; skipping".format(err, fn))
            else:
                front_matter = {
                    'title': title,
                    'layout': 'default',
                    'permalink': args.permalink_prefix + make_permalink(fn),
                }
                creators = get_creators_and_contributors(text_cooked)
                if creators is not None:
                    front_matter['creators'] = creators
                created, modified = get_dates(text_cooked)
                if created is not None:
                    front_matter['created'] = created
                if modified is not None:
                    front_matter['modified'] = modified
                if created is None and modified is None:
                    modified = os.path.getmtime(fn)
                    modified = datetime.datetime.fromtimestamp(modified).strftime("%Y-%m-%d")
                    front_matter['modified'] = modified
                copyright = "Copyright © "
                modified_year = modified.split("-")[0]
                if created is not None:
                    created_year = created.split("-")[0]
                    if created_year != modified_year:
                        copyright += "{0}-".format(created_year)
                copyright += modified_year
                copyright += " The University of North Carolina at Chapel Hill"
                if int(modified_year) > 2007:
                    copyright += " and New York University"
                copyright += "."
                front_matter['copyright'] = copyright
                subject = get_tags(text_cooked)
                if subject is not None:
                    front_matter['subject'] = subject
                front_matter = dump(
                        front_matter, 
                        Dumper=Dumper, 
                        default_style=None,
                        default_flow_style=False,
                        width=1000,
                        allow_unicode=True)


                #strip all lines before the first heading (Plone breadcrumbs)
                i = text_cooked.index(heading)
                logger.debug("heading index: {0}".format(i))
                text_cooked = text_cooked[i:]

                # strip History and Document actions from the end of the document
                omit = True
                try:
                    i = len(text_cooked) - 1 - text_cooked[::-1].index("History\n")
                except ValueError:
                    try:
                        i = len(text_cooked) - 1 - text_cooked[::-1].index("##### Document Actions\n")
                    except ValueError:
                        omit = False
                if omit:
                    logger.debug("history index: {0}".format(i))
                    text_cooked = text_cooked[:i]

                # strip Plone byline and dateline
                foo = text_cooked
                text_cooked = []
                omit = False
                for line in foo:
                    if (
                        line.startswith("Creators: ") 
                        or line.startswith("Contributors: ")
                        or line.startswith("Copyright ")
                        or line.startswith("Last modified ")
                        or line.startswith("tags: ")
                        ):
                        omit = True 
                    elif omit and line.strip() == "":
                        omit = False
                    if not omit:
                        text_cooked.append(line)

                # clean up extra blank lines
                foo = text_cooked
                text_cooked = []
                blanks = 0
                for line in foo:
                    if line.strip() == "":
                        blanks += 1
                    else:
                        blanks = 0
                    if blanks < 2:
                        text_cooked.append(line.strip())

                text_raw = "".join(text_raw)
                text_cooked = "\n".join(text_cooked)
                if text_cooked != text_raw:
                    os.rename(fn, fn+'.bak')
                    with open(fn, 'w') as f:
                        f.write("---\n{0}---\n\n{1}".format(front_matter, text_cooked))
                    logger.info("wrote updates to {0}".format(fn))

if __name__ == "__main__":
    log_level = DEFAULTLOGLEVEL
    log_level_name = logging.getLevelName(log_level)
    logging.basicConfig(level=log_level)

    try:
        parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument ("-l", "--loglevel", type=str, help="desired logging level (case-insensitive string: DEBUG, INFO, WARNING, ERROR" )
        parser.add_argument ("-v", "--verbose", action="store_true", default=False, help="verbose output (logging level == INFO")
        parser.add_argument ("-vv", "--veryverbose", action="store_true", default=False, help="very verbose output (logging level == DEBUG")
        parser.add_argument ("-p", "--permalink_prefix", type=str, default="", help="path prefix for permalinks")
        parser.add_argument("filenames", nargs='+', help="name(s) of files to convert")
        # example positional argument:
        # parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
        args = parser.parse_args()
        if args.loglevel is not None:
            args_log_level = re.sub('\s+', '', args.loglevel.strip().upper())
            try:
                log_level = getattr(logging, args_log_level)
            except AttributeError:
                logging.error("command line option to set log_level failed because '%s' is not a valid level name; using %s" % (args_log_level, log_level_name))
        if args.veryverbose:
            log_level = logging.DEBUG
        elif args.verbose:
            log_level = logging.INFO
        log_level_name = logging.getLevelName(log_level)
        logging.getLogger().setLevel(log_level)
        if log_level != DEFAULTLOGLEVEL:
            logging.warning("logging level changed to %s via command line option" % log_level_name)
        else:
            logging.info("using default logging level: %s" % log_level_name)
        logging.debug("command line: '%s'" % ' '.join(sys.argv))
        main(args)
        sys.exit(0)
    except KeyboardInterrupt as e: # Ctrl-C
        raise e
    except SystemExit as e: # sys.exit()
        raise e
    except Exception as e:
        print("ERROR, UNEXPECTED EXCEPTION")
        print(str(e))
        traceback.print_exc()
        os._exit(1)
