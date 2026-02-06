from django.core.management.base import BaseCommand
from wagtail.models import Page, Site
from home.models import HomePage, SocialMediaSettings, NavigationSettings
from portfolio.models import ProjectIndexPage, ProjectPage
from ..data.content_data import JANE_DOE_HOME, PROJECT_INDEX_DATA, PROJECTS_DATA, SOCIAL_DATA, NAV_DATA, EXTRA_SOCIAL_DATA
import datetime


class Command(BaseCommand):
    help_text = "Automatically seeding dummy data to the database"

    def handle(self, *args, **options):
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
        home = HomePage(
            title="Jane Doe | Portfolio",
            slug="home",
            body=JANE_DOE_HOME,
        )
        root.add_child(instance=home)
        home.add_child(instance=index)

        # 5. Create Individual Project Pages
        for project_data in PROJECTS_DATA:
            project = ProjectPage(
                title=project_data["title"],
                slug=project_data["slug"],
                client=project_data["client"],
                date=datetime.date.today(),
                body=project_data["body"],
            )
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
                ("menu_item", {"title": item["title"], "link_page": target_map.get(item["target"])})
            )
        nav_settings.menu_items = menu_items
        nav_settings.save()

        # 10. Publish everything
        index.save_revision().publish()
        home.save_revision().publish()

        self.stdout.write(self.style.SUCCESS("Successfully seeded multi-page site with settings!"))

