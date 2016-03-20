"""Factory to create Log, Ship, and User instances."""

from logs.models import Ship, Log
from django.contrib.auth.models import User
import random


NAMES = [
    'Teisha Belmont',
    'Britteny Centrich',
    'Keira Diseth',
    'Victorina Macbeth',
    'Carylon Ryant',
    'Ardelia Smith',
    'Phoebe Tindal',
    'Neomi Diseth',
    'Evelynn Dewitt',
    'Makeda Phillips',
    'Maddie Wakeman',
    'Allyn Bechtel',
    'Lorilee McLaren',
    'Maddie McLaren',
    'Lindsy Ducote',
    'Merissa Linkovich',
    'Natalya Alder',
    'Victorina Gammon',
    'Veronika Irani',
    'Katherina Bowdoin',
    'Walton Foxwell',
    'Raphael Vanlaere',
    'Isaias Leath',
    'Darwin Calder',
    'Stefan Wynn',
    'Chet Vilchis',
    'Raphael Buccheri',
    'Rory Barick',
    'Galen Corwin',
    'Malik Corwin',
    'Walton Foxwell',
    'Lucius Kinton',
    'Alden Paulsen',
    'Lenard Volante',
    'Benedict Kehoe',
    'Dante Kehoe',
    'Merlin Dowe',
    'Scotty Paulsen',
    'Willian Sarratt',
    'Jacinto Cantos',
]


def create_user(**extra_fields):
    """Create a django User."""
    username = random.choice(NAMES)
    first_name, last_name = username.split(' ')
    email = '{}@usstartfleet'.format(first_name.lower())
    created = False
    retry = 3
    defaults = {
        'username': username,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
    }
    defaults.update(extra_fields)
    while not created and retry:
        user, created = User.objects.get_or_create(**defaults)
        retry -= 1

    return user
