"""Class Menu module"""

import difflib
import argparse
from enum import Enum
from collections import namedtuple
from constants import MENU_BORDER
from utils import format_cmd, format_param

Command = namedtuple("Command", ["min_required_params", "param_list", "hint"])
Parametr = namedtuple(
    "Parametr",
    ["name", "required", "hint", "choices"],
    defaults=(None, False, None, None),
)


class Menu(Enum):
    """Class"""

    HELLO = Command(0, [], "to show command list")
    ADD_CONTACT = Command(
        2,
        [
            Parametr("name", True, "contact name"),
            Parametr("phone", True, "contact phone number in format XXXXXXXXXX"),
            Parametr("email", False, "contact email address"),
            Parametr("birthday", False, "contact birthday"),
        ],
        "to add a new contact",
    )
    UPDATE_CONTACT = Command(
        3,
        [
            Parametr("name", True, "contact name"),
            Parametr("oldphone", True, "old phone number"),
            Parametr("newphone", True, "new phone number in format XXXXXXXXXX"),
        ],
        "to update a phone",
    )
    DELETE_CONTACT = Command(
        1, [Parametr("name", True, "contact name")], "to delete contact"
    )
    SET_CONTACT_BIRTHDAY = Command(
        2,
        [
            Parametr("name", True, "contact name"),
            Parametr("birthday", True, "contact birthday"),
        ],
        "to set birthday",
    )

    GET_CONTACT_BIRTHDAY = Command(
        1, [Parametr("name", True, "contact name")], "to show birthday"
    )
    GET_CONTACT_BY_NAME = Command(
        1, [Parametr("name", True, "contact name")], "to find a contact by name"
    )
    GET_CONTACT_BY_PHONE = Command(
        1,
        [Parametr("phone", True, "phone number")],
        'text": "to find a contact by phone',
    )
    GET_CONTACT_BY_EMAIL = Command(
        1,
        [Parametr("email", True, "email address")],
        'text": "to find a contact by email',
    )
    GET_ALL_CONTACTS = Command(0, [], "to view a full contact list")
    GET_UPCOMING_BIRTHDAYS = Command(
        0,
        [
            Parametr(
                "days", False, "The number of days to look ahead for upcoming birthdays"
            )
        ],
        "Get a list of upcoming birthdays within the specified number of days.",
    )
    UPDATE_CONTACT_EMAIL = Command(
        2,
        [
            Parametr("name", True, "contact name"),
            Parametr("email", True, "email address"),
        ],
        "to update email",
    )
    ADD_ADDRESS = Command(
        2,
        [
            Parametr("name", True, "contact name"),
            Parametr(
                "addresstype",
                False,
                "address type (Home,Work,Other)",
                ["Home", "Work", "Other"],
            ),
            Parametr("street", False, "street"),
            Parametr("city", False, "street"),
            Parametr("postalcode", False, "street"),
            Parametr("country", False, "street"),
        ],
        "add or edit contact address",
    )
    DELETE_ADDRESS = Command(
        2,
        [
            Parametr("name", True, "contact name"),
            Parametr(
                "addresstype",
                False,
                "address type (Home,Work,Other)",
                ["Home", "Work", "Other"],
            ),
        ],
        "remove the contact address",
    )
    ADD_NOTE = Command(0, [], "to add note")
    FIND_NOTE = Command(1, [Parametr("title", True, "note title")], "to find note by title")
    DELETE_NOTE = Command(1, [Parametr("title", True, "note title")], "to delete note")
    DELETE_ALL_NOTES = Command(0, [], "to delete all notes")
    UPDATE_NOTE = Command(1, [Parametr("title", True, "note title")], "to update note by title")
    SEARCH_NOTES = Command(1, [Parametr("query", True, "search query")], "Search for notes containing the query in their title or content.")
    FILTER_NOTES_BY_TAG = Command(1, [Parametr("tag", True, "tag to filer")], "Filter notes by tag.")
    GET_NOTES_IN_DAYS = Command(1, [Parametr("days", True, "note subject")], "Get notes that are due in the next specified number of days.",)
    GET_ALL_NOTES = Command(0, [], "to view a full notes list")
    EXIT = Command(0, [], "to app close")
    CLOSE = Command(0, [], "to close application")

    @classmethod
    def pretty_print(cls):
        """Print all menu items"""
        res = ""
        res += MENU_BORDER
        for k, v in {x.name.lower(): x.value for x in cls}.items():
            res += f"[x] {format_cmd(k)} "
            res += f"{format_param(' '.join([f'[{x.name}]' for x in v.param_list]))} "
            res += f"{v.hint}\n"
        res += MENU_BORDER
        return res

    @classmethod
    def get_commands_list(cls) -> list:
        """Return all keys"""
        return [x.name.lower() for x in cls]

    @classmethod
    def get_by_name(cls, name: str) -> list:
        """Return all keys"""

        return {x.name.lower().strip(): x for x in cls}.get(name.lower().strip())

    @classmethod
    def check_params(cls, command, args: list) -> str:
        """Return all keys"""
        row = cls(command)
        min = row.value[0]
        max = len(row.value[1])
        if not min <= len(args) <= max:
            raise ValueError(
                f"This command requires {min} to {max} parameters {row.value[1]}"
            )

    @classmethod
    def get_commands_witn_args(cls) -> dict:
        """Return all commands with params"""
        commands = {}
        for command in cls:
            commands[command.name.lower()] = [
                "--" + x.name for x in command.value.param_list
            ]

        return commands

    @staticmethod
    def suggest_similar_commands(input_command):
        """
        Suggests similar commands based on user input command.
        """
        available_commands = Menu.get_commands_list()
        similar_commands = difflib.get_close_matches(input_command, available_commands)
        return similar_commands

    @classmethod
    def create_parser(cls):
        parser = argparse.ArgumentParser(
            description="Assistant bot", exit_on_error=False
        )

        subparsers = parser.add_subparsers(dest="commands")

        for command in cls:
            commandparser = subparsers.add_parser(
                command.name.lower(), help=command.value.hint, exit_on_error=False
            )
            for param in command.value.param_list:
                commandparser.add_argument(
                    "--" + param.name,
                    dest=param.name,
                    required=param.required,
                    help=param.hint,
                    choices=param.choices,
                )

        return parser
