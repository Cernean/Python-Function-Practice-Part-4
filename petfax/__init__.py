# config                    
from flask import Flask

def create_app():

    app = Flask(__name__)

    # factory
    from . import pet
    app.register_blueprint(pet.bp)

# index route
    @app.route('/')
    def index():
        return 'This is the Home page!'  
    
    return app