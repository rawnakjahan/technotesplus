# TechNotesPlus
TechNotesPlus is a note-taking application, which allows users to take notes, manage them and share.
Basic django structure with Login, Logout, Pagination, JWT

## Prerequisites
* Python
* Virtualenv

## Getting Started
1. Clone the repository.
2. Create virtual environment. 
```
virtualenv -p python3 venv --no-site-packages
```
3. Go to project folder
4. Activate the virtualenv on ubuntu.
```
venv/Scripts/activate
```
5. Install requirements 
```
pip install -r requirements.txt
```
5. Migrate 
```
python manage.py migrate
```
6. Load Data 
```
python manage.py loaddata load_data.json
```
7.Run project 
```
python manage.py runserver
```
8.Login using Credential 
```
username: admin
password: 1q2w3e
```
or
```
username: rawnak
password: 1q2w3e
```
9.To send mail as a notification to the user to remind them to see shared note.
```
python manage.py sendremindernotification
```