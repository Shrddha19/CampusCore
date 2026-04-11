from flask import Blueprint,redirect,url_for,session
logout=Blueprint("logout" ,__name__)
@logout.route("/logout",methods=["GET","POST"])
def log():
    if session.pop('user',None):
      return redirect(url_for("/"))
    