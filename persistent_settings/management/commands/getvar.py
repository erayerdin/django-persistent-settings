import logging

from django.core.management.base import BaseCommand, CommandError

from persistent_settings import models

_LOGGER = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Prints out the content of a Variable."

    def add_arguments(self, parser):
        parser.add_argument("name", help="The name of Variable.")
        parser.add_argument(
            "-b",
            "--bash-style",
            action="store_true",
            help="Prints out with bash-style starting with 'export'.",
        )

    def handle(self, *args, **options):
        name = options["name"]
        bash_style = options["bash_style"]

        try:
            _LOGGER.debug("Looking up for variable: {}".format(name))
            variable = models.Variable.objects.get(name=name)
        except models.Variable.DoesNotExist:
            message = "Variable named {} does not exist.".format(name)
            e = CommandError(message)
            _LOGGER.error(message)
            raise e

        if bash_style:
            self.stdout.write(
                'export {name}="{value}"'.format(
                    name=variable.name, value=variable.value
                )
            )
        else:
            self.stdout.write(variable.value)
