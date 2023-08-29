# -*- UTF-8 -*-

"""Function that takes a language code as input and returns the user/users who speak that language.
If the language is not in the user's list of languages,
it defaults to the user with the most languages from the user list.
"""
# It uses random to randomise the user if three are more than one user
import random


class User:
    """Create the User class for user classification purposes"""
   
    def __init__(self, name, langs: list):
        """
        Initialise User to name and land as a List
        :param name:
        :param langs:
        """
        self.langs = langs
        self.name = name


def get_user(language, users: list):
    """
    Get a language and a list, uses a list comprehension to get the users with the required language
    :param language: The language to look up in the users as List argument
    :param users: List of users
    :return: Return a random choice of the list_users if there is not a user for the language returns None
    """
    list_users = [a_user.name for a_user in users if language in a_user.langs]

    # Returns the user, random choice to return different user each time. If no language is found return None
    try:
        return random.choice(list_users) if list_users else None
    
    except IndexError as e:
        print(f"{e}:, returning None")
        return None
