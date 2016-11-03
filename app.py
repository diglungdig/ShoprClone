from flask import Flask, session, redirect, url_for, escape, request, render_template
from flask.ext.bcrypt import Bcrypt
from flask_oauth import OAuth
from decimal import Decimal
import MySQLdb


#Facebook Login Setup
SECRET_KEY = 'Shopr spelt without an e'
DEBUG = True
FACEBOOK_APP_ID = '878577035610496'
FACEBOOK_APP_SECRET = 'ffdd55e74cc7a0e0018a59f80df52991'

#App initialization
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY

#Objects required by the app
oauth = OAuth()
bcrypt = Bcrypt(app)

#Facebook Setup
facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)

#Database Setup
cnx = {'host': 'userdata.cyctvmvxfbyc.us-west-2.rds.amazonaws.com',
  'username': 'admin',
  'password': 'sahilpujari',
  'db': 'shopr',
  'port': '3306'}

#Connect to database
db = MySQLdb.connect(cnx['host'],cnx['username'],cnx['password'], cnx['db'])
cursor = db.cursor()

#Products DB Setup
cnx2 = {'host': 'shoprdevdb.c3qsazu8diam.us-east-1.rds.amazonaws.com',
  'username': 'shopradmin',
  'password': 'shopradmin',
  'db': 'shopr',
  'port': '3306'}

#Connect to products db
db2 = MySQLdb.connect(cnx2['host'],cnx2['username'],cnx2['password'],cnx2['db'])
cursor2 = db2.cursor()

print 'connected'

@app.route('/')
def hello_world():
    if 'user_id' in session:
        return render_template('index.html')
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * \
            FROM users \
            WHERE username='" + username + "' AND \
            password='" + password + "';")
        data = cursor.fetchone()
        if data is None:
            return render_template('login.html', message = "Username or Password is wrong")
        else:
            session['user_id'] = data[0]
            return redirect('/')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')

@app.route('/loginFacebook')
def LoginFacebook():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))

@app.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    #Login failed
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    me = facebook.get('/me')
    #Successfully logged in
    return 'Logged in as id=%s name=%s redirect=%s' % \
        (me.data['id'], me.data['name'], request.args.get('next'))

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')


@app.route('/register', methods=['GET', 'POST'])
def Register():
    if request.method == 'POST':
        username = request.form['UserName']
        password = request.form['Password']
        firstname = request.form['FirstName']
        lastname = request.form['LastName']
        email = request.form['Email']
        query = "SELECT username from users where username='" + username + "';"
        cursor.execute(query)
        data = cursor.fetchone()
        if data is None:
            query = "INSERT INTO users ( " \
                       "username, " \
                       "firstname," \
                       " lastname, " \
                       "email, " \
                       "password ) values " \
                       "( \"" \
                    + username + "\", \"" \
                    + firstname + "\", \"" \
                    + lastname + "\", \"" \
                    + email + "\", \"" \
                    + password \
                    + "\" )"
            cursor.execute(query)
            db.commit()
            return "Created account for " + username
        else:
            return "Credentials already exist"
    else:
        return render_template('register.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method =='POST':
	productId = request.form['productId']
	addToCart(productId, 1)
	return redirect('/cart')
    elif request.args.get('q') is not None:
        addHistory(request.args.get('q'))

        filters = []
        if request.args.get('type') is not None:
            filters.append("type='" + request.args.get('type') + "'")
        if request.args.get('max_price') is not None:
            filters.append("sale_price < " + request.args.get('max_price'))
        if request.args.get('min_price') is not None:
            filters.append("sale_price > " + request.args.get('min_price'))
        if request.args.get('vendor') is not None:
            filters.append("vendor='" + request.args.get('vendor') + "'")
        if request.args.get('product_id') is not None:
            filters.append("product_id='" + request.args.get('product_id') + "'")

        query = "SELECT ds, upc, name, regular_price, sale_price, image, thumbnail, short_desc, \
                        long_desc, cust_review_count, cust_review_avg, vendor, category_path \
            FROM products \
            WHERE name LIKE '%" + request.args.get('q') + "%'"

        for filter in filters:
            query += (" AND " +  filter)

        query += " LIMIT 25;"
        cursor2.execute(query)
        data = cursor2.fetchall()
        return render_template('search.html', search = request.args.get('q'), items = data)
    else:
        return redirect('/')

    
    
@app.route('/product', methods=['GET', 'POST'])
def product():
    if request.method =='POST':
        #upc = request.form['UPC']
        upc=request.args.get('my_var', None)
        print(upc)
        return render_template('product.html')
    else:
        return redirect('/')

    
    
@app.route('/history')
def history():
    if 'user_id' in session:
        query = "SELECT search \
            FROM history \
            WHERE user_id='" + str(session['user_id']) + "' \
            ORDER BY time DESC \
            LIMIT 10;"
        cursor.execute(query)
        data = cursor.fetchall()
        return render_template('history.html', items = data)
    else:
        return redirect('/login')

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if 'user_id' in session:
        if request.method == 'POST':
            if request.form['product_id'] is not None and request.form['quant'] is not None:
                addToCart(request.form['product_id'], request.form['quant'])
        else:
            query = "SELECT a.name, b.quant \
                FROM products a, shopping_cart b \
                WHERE b.user_id='" + str(session['user_id']) + "' \
                AND a.product_id=b.product_id \
                ORDER BY time DESC \
                LIMIT 25;"
            cursor.execute(query)
            data = cursor.fetchall()
            return render_template('cart.html', items = data)
    else:
        return redirect('/login')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        realname = request.form['realname']
        email = request.form['email']
        comments = request.form['comments']
        query = "INSERT " \
                "INTO feedback " \
                "VALUES('%s','%s','%s');" % (realname, email, comments)
        cursor.execute(query)
        db.commit()
        return redirect('/')
    else:
        return render_template('feedback.html')

@app.route('/wishlist', methods=['GET', 'POST'])
def wishlist():
    if request.method == 'POST':
        productID = request.form['productID']
        query = "INSERT " \
                "INTO wishlist " \
                "VALUES('%s','%s', NOW());" % (str(session['user_id']), productID)
        cursor.execute(query)
        db.commit()
        return redirect('/wishlist')
    else:
        query = "SELECT * FROM wishlist WHERE user_id='" + str(session['user_id']) + "';"
        print query
        cursor.execute(query)
        data = cursor.fetchall()
        return render_template('wishlist.html', items = data)

@app.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query = "UPDATE users " \
                "SET PASSWORD='%s' " \
                "WHERE username='%s';" % (password, username)
        cursor.execute(query)
        db.commit()
        return render_template('login.html', message = "New password was set for account:" + username)
    else:
        return render_template('forgotPassword.html')

def addToCart(product_id, quant):
    if 'user_id' in session:
        query = "INSERT INTO shopping_cart \
            VALUES('" + str(session['user_id']) + "', \
                %s, \
                %s, \
                NOW());" % (product_id, quant)
        cursor.execute(query)
        db.commit()

def addHistory(search):
    if 'user_id' in session:
        query = "INSERT INTO history \
            VALUES('" + str(session['user_id']) + "', \
                '" + search + "', \
                NOW());"
        cursor.execute(query)
        db.commit()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
