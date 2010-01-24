#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file is part of the prometeo project.

This program is free software: you can redistribute it and/or modify it 
under the terms of the GNU Lesser General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

__author__ = 'Emanuele Bertoldi <zuck@fastwebnet.it>'
__copyright__ = 'Copyright (c) 2010 Emanuele Bertoldi'
__version__ = '$Revision$'

from django.conf.urls.defaults import *

urlpatterns = patterns('uoms.views',

    # UOMs.
    (r'^$', 'uom_index'),
    (r'^add/$', 'uom_add'),
    (r'^view/(?P<id>\d+)/$', 'uom_view'),
    (r'^edit/(?P<id>\d+)/$', 'uom_edit'),
    (r'^delete/(?P<id>\d+)/$', 'uom_delete'),
    
    # Categories.
    (r'^categories/$', 'category_index'),
    (r'^categories/add/$', 'category_add'),
    (r'^categories/view/(?P<id>\d+)/$', 'category_view'),
    (r'^categories/edit/(?P<id>\d+)/$', 'category_edit'),
    (r'^categories/delete/(?P<id>\d+)/$', 'category_delete'),
)