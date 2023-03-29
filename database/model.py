from peewee import Model, CharField, Check, SqliteDatabase, DecimalField
from .config import db_path


db = SqliteDatabase(db_path)


class BaseModel(Model):
    class Meta:
        database = db


class Park(BaseModel):
    park_id = CharField(unique=True, constraints=[Check('length(park_id) <= 500')])
    name = CharField(null=False, constraints=[Check('length(park_name) <= 500')]) 
    park_city = CharField(null=False, constraints=[Check('length(park_city) <= 500')])
    state_code = CharField(null=False, constraints=[Check('length(park_city) <= 500')])
    park_code = CharField(null=False, constraints=[Check('length(park_city) <= 500')])
    phone = CharField(null=False, constraints=[Check('length(park_city) <= 500')])
    email = CharField(null=False, constraints=[Check('length(park_city) <= 500')])
    park_state = CharField(null=False, constraints=[Check('length(park_state) <= 500')]) 
    description = CharField(null=False, constraints=[Check('length(park_description) <= 1000')])
    latitude = DecimalField(null=False, constraints=[Check('length(latitude) <= 500')])
    longitude = DecimalField(null=False, constraints=[Check('length(longitude) <= 500')])


    def __str__(self):
        return f"{self.park_id} {self.park_name} {self.park_city} {self.park_state} {self.park_description} {self.latitude} {self.longitude}"


    def dump(self):
        return {"park": {"id": self.park_id,
                          "name": self.park_name,
                          "city": self.park_city,
                          "state": self.park_state,
                          "description" : self.park_description,
                          "latitude" : self.latitude,
                          "longitude" : self.longitude
                          }}


def create_db():
    db.connect()
    db.create_tables([Park])
    