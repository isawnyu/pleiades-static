---
contributors:
- name: Sean Gillies
  path: /author/sgillies
- name: Jeffrey Becker
  path: /author/jbecker
- name: Stefano Costa
  path: /author/scosta
- name: Adam Rabinowitz
  path: /author/arabinowitz
- name: Sarah Bond
  path: /author/sbond
- name: Brian Turner
  path: /author/bdturner
- name: Scott Vanderbilt
  path: /author/sarcanon
- name: Noah Kaye
  path: /author/nkaye
- name: Ryan Horne
  path: /author/rmhorne
copyright: Copyright © 2015 New York University, Jeffrey Becker, Stefano Costa, Adam Rabinowitz, Sarah Bond, Brian Turner, Scott Vanderbilt, Noah Kaye, and Ryan Horne.
created: '2015-04-21'
creators:
- name: Tom Elliott
  path: /author/thomase
layout: helppage
modified: '2015-04-21'
permalink: /help/reference-attributes-of-places
title: 'Reference: Attributes of Places'
---

#  Reference: Attributes of Places

A list of every attribute (field) in a Pleiades place resource, complete with
definition and editorial guidelines for each.

Attributes are arranged as they appear on the tabs in the "edit" view (i.e.,
the "add place" form).

### "Default" tab:

Attribute | Definition and guidelines
---|---
Title | **Required: **A short title for the place record, suitable for
listings, search results, and other summaries. The following guidelines apply:

* Titles are always rendered in Roman characters.
* When there is an ancient toponym that can be assigned to a place with full confidence, that toponym should be used in the title of the place resource.
* When no ancient toponym can be assigned to the place with full confidence, the modern toponym conventionally associated with the place by historians and archaeologists should be used.
* Multiple toponyms may be separated by a slash, but keeping the title short enough to be useful in a listing is important, so alternate names and minor variants may be omitted.
* Note that all toponyms appearing in a place title must also be fully recording using subordinate "name" resources for each.
* When there is neither an ancient nor a modern toponym firmly associated with the place, a descriptive title using the type of place should be used. These titles may incorporate short statements of spatial proximity. E.g., "Roman Bridge near Twice Brewed" or “Gladiatorial School at Carnuntum”
* Where the appropriate title for a place is the same as the title of a related place of a different type (e.g., a settlement on an island of the same name), a short English-language gloss of the type may be appended in parentheses, as in "Chios (island)".
Description | **Required: **A concise account of the place in question,
preferably no more than 280 characters in length. The purpose of the
description is to aid users in identifying a place of interest and, in
particular, disambiguating multiple, same-titled entries in a search result
list. When an ancient name appears in the title, the associated modern name
should appear in the description.
Place type | **Required: **Choose one or more appropriate terms from the
Pleiades Place Type vocabulary. Remove the default value of "unknown".
Makes a connection with | If the place described falls within a larger place
or space (e.g., a temple within a city or a settlement on an island), use this
attribute to indicate the next larger place.
Initial provenance | Original publication context for this place resource. New
resources created through the web interface will be given the value "Pleiades"
and there is normally no reason to change it. If, however, you wish to copy
information verbatim from another reference resource, please contact
pleiades.admin@nyu.edu for guidance before proceeding.
Change note | Each time you save the record, make a brief descriptive entry
here indicating what was added or changed. This information will be stored in
the record history.

### "References" tab:

In accordance with standard scholarly practice, the [Pleiades Citation
Policy](../docs/policies/citation-policy "Citation Policy" ) "mandates
appropriate citation of primary and secondary sources for all content". The
"References" tab on the edit view provides a mechanism for this practice. All
materials, whether published in print or online, that were used to create and
inform the place record must be cited here. The "add reference" widget
provides a repeatable form (one for each cited reference) to structure the
citations. Recording of the following attributes is facilitated by the form:

Attribute | Definition and guildelines
---|---
Reference identifier | **Required: **A unique identifying number or
alphanumeric string for the item being cited. Wherever possible, this
identifier should be a Uniform Resource Identifier (URI), i.e., a stable web
address.

* If the item in question is available online (e.g., via JSTOR), the "stable URL", "permalink" or similar address must be entered in this field.
* If the item is not itself available online, but the item is bibliographically cataloged (e.g., at WorldCat), then the "stable address" or "permalink" for the bibliographic record must be entered in this field.
* If no URI for the item or a corresponding bibliographic record can be found, please email pleiades.admin@nyu.edu with a complete bibliographic citation so that it can be added to the Pleiades Zotero library, which will create a URI that can be used in this field.
Specific citation | **Required: **A human-readable citation of the work in
question. If the reference identifier (above) makes use of JSTOR, WorldCat, or
the Pleiades Zotero Library, then a short-form citation including the last
name of the first author and the year of publication may be used (along with
page or item numbers, if appropriate). Otherwise, a long-form citation should
be used, following [the conventions of the _American Journal of
Archaeology_](http://www.ajaonline.org/submissions/references) (omit italics).
Citation type | **Required: **Pleiades provides several "citation types" that
are to be used in order to indicate the function of an individual citation
vis-à-vis the place record. The following types are appropriate for place
records:

* "See further": item cited specifically treats the place in question as its primary topic and is a good resource for additional information
* "See also": item cited incidentally treats the place in question and is a good resource for additional information, but has some other primary topic (e.g., a Wikipedia article about a modern city that includes a subsection addressing relevant ancient history or archaeology)
* "Related": item cited treats a related or co-incident place. This citation type is normally used for references to other gazetteers, e.g., GeoNames and DARMC.
* "Citation": item cited was used and/or is quoted in the material presented in the place resource, but for some reason is not deemed to be a good resource for additional information (use of this type should be justified to the editors in lieu of "see further" or "see also".
Other citation types (e.g., "Data Source" and "Evidence" are not appropriate
for use on place resources.

### "Categorization" tab

Detailed help is to be added. There are no required entries on this tab.

### "Ownership" tab

_Pleiades_ automatically captures the usernames of individuals who add and
edit place resources, adding them to appropriate fields on this form. If other
individuals have assisted in the creation or modification of a place resource
(e.g., through conversation or email exchange), they must be credited by
adding their _Pleiades_ usernames (preferred) or plain-text full names (if
unwilling to join Pleiades for the purpose) in the "Creators" or
"Contributors" lists, as appropriate. Note that only individuals referenced
here by _Pleiades_ username will be indicated on the [_Pleiades_
Credits](http://pleiades.stoa.org/credits) page.

If an automatically added username needs to be removed, or if the primary
ownership of the resource needs to be changed, please send an email to
pleiades.admin@nyu.edu explaining the situation and including the URI of the
place resource in question.

###  "Details" tab

This tab provides a rich-text entry field for a "details" attribute that may
be as long or as short as the creators, contributors, and editors deem
necessary. Appropriate contents include, but are not limited to: specific
information about the history and archaeology of the place; the precise dates
of its construction, occupation, or destruction; the person or people who
built it; what it was used for; when it was excavated, and the like.
Difficulties of identifying attestations in ancient literature with extant
archaeological remains are especially useful.

### Names and Locations

In Pleiades, "names" (modern or ancient) and "locations" (coordinates and
associated data) are separate resources, subordinate to individual place
resources. Their attributes are described in separate reference documents.
