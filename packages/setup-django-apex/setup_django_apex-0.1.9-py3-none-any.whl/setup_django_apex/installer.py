import os
import subprocess

def create_django_project():
    project_name = input("Enter the name of the Django project: ")
    subprocess.run(["django-admin", "startproject", project_name])
    
    # Change to the project directory
    os.chdir(project_name)
    
    # Ask for the number of apps and their names
    num_apps = int(input("How many apps do you want to create? "))
    app_names = []
    for _ in range(num_apps):
        app_name = input("Enter the name of the app: ")
        app_names.append(app_name)
        subprocess.run(["django-admin", "startapp", app_name])

    # Update the settings.py file to include the new apps
    settings_path = os.path.join(project_name, "settings.py")
    with open(settings_path, 'r') as file:
        settings_content = file.readlines()

    with open(settings_path, 'w') as file:
        for line in settings_content:
            file.write(line)
            if line.strip() == 'INSTALLED_APPS = [':
                for app_name in app_names:
                    file.write(f"    '{app_name}',\n")



def create_django_drf_project():
    project_name = input("Enter the name of the Django project: ")
    subprocess.run(["django-admin", "startproject", project_name])
    
    # Change to the project directory
    os.chdir(project_name)
    
    # Ask for the number of apps and their names
    num_apps = int(input("How many apps do you want to create? "))
    app_names = []
    for _ in range(num_apps):
        app_name = input("Enter the name of the app: ")
        app_names.append(app_name)
        subprocess.run(["django-admin", "startapp", app_name])

    # Update the settings.py file to include the new apps and DRF
    settings_path = os.path.join(project_name, "settings.py")
    with open(settings_path, 'r') as file:
        settings_content = file.readlines()

    with open(settings_path, 'w') as file:
        for line in settings_content:
            file.write(line)
            if line.strip() == 'INSTALLED_APPS = [':
                for app_name in app_names:
                    file.write(f"    '{app_name}',\n")
                file.write("    'rest_framework',\n")  # Add Django REST Framework

    # Create serializers.py, views.py, and urls.py in each app for implementing DRF
    for app_name in app_names:
        app_path = os.path.join(app_name)
        serializers_path = os.path.join(app_path, "serializers.py")
        with open(serializers_path, 'w') as file:
            file.write("from rest_framework import serializers\n")
            file.write("from .models import YourModel\n\n")
            file.write("class YourModelSerializer(serializers.ModelSerializer):\n")
            file.write("    class Meta:\n")
            file.write("        model = YourModel\n")
            file.write("        fields = '__all__'\n")

        views_path = os.path.join(app_path, "views.py")
        with open(views_path, 'w') as file:
            file.write("from rest_framework import viewsets\n")
            file.write("from .models import YourModel\n")
            file.write("from .serializers import YourModelSerializer\n\n")
            file.write("class YourModelViewSet(viewsets.ModelViewSet):\n")
            file.write("    queryset = YourModel.objects.all()\n")
            file.write("    serializer_class = YourModelSerializer\n")

        urls_path = os.path.join(app_path, "urls.py")
        with open(urls_path, 'w') as file:
            file.write("from django.urls import path\n\n")
            file.write("urlpatterns = [\n")
            file.write("    # Define your URL patterns here\n")
            file.write("]\n")

    print("Django DRF project setup completed.")

if __name__ == "__main__":
    create_django_project()

if __name__ == "__main__":
    create_django_project()
    create_django_drf_project()

