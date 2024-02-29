from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    #id = db.Column(db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10))

    def __init__(self, long, short):
        self.long = long
        self.short = short