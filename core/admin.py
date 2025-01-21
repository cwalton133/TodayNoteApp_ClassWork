from django.contrib import admin
from .models import Notebook, Note, NoteCategory

@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner')
    search_fields = ('name', 'description')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'notebook', 'category', 'is_archived', 'is_pinned')
    list_filter = ('is_archived', 'is_pinned', 'category')
    search_fields = ('title', 'content')

@admin.register(NoteCategory)
class NoteCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
