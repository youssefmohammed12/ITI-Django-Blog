# 📝 Django CRUD Blog

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-green?logo=django&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)

---

## 📖 Description

A **CRUD Blog Application** built with **Django** — created as a learning project to understand Django's core concepts including **templates**, **static files**, **ModelForms**, **Generic Class-Based Views**, **URL routing**, **database models**, **authentication**, **environment variables**, and **deployment preparation**.

This project demonstrates a complete **Create, Read, Update, Delete** workflow for blog posts, with user authentication, a post detail page, and a clean responsive UI powered by custom CSS.

---

## ✨ Features

- ✅ **Display all blog posts** — View all posts on the homepage with title, author, publication date, and a truncated body preview.
- ✅ **Create new posts** — Use a Django ModelForm to submit new blog posts with title, body, publication date, and author selection.
- ✅ **Edit existing posts** — Update any post's content through a pre-filled edit form.
- ✅ **Delete existing posts** — Remove posts with a confirmation page. Deletion is performed via a **POST request** for safe, intentional removal.
- ✅ **Author information** — Each post is linked to an Author via a **ForeignKey** relationship.
- ✅ **Template inheritance** — Reusable `base.html` layout extended by all child templates.
- ✅ **Static CSS styling** — Custom `style.css` provides a clean, responsive design.
- ✅ **Template filters** — Date formatting (`date:"F d, Y"`) and word truncation (`truncatewords:25`) applied to post content.
- ✅ **CSRF protection** — All forms include `{% csrf_token %}` for security.
- ✅ **Redirect after submission** — Successful form submissions redirect to the post list page.
- ✅ **Responsive UI** — Mobile-friendly layout with max-width container and clean card-based design.
- ✅ **SQLite database** — Lightweight, file-based database for development.
- ✅ **Django Admin** — Manage Authors and Posts through the built-in admin interface.
- ✅ **Authentication** — Users can log in and log out using Django's built-in authentication system.
- ✅ **Protected CRUD operations** — Creating, editing, and deleting posts requires users to be logged in.
- ✅ **Generic Class-Based Views** — Views are implemented using Django's `ListView`, `DetailView`, `CreateView`, `UpdateView`, and `DeleteView`.
- ✅ **Post detail page** — Clicking "Read More" opens a full-page view of the complete blog post.
- ✅ **Environment variables** — Sensitive settings like `SECRET_KEY` and `DEBUG` are loaded from a `.env` file using `python-decouple`.
- ✅ **Deployment-ready static files** — Configured `STATIC_ROOT` with `collectstatic` support for production deployments.

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Backend programming language |
| **Django 6.0** | Web framework |
| **HTML5** | Template structure |
| **CSS3** | Styling and layout |
| **SQLite** | Database |

---

## 📁 Project Structure

```
myLab/
│
├── blog/                          # Main blog application
│   ├── migrations/                 # Database migrations
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   ├── static/
│   │   └── blog/
│   │       └── style.css          # Custom CSS styles
│   │
│   ├── templates/
│   │   ├── blog/
│   │   │   ├── base.html          # Base template (inherited by all pages)
│   │   │   ├── post_list.html      # Homepage — lists all posts
│   │   │   ├── post_detail.html    # Post detail page (full article)
│   │   │   ├── post_form.html      # Create/Edit post form
│   │   │   ├── edit_post.html      # Edit existing post form
│   │   │   └── delete_post.html    # Delete post confirmation page
│   │   │
│   │   └── registration/
│   │       └── login.html          # Login page
│   │
│   ├── __init__.py
│   ├── admin.py                   # Django Admin registration
│   ├── apps.py                    # App configuration
│   ├── forms.py                   # ModelForm for Post model
│   ├── models.py                  # Author and Post models
│   ├── tests.py                   # Test stubs
│   ├── urls.py                    # App-level URL routes
│   └── views.py                   # Generic Class-Based Views
│
├── myLab/                         # Project configuration
│   ├── __init__.py
│   ├── asgi.py                    # ASGI config
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Root URL configuration
│   └── wsgi.py                    # WSGI config
│
├── .env                           # Environment variables (not committed)
├── .gitignore                     # Git ignore rules
├── db.sqlite3                     # SQLite database file
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── staticfiles/                   # Collected static files (for deployment)
└── README.md                      # Project documentation
```

