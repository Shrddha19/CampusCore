from flask import Blueprint,redirect,render_template,request,jsonify
from database import student
update=Blueprint("update",__name__)
@update.route("/update",methods=["POST","GET"])
def updata():
    if request.method=="POST":
        name=request.form["n"]
        roll=request.form["no"]
        mark=request.form["m"]
        if name=="" or roll=="" or mark=="":
            return "enter valid No"
        else:
            conn2=student()
            cur2=conn2.cursor()
            up="update  students set mark=%s where prn=%s"
            val=(mark,roll)
            cur2.execute(up,val)
            conn2.commit()
            sel="select *from students where prn=%s"
            cur2.execute(sel,(roll,))
            data=cur2.fetchone()
            if data:
                return jsonify(data)
            
            
    return  render_template("update.html")