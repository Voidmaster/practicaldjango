import datetime
import os.path

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

from tagging.fields import TagField

from markdown import markdown




class Category(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s" % self.slug
    
class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (1, 'Live'),
        (2, 'Draft'),
        (3, 'Hidden'),
    )

    class Meta:
        verbose_name_plural = "Entries"

    def save(self):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save()

    def get_absolute_url(self):
        return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)

    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=250)
    slug = models.SlugField(unique_for_date='pub_date')
    excerpt = models.TextField()
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    image = models.ImageField(upload_to='media')
    
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)

    categories = models.ManyToManyField(Category)
    tags = TagField()

