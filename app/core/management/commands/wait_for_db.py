import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django Command to pause execution until db is availble"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for Database....")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write(
                    "Database unavailable, waiting 1 second ....")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Available!'))
