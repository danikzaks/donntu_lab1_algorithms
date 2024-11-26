import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

from app.utils import clear_data
from db import Base, get_session, Booking
from generate_data import generate_room_types, generate_rooms, generate_guests, generate_bookings

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL, echo=True)


def create_tables():
    Base.metadata.create_all(engine)
    print("Tables created successfully.")


def main():
    session = get_session()

    create_tables()

    generate_room_types(session, num=5)
    generate_rooms(session, num=20)
    generate_guests(session, num=20)
    generate_bookings(session, num=15)

    bookings = session.query(Booking).all()
    for booking in bookings:
        print(booking)

    clear_data(session)

    session.close()


if __name__ == "__main__":
    main()
