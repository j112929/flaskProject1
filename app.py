# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
# if __name__ == '__main__':
#     app.run()

import pymongo as pymongo
from bson.objectid import ObjectId
# let's import the flask
from flask import Flask, render_template, request, redirect, url_for
import os # importing operating system module

app = Flask(__name__)
# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


MONGODB_URI = 'mongodb+srv://j1129290218:hGhysam5E899vDbA@cluster0.zuw12uv.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)

# print(client.list_database_names())
# db = client.thirty_days_of_python
# Creating students collection and inserting a document
# db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
# print(client.list_database_names())

# students = [
#         {'name':'David','country':'UK','city':'London','age':34},
#         {'name':'John','country':'Sweden','city':'Stockholm','age':28},
#         {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
#     ]
# for student in students:
#     db.students.insert_one(student)

db = client['thirty_days_of_python'] # accessing the database
# student = db.students.find_one()
# student = db.students.find_one({'_id':ObjectId('649872bf30a64490e10428ea')})
# print(student)
# students = db.students.find()
# db.students.find().limit(3)
# students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 means not include and 1 means include
# query = {
#     "country":"Finland",
#     "city":"Helsinki"
# }
# query = {"age":{"$gt":30}}
# query = {"age":{"$lt":30}}
# students = db.students.find(query)
# for student in students:
#     print(student)

# students = db.students.find().sort('name')
# for student in students:
#     print(student)
#
#
# students = db.students.find().sort('name',-1)
# for student in students:
#     print(student)
#
# students = db.students.find().sort('age')
# for student in students:
#     print(student)
#
# students = db.students.find().sort('age',-1)
# for student in students:
#     print(student)


# query = {'age':250}
# new_value = {'$set':{'age':38}}
#
# db.students.update_one(query, new_value)
# # lets check the result if the age is modified
# for student in db.students.find():
#     print(student)

# query = {'name':'John'}
# db.students.delete_one(query)
#
# # lets check the result if the age is modified
# for student in db.students.find():
#     print(student)
db = client['thirty_days_of_python'] # accessing the database
db.students.drop()



@app.route('/') # this decorator create the home route
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods= ['GET','POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
         return render_template('post.html', name = name, title = name)
    if request.method =='POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))

if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)