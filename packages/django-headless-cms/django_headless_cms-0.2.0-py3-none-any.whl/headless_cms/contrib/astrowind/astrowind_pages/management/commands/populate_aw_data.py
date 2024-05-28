from django.core.management import call_command
from reversion.management.commands import BaseRevisionCommand


class Command(BaseRevisionCommand):

    help = "Deletes outdated drafts."

    def handle(self, *app_labels, **options):
        call_command(
            "import_cms_data",
            "astrowind_posts",
            "astrowind_pages",
            input="https://raw.githubusercontent.com/huynguyengl99/dj-hcms-data/main/data/astrowind/astrowind.zip",
        )
