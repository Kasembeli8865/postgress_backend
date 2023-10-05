from flask import Flask
from flask_migrate import Migrate
from models import db
from routes import main
from routes import hospital_routes
from seed import seed_data

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#postgres://lionel_kasembeli_user:uDab0goDF3Lo66TOLYBKJzSRbKYQFFo6@dpg-ckfj2oo4sbec73coven0-a.oregon-postgres.render.com/lionel_kasembeli

# Use the db object that you imported and initialized from models.py
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(main)
app.register_blueprint(hospital_routes)

@app.route('/')
def index():
    return 'Welcome to the MediFinder application!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
