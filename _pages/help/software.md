---
copyright: Copyright © 2011-2013 New York University.
created: '2011-10-24'
creators:
- name: Tom Elliott
  path: /author/thomase
layout: helppage
modified: '2013-02-11'
permalink: /help/software
title: Pleiades Software Components
---

#  Pleiades Software Components

Information about the open-source software that powers Pleiades.

The OWSLib Python package is for working with OGC W*S protocols. Pleiades does
not use it.

The GeoJSON format is employed internally and in JSON representations of
Locations and Places.

We've used OpenLayers in the past (and have contributed code and ideas to the
project), we use Google Maps currently, and we may return to OpenLayers. We've
tried to do mapping in a declarative style rather than an procedural style,
designing KML representations of places that allow us to switch javascript
APIs easily.

Sean Gillies started the [OWSLib](http://trac.gispython.org/lab/wiki/OwsLib)
project, but it is now carried forward by programmers at Natural Resources
Canada and the British Atmospheric Data Center.

[GeoJSON](http://geojson.org/), the data format, has some roots in the
Pleiades project and Sean was one of the authors of the specification.

[Shapely](http://trac.gispython.org/lab/wiki/Shapely) is a direct product of
Pleiades. It enjoys crucial contributions from other programmers.

[Rtree](http://trac.gispython.org/lab/wiki/Rtree) is also a direct product of
Pleiades. It is now largely the work of open source LiDAR software developer,
Howard Butler (of [libLAS](http://liblas.org/)), and bio-informatics
programmer, Brent Pederson (University of California, Berkeley).

We're very proud to be sharing code and formats across institutions and
application domains.
