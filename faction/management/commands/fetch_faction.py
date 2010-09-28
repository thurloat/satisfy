from django.core.management.base import BaseCommand, CommandError
from faction.models import Topic, CompanyWatch

import urllib, urllib2
import feedparser

class Command(BaseCommand):
    """
    This should execute a call to getsatisfaction and fetch the latest
    topics. put them into 'un-topic-ed' externals.
    """
    args = ''
    help = 'Fetches latest externals from get satisfaction'
    
    def handle(self, *args, **kwargs):
        print "begun"
        cps = CompanyWatch.objects.all()
        for cp in cps:
            print cp.company
            print cp.company_url
            req = urllib2.Request("%s/topics" % cp.company_url)
            res = urllib2.urlopen(req).read()
            
            feed = feedparser.parse(res)
            for e in feed['entries']:
                print e.title
        