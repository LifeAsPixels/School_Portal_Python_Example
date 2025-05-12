cd $PSScriptRoot

$name = "School_Portal_Django"

django-admin startproject $name
cd $name
python manage.py startapp core
