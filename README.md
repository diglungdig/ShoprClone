# Shopr - Get the best deals [![Build Status](https://api.travis-ci.com/pujarisahil/Shopr.svg?token=x7P2DWhixDyxsSAFzpRR)]

### Run

Run each in a different terminal window...

```sh
# the app
$ pip install -r requirements.txt
$ npm install
# if npm install gives an issue, run it with admin rights using sudo
$ python app.py
```

### Deployment on Heroku

The web app is deployed on Heroku and can be accessed at

```sh
https://shoprtest.herokuapp.com/
```

### Connect to Amazon MySQL RDS via Terminal

```sh
$  mysql -h shoprdevdb.c3qsazu8diam.us-east-1.rds.amazonaws.com -P 3306 -u shopradmin -p
#Password is "shopradmin"
```

### Set up Migrations (Don't unless we're ready to get to Production instance)

```sh
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```
