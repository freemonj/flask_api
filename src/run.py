from flask import Flask
import traceback
import argparse
import sys

def create_app(config_filename):
    """
    Instantiates the Flask instance and associated parameters.
    :params: configuration filename
    :return: flask app
    :rtype: flask object
        """         
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from Model import db
    with app.app_context():
        db.init_app(app)
        db.create_all([None])
    return app


if __name__ == "__main__":    
    assert (sys.version_info >= (3,0,0)), "python version 3.x is required!"
    if len(sys.argv) > 1:
        print("Usage:")
        print("python run.py ")
        sys.exit()
    try:
        #cliparser = argparse.ArgumentParser(description="Flask IP Address API")
        app = create_app("config")
        app.run(ssl_context="adhoc",debug=True)        
    except:
        if len(sys.argv) <= 1:
            print("error trace = {}".format(traceback.format_exc()))
        else:
            print("error trace = {}".format(traceback.format_exc()))
    