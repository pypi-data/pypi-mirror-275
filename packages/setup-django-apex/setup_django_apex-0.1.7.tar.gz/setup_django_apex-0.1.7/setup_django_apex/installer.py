import os
import subprocess

def create_django_project():
    project_name = input("Enter the name of the Django project: ")
    os.makedirs(project_name, exist_ok=True)
    subprocess.run(["django-admin", "startproject", project_name], cwd=project_name)

if __name__ == "__main__":
    create_django_project()
