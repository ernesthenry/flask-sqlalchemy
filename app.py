from flask import Flask
from flask-sqlalchemy import  SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/example'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello Ernest!'


class Person(db.Model):
    __tablename__ = "persons"
    id =  db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(), nullable=False)

if __name__ == '__main__':
    app.run()
