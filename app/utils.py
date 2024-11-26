from app.db import Booking, Room, Guest, RoomType


def clear_data(session):
    session.query(Booking).delete()
    session.query(Room).delete()
    session.query(Guest).delete()
    session.query(RoomType).delete()
    session.commit()
    print("Data cleared successfully.")
