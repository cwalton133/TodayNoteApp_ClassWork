# Note Taking Application

Welcome to the Note Taking Application! This project is designed to provide users with a simple and intuitive way to create and manage notes within organized notebooks. Built using Django, this application leverages Django's powerful ORM and user authentication to streamline note-taking tasks.

## Features

User Authentication: Sign up and log in to securely access your notebooks and notes.
Notebook Management: Create, view, and manage multiple notebooks, each representing a separate collection of notes.
Categorization: Organize your notes into categories for easy navigation and retrieval.
Note Management: Create, edit, and delete notes within each notebook, with options to pin or archive them for better organization.
Timestamps: Each model includes created and updated timestamps for easy tracking of your notes.

### 1. Model Overview

The application is centered around three primary models: Notebook, NoteCategory, and Note, which are implemented in the models file as follows:

TimestampedModel
An abstract base model that adds automatic timestamp fields to any inheriting model.

class TimestampedModel(models.Model):
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

### 2. NoteBook

Notebook
Represents a collection of notes created by a user.

name: The name of the notebook (unique).
description: Optional description of the notebook.
owner: The user who owns the notebook.

class Notebook(TimestampedModel):
name = models.CharField(max_length=200, unique=True)
description = models.TextField(blank=True, null=True)
owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notebooks")

### 3. NoteCategory

Represents a category under which notes may be organized.

name: The name of the category (unique).
description: Optional description of the category.

class NoteCategory(TimestampedModel):
name = models.CharField(max_length=100, unique=True)
description = models.TextField(blank=True, null=True)
```

### 4. Note

-Represents an individual note created by the user.

title: The title of the note.
content: The main content of the note.
notebook: The notebook to which this note belongs.
category: The category of the note (optional).
is_archived: Boolean flag indicating if the note is archived.
is_pinned: Boolean flag indicating if the note is pinned for easy access.

class Note(TimestampedModel):
title = models.CharField(max_length=200)
content = models.TextField()
notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, related_name="notes")
category = models.ForeignKey(NoteCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="notes")
is_archived = models.BooleanField(default=False)
is_pinned = models.BooleanField(default=False)

    class Meta:
        ordering = ["-updated_at"]

### 5. Installation

To run this application locally, follow these steps:

### 6. Clone the Repository

git clone https://github.com/cwalton133/TodayNoteApp_ClassWork.git

cd note-taking-app

### 7. Create a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

### 8. Install dependencies:

pip install -r requirements.txt

### 8. Apply migrations:

:python manage.py migrate

### 9. Create a Superuser:

python manage.py createsuperuser

### 10. Run the development server:

:python manage.py runserver

### 11. Access the application::

Open your web browser and go to http://127.0.0.1:8000/.

### 12. Contributing

We welcome contributions! If you have suggestions or improvements, please fork the repository, create a new branch, and submit a pull request.

### 13. License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Thank you for checking out the Note Taking Application! We hope you find it useful for your note-taking needs. Happy noting!
