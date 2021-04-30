from warnings import resetwarnings
from flask import Flask, render_template, redirect, request
from flask.globals import request
from werkzeug.utils import escape
from forms import SignUpForm, WeightForm

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


import algoImp as al

################## NEW ########################
from sqlite3 import Error
import sqlite3
import storeWk as archive
################## NEW ########################



app = Flask(__name__)
app.config['SECRET_KEY'] = 'guacbanana'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userEntry2.db'
db = SQLAlchemy(app)

#go back to here for for loops, to loop through the program and print it to the page https://www.youtube.com/watch?v=xh3mFxbnc4o&list=PLB5jA40tNf3vX6Ue_ud64DDRVSryHHr1h&index=4

@app.route('/')
def home():
    return (render_template('homepage.html'))

@app.route('/about')
def about():
    return (render_template('about.html'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form

        wk = al.workoutGen()
        wkls = None
        while(True):
            try:
                wkls = wk.generator(result.get("sport").lower().strip(), result.get("skillLevel").lower().strip())
                break
            except:
                pass

        wk1,wk2 = wk.formatter(wkls.wk)

        ################## NEW ########################

        archive.archive().archive(wk1,wk2,result.get("email")) #archiving the workout
 
        ################## NEW ########################
        
        return render_template('display.html', wk1=wk1, wk2=wk2, fName = result.get("first_name"), lName = result.get("last_name"), email = result.get("email"))


    return render_template('signup.html', form=form)

    #pass the arrays into the html page as variables as jinja. Reference the about page

@app.route('/retrieve', methods=['GET', 'POST'])
def retrieve():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form

        try:
            wk1,wk2 = archive.archive().get(result.get("email"))

        except:
            return render_template('errorFound.html', err="The email address given doesn't exist within the database. It's likely a typo or an initial workout hasn't been generated yet")

        print("Workout for {} retreived".format(result.get("email")))

        return render_template('display.html', wk1=wk1, wk2=wk2, fName = "Archived", lName = "Result", email = result.get("email"))


    return render_template('retrieve.html', form=form)

@app.route('/addWeight/<email>', methods=['GET', 'POST'])
def addWeight(email):
    form = WeightForm()
    if form.is_submitted():
        result = request.form
        if result.get("wk1ex1") != "" and result.get("wk1ex2") != "":
            archive.archive().adjustWeight(email,0,0,result.get("wk1ex1"))
            archive.archive().adjustWeight(email,0,1,result.get("wk1ex2"))
            archive.archive().adjustWeight(email,0,2,result.get("wk1ex3"))
            archive.archive().adjustWeight(email,0,3,result.get("wk1ex4"))

            try:
                wk1,wk2 = archive.archive().get(email)

            except:
                return render_template('errorFound.html', err="Matthew dun goofed")

            return render_template('display.html', wk1=wk1, wk2=wk2, fName = "Archived", lName = "Result", email = result.get("email"))

            

        elif result.get("wk2ex1") != "" and result.get("wk2ex2") != "":
            archive.archive().adjustWeight(email,1,0,result.get("wk2ex1"))
            archive.archive().adjustWeight(email,1,1,result.get("wk2ex2"))
            archive.archive().adjustWeight(email,1,2,result.get("wk2ex3"))
            archive.archive().adjustWeight(email,1,3,result.get("wk2ex4"))
            
            try:
                wk1,wk2 = archive.archive().get(email)

            except:
                return render_template('errorFound.html', err="Matthew dun goofed")

            return render_template('display.html', wk1=wk1, wk2=wk2, fName = "Archived", lName = "Result", email = result.get("email"))

        else:
            return render_template('errorFound.html', err="Both exercise's weights were left blank")


    try:
        wk1,wk2 = archive.archive().get(email)

    except:
        return render_template('errorFound.html', err="If you're seeing this then Matthew has royally fucked up ¯\_(ツ)_/¯")

    return render_template('addWeight.html', form=form, wk1=wk1,wk2=wk2)

@app.route("/submitWeight",methods=["POST","GET"])
def submitWeight():
    if request.method == "POST":
        todo = request.form.get("todo")
        email = request.form.get("email")
        wkNum = int(request.form.get("workout"))
        exNum = int(request.form.get("exNum"))

        print("email: {}, workout number: {}, exercise number: {}, weight: {}".format(email,wkNum,exNum,todo))

        #print(todo,email,wkNum,exNum)
        archive.archive().adjustWeight(email,wkNum,exNum,todo)

    return render_template('weightTest.html')
  
@app.route("/success",methods=["POST","GET"])
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run()


"""
        try:
            #sqlExe = "INSERT INTO userInfo({},{},{},{});".format(result.get("first_name"), result.get("last_name"), result.get("email"),result.get("sport"))
            #print(sqlExe)
            sqlExe = 'INSERT INTO "main"."userInfo"("first_name","last_name","email","sport") VALUES ("{}","{}","{}","{}");'.format(result.get("first_name"), result.get("last_name"), result.get("email"),result.get("sport"))
            db.session.execute(sqlExe)
            db.session.commit()

            print("Your info was successfully added")

        except Exception as e:
            print("Your query couldn't be inserted into the databse because: {}".format(e))


        #print(result)
        return render_template('user.html', result=result)

        """

"""
@app.context_processor
def utility_processor():
    def updateWeight(email,wkNum,exNum,weight):

        return archive.archive().adjustWeight(email,wkNum,exNum,weight)

    return dict(format_price=updateWeight)


#rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    #archive.archive().adjustWeight(email,wkNum,exNum,weight)
    print("meow")
    return ("nothing")
"""