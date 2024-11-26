import random
from datetime import timedelta

from faker import Faker

from db import RoomType, Room, Guest, Booking

fake = Faker()


def generate_room_types(session, num=5):
    for _ in range(num):
        room_type = RoomType(
            type_name=fake.word(),
            description=fake.sentence()
        )
        session.add(room_type)
    session.commit()


def generate_rooms(session, num=10, room_types_count=5):
    for _ in range(num):
        room = Room(
            room_number=fake.unique.random_number(digits=3),
            room_type_id=random.randint(1, room_types_count),
            price_per_night=random.randint(50, 300),
            status=random.choice(["Available", "Booked", "Maintenance"])
        )
        session.add(room)
    session.commit()


def generate_guests(session, num=20):
    for _ in range(num):
        guest = Guest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            passport_number=fake.unique.random_number(digits=9),
            phone_number=fake.phone_number(),
            email=fake.email()
        )
        session.add(guest)
    session.commit()


def generate_bookings(session, num=15, rooms_count=10, guests_count=20):
    for _ in range(num):
        check_in_date = fake.date_this_year(before_today=False, after_today=True)
        check_out_date = check_in_date + timedelta(days=random.randint(1, 7))

        booking = Booking(
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            room_id=random.randint(1, rooms_count),
            guest_id=random.randint(1, guests_count)
        )
        session.add(booking)
    session.commit()
