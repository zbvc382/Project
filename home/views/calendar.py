from django_ical.views import ICalFeed
from ..models import Event


class EventFeed(ICalFeed):

    product_id = 'rhul.herokuapp.com'
    timezone = 'UTC'
    file_name = "Absences.ics"

    def items(self):
        return Event.objects.all().order_by('-start')

    def item_guid(self, item):
        return "{}{}".format(item.id, "global_name")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_start_datetime(self, item):
        return item.start

    def item_end_datetime(self, item):
        return item.end

    def item_link(self, item):
        return "http://www.google.de"

    def __call__(self, request, *args, **kwargs):
        self.request = request
        return super(EventFeed, self).__call__(request, *args, **kwargs)