---

## 🧩 Models

### Author

| Field | Type | Description |
|-------|------|-------------|
| `name` | `CharField(max_length=100)` | Author's display name |

### Post

| Field | Type | Description |
|-------|------|-------------|
| `title` | `CharField(max_length=250)` | Post title |
| `body` | `TextField()` | Full content of the post |
| `published_on` | `DateField()` | Date the post was published |
| `author` | `ForeignKey(Author, on_delete=models.CASCADE)` | Links to the Author model |

### Relationship

- **Author** has a **one-to-many** relationship with **Post** — one author can write multiple posts.
- Deleting an Author will **cascade-delete** all their associated posts (`on_delete=models.CASCADE`).

---

## 🌐 Implemented Pages

### 🏠 Home Page (`/`)

- Lists **all blog posts** in reverse chronological order.
- Each post card displays:
  - **Title** (clickable, links to the post detail page)
  - **Author name** (via `post.author.name`)
  - **Published date** (formatted with `|date:"F d, Y"`)
  - **Body preview** (truncated to 25 words with `|truncatewords:25`)
- Each post has a **"Read More"** button to open the full article.
- If the user is logged in, **Edit** and **Delete** buttons are also shown.
- Extends `base.html` for consistent layout.

### 📄 Post Detail (`/post/<id>/`)

- Displays the **full blog post** with complete body content.
- Shows the **author name** and **publication date**.
- Body is rendered with `|linebreaks` for proper paragraph formatting.
- If the user is logged in, **Edit** and **Delete** buttons are shown.
- Includes a **"Back"** button to return to the home page.
- Extends `base.html`.

### ➕ Create Post (`/create/`)

- Uses a **Generic Class-Based View** (`CreateView`) with `LoginRequiredMixin`.
- Displays a **ModelForm** for creating a new post.
- Fields: Title, Body, Published On, Author (dropdown).
- **GET request** — renders an empty form.
- **POST request** — validates and saves the form, then redirects to the home page.
- Requires the user to be **logged in** to access.
- Includes **CSRF token** for security.
- Extends `base.html`.

### ✏️ Edit Post (`/edit/<id>/`)

- Uses a **Generic Class-Based View** (`UpdateView`) with `LoginRequiredMixin`.
- Pre-populates the form with the **existing post data**.
- **GET request** — renders the form with current values.
- **POST request** — validates and updates the post, then redirects to the home page.
- Requires the user to be **logged in** to access.
- Includes a **Cancel** button to return to the home page.
- Includes **CSRF token** for security.
- Extends `base.html`.

### 🗑 Delete Post (`/delete/<id>/`)

- Uses a **Generic Class-Based View** (`DeleteView`) with `LoginRequiredMixin`.
- Displays a **confirmation page** asking the user to confirm the deletion.
- Shows the **post title** so the user knows exactly what they are deleting.
- **GET request** — renders the confirmation form.
- **POST request** — deletes the post and redirects to the home page.
- Deletion is **only performed after submitting the confirmation form**, preventing accidental removals.
- Requires the user to be **logged in** to access.
- Includes a **Cancel** button to return to the home page.
- Includes **CSRF token** for security.
- Extends `base.html`.

### 🔧 Django Admin (`/admin/`)

- Manage **Authors** (add, edit, delete).
- Manage **Posts** (add, edit, delete).
- Requires a **superuser** account to access.

---

## 🧭 URL Routes

