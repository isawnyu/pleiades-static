---
contributors:
- name: Sean Gillies
  path: /author/sgillies
copyright: Copyright © 2011-2013 New York University.
created: '2011-11-02'
creators:
- name: Tom Elliott
  path: /author/thomase
layout: helppage
modified: '2013-02-11'
permalink: /help/modern-names
title: Does Pleiades record modern names?
---

#  Does Pleiades record modern names?

Yes we do, and here's how to search for them, add them, and find them in the
downloads files.

Pleiades names should be associated with time periods. You'll see the
associated time periods summarized on the names listing on the place resource
page and also on the individual name resources pages. Whenever a contributor
[adds a new name](../docs/getting-started#adding-a-new-modern "Getting
Started" ), they should indicate the time period(s) during which the name is
attested or thought to have been in use using the appropriate combo box on the
edit form. Modern names for the sites themselves can also be added; there is a
"modern" time period defined for this purpose. Names of nearby modern villages
or towns, first-order administrative divisions and other descriptions of the
location of a place should be added to the "description" or "details" field on
the place resource (or on a "location" resource), not as a modern name.
Editors will check for this before publishing new resources. Users of the
[Pleiades download files](../downloads "Data for download" ) will find the
time period information in the "timePeriodsKeys" field of the CSV "names"
file.

Note that most of the "modern names / locations" recorded in the_ Barrington
Atlas Map-by-Map Directory_ are *not* currently recorded as names in Pleiades.
Rather, they've been added as notes to our "details" field on the place
resource. This is because the _Barrington_ used a single column in the
directory table that doesn't unambiguously differentiate between the actual
modern name of a site, the modern name of the nearest village, the first-order
administrative division containing the site, etc. The details field is fully
searchable, so entering a modern name in the Pleiades search box will turn up
the corresponding Pleiades place resource provided that the Barrington
registered that form of the modern name. Users of the Pleiades download files
will find the original _Barrington Atlas_ "modern name / location" strings in
the "geoContext" field in the CSV "places" file.
