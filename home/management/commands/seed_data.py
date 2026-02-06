from django.core.management.base import BaseCommand
from wagtail.models import Page, Site
from home.models import HomePage
from .content_data import JANE_DOE_HOME


class Command(BaseCommand):
    help_text = "Automatically seeding dummy data to the database"

    def handle(self, *args, **options):
        self.stdout.write("Seeding initial data for Jane Doe...")

        # 1. Get the Wagtail Root page (The absolute base of the tree)
        root = Page.get_first_root_node()

        # 2. Cleanup: Remove existing sites and homepages to start fresh
        # This prevents "Slug already exists" errors when you run this multiple times
        for page in root.get_children():
            page.delete()
        Site.objects.all().delete()
        Page.fix_tree()

        root = Page.get_first_root_node()

        # 3. Create the Home Page Instance
        # The 'body' list uses tuples: (block_type, block_data_dict)
        home = HomePage(
            title="Jane Doe | Portfolio",
            slug="home",
            body=JANE_DOE_HOME,
        )

        # 4. Add Home Page as a child of Root
        # This 'plants' the page in the Wagtail tree and saves it to the DB
        root.add_child(instance=home)

        # 5. Create a Site record
        # This tells Wagtail that when you visit localhost:8000, it should show the 'home' page
        Site.objects.create(
            hostname="localhost",
            port=8000,
            root_page=home,
            is_default_site=True,
            site_name="Jane Doe Portfolio",
        )

        # 6. Optional: Create a revision and publish it
        # This makes the page 'Live' immediately so you don't have to click publish in admin
        home.save_revision().publish()

        self.stdout.write(self.style.SUCCESS("Successfully seeded site for Jane Doe!"))
        self.stdout.write("Visit http://localhost:8000 to see the result.")
