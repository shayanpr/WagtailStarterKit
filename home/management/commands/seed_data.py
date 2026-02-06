import os
import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from wagtail.images.models import Image
from wagtail.models import Page, Site
from home.models import HomePage, SocialMediaSettings, NavigationSettings
from portfolio.models import ProjectIndexPage, ProjectPage
from ..data.content_data import (
    JANE_DOE_HOME,
    PROJECT_INDEX_DATA,
    PROJECTS_DATA,
    SOCIAL_DATA,
    NAV_DATA,
    EXTRA_SOCIAL_DATA,
)
import datetime


def get_image(url_or_path, title):
    """
    Fetches an image from a URL or local path and saves it as a Wagtail Image object.
    """
    try:
        file_name = f"{title.replace(' ', '_')}.jpg"
        
        if url_or_path.startswith(('http://', 'https://')):
            # Remote URL
            response = requests.get(url_or_path, timeout=10)
            if response.status_code == 200:
                image_file = ImageFile(ContentFile(response.content), name=file_name)
            else:
                return None
        else:
            # Local Path
            if os.path.exists(url_or_path):
                with open(url_or_path, 'rb') as f:
                    image_file = ImageFile(ContentFile(f.read()), name=file_name)
            else:
                print(f"Local file not found: {url_or_path}")
                return None

        image = Image(title=title, file=image_file)
        image.save()
        return image
    except Exception as e:
        print(f"Error processing image {url_or_path}: {e}")
    return None


class Command(BaseCommand):
    help_text = "Automatically seeding dummy data to the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Delete existing data before seeding",
        )

    def handle(self, *args, **options):
        # Safety Check: Prevent accidental wipe
        if not options["force"] and HomePage.objects.exists():
            self.stdout.write(
                self.style.ERROR(
                    "ABORTING: Data already exists. Seeding will WIPE everything. "
                    "Use --force to proceed (e.g. uv run python manage.py seed_data --force)"
                )
            )
            return

        self.stdout.write("Seeding initial data for Jane Doe...")

        # 1. Get the Wagtail Root page
        root = Page.get_first_root_node()

        # 2. Cleanup
        for page in root.get_children():
            page.delete()
        Site.objects.all().delete()
        Page.fix_tree()

        root = Page.get_first_root_node()

        # 3. Create Project Index Page
        index = ProjectIndexPage(
            title=PROJECT_INDEX_DATA["title"],
            slug=PROJECT_INDEX_DATA["slug"],
            intro=PROJECT_INDEX_DATA["intro"],
        )

        # 4. Create the Home Page Instance
        # Process Home Page Images
        for block_type, block_value in JANE_DOE_HOME:
            if "image_url" in block_value:
                url = block_value.pop("image_url")
                img_obj = get_image(url, f"Home_{block_type}")
                block_value["image"] = img_obj

        home = HomePage(
            title="Jane Doe | Portfolio",
            slug="home",
            body=JANE_DOE_HOME,
        )
        root.add_child(instance=home)
        home.add_child(instance=index)

        # 5. Create Individual Project Pages
        for project_data in PROJECTS_DATA:
            url = project_data.pop("image_url", None)

            project = ProjectPage(
                title=project_data["title"],
                slug=project_data["slug"],
                client=project_data["client"],
                date=datetime.date.today(),
                body=project_data["body"],
            )
            # Handle Project Image
            if url:
                project.main_image = get_image(url, f"Project_{project_data['slug']}")

            index.add_child(instance=project)
            project.save_revision().publish()

        # 6. Update Home Page "Showcase" to link to the index and projects
        for block in home.body:
            if block.block_type == "showcase":
                block.value["link_target"] = index
                block.value["projects"] = index.get_children().live()

        home.save()

        # 7. Create a Site record
        site = Site.objects.create(
            hostname="localhost",
            port=8000,
            root_page=home,
            is_default_site=True,
            site_name="Jane Doe Portfolio",
        )

        # 8. Seed Social Media Settings (Dynamic)
        social_settings = SocialMediaSettings.for_site(site)
        for key, value in SOCIAL_DATA.items():
            if hasattr(social_settings, key):
                setattr(social_settings, key, value)

        # Handle Extra Links StreamField
        extra_links = []
        for item in EXTRA_SOCIAL_DATA:
            extra_links.append(("social_link", item))
        social_settings.extra_links = extra_links

        social_settings.save()

        # 9. Seed Navigation Settings
        nav_settings = NavigationSettings.for_site(site)
        # Map targets to actual objects
        target_map = {"home": home, "work": index}
        menu_items = []
        for item in NAV_DATA:
            menu_items.append(
                (
                    "menu_item",
                    {
                        "title": item["title"],
                        "link_page": target_map.get(item["target"]),
                    },
                )
            )
        nav_settings.menu_items = menu_items
        nav_settings.save()

        # 10. Publish everything
        index.save_revision().publish()
        home.save_revision().publish()

        self.stdout.write(
            self.style.SUCCESS("Successfully seeded multi-page site with settings!")
        )
