# mv-draft-backend

This backend program was created in [Python 3.7.3](https://www.python.org/downloads/release/python-373/). Full compatibility can be expected with at least Python 3.6 and pip 20 (lower pip versions means you will have to sift through requirements.txt to look for older versions of packages that may not work).

Live API: [http://itskevm.pythonanywhere.com/api/]\
Admin: [http://itskevm.pythonanywhere.com/admin/]

## Installation
1. With python and pip installed, clone the repository and navigate into the directory.
2. In the root directory, install (or update if already installed) virtualenv by running: `pip install virtualenv`
3. Initialize this virtual environment (keep out of source control): `virtualenv env`
4. Source the virtual environment.\
MacOS and Linux: `source env/bin/activate`\
Windows: `.\env\Scripts\activate`\
5. Install the needed packages using pip: `pip install -r requirements.txt`
6. Navigate to the src folder and start the backend server: `python manage.py runserver`

Note! If needed, virtualenv can be turned off when a terminal is not running a process, by using: `deactivate`


## List of resources
[editing the vscode settings json](https://supunkavinda.blog/vscode-editing-settings-json#workspace)\
[setting python 3.7.3 as global default on macOS](https://opensource.com/article/19/5/python-3-default-mac)\
[deciding to choose virtualenv over venv](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)\
[reinstalling pip properly](https://ahmadawais.com/install-pip-macos-os-x-python/)\
[initializing a dj server](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)\
[understanding the need for dj migrations](https://docs.djangoproject.com/en/3.1/ref/django-admin/#django-admin-migrate)\
[example on default values for models](https://tutorial.djangogirls.org/en/django_models/)\
[fix security concern](https://stackoverflow.com/questions/31883505/how-to-i-hide-my-secret-key-using-virtualenv-and-django/31883650#31883650)\
[how to properly store the env](https://docs.activestate.com/platform/projects/requirements-txt/)\
[reinstalling the env](https://stackoverflow.com/questions/9586346/virtualenv-and-source-version-control)\
[understanding static files on pythonanywhere](https://stackoverflow.com/questions/42970053/how-do-i-get-to-collect-static-files-i-cant-run-this-project-it-raises-the-err#comment73033415_42970283)\
[deploying backend source code to pythonanywhere](https://www.youtube.com/watch?v=Y4c4ickks2A)