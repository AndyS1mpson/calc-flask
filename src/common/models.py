
from app import db

class Member(db.Document):
    fitrst_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    last_request = db.IntField()

    