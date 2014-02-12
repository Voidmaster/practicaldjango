from django.contrib import admin

from weblog.models import Category, Entry, Artista, Encuesta, OpcionEncuesta, Cancion, Genero
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} 
    ordering = ['title']

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['pub_date']

class OpcionEncuestaInLine(admin.StackedInline):
	model = OpcionEncuesta
	extra = 1

class GeneroAdmin(admin.ModelAdmin):
	ordering = ['nombre']
	prepopulated_fields = {'slug': ('nombre',)}	

class EncuestaAdmin(admin.ModelAdmin):
    ordering = ['fecha_publicacion']
    inlines = [OpcionEncuestaInLine]

class OpcionEncuestaAdmin(admin.ModelAdmin):
    ordering = ['texto']

class CancionInLine(admin.StackedInline):
	model = Cancion
	extra = 14
	
class ArtistaAdmin(admin.ModelAdmin):
	ordering = ['nombre']
	prepopulated_fields = {'slug': ('nombre',)}
	inlines = [CancionInLine]
	search_fields = ('nombre', 'genero__nombre')
	list_filter = ('nombre', 'genero__nombre')

class CancionAdmin(admin.ModelAdmin):
	ordering = ['titulo']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Genero, GeneroAdmin)

admin.site.register(OpcionEncuesta, OpcionEncuestaAdmin)
admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Cancion, CancionAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)