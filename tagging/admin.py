from django.contrib import admin
from tagging.models import Tag, TaggedItem
from tagging.forms import TagAdminForm

class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm





