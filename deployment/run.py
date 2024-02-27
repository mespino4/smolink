from app import app
from app.models import db
from flask_cors import CORS

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smolink.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)
with app.app_context():
    db.create_all()

# Enable CORS for all routes
CORS(app, origins=["http://localhost:5173"])

if __name__ == '__main__':
    app.run(port=5000, debug=True)