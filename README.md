# Django_MyBlog
learning the django..4th project on blogging site

use anaconda prompt for window 10

1 -> conda -V          (to check conda version)

2 -> conda info --envs   (to check all environment present now)

3 -> conda create --name djangoenv python=3.7

4 -> conda activate djangoenv

5 -> conda install -c anaconda django

6 -> python -m django --version

7 -> go to project directory 

8 -> django-admin startproject 'project_name'

9 -> cd 'project_name'

10 -> python manage.py runserver

11 -> python manage.py startapp 'app_name'

12 -> some variable in setting for static files

13 -> python manage.py collectstatic

14 -> model-views-template (for dynamic)

15 -> postgresql username  = postgres and port = 5432

16 -> mysql username = root and port = 3306

17 -> open pgadmin for postgres

18 -> create model and register in setting 

19 -> conda install -c anaconda pillow (for image field)

20 -> python manage.py makemigrations (to create table)

21 -> python manage.py sqlmigrate travello(app_name) 0001(file_name) 

22 -> python manage.py migrate ( now table has created  )

23 -> python manage.py help ( for any help )

23.1 - > superuser can be created after migrate command

24 -> python manage.py createsuperuser and set username = sk007

25 -> register model to admin.py for django admin

26 -> to save uploaded files,set MEDIA_ROOT = os.path.join(BASE_DIR,'media') like template folder in settings

26.1 -> to use media in html , set MEDIA_URL = 'media' in settings

27 -> set media url to main url

28 -> to improve form use crispy-form using conda install -c conda-forge django-crispy-forms and set variable to setting for it and then load it to html file

29 -> to use inbuild login and redirect after login, then,  set LOGIN_REDIRECT_URL = 'home' in setting

30 -> to redirect login_required pages to login , set LOGIN='login' in setting

31 -> to do some automatic important task in background , create signals.py in accounts and register it in apps.py 

32 - > use ListView, updateView and DeleteView for model  

33 - > CreateView expect template path like <app_name>/<model_name>_form.html

34 -> ListView expect template path like <app_name>/<model_name>_list.html

35 -> DetailView expect template path like <app_name>/<model_name>_detail.html  
