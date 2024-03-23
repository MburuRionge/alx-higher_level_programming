#!/usr/bin/python3
"""
    A script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
 """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from relationship_state imporrt Base, State
from relationship_city import City
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.querry(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
        for city_ins in instance.cities:
            print(" ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
