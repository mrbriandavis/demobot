from django.db import models
from django.db.models import signals
from django.dispatch import dispatcher





class Playbook(models.Model):
    name = models.CharField(max_length=20)

class Act(models.Model):
    playbook = models.ForeignKey(Playbook)
    name = models.CharField(max_length=20)

class Line(models.Model):
    act = models.ForeignKey(Act)
    name = models.CharField(max_length=20)
    # token = ""
    # action = ""
    # delay = 10
    # in_reply_to = "" # optional

class Event(models.Model):
    name = models.CharField(max_length=20)


def event_post_save(sender, instance, signal, *args, **kwargs):
    # Creates user profile
    from hackday.tasks import add
    from celery import group

    jobs = []

    for x in range(1,10):
        st = add.subtask((1, x))
        jobs.append(st)

    job = group(jobs)
    result = job.apply_async()
    res = result.join()

models.signals.post_save.connect(event_post_save, sender=Event)

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice
