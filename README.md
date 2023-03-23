This is a django website inspired by self-paced learning tutorials.

The project is developed in Python 3.11.0rc2 and Django 4.1.7.   
  
Sequence of steps:  
1. Create project in PyCharm with venv;  
2. Git initialization with .gitignore file:
```
git init
touch .gitignore
```
3. Write into a file .gitignore:
>.idea/  
/venv/
4. Upgrade pip and packages for last version:  
```commandline  
pip install --upgrade pip  
pip install --upgrade setuptools  
pip install --upgrade wheel  
```  
5. Install Django web framework:  
```commandline  
pip install django  
```  
6. Create new site project "mysite":  
```commandline  
django-admin startproject mysite 
```
7. Start test server:
```
cd mysite
python manage.py migrate
python manage.py runserver
```

