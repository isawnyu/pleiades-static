---
contributors:
- name: Brian Turner
  path: /author/bdturner
- name: Tom Elliott
  path: /author/thomase
copyright: Copyright © 2011-2013 New York University and Brian Turner.
created: '2011-10-24'
creators:
- name: Sean Gillies
  path: /author/sgillies
layout: helppage
modified: '2013-02-11'
permalink: /help/batch-upload
title: Is there a way to upload large collections of data into Pleiades?
---

#  Is there a way to upload large collections of data into Pleiades?

At present, no. But we're working on it and would be grateful for your
feedback.

Pleiades has multiple [users](../../credits/) and [partners](../../docs/using-
our-data "Using Our Data" ) that want to make data contributions in bulk, but
we don't have the wherewithal to support multiple input data formats or do the
conversions from multiple formats. We're going to standardize on one single
format that is very much like the format for [our daily CSV
dumps](../../downloads "Data for download" ).

In the interest of soliciting suggestions, questions, and other feedback
during the design phase, we have posted the draft specification, process
description, and related materials online at
<https://github.com/isawnyu/pleiades-update-overlays/blob/master/README.rst>.

What we're describing isn't a web API for Pleiades (something we'd like to
develop in the future). Rather, it's a way to describe a set of pre-reviewed
changes that can be attached as a CSV file to a [content development
project](../../docs/content-development-projects "Content Development
Projects" ) and then incorporated into Pleiades by a script run and supervised
by a member of the Pleiades technical team. It's designed for making many
(100-1000+) changes on a theme: adding the missing attested forms of names,
adding references, making connections between places, etc.

Your feedback is gratefully appreciated, and we'll be happy to provide more
specific examples based on the feedback we get.
