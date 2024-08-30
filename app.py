from flask import Flask, request, jsonify,render_template,redirect,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'vwqae&(6hjeu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///delivery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    usermail = db.Column(db.String(100), unique=True, nullable=False)
    userpass = db.Column(db.String(100), nullable=False)
    def __repr__(self) -> str:
        return f"{self.username}-{self.usermail}-{self.userpass}"
    
    
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restName = db.Column(db.String(100), nullable=False)
    restLocation = db.Column(db.String(100), nullable=False)
    restHours = db.Column(db.String(50))

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restId = db.Column(db.String(100), nullable=False)
    itemName = db.Column(db.String(100), nullable=False)
    itemDescription = db.Column(db.String(500), nullable=False)
    itemPrice = db.Column(db.String(50), nullable=False)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    order_name = db.Column(db.String(100), nullable=False)
    pay_money = db.Column(db.Integer,nullable=False)


    

# Initialize Database
with app.app_context():
    db.create_all()

# Root Route
@app.route('/')
def home():
    return render_template("index.html")
# User Registration Route
@app.route('/register', methods=['POST','GET'])
def register_user():
    try:

        if request.method=='POST':
            username =request.form['username']
            usermail =request.form['usermail']
            userpass =request.form['userpass']
            new_user=User(username=username,usermail=usermail,userpass=userpass)
            db.session.add(new_user)
            db.session.commit()
            flash("scuessfully register")
        new_user_detailes=User.query.all()
        print(new_user_detailes)
    except Exception as e :
        print(e)
    finally:
       return redirect("/")


# Add Restaurant Route
@app.route('/restaurants', methods=['POST','GET'])
def add_restaurant():
    try:

        if request.method=='POST':
            restName=request.form['restName']
            restLocation=request.form['restLocation']
            restHours=request.form['restHours']
            userinput=Restaurant(restName=restName,restLocation=restLocation,restHours=restHours)
            print(userinput)
            db.session.add(userinput)
            db.session.commit()
    except Exception as e:
        flash(str(e))
    finally:
        flash("Add sucessfully.")
        return redirect("/")

@app.route('/add_manue', methods=['POST','GET'])
def add_manue():
    try:
        if request.method=='POST':
            restId=request.form['restId']
            itemName=request.form['itemName']
            itemDescription=request.form['itemDescription']
            itemPrice=request.form['itemPrice']
            user_menu=Menu(restId=restId,itemName=itemName,itemDescription=itemDescription,itemPrice=itemPrice)
            db.session.add(user_menu)
            db.session.commit()
            flash("Menu add scuessfully.")
    except Exception as e:
        flash(str(e))
    finally:
        
        return redirect("/")
       
@app.route('/order', methods=['POST','GET'])
def order():
    try:

        if request.method=='POST':
            user_name=request.form['username']
            order_name=request.form['useroder']
            pay_money=request.form['userpay']
            place_oredr=Order(user_name=user_name,order_name=order_name,pay_money=pay_money)
            db.session.add(place_oredr)
            db.session.commit()
            flash("Oder scuessfully done.")
    except Exception as e:
        flash(str(e))
    finally:
        return redirect("/")

@app.route('/menutable',methods=['POST','GET'])
def menutable():
   if request.method=='POST':
       flash("Oder scuessfully placeed.")
   totalmenu=Menu.query.all()
#    print(total)
   return  render_template("menutable.html",totalmenu=totalmenu)

    


if __name__ == '__main__':
      # Initialize the database
    app.run(debug=True)
