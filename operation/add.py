from flask import Blueprint,render_template,redirect,request,url_for,flash,session,Flask
from database import student
operation=Blueprint("operation",__name__)
@operation.route("/add",methods=["GET","POST"])
def add():
    

    if request.method=="POST":
       
            
          studentn=request.form["student"]
          Prn=request.form["PRN"]
          Course=request.form["course"]
          Mark=request.form["mark"]
          if studentn=="" or Prn=="" or Course=="" or Mark=="":
            flash ("Plz enter all value")
          else:
            
            add="insert into students values(%s,%s,%s,%s)"
            val=(studentn,Prn,Course,Mark)
            conn2=student()
            cur2=conn2.cursor()
            cur2.execute(add,val)
            conn2.commit()
            conn2.close()
            
            flash("Added succesfully")
        
            
    return render_template("add.html")   