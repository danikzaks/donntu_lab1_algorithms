import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()


class RoomType(Base):
    __tablename__ = 'room_types'

    id = Column(Integer, primary_key=True)
    type_name = Column(String, nullable=False)
    description = Column(String)

    def __repr__(self):
        return f"<RoomType(id={self.id}, type_name={self.type_name})>"


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    room_number = Column(Integer, nullable=False, unique=True)
    room_type_id = Column(Integer, ForeignKey('room_types.id'), nullable=False)
    price_per_night = Column(Integer, nullable=False)
    status = Column(String, default="Available")

    room_type = relationship("RoomType", back_populates="rooms")

    def __repr__(self):
        return f"<Room(id={self.id}, room_number={self.room_number}, price_per_night={self.price_per_night})>"


RoomType.rooms = relationship("Room", back_populates="room_type")


class Guest(Base):
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    passport_number = Column(String, unique=True, nullable=False)
    phone_number = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"<Guest(id={self.id}, first_name={self.first_name}, last_name={self.last_name})>"


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    check_in_date = Column(Date, nullable=False)
    check_out_date = Column(Date, nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    guest_id = Column(Integer, ForeignKey('guests.id'), nullable=False)

    room = relationship("Room")
    guest = relationship("Guest")

    def __repr__(self):
        return f"<Booking(id={self.id}, check_in={self.check_in_date}, check_out={self.check_out_date})>"


def create_tables():
    Base.metadata.create_all(engine)
    print("Tables created successfully.")


def get_session():
    Session = sessionmaker(bind=engine)
    return Session()
