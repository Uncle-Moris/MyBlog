from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("This is hello command for posts")

    def add_arguments(self, parser):
        pass