| Route | View Name | View Class | Description |
|-------|-----------|------------|-------------|
| `/` | `post_list` | `PostListView` | Home page — displays all blog posts |
| `/post/<int:pk>/` | `post_detail` | `PostDetailView` | Post detail — full article view |
| `/create/` | `create_post` | `PostCreateView` | Form page — create a new blog post (login required) |
| `/edit/<int:post_id>/` | `edit_post` | `PostUpdateView` | Form page — edit an existing blog post (login required) |
| `/delete/<int:post_id>/` | `delete_post` | `PostDeleteView` | Confirmation page — delete a blog post (login required) |
| `/accounts/login/` | `login` | Django built-in | Login page |
| `/accounts/logout/` | `logout` | Django built-in | Logout action |
| `/admin/` | `admin:index` | Django Admin | Django Admin interface |

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

### 3️⃣ Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 4️⃣ Configure environment variables

Create a `.env` file in the project root (`myLab/`) with the following content:

```env
SECRET_KEY='django-insecure-your-secret-key-here'
DEBUG=True
```

> **Note:** The `.env` file is listed in `.gitignore` and will not be committed to version control.

### 5️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Run database migrations

```bash
python manage.py migrate
```

### 7️⃣ Collect static files (for deployment)

```bash
python manage.py collectstatic
```

### 8️⃣ Create a superuser (for Django Admin)

```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

### 9️⃣ Run the development server

```bash
python manage.py runserver
```

### 🔟 Open the application

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 📸 Screenshots

### 🏠 Home Page

> ![Home Page](screenshot/home.png)

---

### ➕ Create Post

> ![Create Post](screenshot/create.png)

---

### ✏️ Edit Post

> ![Edit Post](screenshot/edit.png)

---

### 🗑 Delete Post

> ![Delete Post](screenshot/delete.png)

---

## 📚 Learning Objectives

This project demonstrates the following **Django concepts**:

| Concept | Implementation |
|---------|---------------|
| **Django Models** | `Author` and `Post` models with `CharField`, `TextField`, `DateField` |
| **ORM & Queries** | `Post.objects.all()`, `get_object_or_404()` |
| **ForeignKey Relationships** | `Post.author → Author` — accessing author name via `post.author.name` |
| **Generic Class-Based Views** | `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` |
| **Django Authentication** | Login, logout, and session management via Django's built-in auth system |
| **LoginRequiredMixin** | Protects create, edit, and delete views from unauthenticated access |
| **URL Routing** | `path()` with named routes and URL parameters (`<int:pk>`, `<int:post_id>`) |
| **Template Inheritance** | `{% extends 'blog/base.html' %}` and `{% block %}` tags |
| **Static Files** | `{% load static %}` and `{% static 'blog/style.css' %}` |
| **ModelForms** | `PostForm` auto-generated from `Post` model, with instance editing |
| **CRUD Operations** | Create, Read, Update, and Delete blog posts — safe deletion via POST request |
| **Template Filters** | `|date:"F d, Y"`, `|truncatewords:25`, and `|linebreaks` |
| **CSRF Protection** | `{% csrf_token %}` in all forms |
| **Environment Variables** | `SECRET_KEY` and `DEBUG` loaded from `.env` via `python-decouple` |
| **Deployment Preparation** | `ALLOWED_HOSTS`, `STATIC_ROOT`, and `collectstatic` configured for production |
| **Django Admin** | Registered models for admin interface management |


---

## 🔐 Environment Variables

This project uses **`python-decouple`** to manage sensitive configuration outside of the source code.

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django's secret key for cryptographic signing | Required |
| `DEBUG` | Enables/disables debug mode | `False` |

Create a `.env` file in the project root (`myLab/`) to define these values. The `.env` file is excluded from version control via `.gitignore` to prevent accidental exposure of secrets.

---

## 🚀 Deployment Preparation

The project includes several configurations to prepare for production deployment:

- **`ALLOWED_HOSTS`** — Configured with `127.0.0.1` and `localhost`; update for your domain.
- **`STATIC_ROOT`** — Set to `staticfiles/`, the directory where static files are collected.
- **`collectstatic`** — Run `python manage.py collectstatic` to gather all static files into the `staticfiles/` directory.
- **`gunicorn`** — Included in `requirements.txt` as a production-ready WSGI server.

---

## 📄 License

**MIT License**

```
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

> **Built with ❤️ using Django** — Thanks to our instructor for her hard work at teaching us.