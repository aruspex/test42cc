from django.core.management.base import NoArgsCommand
from django.db import models


class Command(NoArgsCommand):
    help = "prints all project models and the count of objects in every model"

    def handle(self, *args, **options):
        all_models = models.get_models()
        output = ['%s %s' % (m._meta.db_table,
                             m.objects.count()) for m in all_models]
        self.stdout.write('\n'.join(output))
        self.stderr.write('error: ' + '\nerror: '.join(output))
