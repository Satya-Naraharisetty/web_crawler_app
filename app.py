from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import the routes and register them
    from routes import crawl_bp
    app.register_blueprint(crawl_bp)

    return app