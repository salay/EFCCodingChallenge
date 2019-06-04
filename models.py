import datetime
from peewee import *
import os
from playhouse.db_url import connect

DATABASE = PostgresqlDatabase('flourdeliveries')

class Location(Model):
    name = CharField()
    address = CharField()

    class Meta:
        database = DATABASE

class Truck(Model):
    region = CharField()
    flourCapacity = IntegerField()

    class Meta:
        database = DATABASE

class Deliveries(Model):
    truck = ForeignKeyField(model=Truck)
    location = ForeignKeyField(model=Location)
    deliveryDatetime = DateTimeField(default=datetime.datetime.now)
    flourAmt = IntegerField()

    class Meta:
        database = DATABASE
        order_by = ('-deliveryDatetime',)
    

# class Appointment(Model):
#     counselor = ForeignKeyField(model=User)
#     client = ForeignKeyField(model=User)
#     date = DateTimeField()
#     time = CharField()
#     #time = DateTimeField(default=datetime.datetime.now)

#     class Meta:
#         database = DATABASE

#     @classmethod
#     def create_appointment(cls, counselor, client, date, time):
#         try:
#             cls.create(
#                 counselor=counselor,
#                 client=client,
#                 date=date,
#                 time=time
#             )
#         except IntegrityError:
#             raise

            
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Location, Truck, Deliveries], safe=True)
    DATABASE.close()
