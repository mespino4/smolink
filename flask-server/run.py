from app.routes import app  # Importing 'app' instance from routes.py in the app package
from app.models import Urls, db
from flask_cors import CORS

# Configuration
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smolink.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/smolink'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)
with app.app_context():
    db.create_all()

# Enable CORS for all routes
#CORS(app, resources={r"/shorten": {"origins": "*", "methods": ["GET", "POST"]}})
#CORS(app, resources={r"/shorten": {"origins": "*"}})
CORS(app, origins=["http://localhost:5173"])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
    #app.run(port=5000, debug=True)