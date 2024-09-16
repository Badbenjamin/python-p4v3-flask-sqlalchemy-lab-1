from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
# serializer mixin has a todict method that creates a dictionary from its attributes
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()


db = SQLAlchemy(metadata=metadata)

# needs to inherit from model
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    def __repr__(self):
        return f'<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>'
