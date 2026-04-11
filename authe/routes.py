from flask import Blueprint,render_template,redirect,url_for,request,session,flash
from werkzeug.security import generate_password_hash,check_password_hash
from database import logins

authe=Blueprint("authe",__name__)
@authe.route("/",methods=["GET","POST"])
def sign():
    if request.method=="POST":
        name=request.form["name"]
        password=request.form["password"]
        if name=="" or len(password)<=6:
            flash("Plz enter name or password")
        else:
            
            new_pass=generate_password_hash(password)
            insert="insert into login values(%s,%s)"   
            val=(name,new_pass)
            conn1=logins()
            cur1=conn1.cursor()
            cur1.execute(insert,val)
            conn1.commit()
            conn1.close()
            flash("Account Created  Succcesfully")
            return redirect(url_for("select.sel"))
    return render_template("signin.html")
    
@authe.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
       name=request.form["name"]
       pwd=request.form["password"]
       if name=="" or len(pwd)<=6:
         return "invalid email or password"
    
       else:
        
        insert="select *from login where name=%s"   
        
        conn1=logins()
        cur1=conn1.cursor()
        cur1.execute(insert,(name,))
        data=cur1.fetchone()
        
        conn1.close()
        if data and check_password_hash(data[1],pwd):
              session['user']=name
              return redirect(url_for("select.sel"))
            
        else:
            return "invalid login"    
        
         
    return render_template("login.html")     

