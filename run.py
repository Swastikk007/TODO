from app import create_app, db
from app.model import Task
from app.model2 import user_credentials
 
app = create_app()
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug = True)