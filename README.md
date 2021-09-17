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
source venv/bin/activate
```
5. Install requirements 
```
pip install -r requirements.txt
```
5. Migrate 
```
python manage.py migrate
```
6.Run project 
```
python manage.py runserver
```
7.Load Data 
```
python manage.py loaddata load_data.json
```
8.Login using Credential are give in file user_credential.txt

9.To send mail as a notification to the user to remind them to see shared note.
```
python manage.py sendremindernotification
```

10. To get JWT token api import the file "TechNote.postman_collection.json" to the Postman