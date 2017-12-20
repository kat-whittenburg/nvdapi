

# NVDAPI

NVDAPI is a JSON REST API project to share the list of vulnerabilities of the [National Vulnerability Database]

It provides a method to list and detail CVEs and some filters/searchs as well.

Installation directions are written for Ubuntu 16.04.

Before you begin, please run the following command: `sudo apt-get update`

## Dependencies

- Pip (`sudo apt install python-pip` and `pip install --upgrade pip`)
- Virtualenv (```sudo pip install virtualenv```)
- Unzip utility (`sudo apt-get install unzip`)
- Postgres (`sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib`)

## Installation

```sh
git clone https://github.com/Diviei/nvdapi.git
cd nvdapi
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a file called `local_settings.py` inside nvdapi folder (where settings.py is) and add your SECRET_KEY. (If you don't have one, you can create one [here].

```python
SECRET_KEY = "whatever"
```

And now run the migrations

```sh
python manage.py migrate
```

[National Vulnerability Database]: <https://nvd.nist.gov/>
[here]: <https://www.miniwebtool.com/django-secret-key-generator/>
