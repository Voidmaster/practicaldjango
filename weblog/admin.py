from django.contrib import admin
from weblog.models import Category, Entry, Artista, Encuesta, OpcionEncuesta

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} 
    ordering = ['title']

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['pub_date']

class EncuestaAdmin(admin.ModelAdmin):
    ordering = ['fecha_publicacion']

class OpcionEncuestaAdmin(admin.ModelAdmin):
    ordering = ['texto']

class ArtistaAdmin(admin.ModelAdmin):
	ordering = ['nombre']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(OpcionEncuesta, OpcionEncuestaAdmin)
admin.site.register(Encuesta, EncuestaAdmin)
