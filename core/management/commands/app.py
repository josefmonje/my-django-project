from os import makedirs, path

from django.conf import settings
from django.core.management.templates import TemplateCommand


class Command(TemplateCommand):
    help = (
        "Creates a Django app directory structure for the given app name in "
        "the apps directory."
    )
    missing_args_message = "You must provide an application name."

    def handle(self, **options):
        app_name = options.pop('name')
        target = 'apps/{0}'.format(app_name)
        top_dir = path.abspath(path.expanduser(target))
        try:
            makedirs(top_dir)
        except FileExistsError:
            raise CommandError("'%s' already exists" % top_dir)
        except OSError as e:
            raise CommandError(e)
        super().handle('app', app_name, target, **options)
