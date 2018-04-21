from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    url(r'^finishes/$', FinishCreateView.as_view(), name="create"),
    url(r'^finishes/(?P<pk>[0-9]+)/$',
        FinishDetailsView.as_view(), name="details"),
    url(r'^sizes/$', SizeCreateView.as_view(), name="create"),
    url(r'^sizes/(?P<pk>[0-9]+)/$',
        SizeDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
