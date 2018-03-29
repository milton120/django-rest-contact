from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ContactList, ContactDetail

urlpatterns = [
    url(r'^contact/$', ContactList.as_view(), name='contact-list'),
    url(r'^contact/(?P<pk>[0-9]+)$', ContactDetail.as_view(), name='contact-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

