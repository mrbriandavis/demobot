# myapp/api.py
from tastypie.resources import ModelResource
from hackday.models import Event
from tastypie.authorization import Authorization

class EventResource(ModelResource):
    class Meta:
#        queryset = Entry.objects.all()
        queryset = Event.objects.all()
        resource_name = 'event'
        authorization= Authorization()
