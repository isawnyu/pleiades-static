---
contributors:
- name: Sean Gillies
  path: /author/sgillies
copyright: Copyright © 2011-2015 New York University.
created: '2011-10-24'
creators:
- name: Tom Elliott
  path: /author/thomase
layout: helppage
modified: '2015-02-08'
permalink: /help/pleiades-objects
title: What classes of "object" are treated by the Pleiades data model?
---

#  What classes of "object" are treated by the Pleiades data model?

We're using the architecture of the web for Pleiades. It's designed in terms
of resources and representations. There are 2 categories of resources: ancient
world resources, and research resources.

Ancient world resources are: Places, Locations, Names. These are descriptions
of historical entities. A Place resource, such as [Vani](../places/863918), is
_about_ an ancient place. Locations and Names always have a Place as context.
All ancient world resources are governed by revision control and editorial
policies and they will have a listing of supporting references. These
resources comprise what people usually agree to call a "dataset".

Research resources are not part of the dataset. There are some site-wide
shared resources like time period and feature type
[vocabularies](../vocabularies "vocabularies" ), and
[collections](../collections "Collections" ) (saved queries) of ancient world
resources. Users may also create [custom](../Members/sgillies/news-
items/spatial-criteria-for-collections "Spatial criteria for collections" )
collections for their own research.

Underneath all of this are thousands of Python objects in several large
B-trees, but that's an implementation detail. The reality of Pleiades is web
resources.

###  See further:

* [Technical Introduction to Places](../docs/technical-intro-places "Technical Introduction to Places" )
