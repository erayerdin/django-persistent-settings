import logging

from django.core.management.base import BaseCommand, CommandError

from persistent_settings import models

_LOGGER = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Deletes the named Variable."

    def add_arguments(self, parser):
        parser.add_argument("name", help="The name of Variable.")
        parser.add_argument(
            "-n",
            "--no-error",
            action="store_true",
            help="The command does not raise any exceptions if Variable does not exist.",
        )

    def handle(self, *args, **options):
        name = options["name"]
        no_error = options["no_error"]

        try:
            _LOGGER.debug("Looking up for variable: {}".format(name))
            variable = models.Variable.objects.get(name=name)
        except models.Variable.DoesNotExist:
            message = "Variable named {} does not exist.".format(name)
            _LOGGER.error(message)

            if no_error:
                self.stdout.write(message)
                return

            e = CommandError(message)
            raise e

        variable.delete()
        self.stdout.write("Successfully deleted Variable named {}.".format(name))
