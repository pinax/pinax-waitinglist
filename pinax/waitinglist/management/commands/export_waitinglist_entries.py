import csv

from django.core.management.base import BaseCommand

from pinax.waitinglist.models import WaitingListEntry


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("filename", help="the name of the file used for the export")

    def handle(self, **options):
        fieldnames = [
            "email",
            "created",
        ]
        data = []
        for entry in WaitingListEntry.objects.all().order_by("created"):
            data.append({
                "email": entry.email,
                "created": entry.created.isoformat()
            })

        with open(options["filename"], "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for d in data:
                writer.writerow(d)
