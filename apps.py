from flask import Flask ,redirect,render_template,url_for
from werkzeug.security import generate_password_hash,check_password_hash
def create_app():
    app=Flask(__name__)
    app.secret_key="shradha19"
    from authe.routes import authe
    from operation.add import operation
    from option.select import select
    from operation.view import view
    from operation.update import update
    from operation.delete import delete
    from authe.logout import logout
    
    
    app.register_blueprint(authe)
    app.register_blueprint(operation)
    app.register_blueprint(select)
    app.register_blueprint(view)
    app.register_blueprint(update)
    app.register_blueprint(delete)
    app.register_blueprint(logout)
    
    return app