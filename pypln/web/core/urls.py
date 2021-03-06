# -*- coding:utf-8 -*-
#
# Copyright 2012 NAMD-EMAP-FGV
#
# This file is part of PyPLN. You can get more information at: http://pypln.org/.
#
# PyPLN is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyPLN is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyPLN.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from pypln.web.core.views import CorpusList, CorpusDetail, CorpusDocumentList
from pypln.web.core.views import DocumentList, DocumentDetail
from pypln.web.core.views import PropertyList, PropertyDetail

urlpatterns = patterns('pypln.web.core.views',
    url(r'^$', 'api_root'),
    url(r'^user/api-token/$', 'auth_token', name='auth_token'),
    url(r'^corpora/$', CorpusList.as_view(), name='corpus-list'),
    url(r'^corpora/(?P<pk>\d+)/$', CorpusDetail.as_view(), name='corpus-detail'),
    url(r'^corpora/(?P<pk>\d+)/documents/$', CorpusDocumentList.as_view(),
                name='corpus-document-list'),
    url(r'^documents/$', DocumentList.as_view(), name='document-list'),
    url(r'^documents/(?P<pk>\d+)/$', DocumentDetail.as_view(), name='document-detail'),
    url(r'^documents/(?P<pk>\d+)/properties/$',
        PropertyList.as_view(), name='property-list'),
    url(r'^documents/(?P<pk>\d+)/properties/(?P<property>[\w\d-]+)/$',
        PropertyDetail.as_view(), name='property-detail'),
)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
