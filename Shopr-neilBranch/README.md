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
### Connect to Amazon MySQL RDS via Terminal

```sh
$ mysql -h userdata.cyctvmvxfbyc.us-west-2.rds.amazonaws.com -P 3306 -u admin -p
#Password is "sahilpujari"
```

### Set up Migrations (Don't unless we're ready to get to Production instance)

```sh
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```
