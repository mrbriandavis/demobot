# myapp/api.py
from tastypie.resources import ModelResource
from hackday.models import Event, Post
from tastypie.authorization import Authorization

class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        authorization= Authorization()

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        authorization= Authorization()
