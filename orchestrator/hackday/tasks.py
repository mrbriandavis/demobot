from celery import task
from time import sleep
from django.db import models
from hackday.models import Script, Post, Thread
import requests
import sys

try:
    import json
except ImportError:
    import simplejson as json

def _oauth_header(token):
    return {"Authorization": "Bearer %s" % token}

def build_posts(thread):
    ordered_posts = []
#    print 'assembling posts for: %s' % thread
    posts = Post.objects.filter(thread__name=thread.name).all().order_by('-is_starter')
#    print 'posts in thread: %s' % posts
    for post in posts:
#        print
#        print '%s\t%s\t%s' % (post.name, post.is_starter, post.content)
#        print
        ordered_posts.append(post)

    return ordered_posts

def post_thread(thread, group_id):
    base_url = 'https://www.yammer.com/api/v1/'
    config = {'verbose': sys.stderr}
    endpoint = 'messages'
    url = '%s%s%s' % (base_url, endpoint, '.json')

    for post in thread:
        payload = {'body': post.content}

        if group_id is not None:
#            print group_id
            payload['group_id'] = group_id

        r = requests.post(url, headers=_oauth_header(post.token), params=payload, config=config)
        print r.text

#        print payload
#
#        print r.text

        sleep(post.delay)


@task()
def add(x, y):
    # sleep(400)
    return x + y

@task()
def start(event_name):
    print "Starting to process: %s" % event_name

    threads = Thread.objects.filter(script__name=event_name).all()

    threads_to_post = []
    for thread in threads:
        t = {
            'posts': build_posts(thread),
            'group_id': thread.group_id
        }
        threads_to_post.append(t)
#        threads_to_post.append(build_posts(thread))

    for t in threads_to_post:
        post_thread(t['posts'], t['group_id'])
        print t



    return threads.count()

# Working code
#    posts = Post.objects.filter(thread__name=event_name).all()
#
#    base_url = 'https://www.yammer.com/api/v1/'
#    config = {'verbose': sys.stderr}
#    endpoint = 'messages'
#
#    url = '%s%s%s' % (base_url, endpoint, '.json')
#
#    for p in posts:
#
#    #        print dir(t)
#        print p.thread.name
#        print p.name
#        print p.delay
#
#        msg = '{"body":["%s"]}' % p.content
#        msg = 'test'
#        payload = {'body': p.content}
#        print payload
#        r = requests.post(url, headers=_oauth_header(p.token), params=payload, config=config)
#        print r.text
#        sleep(p.delay)
#


#    return r.json


#    return 'Item count: %s' % posts.count()
