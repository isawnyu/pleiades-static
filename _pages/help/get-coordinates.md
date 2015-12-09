---
contributors:
- name: Brian Turner
  path: /author/bdturner
- name: Sean Gillies
  path: /author/sgillies
copyright: Copyright © 2011-2013 New York University and Brian Turner.
created: '2011-11-09'
creators:
- name: Tom Elliott
  path: /author/thomase
layout: helppage
modified: '2013-02-11'
permalink: /help/get-coordinates
title: I see a map for a place, but how do I get the coordinates?
---

#  I see a map for a place, but how do I get the coordinates?

Coordinate information is stored in Pleiades "location" resources, which are
grouped inside the "place" resources, so you need to drill down.

Pleiades "place resources", e.g.
[http://pleiades.stoa.org/places/108882](../places/108882), are essentially
containers for information about notional places. The maps on each place are
pulling their coordinates from any "location resources" that have been
assigned to that place. You'll see links to these under "In This Context" -->
"Locations". If you click on a location there, you'll see information about
coordinates. This lets us work with places whose locations are contested or
unknown.

These same coordinates are encoded in the alternate KML representations for
each place so that you can visualize Pleiades content in Google Earth and
other software that can read KML files. Look down the place resource page for
a link labeled "KML". The coordinates are also encoded in the alternate JSON
representation for each place. The map for the settlement at le Châtelet de
Gourzon (introduced above) is, in fact, rendered from the data in
[http://pleiades.stoa.org/places/108882/json](../places/108882/json).

You can also download all of our data here:
[http://pleiades.stoa.org/downloads](../downloads). The places tables include
"reprLong", "reprLat" and "reprLatLong" columns which hold the coordinates of
a single representative point for a place. If you'd just like the agreed upon,
single representative latitude and longitude pair for a place, that's the best
data source.

You can read more about how we model place information and what "place",
"location" and "name" resources mean in the context of Pleiades here:
[http://pleiades.stoa.org/places](../places).
