from flask import Flask, request, render_template
from sqlite import *

#user = user(name='rajesh2342',fullname='rajeshkumar2324',password='rajesh342123')
#ses.add(user)
#ses.commit()

app=Flask(__name__,template_folder='templates')
@app.route("/python/<appname>")
def web(appname):
    return "this is the flask web developement %s" %appname

@app.route("/",methods=['GET','POST'])
def post():
    name = ''
    full_name = ''
    pwd=''
    if request.method == 'POST':
        name = request.form['name']
        full_name = request.form['full_name']
        pwd = request.form['password']
        users = user(name=name,fullname=full_name,password=pwd)
        ses.add(users)
        ses.commit()
    return render_template('getdetail.html',name=name,fullname=full_name,password=pwd)

@app.route("/showpost", methods=['GET','POST'])
def showpost():
    if request.method =='POST':
        return "Post method is POST"
    else:
        return "Method is GET"

@app.route("/templates/<name>")
def template(name):
    return render_template('getdetail.html',name=name)
    
if __name__=="__main__":
    app.run(debug=True)
