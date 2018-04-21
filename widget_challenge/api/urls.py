from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    url(r'^finishes/$', FinishCreateView.as_view(), name="finish_create"),
    url(r'^finishes/(?P<pk>[0-9]+)/$',
        FinishDetailsView.as_view(), name="finish_details"),
    url(r'^sizes/$', SizeCreateView.as_view(), name="size_create"),
    url(r'^sizes/(?P<pk>[0-9]+)/$',
        SizeDetailsView.as_view(), name="size_details"),
    url(r'^widgets/$', WidgetCreateView.as_view(), name="widget_create"),
    url(r'^widgets/(?P<pk>[0-9]+)/$',
        WidgetDetailsView.as_view(), name="widget_details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
