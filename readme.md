# Note Taking Application

Welcome to the Note Taking Application! This project is designed to provide users with a simple and intuitive way to create and manage notes within organized notebooks. Built using Django, this application leverages Django's powerful ORM and user authentication to streamline note-taking tasks.

## Table of Contents

- [Features](#features)
- [Model Overview](#model-overview)
  - [1. TimestampedModel](#1-timestampedmodel)
  - [2. Notebook](#2-notebook)
  - [3. NoteCategory](#3-notecategory)
  - [4. Note](#4-note)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Authentication**: Sign up and log in to securely access your notebooks and notes.
- **Notebook Management**: Create, view, and manage multiple notebooks, each representing a separate collection of notes.
- **Categorization**: Organize your notes into categories for easy navigation and retrieval.
- **Note Management**: Create, edit, and delete notes within each notebook, with options to pin or archive them for better organization.
- **Timestamps**: Each model includes created and updated timestamps for easy tracking of your notes.

## Model Overview

The application is centered around four primary models: **TimestampedModel**, **Notebook**, **NoteCategory**, and **Note**.

### 1. TimestampedModel

An abstract base model that adds automatic timestamp fields to any inheriting model.

```python
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

2. Notebook
Represents a collection of notes created by a user.

name: The name of the notebook (unique).
description: Optional description of the notebook.
owner: The user who owns the notebook.


class Notebook(TimestampedModel):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notebooks")


    3. NoteCategory
Represents a category under which notes may be organized.

name: The name of the category (unique).
description: Optional description of the category.



3. NoteCategory
Represents a category under which notes may be organized.

name: The name of the category (unique).
description: Optional description of the category.


class NoteCategory(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)



    4. Note
Represents an individual note created by the user.

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
        
        
Installation
To run this application locally, follow these steps:

Clone the Repository

git clone https://github.com/cwalton133/TodayNoteApp_ClassWork.git
cd note-taking-app


Create a Virtual Environment
python -m venv venv

On Windows, use:
venv\Scripts\activate

On macOS/Linux, use:
source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

Apply Migrations
python manage.py migrate

Create a Superuser
python manage.py createsuperuser

Run the Development Server
python manage.py runserver

Access the Application
Open your web browser and go to http://127.0.0.1:8000/.

Contributing
We welcome contributions! If you have suggestions or improvements, please fork the repository, create a new branch, and submit a pull request.


License
This project is licensed under the MIT License.

Contact
For any questions or feedback, please contact:

Charles Walton - cwalton1335@gmail.com
GitHub: cwalton133
Thank you for checking out the Products Application!

:
