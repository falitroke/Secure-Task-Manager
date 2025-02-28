"""Secure Task Manager Flask Backend"""
from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///tasks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET', 'supersecretkey')
db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app)  # Enable CORS for React frontend

# Task Model
class Task(db.Model):
    """Task database model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    assignee = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert task to dictionary"""
        return {"id": self.id, "title": self.title, "assignee": self.assignee}

# Routes
@app.route('/')
def serve_frontend():
    """Serve the React frontend"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/login', methods=['POST'])
def login():
    """Authenticate user and return JWT"""
    data = request.get_json()
    # Demo credentials (replace with proper user auth in production)
    if data.get('username') == 'admin' and data.get('password') == 'securepass':
        token = create_access_token(identity='admin')
        return jsonify({'access_token': token}), 200
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    """Retrieve all tasks"""
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

@app.route('/api/tasks', methods=['POST'])
@jwt_required()
def create_task():
    """Create a new task"""
    data = request.get_json()
    if not data.get('title') or not data.get('assignee'):
        return jsonify({'error': 'Title and assignee are required'}), 400
    task = Task(title=data['title'], assignee=data['assignee'])
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Initialize database tables
    app.run(host='0.0.0.0', port=5000, debug=True)