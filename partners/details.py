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

from django.utils.translation import ugettext_lazy as _

from prometeo.core import details

class PartnerListDetails(details.ModelPaginatedListDetails):
    def row_template(self, row):
        i = self._header.index(_('managed'))
        if row[i]:
            return u'\t<tr class="managed">\n'
        return super(PartnerListDetails, self).row_template(row)
        
    def column_template(self, row, index):
        i = self._header.index(_('managed'))
        j = self._header.index(_('name'))
        if index == j and row[i]:
            value = row[index]
            return u'\t\t<td class="name"><span class="sign">(*)</span>%s</td>\n' % details.value_to_string(value)
        return super(PartnerListDetails, self).column_template(row, index)
