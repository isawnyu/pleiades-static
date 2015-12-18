---
copyright: "Copyright © 2007-2015 Jeffrey Becker, Sarah Bond, Noah Kaye, Adam Rabinowitz, Brian Turner, The University of North Carolina at Chapel Hill, and New York University."
created: '2007-01-01'
creators:
- name: Jeffrey Becker
  path: /author/jbecker
- name: Sarah Bond
  path: /author/sbond
- name: Tom Elliott
  path: /author/thomase
- name: Sean Gillies
  path: /author/sgillies  
- name: Noah Kaye
  path: /author/nkaye
- name: Adam Rabinowitz
  path: /author/arabinowitz
- name: Brian Turner
  path: /author/bdturner
description: "This document describes editorial standards for the creation of clear and complete resources for places, locations, and names."
layout: default
lede: "This document describes editorial standards for the creation of clear and complete resources for places, locations, and names."
modified: '2015-12-18'
permalink: /help/editorial-guidelines
title: "Editorial Guidelines for Places, Locations, and Names"
---

## Conceptual Overview

_Pleiades_ is a gazetteer of ancient _places_. _Pleiades_ _places_ are conceptual entities: the term applies to any locus of human attention, material or intellectual, in a real-world geographic context. A settlement mentioned in an ancient text is a _place_, whether or not it can now be located; an archaeological site is a _place_; a modern city located atop an ancient settlement is a _place_. Basically, any spatial feature that is connected to the pre-modern past and that a human being has noticed and discussed as such between the past and the present is a _place_.

_Places_ in _Pleiades_ can therefore represent areas of fairly intensive human activity (settlement, sanctuary); large-scale geological features known in antiquity (mountains, rivers, lakes); political, social, or cultural constructs like provinces and mining districts; and individual structures, when they have been referred to individually by ancient sources or modern scholars (the Parthenon, the Queen’s Megaron at Knossos, the Basilica Iulia, the House of the Faun).

_Places_ are entirely abstract, conceptual entities. They are objects of thought, speech, or writing, not tangible, mappable points on the earth’s surface. They have no spatial or temporal attributes of their own. A _place_ can exist in name only in an ancient source, without any material correlate; conversely, an archaeological site can exist as a _place without an ancient name.

The spatial aspects of _Pleiades_ _places_ (i.e., latitude and longitude coordinates in space), as well as their ancient and modern names, are addressed through two other conceptual entities: _locations_ and _names_.

_Locations_ in _Pleiades_ connect _places_ to coordinates in space. A _location_ identifies a specific area of interest on the earth's surface that is associated with a _place_ during a particular date range. A _place_ can contain multiple _locations_. _Locations_, on the other hand, are associated with one and only one _place_. Depending on the state of the evidence, the association between _location_ and _place_ may vary in certainty; some _places_, attested by name in ancient sources, may have no associated _location_ at all because modern scholarship cannot pinpoint reliably the ancient site or area in question.

_Names_ in _Pleiades_ are also connected with _places_. A _name_ reflects the identity of a _place_ in human language, not its physical location in the landscape. _Names_ have no spatial coordinates, but they are always annotated with the time period(s) of the textual source(s) in which they are attested. As with _locations_, a single _place_ can have multiple _names_, but an individual _name_ can be associated with one and only one _place_. This is true even if the same sequence of characters is also attested as a _name_ for another _place_; _Pleiades_ treats these "identical" _names_ as separate entities.

### Database Structure

The _Pleiades_ system documents and describes each of these three conceptual entities using a corresponding _information resource_. _Information resources_ are bundles of structured data that are similar in function to records in a database or index cards in a card file. Each _place_ resource contains the _name_ and _location_ resources with which it is associated. This encapsulation is expressed in the layout of information on the _Pleiades_ website, and in the hierarchical structure of the Uniform Resource Identifiers (URIs: web addresses) assigned to each resource. Each _place_ resource has a corresponding web page in _Pleiades_, and each _place_ page links to individual pages for all the _name_ and _location_ resources that have been associated with it.

The structure and implementation of the _Pleiades_ database are described in more detail in the [_Pleiades_ Data Model document](pleiades-data-model).

### About Titles

