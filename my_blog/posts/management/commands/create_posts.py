from django.core.management import BaseCommand

from posts.utils import create_fake_posts


class Command(BaseCommand):
    help =  "Creating new posts"

    def handle(self, *args, **options):
        n = options.get("number", 10)
        create_fake_posts(n)

    def add_arguments(self, parser):
        parser.add_argument(
            "-n",
            "--number",
            type=int,
            default=10,
            dest="number",
            help='Amount of books'
        )
