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

if __name__ == "__main__":
    create_django_project()
