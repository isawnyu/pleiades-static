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
RX_SPACES = re.compile(r"\s+")
RX_USERS = re.compile(r"^\[(.+)\]\((.+)\)")
RX_LINK_LIST_DELIM = re.compile(r"\[\s*\!\[Page\]\(http:\/\/pleiades\.stoa\.org/document_icon\.gif\)\s*\]\(http:\/\/pleiades\.stoa\.org\/[^\)]+\)")
BOGUS = ["Joe User", "Anne User"]

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
    logger = logging.getLogger(sys._getframe().f_code.co_name)

    creators = []
    capture = False
    for line in lines:
        if line.startswith("Creators:"):
            capture = True
            creators.append(line[10:])
        elif line.strip() == ""  or line.startswith("Copyright"):
            capture = False
        elif capture:
            creators.append(line)
    # sometimes Copyright slips into preceding line with no spaces
    foo = creators
    creators = []
    punt = False
    for creator in foo:
        try:
            i = creator.index("Copyright")
        except ValueError:
            pass
        else:
            creator = creator[0:i].strip()
            punt = True
        creators.append(creator)
        if punt:
            break
    # cleanup, regularize, and prune
    creators = " ".join(creators).split(",")
    creators = [RX_SPACES.sub(" ", creator.strip()) for creator in creators]
    creators = [creator for creator in creators if creator != ""]


    contributors = []
    capture = False
    for line in lines:
        if line.startswith("Contributors:"):
            capture = True 
            contributors.append(line[14:])
        elif line.strip() == "" or line.startswith("Copyright"):
            capture = False
        elif capture:
            contributors.append(line)
    # sometimes Copyright slips into preceding line with no spaces
    foo = contributors
    contributors = []
    punt = False
    for contributor in foo:
        try:
            i = contributor.index("Copyright")
        except ValueError:
            pass
        else:
            contributor = contributor[0:i].strip()
            punt = True
        contributors.append(contributor)
        if punt:
            break
    # cleanup, regularize, and prune        
    contributors = " ".join(contributors).split(",")
    contributors = [RX_SPACES.sub(" ", contributor.strip()) for contributor in contributors]
    contributors = [contributor for contributor in contributors if contributor != "" and contributor not in creators]

    if '\nHistory\n' in ''.join(lines):
        others = [line for line in lines if RX_REVISION.match(line) is not None]
        others = [RX_REVISION.match(line).groups() for line in others]
    else:
        others = []
    others = ["[{0}]({1})".format(other[0], other[1].replace("http://pleiades.stoa.org", "")) for other in others]
    others = list(set(others))
    others = [other for other in others if other not in creators and other not in contributors]
    contributors.extend(others)

    if len(creators) > 0:
        logger.debug("creators: {0}".format(creators))
        creators = [RX_USERS.match(creator).groups() for creator in creators]
        creators = [{"name": creator[0], "path": creator[1]} for creator in creators if creator[0] not in BOGUS]

    if len(contributors) > 0:
        logger.debug("contributors: {0}".format(contributors))
        try:
            contributors = [RX_USERS.match(contributor).groups() for contributor in contributors]
        except AttributeError:
            oddballs = [contributor for contributor in contributors if RX_USERS.match(contributor) is None]
            oddballs = [{"name": o} for o in oddballs]
            logger.warning("The following contributors did not have associated paths: {0}".format(oddballs))
            contributors = [contributor for contributor in contributors if contributor not in oddballs]
        else:
            oddballs = []
        contributors = [{"name": contributor[0], "path": contributor[1]} for contributor in contributors if contributor[0] not in BOGUS]
        contributors.extend(oddballs)

    return creators, contributors

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
                creators, contributors = get_creators_and_contributors(text_cooked)
                if len(creators) > 0:
                    front_matter['creators'] = creators
                if len(contributors) > 0:
                    front_matter['contributors'] = contributors
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
                copyright += modified_year + " "
                staff_list = ["Tom Elliott", "Sean Gillies"]
                staff = [p["name"] for p in creators if p["name"] in staff_list]
                staff.extend([p["name"] for p in contributors if p["name"] in staff_list])
                logger.debug("staff: {0}".format(staff))
                copyowners = [p["name"] for p in creators if p["name"] not in staff]
                if len(staff) > 0:
                    if int(created_year) < 2009 or int(modified_year) < 2009:
                        copyowners.append("The University of North Carolina at Chapel Hill")
                    if int(created_year) > 2007 or int(modified_year) > 2007:
                        copyowners.append("New York University")
                copyowners.extend([p["name"] for p in contributors if p["name"] not in staff])
                if len(copyowners) == 2:
                    copyright += " and ".join(copyowners)
                elif len(copyowners) > 2:
                    copyright += ", ".join(copyowners[:-1]) + ", and " + copyowners[-1]
                else:
                    copyright += copyowners[0]
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

                #if present, strip topic/folder-related links
                #also, set a flag for later conditional processing
                try:
                    i = len(text_cooked) - 1 - text_cooked[::-1].index("[ ![KML](google_earth_link_14.png) Download KML\n")
                except ValueError:
                    topic = False
                else:
                    topic = True
                    foo = text_cooked
                    text_cooked = []
                    text_cooked.extend(foo[0:i-1])
                    while i < len(foo) and foo[i].strip() != "":
                        i += 1;
                    text_cooked.extend(foo[i:])

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

                # handle topic-specific formatting
                if topic and "Title | Description" in "".join(text_cooked):
                    i = 0
                    while not text_cooked[i].startswith("Title | Description"):
                        i += 1
                    j = i + 1
                    while j < len(text_cooked) and text_cooked[j].strip != "":
                        j += 1
                    link_list = text_cooked[i+1:j]
                    link_list = "".join(link_list)
                    link_list = link_list.replace("---|---", "")
                    link_list = link_list.replace("\n", " ")
                    link_list = RX_SPACES.sub(" ", link_list)
                    link_list = RX_LINK_LIST_DELIM.sub("\n", link_list)
                    link_list = link_list.replace(" | ", "\n: ")
                    link_list = link_list.split("\n")
                    link_list = [line.strip() for line in link_list if line.strip() != ""]
                    link_list = [line + " " if line == ":" else line for line in link_list]   # force kramdown to continue dl in absence of dd content
                    link_list = ["\n" + line if line[0] == "[" else line for line in link_list]
                    link_list = "\n".join(link_list).split("\n")
                    foo = text_cooked
                    text_cooked = foo[:i]
                    text_cooked.extend(link_list)
                    text_cooked.extend(foo[j:])

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
                        text_cooked.append(line if line == ": " else line.strip())

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
