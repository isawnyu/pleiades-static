---
copyright: Copyright © 2014 New York University.
created: '2014-11-17'
creators:
- name: Tom Elliott
  path: /author/thomase
layout: helppage
modified: '2014-11-17'
permalink: /help/pleiades-identifiers-place-numbers
title: Pleiades Identifiers (place numbers)
---

#  Pleiades Identifiers (place numbers)

This document describes the various identifier schemes that have been used for
Place Resources in Pleiades over the lifetime of the project. It also provides
information about how data using one set or another of legacy identifiers can
be "crosswalked" to the current, stable Uniform Resource Identifiers that are
used throughout the site today.

## Current Identifier Scheme

### Uniform Resource Identifiers (URIs)

Pleiades identifies each of its Place Resources with a Uniform Resource
Identifier (URI). This identifier scheme and its use is fully documented in a
separate document entitled "[What are Pleiades URIs?](what-are-pleiades-uris
"What are Pleiades URIs?" )".

### Pleiades IDs

The URIs incorporate a component known as a "Pleiades ID." Each Pleiades ID is
a string unique to the container at http://pleiades.stoa.org/places/. When
concatenated to that URL it produces the permanent URIs of objects in the
Pleiades system (like '148107' -> 'http://pleiades.stoa.org/places/148107').
Bare Pleiades IDs are used in some third-party systems for tagging purposes,
e.g., in Flickr machine tags.

Legacy Identifier Schemes

There are two earlier identifier schemes, now both deprecated, that were used
during earlier phases of the project.

### Feature IDs

The "feature id" is our oldest legacy identifier and is formatted like
"batlas-MM-TT-RR" where MM is the map number, TT is the table number within
the map directory, and RR is the row number within the table.

### BAtlas IDs

The "batlas id" is formed by normalizing to ASCII the map labels for a given
place (spaces replaced with hyphens) and concatenating "-MM-GG" where MM is
the map number and GG is the grid cell in lower case. All BAtlas IDs created
by the project were released online in machine-readable form at
<http://www.atlantides.org/batlas/>, including human-readable PDF and HTML
versions for manual reference.

## Conversion

Datasets that contain legacy identifier schemes can be programmatically and
reliably updated (cross-walked) to Pleiades IDs and URIs. A complete machine-
readable concordance for this purpose (in comma-separated-values -- i.e. "CSV"
-- format) between feature IDs, BAtlas IDs, and Pleiades IDs may be downloaded
at [http://www.atlantides.org/downloads/pleiades/batlasids-2011.tar.gz](http:/
/www.atlantides.org/downloades/pleiades/batlasids-2011.tar.gz).
