---
contributors:
- name: Tom Elliott
  path: /author/thomase
copyright: Copyright © 2011-2015 New York University.
created: '2011-10-14'
creators:
- name: Sean Gillies
  path: /author/sgillies
layout: helppage
modified: '2015-04-21'
permalink: /help/technical-intro-places
title: Technical Introduction to Places
---

#  Technical Introduction to Places

What are these places and how are they related to names and locations?

### The Concepts

A _Place_ is a geographical and historical context for _Names_ and
_Locations_. Places may have within their core some features of the physical
world – a sea, a bay, a river, a mountain range, a pass, a road, a settlement,
or an ethnic region – but their primary quality is that, in the words of Yi-fu
Tuan [1], they are constructed by human experience. Places may be no larger
than a family dwelling or as big as an empire, be temporally enduring or
fleeting. They may expand, constract and evolve over time. A place may be
unnamed, unlocated, falsely attested, or even mythical.

A _Location_ is a current or former, concrete spatial entity. The midline of a
river channel is a location. The center of a bridge's span is a location. The
perimeter of a walled settlement is a location. Every location belongs to a
place. The highest point of a mountain summit, for example, would be a
location while the entirety of the mountain: its faces, ridges, couloirs, and
forested slopes – and its significance in human history – would be the place
context. The location entitled "[Temple of
Vesta](../../../places/423025/temple-of-vesta)" is but a small part of its
context, [Rome](../../../places/423025/), while the place entitled "[Hafir far
west of Araba](../../places/963101101)" provides only the barest semi-
anonymous context for its sole desert waterhole location.

A _Name_ is a current or former, abstract textual entity. Like a location, a
name belongs to a place. The [Πάπρημις](../../../places/730136/) of Herodotus
2.59 is one of many with no known locations in the same place. At the other
end of the spectrum, [Ἀφροδισιάς](../../../places/638753/aphrodisias) belongs
to a place rich in locations and names.

These Pleiades concepts are somewhat different from those of other conceptual
systems in the cultural heritage and geographic information domains. The
entity of the [CIDOC Conceptual Reference Model](http://www.cidoc-crm.org/)
(CRM) labeled _E53 Place_, which

> ... comprises extents in space, in particular on the surface of the earth,
in the pure sense of physics: independent from temporal phenomena and matter,

is almost exactly equivalent to the Pleiades concept of _Location_. The
Pleiades _Place_ has no single equivalent entity in the CRM. Many places are
localized (settlements, stations, temples and monuments) and have much in
common with the CRM's _E27 Site_. Others like ethnic territories, areas of
centuriation, or mining districts are rather different.

The concept of _Feature_ in the [OGC/ISO 19101
system](http://www.opengeospatial.org/ogc/glossary/f) on which many enterprise
GIS systems are founded overlaps with both Pleiades _Location_ and to a lesser
degree _Place_. Pleiades _Names_ are nothing like ISO 19101 _Features_ and, as
entities in their own rights, are much more than simple feature attributes.

### The Objects

Instances of the Pleiades _Location_, _Name_, or _Place_ entities are
maintained in a database and come to life (so to speak) as needed as _objects_
in the Pleiades web application. The relationship depicted with a line and a
filled diamond between a place object and a location or name object in the
abridged Unified Modeling Language (UML) diagram below is _containment_.

![entities.png](../../../images/entities.png/image_large)

We often say that place objects are _parents_ and their location and name
objects are their _children_. Time periods for which an instance is attested
to be contained (or to be present in a particular context) are modeled as
attributes of name and location objects. Place objects may relate to or be
geographically connected with other place objects in the non-containing way
depicted with a dashed line above.

Every object has a short name (or_ id_) unique within its containing object.
The container for places is itself an object and its id is "places". Our
convention is that ids contain only lowercase letters of the Latin alphabet,
numbers, and dashes. Places have numerical ids such as "1043", those of
locations are derived from their titles ("barrington-atlas-location", in many
cases, or "castellum"), and the ids of names are formed by transliteration of
their attested spelling ("ad-fines", for example).

Easy disambiguation and unique identifiers are properties of this object
model. There are many instances of "Alexandria" names in the ancient world.
The object with id "alexandria" in the context of place "727070", or
places["727070"]["alexandria"] in a notation like that of the Python or
Javascript programming language syntax, is distinguished from another
"alexandria" object in the context of place "59669"
(places["59669"]["alexandria"]).

The other important aspect of an object's existence is _workflow state_.
Pleiades has a simple publication workflow that keeps _drafting-state_ objects
semi-private and protects _published-state_ objects against corruption.

### The Web

Pleiades users do not interact directly with the objects described above. The
interface through which researchers and the public (including machine users
like web crawlers) access our information follows the architecture of the
World Wide Web [2]. Every instance of a Pleiades entity has a corresponding
_Resource_ on the web. The resource is identified using a _Uniform Resource
Identifier_ (URI) that maps to object names in their containment context. The
resource corresponding to the object places["727070"]["alexandria"] is
identified by and addressed with the URI [http://pleiades.stoa.org/places/7270
70/alexandria](../../../places/727070/alexandria).

In other words: Pleiades provides a web page for every place, name, and
location. The content of these pages are generated for a user from objects
stored in the database, filtered according to their workflow state and the
user's roles. Reviewers get a somewhat richer view than authenticated users,
who in turn get to see more than anonymous users.

Pleiades places are thoroughly crawled and indexed by search engines of the
web and can be found readily via queries like
"[aphrodisias+pleiades](http://google.com?q=aphrodisias+pleiades)".

### The Catalog

The catalog of Pleiades objects can be searched via [simple](../../../search)
or [advanced](../../../search_form) forms and is also written every morning to
[files](../../../downloads) that can be opened in a spreadsheet program.

### References

[1] Y. Tuan, "Place: An Experiential Perspective," Geographical Review, vol.
65, Apr. 1975, pp. 151-165.

[2] Jacobs, I. and N. Walsh, "Architecture of the World Wide Web, Volume One,"
W3C Recommendation, 15 Dec. 2004. http://www.w3.org/TR/webarch/
