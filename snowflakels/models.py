from django.db import models

# Create your models here.

class Entry(models.Model):
    question = models.TextField(max_length=3000)
    desc = models.TextField(null=True, blank=True)
    active = models.NullBooleanField()
    answers = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    
    def __unicode__(self):
        return self.question

class Response(models.Model):
    entry = models.ForeignKey(Entry)
    headline = models.CharField(max_length=200)
    body_text = models.TextField()
    pub_date = models.DateTimeField(null=True, blank=True)
    author = models.CharField(max_length = 100, null=True, blank=True)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.headline
