import builtins
import logging

from django.core.management.base import BaseCommand, CommandError

from persistent_settings import models

_LOGGER = logging.getLogger(__name__)
_FALSE_MAP = ("0", "f", "n", "false", "no")


class Command(BaseCommand):
    help = "Creates/updates a Variable."

    def add_arguments(self, parser):
        parser.add_argument("name", help="The name of Variable.")
        parser.add_argument(
            "value", nargs="?", default=None, help="The value of Variable."
        )
        parser.add_argument(
            "-t",
            "--type",
            default="str",
            choices=("str", "bool", "int", "float"),
            help="The type of value.",
        )
        parser.add_argument(
            "-n",
            "--no-update",
            action="store_true",
            help="The command raises exception if Variable exists.",
        )

    def _transform_type_value(self, typ_: str, value):
        """
        Transforms the type of value.
        """
        _LOGGER.debug("Transforming the value to type {}...".format(typ_))

        if value is None:
            _LOGGER.debug("No value is given. Resulting None...")
            return None
        elif typ_ == "bool" and value.lower() in _FALSE_MAP:
            _LOGGER.debug(
                "The type of bool with given value {} results in False.".format(value)
            )
            return False

        return getattr(builtins, typ_)(value)  # if "int", wraps as int(value)

    def handle(self, *args, **options):
        name = options["name"]
        typ_ = options["type"]
        value = self._transform_type_value(typ_, options["value"])
        no_update = options["no_update"]

        if no_update and models.Variable.objects.filter(name=name).exists():
            message = "Variable named {} already exists.".format(name)
            e = CommandError(message)
            _LOGGER.error(message, e)
            raise e

        _LOGGER.debug("Creating/updating variable: {}".format(name))
        _, created = models.Variable.objects.update_or_create(
            name=name, defaults={"value": value}
        )

        message = "Successfully {op} Variable named {name}."

        if created:
            _LOGGER.debug("Generating message for create operation...")
            message = message.format(op="created", name=name)
        else:
            _LOGGER.debug("Generating message for update operation...")
            message = message.format(op="updated", name=name)

        self.stdout.write(message)
