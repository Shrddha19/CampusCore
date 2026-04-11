from flask import Blueprint,request,render_template
from database import student
delete=Blueprint("delete",__name__)
@delete.route("/delete" , methods=["GET","POST"])
def dele():
    if request.method=="POST":
      rno=request.form["roll"]
      if rno=="":
          return "invalid roll_no"
      else:
          conn2=student()
          cur2=conn2.cursor()
          delete="delete from students where prn=%s"
          cur2.execute(delete,(rno,))
          return "Data Deleted"
      
    return render_template("delete.html")  