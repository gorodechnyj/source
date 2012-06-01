# -*- coding: utf-8 -*-
'''
Created on 01.06.2012

@author: gorodechnyj
'''

from django.db import models

class Source(models.Model):
    ''' Description of source database, information was loaded from. 
        Needed for future updates.'''
    name = models.CharField(max_length=200)
    
    class Meta:
        app_label = 'source'
    
    def __unicode__(self):
        return self.name
    
class External(models.Model):
    ''' Objects loaded from external source database. Holds information 
        about external database and object's key in source database.'''
    id = models.CharField('Composite primary key', max_length=138, primary_key = True, default=None)
    source = models.ForeignKey(Source, related_name="external_%(class)s_set", default=None)    
    source_code = models.CharField('Key value of source object in external database', max_length=128, default=None)
    
    class Meta:
        abstract = True
        app_label = 'source'
    
#    def save(self, *args, **kwargs):
##        if not self.source_id:
##            self.source = Source.objects.get(id = 1) #name = 'constructor'
##        self.id = str(self.source_id).ljust(10,'0')+self.source_code
#        super(External, self).save(*args, **kwargs)