The _Pleiades_ _information resource_ for each _place_, _location_, or _name_ always includes a title, but each type of entity has different titling conventions. A _place_ may have multiple _names_ at different points in time, and a _name_ may have multiple transliterations, but the _place_ resource and each of the associated _name_ resources receives only one title each. Similarly, each _location_ has only one title, but there are several different types of _location_ in _Pleiades_, and conventions for titling differ between them. Policy and examples for each case are provided below. In general, punctuation (commas, periods, apostrophes) should be avoided wherever possible in titles (so "Arch of Trajan", rather than "Trajan's Arch").

### About Dates

Our places exist independently of time and contain no temporal information themselves. Temporal information is applied to the _locations_ and _names_ with which a _place_ is associated. This approach, which is reflected in the data structure of the corresponding information resources, gives _Pleiades_ users the flexibility necessary to model the known temporal distribution of the individual _names_ for a _place_ and to identify (wherever possible) the age and longevity of the various spatial features that constitute its _locations_. _Pleiades_ uses a heterogenous and growing list of named time periods when assigning individual _location_ and _name_ resources in time.

### About References

__to be added__

## Guidelines for Place Resources

The following editorial conventions are employed in the titling of _place_ resources in _Pleiades_:

### Place Titles

Titles for _place_ resources in _Pleiades_ are always rendered in Roman characters. Transliteration practice is laid out in the _Name Transliteration Guide_.

When appropriate, titles can contain one or more toponyms.

- For every toponym used in the "title" field of the place resource, a corresponding _name_ resource must be attached to the _place_ resource before submitting for review.

- When there is an ancient toponym that can be assigned to a _place_ with full confidence, and that toponym is well-known or appears widely in literature, that toponym should be used in the title of the _place_ resource. Minor variants (e.g., "Aphrodeisias" for "Aphrodisias") registered as _names_ should not be considered for place titles.

- When no ancient toponym can be assigned to the _place_ with full confidence, the modern toponym conventionally associated with the _place_ by historians and archaeologists should be used in the title of the corresponding _place_ resource (e.g. "Franchthi Cave"). Where common, the use of English spellings for modern toponyms in _place_ resource titles are preferred (e.g., "Munich" rather than "München"), but otherwise the most common or native modern language name should be used.

- If the _place_ is a natural feature and is consistently referred to by a compound name in historical sources (e.g. "Olympus Mons"), use the Romanized version of the name as it appears in those sources. In all other cases, Latin feature-type strings and abbreviations ("M.", "fl.", "ins.") are now deprecated, and English terms should be used instead: so "Tiber River" instead of "Tiber fl.", "Chios island" instead of "Chios ins.", "Mount Ida" instead of "Ida M.".

- When multiple toponyms are included in a _place_ title, they must be separated with a slash (“/”) character. When many toponyms are attested for a single _place_, _Pleiades_ users and editors should exercise their best judgment as to how many to include in the title, and in what order. The editors will only in exceptional circumstances approve titles containing more than two toponyms. Preference should be given to the most common toponyms, and those representing distinct linguistic and cultural threads in the history of the _place_. Toponyms used regularly in modern scholarship and general literature are preferred over more obscure ones.

When there is neither an ancient nor a modern toponym firmly associated with the place, a descriptive title using the type of place should be used. These titles may incorporate short statements of spatial proximity. E.g., "Roman Bridge near Twice Brewed" or “Gladiatorial School at Carnuntum”.

## Guidelines for Location Resources

In _Pleiades_, _locations_ provide a link between a conceptual _place_ and specific geographic and temporal coordinates. They can be of three types, each of which must have a spatial geometry (point, polyline, or polygon) and at least one associated chronological period. Each type should be titled in a particular manner, as described below. 

### Representative Locations

A representative point, polyline, or polygon for the _place_ as a whole, including approximations and estimates of centerpoint, extent, perimeter, or area.

#### Title

The title of a _Representative Location_ must reflect the source of the coordinates. When the coordinates are copied from an external data source (like OpenStreetMap or a digitized map), abbreviate the title of the external source and append the word "location". For example:

- "DARMC location"
- "OSM location"
- "DARE location"
- "TAVO location" 

When coordinates are obtained through imagery analysis or data collection in the field, follow a similar pattern for the title (e.g., "GPS location" or "Imagery location").

#### Description

The description for a _Representative Location_ must indicate that the location is "representative", and then go on to summarize the nature and process of collection for the coordinates and other information contained in the _location_ resource. The names of data sources, when abbreviated in the title, should be spelled out in the description for the benefit of new users and third-party consumers of exported data. Some examples: 

