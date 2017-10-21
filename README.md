# LeafletServer

Server for Zarkoix/Leaflet

## Installation

### Repository

```bash
git clone git@github.com:Zarkoix/LeafletServer.git
cd LeafletServer
# use of a virtualenv is recommended when installing python packages
pip3 install -r requirements.txt
```

### Set up Postgresql (dev)

```bash
cd dev
chmod +x createdatabase.sh
./createdatabase.sh
```

### Create migrations and migrate models

```bash
./manage.py makemigrations notebooks sections leaflets leaves users
./manage.py migrate
```

### Create admin user

```bash
./manage.py createsuperuser
# for dev, set this username and password
# username: admin
# password: rootroot
```

### Set up Google Auth (dev)

1. go to [http://localhost:8000/admin/](http://localhost:8000/admin/) in browser
2. login with admin user credentials
3. click on 'sites'
4. on the site marked 'example.com'
5. change the domain and display name to 'localhost:8000'
6. click on 'home'
7. add a new social application
    * provider: Google
    * name: Google App
    * Client id: \$ID\$.apps.googleusercontent.com
    * secret key: \$SECRET KEY\$
    * sites: localhost:8000
    * click on save

## Convention and linting

### Editorconfig

* .editorconfig

### Python

* .pylintrc

### Markdown

* .mdlrc
* .mdl_style.rb

## Run server

```bash
python3 manage.py runserver
# or
./manage.py runserver
```
