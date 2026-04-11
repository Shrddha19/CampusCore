from flask import Blueprint,redirect,render_template,url_for,request,jsonify
from database import student
view=Blueprint("view",__name__)
@view.route("/view",methods=(["GET","POST"]))
def views():
    if request.method=="POST":
        name=request.form["name"]
        rollno=request.form["no"]
        if name=="" or rollno=="":
            return "invalid name or roll no"
        else:
            conn2=student()
            view="select *from students where prn=%s "
            
            cur2=conn2.cursor()
            cur2.execute(view,(rollno,))
            data=cur2.fetchone()
        
            if data:
                return jsonify({
                    "Name": data[0],
                    "Roll_no":data[1],
                    "Course":data[2],
                    "Mark":data[3]  })
                
            else:
                return "No Data Found "
        
    return render_template("view.html")    
            
        