- "Representative point derived from an OpenStreetMap node"
- "Polygon representing the perimeter of the archaeological site, derived from an OpenStreetMap way"
- "Representative point derived from GeoNames. Dates after the Barrington Atlas."

#### Dates

The date range for a _location_ of this type should include all periods for which evidence of significant human activity can be associated with the site. Archaeological evidence is the preferred source of such dates; however, literary and documentary testimony of existence or activity may also serve (and sometimes may be the only option). Care should be exercised whenever possible to avoid asserting activity in a period based solely on an antiquarian collection of placenames (e.g., the Suda or Stephanus of Byzantium). Incomplete date ranges are acceptable when data available to the editor and contributor are insufficient. It is preferable to get a correct, if incomplete, record published sooner rather than deferring publication for an extended period of time pending the acquisition of additional information.

#### References

When geometry has been copied from an external data source, whether already digital or freshly digitized, the original source of the data must be cited. The citation type to use is "Cite As Data Source". The source of date information must also be cited. When following published, modern argument appearing in secondary literature, use the simple "Cite" citation type. When inferring date from an ancient literary or documentary source, use the "Cite as Evidence" citation type.

#### Retraction rules

__TBD__

### Associated Modern Location

A point, line, or polygon for a modern settlement or physical feature associated with an ancient _place._ When the precise location of an ancient cultural site is unknown (or data is presently unavailable), a nearby or associated modern settlement may be used (especially when that settlement's name is often used in the scholarly literature as a proxy title for the ancient site). Similarly, in the absence of solid geophysical and geoarchaeological data for the location of an ancient physical feature, an _Associated Modern Location_ can be used. 

NB: _Associated Modern Locations_ should not be used to link _Pleiades_ content to external, presentist gazetteers like [GeoNames](http://geonames.org). A new citation type ("Related To") has been added to references and should be used at the _place_ level for this purpose.

#### Title

The title of an _Associated Modern Location_ must follow the titling guidance laid out above for _Representative Locations_, with the following additions. The title for a cultural location should have a string like "of modern \[Romanized modern placename\]" appended. The title of a physical feature should have a string like "of \[Romanized modern placename\]" appended. ~~The title should be "Location of modern settlement of \[romanized name as it appears in OSM or GeoNames\]".~~

#### Description

The description for an _Associated Modern Location_ must indicate that it is an associated modern location, and also summarize the nature and process of collection for the coordinates and other information contained in the location resource in the same manner as for _Representative Locations_. Some examples: "Polygonal geometry representing the perimeter of the modern commune of Crecy, which is thought to be associated with the ancient site of Cremium. Geometry derived from an OpenStreetMap way;" "Point marking the modern summit of Gebel Musa, which is identified with the ancient Tiberius Mons. Point derived from an OpenStreetMap way."

#### Dates

For cultural features, the date range for a _location_ of this type should begin with the earliest phase of the modern settlement presently known or available to the contributors and editors and continue to the present. For natural features (rivers, lakes, mountains, coastlines, etc.), even when there is evidence that those features were _places_ in antiquity, the date range should be "modern". There have been substantial geological changes between antiquity and the present, and the location of a river or lake today is often different from its location in antiquity.

#### References

__TBD__

#### Retraction Rules

__TBD__

### Archaeological Location

A representative point, line, or polygon for a specific monument or feature of an ancient site, such as an aqueduct, tunnel, open square, public building, etc. Note that geometry associated with the modern extent of an archaeological area or preserve should be treated as an _Associated Modern Location_.

#### Title

Titles of _Archaeological Locations_ must begin with the same conventions outlined above for _Representative Locations_ (e.g., "OSM Location"). Then a string identifying the feature must be added. For example: "BAtlas Location of the Athenian Agora" or "GPS Location of the extant spans of the aqueduct". The title should provide clear, concise descriptive information about the coordinates chosen: "Centerpoint of the Athenian Agora"; "of the North end of aqueduct"; "of the present-day span of bridge". When the feature has a commonly used proper name, the title should employ it (e.g., "OSM Location of the Library of Celsus"). When a commonly used modern proper name is seen to be erroneous or otherwise misleading (e.g., when a tomb is imaginatively assigned to a famous historical figure), contributors and editors may choose to relegate this information to the "description" field on the location or even the "details" field on the place, and add the words "so-called," surround the proper name in quotation marks, or otherwise caveat the information. This preserves searchability, but avoids specious repetition of incorrect information

#### Description

__TBD__

#### Dates

For _locations_ of this type and the next, the associated periods should begin with the date of the feature's creation and continue to its abandonment. This will not necessarily be clear-cut, since some buildings were active parts of the landscape even after they had fallen into ruin, and others were transformed but remained continually in use into the modern period (for example, the Hephaisteion in Athens, which was used as a church until the 20th century). When in doubt, provide at a minimum the period during which the feature was created.

#### References

__TBD__

#### Retraction Rules

__TBD__

Usually, the description field for _Representative and Associated Modern Locations_ will reflect only information about the coordinates themselves (scale, source, reason for choice, etc.), since information about the _place_ is provided in the main Place page. The description field for _Archaeological Locations_, however, may also include brief descriptive information about the things they represent (an aqueduct, a temple).

## Name Resources

A single _place_ can have many _names_ over time, or may be called different _names_ by different groups: [_Ephesus_](http://_Pleiades_.stoa.org/places/599612/?searchterm=ephesus_), for example, has also been known as Arsinoe, Afsis, and Aya Soluk, among others.

![](media/image02.png)

The __title__ for a _Pleiades_ _place_ is usually its Roman-period Romanized (Latin) _name. _

![](media/image03.png)

Using the example from above, this would be Ephesus. It is useful to associate a _place_ with other _names_ by which it is or has been known because it makes it easier for users working on different periods or from various geographic regions to find _places_. It also helps to connect references to _places_ in textual sources to _Pleiades_ records.

Instructions for adding a _name_ to a _place_ in _Pleiades_, with video tutorial, can be found here: [_http://_Pleiades_.stoa.org/help/how-to-add-a-new-name-resource_](http://_Pleiades_.stoa.org/help/how-to-add-a-new-name-resource). A few formatting clarifications are offered below. For a model for the structure of alternate _names_ and their relation to time periods, see the site of Chersonesos in Crimea: [_http://_Pleiades_.stoa.org/places/226564_](http://_Pleiades_.stoa.org/places/226564). The examples below are derived from the Byzantine-period names for Chersonesos.

-   The primary form of a new _name_ should be its unaccented, Romanized version (any accented or alternate Romanized transliterations should follow as a comma-separated list).

    -   E.g. _Romanized name_: Cherson, Kherson

-   Wherever possible, the _name_ should be supplied in the "name as attested" field in its original language and script, using UTF-8 Unicode encoding ([_see here for an explanation of Unicode and UTF-8_](http://en.wikipedia.org/wiki/UTF-8)). This is usually possible using system keyboards to type directly into your browser, but be careful when cutting-and-pasting from other documents or webpages. Provide this information under the "Transcription" tab and provide an identification of the original language and script using the pull-down menu. The more versions of a _name_ there are in _Pleiades_, the easier it will be to discover the information and associate it with references in other texts -- so please try to provide a version in the original language for each non-Latin entry.

    -   E.g. _Name as attested_: Χερσών, Greek (ancient)

    -   NB: if the language or script of the attested _name_ is not present in the pull-down menu, please submit a request for the addition of that language through the _Pleiades_ Feedback page

-   Unlike a _location_, for which there may only be archaeological evidence, a _name_ MUST be attested in, or able to be inferred from, a textual source; therefore a record for a _name_ should always have at least one reference (of type "Cites as evidence") to a textual source in which it is attested. When the _name_ is ancient, attestations should also be ancient: in most cases, modern scholarship should only be cited as evidence for an ancient _name_ if it involves the primary publication of ancient written sources like coins or inscriptions.

    -   E.g. _Cites As Evidence_: [_Procopius, De bellis, 8.5.27_](http://data.perseus.org/citations/urn:cts:greekLit:tlg4029.tlg001.perseus-grc1:8.5.27)

-   A _name_ MUST also always be associated with one or more temporal attestations; at a minimum, it should be associated with the period during which the primary textual source that mentions it was created (or, if the textual source is clearly referring to an earlier time -- "in the time of Peisistratus, it was called X" -- to the period with which the textual source associates it).

    -   E.g. _Temporal attestations*: Late Antique (AD 300-AD 640) (confident)

