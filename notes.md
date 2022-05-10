# Notes on the SOHS Mathc App

## General Stack

- Using a Postgres DB with Django ORM
- Python Django App

  - Announcements App
  - Registrations App

- Hugo CMS (Session Notes? May or may not be present)

## Django App

### Models

Announcement:

- title (CharField(max_length=255))
- text (TextField())
- timestamp (DateTimeField(auto_now_add=True))
- Meta (ordering=['-timestamp'])

User (auto-gen by django auth)

Groups:

- editor (can see registrations, edit contests/announcements)

Registration:

- user (ManyToManyField(User))
- timestamp (DateTimeField(auto_now_add=True))
- Meta (ordering=['-timestamp'])

Contest:

- title (CharField(max_length=255))
- deadline (DateField)
- registration (ManyToManyField(Registration))
- Meta (ordering=['timestamp'])
