from django.urls import path
from .views import (
    NotebookListView, NotebookDetailView, NotebookCreateView, NotebookUpdateView, NotebookDeleteView,
    NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView
)

urlpatterns = [
    path('core/', NotebookListView.as_view(), name='notebook-list'),
    path('core/<int:pk>/', NotebookDetailView.as_view(), name='notebook-detail'),
    path('core/create/', NotebookCreateView.as_view(), name='notebook-create'),
    path('core/<int:pk>/update/', NotebookUpdateView.as_view(), name='notebook-update'),
    path('core/<int:pk>/delete/', NotebookDeleteView.as_view(), name='notebook-delete'),

    path('core/', NoteListView.as_view(), name='note-list'),
    path('core/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('core/create/', NoteCreateView.as_view(), name='note-create'),
    path('core/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('core/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]