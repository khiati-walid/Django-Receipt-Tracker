# Django Receipt Tracker

## Table of Contents

- [Django Receipt Tracker](#django-receipt-tracker)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Getting Started](#getting-started)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Create a Virtual Environment](#2-create-a-virtual-environment)
    - [3. Activate the Virtual Environment](#3-activate-the-virtual-environment)
    - [4. Install Project Dependencies](#4-install-project-dependencies)
    - [5. Apply Database Migrations](#5-apply-database-migrations)
    - [6. Create a Superuser](#6-create-a-superuser)
    - [7. Run the Development Server](#7-run-the-development-server)
  - [Features](#features)
  - [Testing](#testing)
  - [Deployment](#deployment)

## Requirements

- Python 3.10
- Django 5.0 (install dependencies using `pip install -r requirements.txt`)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-receipt-tracker.git
```

### 2. Create a Virtual Environment

```bash
cd django-receipt-tracker
python3.10 -m venv venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
.\venv\Scripts\activate
```

On Unix or MacOS:

```bash
source venv/bin/activate
```

### 4. Install Project Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

## Features

- User Authentication: Register, login, and logout functionalities.
- Receipt Management: Create, read, update, and delete receipts.
- Only Authenticated Users: Ensure users can only view and manage their own receipts.

## Testing

Basic tests for models and views are available. Run tests using:

```bash
python manage.py test
```

## Deployment

The live version of the website can be accessed at [http://walidkhiati.pythonanywhere.com/](http://walidkhiati.pythonanywhere.com/).

You can either register a new user or use the existing staff user:

- **Username:** rairon
- **Password:** 111
