# core/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notebook, Note

class NotebookListView(LoginRequiredMixin, ListView):
    model = Notebook
    template_name = 'notebooks/notebook_list.html'
    context_object_name = 'notebooks'

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)

class NotebookDetailView(LoginRequiredMixin, DetailView):
    model = Notebook
    template_name = 'notebooks/notebook_detail.html'
    context_object_name = 'notebook'

class NotebookCreateView(LoginRequiredMixin, CreateView):
    model = Notebook
    fields = ['name', 'description']
    template_name = 'notebooks/notebook_form.html'
    success_url = reverse_lazy('notebook-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NotebookUpdateView(LoginRequiredMixin, UpdateView):
    model = Notebook
    fields = ['name', 'description']
    template_name = 'notebooks/notebook_form.html'
    success_url = reverse_lazy('notebook-list')

class NotebookDeleteView(LoginRequiredMixin, DeleteView):
    model = Notebook
    template_name = 'notebooks/notebook_confirm_delete.html'
    success_url = reverse_lazy('notebook-list')

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return self.model.objects.filter(notebook__owner=self.request.user)

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content', 'notebook', 'category', 'is_archived', 'is_pinned']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['notebook'].queryset = Notebook.objects.filter(owner=self.request.user)
        return form

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'content', 'notebook', 'category', 'is_archived', 'is_pinned']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['notebook'].queryset = Notebook.objects.filter(owner=self.request.user)
        return form

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note-list')