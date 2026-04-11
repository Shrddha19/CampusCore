from flask import Blueprint,render_template,redirect,url_for,request,session
select=Blueprint("select" ,__name__)
@select.route("/option",methods=["GET","POST"])
def sel():
    if "user" in session:
      return redirect(url_for("select.sel"))

    return render_template("option.html")
    