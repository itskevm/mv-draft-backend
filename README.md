# mv-draft-backend
## Installation
1. With python and pip installed, run the following: `pip install --user virtualenv`
2. Initialize the virtual environment you just installed (keep out of source control): `virtualenv env`
3. Source the virtual environment.\
MacOS and Linux: `source env/bin/activate`\
Windows: `.\env\Scripts\activate`\
4. Install the needed packages using pip: `pip install -r requirements.txt`
5. Run the backend server: `python manage.py runserver`
6. To stop using virtualenv, run: `deactivate`


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
[reinstalling the env](https://stackoverflow.com/questions/9586346/virtualenv-and-source-version-control)