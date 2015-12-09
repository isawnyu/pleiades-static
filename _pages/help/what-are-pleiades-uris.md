---
copyright: Copyright © 2012-2015 New York University.
created: '2012-02-02'
creators:
- name: Tom Elliott
  path: /author/thomase
layout: helppage
modified: '2015-04-21'
permalink: /help/what-are-pleiades-uris
title: What are Pleiades URIs?
---

#  What are Pleiades URIs?

URI stands for Uniform Resource Identifier. A URI is a string of characters
that is used uniquely to identify a name or a resource on the World-Wide Web.
There is [a formal specification for
URIs](http://tools.ietf.org/html/rfc3986), and Wikipedia also provides [a
helpful article](http://en.wikipedia.org/wiki/Uniform_resource_identifier)
about them.

Pleiades uses a particular type of URI known colloquially as "http URIs" to
identify the three main types of information resources we supply: places,
locations, and names. We promise to [keep these URIs
stable](http://www.w3.org/Provider/Style/URI.html), so that third parties,
like [our Pelagios partners](http://pelagios.dme.ait.ac.at/api/datasets), can
make confident use of them in links, linked data, and other applications.

Here are the basic Pleiades URI patterns (we use regular expressions here in
accordance with [the VOID specification](http://www.w3.org/TR/void/#pattern)):

* places: ^http://pleiades\\\\.stoa\\\\.org/places/(\d+)$ (e.g., [http://pleiades.stoa.org/places/197189](../places/197189))
* names: ^http://pleiades\\\\.stoa\\\\.org/places/(\d+)/(.+)$ (e.g., [http://pleiades.stoa.org/places/314921/carthage](../places/314921/carthage))
* locations: ^http://pleiades\\\\.stoa\\\\.org/places/(\d+)/(.+)$ (e.g., [http://pleiades.stoa.org/places/658494/ruins-of-ancient-church-at-kafr-nabo](../places/658494/ruins-of-ancient-church-at-kafr-nabo))
