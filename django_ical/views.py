# Title: django-ical source code
# Author: Ian Lewis
# Date: 2012
# Code version: 1.4
# Availability: https://github.com/pinkerton/django-ical

from datetime import datetime
from calendar import timegm
import django
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.syndication.views import Feed
from django.utils.http import http_date
try:
    from django.utils import six
except ImportError:
    import six

from django_ical import feedgenerator

__all__ = (
    'ICalFeed',
)

FEED_EXTRA_FIELDS = (
    'method',
    'product_id',
    'timezone',
)

ICAL_EXTRA_FIELDS = [
    'timestamp',        # dtstamp
    'created',          # created
    'start_datetime',   # dtstart
    'end_datetime',     # dtend
    'transparency',     # transp
    'location',         # location
    'geolocation',      # latitude;longitude
    'organizer',        # email, cn, and role
]

if django.VERSION < (1, 7):
    ICAL_EXTRA_FIELDS.append('updateddate')


class ICalFeed(Feed):

    feed_type = feedgenerator.DefaultFeed

    def __call__(self, request, *args, **kwargs):

        try:
            obj = self.get_object(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise Http404('Feed object does not exist.')
        feedgen = self.get_feed(obj, request)
        response = HttpResponse(content_type=feedgen.mime_type)
        if hasattr(self, 'item_pubdate') or hasattr(self, 'item_updateddate'):
            response['Last-Modified'] = http_date(
                timegm(feedgen.latest_post_date().utctimetuple()))
        feedgen.write(response, 'utf-8')

        filename = self._get_dynamic_attr('file_name', obj)
        if filename:
            response['Content-Disposition'] = 'attachment; filename="%s"' % filename

        return response

    def _get_dynamic_attr(self, attname, obj, default=None):

        try:
            attr = getattr(self, attname)
        except AttributeError:
            return default
        if callable(attr):
            try:
                code = six.get_function_code(attr)
            except AttributeError:
                code = six.get_function_code(attr.__call__)
            if code.co_argcount == 2:
                return attr(obj)
            else:
                return attr()
        return attr

    link = ''

    def method(self, obj):
        return 'PUBLISH'

    def feed_extra_kwargs(self, obj):
        kwargs = {}
        for field in FEED_EXTRA_FIELDS:
            val = self._get_dynamic_attr(field, obj)
            if val:
                kwargs[field] = val
        return kwargs

    def item_timestamp(self, obj):
        return datetime.now()

    def item_extra_kwargs(self, obj):
        kwargs = {}
        for field in ICAL_EXTRA_FIELDS:
            val = self._get_dynamic_attr('item_' + field, obj)
            if val:
                kwargs[field] = val
        return kwargs
