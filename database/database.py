from peewee import IntegrityError
from .model import Park


def save_park(park):
    try:
        park.save()
    except IntegrityError:
        return "Data already in database." #TODO make this better


def get_parks_by_state(state):
    parks = Park.select().where(Park.park_state == state).execute()
    return parks


def get_park_by_code(code):
    park = Park.get_or_none(Park.park_id == code)
    return park






