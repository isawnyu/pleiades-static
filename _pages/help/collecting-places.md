---
contributors:
- name: Brian Turner
  path: /author/bdturner
- name: Tom Elliott
  path: /author/thomase
copyright: Copyright © 2012-2013 New York University and Brian Turner.
created: '2012-03-14'
creators:
- name: Sean Gillies
  path: /author/sgillies
layout: helppage
modified: '2013-02-11'
permalink: /help/collecting-places
title: Collecting Places
---

#  Collecting Places

How to save, tend, and share collections of places

Pleiades has a type of content object called a _collection_. This is a highly
configurable and persistent searching and sorting tool with folder-like
properties. _Collections_ are our best way to gather together related places
(or other objects) and share them with others. This document will explain how
to use them.

## Introduction to using collections

Section [5\. Using
Collections](http://plone.org/documentation/manual/plone-3-user-manual/using-
collections) in the Plone 3 Manual is required reading. In the examples below,
it will be assumed that you've at least skimmed that documentation. It's only
a couple pages, so go do it now.

## Starting with search

A search of the site is a good way to get started. For example, say you want
to collect some places that cite Wikipedia. Browse to the search form, type
"Wikipedia" in the Cites field of the Authorship, Citation, and Provenance tab
and search for [places that cite
Wikipedia](../search?portal_type=Place&Cites=Wikipedia).

![search-results.jpg](images/search-results.jpg/image_large)

There's a new element in this page: an embedded list of short names (or _ids_)
for all items in this single batch of 30 search results. Select all those
names, copy them to your clipboard, or just leave this browser tab or window
untouched and open a new one for the next step.

![copy-names.jpg](images/copy-names.jpg/image_large)

## Creating a collection

Go to your personal folder by following the link in the upper right corner of
every page and seek "Smart Folder" (another name for _collections_) in the
_Add new..._ menu.

![create-action.jpg](images/create-action.jpg/image_large)

Give the new object a good title and description. Add some annotation or
narrative to the Body Text field if you'd like. More metadata can be added via
the Categorization tab.

![create-form.jpg](images/create-form.jpg/image_large)

Click save at the bottom of the form and you will be redirected to the default
view of this collection at its new URI.

![new-collection.jpg](images/new-collection.jpg/image_large)

As it says, there are currently no criteria on which to search, and therefore
no results. Click on the Criteria tab to add one that will hold all of the
short names we've copied above.

## Short name criteria

No criteria are defined yet for this collection. Select "Short Name" from the
Field name list as shown below.

![adding-criteria.jpg](images/adding-criteria.jpg/image_large)

Then click the "Add criteria" button. You will be offered a form for entering
values for all criteria.

![empty-field.jpg](images/empty-field.jpg/image_large)

Paste into the Values field the copied list of short names.

![values-entered.jpg](images/values-entered.jpg/image_large)

Click save. If you want to add more short names, copy more and paste them to
the end of this list. Is there a limit? No hard limit, but collections don't
scale well to hundreds of items. It will be best to keep the number of short
name values under 100. You can return to this form as often as you like to add
or remove values and thereby tend the collection.

## Share the collection

Click on the View tab (left of Criteria and Edit tabs) and the Pleiades
catalog is searched using your criteria. The results are shown like so.

![final-view.jpg](images/final-view.jpg/image_large)

You automatically get a KML representation of collected places that you can
download and use in Google Earth. However, because your collection is in the
private state, it can't be accessed by anyone other than you and the managers
of Pleiades. Select "Publish" from the State action and your collection can be
viewed, but not edited, by others. The KML link can then be used in Google
Maps, for example: <http://g.co/maps/mu3n7>.
