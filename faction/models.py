import datetime

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from django.core.urlresolvers import reverse

class CompanyWatch(models.Model):
    """(FetchHistory description)"""
    
    company = models.CharField(blank=True, max_length=100) #compant name
    company_url = models.CharField(blank=True, max_length=100) #getsatisfaction uri
    last_id = models.IntegerField(blank=True, null=True) #checked against getsatisfaction atom feed
    company_slug = models.SlugField()
    
    class Admin:
        list_display = ('',)
        search_fields = ('',)
    
    def save(self, *args, **kwargs):
        """sluggyness must occur ici"""
        self.company_slug = slugify(self.company)
        super(CompanyWatch, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"Company: %s" % self.company
        
    def get_absolute_url(self):
        """/faction/company/blllaaahhh"""
        return reverse("faction-company-dashboard", args=[self.company_slug])
        

class Topic(models.Model):
    """Meta discussion about a bunch of linked externals (getsatisfaction topics)"""
    
    company = models.ForeignKey(CompanyWatch, related_name="company_topic")
    title = models.CharField(blank=True, max_length=100)
    topic_id = models.CharField(blank=True, max_length=100)
    satisfaction_user = models.CharField(blank=True, max_length=100)
    open = models.BooleanField(default=True)
    created_stamp = models.DateTimeField(blank=True, default=datetime.datetime.now)
    activity_stamp = models.DateTimeField(blank=True, default=datetime.datetime.now)
    people = models.ManyToManyField(User)
    
    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"Topic"

class External(models.Model):
    """Some sort of exernal resource that is attached to a Topic
    This is restricted to getsatisfaction right now, pulled every x
    """
    
    topic = models.ForeignKey(Topic)
    type = models.CharField(blank=True, max_length=100) #is it a faq, praise, issue?
    source = models.CharField(blank=True, max_length=100) #always getsatisfaction
    title = models.CharField(blank=True, max_length=100) #cached title from the atom feed, save on requests
    gs_id = models.IntegerField(blank=True, null=True) #getsatisfaction id.
    timestamp = models.DateTimeField(blank=True, default=datetime.datetime.now)
    
    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"External"


class InternalComment(models.Model):
    """Comments internal about the topic"""
    topic = models.ForeignKey(Topic)
    body = models.CharField(blank=True, max_length=100)
    user_name = models.CharField(blank=True, max_length=100) # user name TODO: change to user model
    timestamp = models.DateTimeField(blank=True, default=datetime.datetime.now)
    
    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"InternalComment"
