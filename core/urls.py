# core/urls.py

from django.urls import path
from .views import (
    NotebookListView, NotebookDetailView, NotebookCreateView,
    NotebookUpdateView, NotebookDeleteView,
    NoteListView, NoteDetailView, NoteCreateView,
    NoteUpdateView, NoteDeleteView,
)

urlpatterns = [
    path('notebooks/', NotebookListView.as_view(), name='notebook-list'),
    path('notebooks/<int:pk>/', NotebookDetailView.as_view(), name='notebook-detail'),
    path('notebooks/create/', NotebookCreateView.as_view(), name='notebook-create'),
    path('notebooks/update/<int:pk>/', NotebookUpdateView.as_view(), name='notebook-update'),
    path('notebooks/delete/<int:pk>/', NotebookDeleteView.as_view(), name='notebook-delete'),
    path('notes/', NoteListView.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/create/', NoteCreateView.as_view(), name='note-create'),
    path('notes/update/<int:pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('notes/delete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
]