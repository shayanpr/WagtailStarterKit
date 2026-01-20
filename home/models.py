from django.db import models
from wagtail.models import Page
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSiteSetting):
    email = models.EmailField(
        blank=True, null=True, help_text="Enter your email address"
    )
    linkedin = models.URLField(
        blank=True, null=True, help_text="Enter your LinkedIn profile URL"
    )
    github = models.URLField(
        blank=True, null=True, help_text="Enter your GitHub profile URL"
    )
    twitter = models.URLField(
        blank=True, null=True, help_text="Enter your Twitter profile URL"
    )

    panels = [
        FieldPanel("email"),
        FieldPanel("linkedin"),
        FieldPanel("github"),
        FieldPanel("twitter"),
    ]

    class Meta:
        verbose_name = "Social Media Settings"
        verbose_name_plural = "Social Media Settings"


class MenuItem(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    link_page = blocks.PageChooserBlock(
        required=False, help_text="Link to an internal page"
    )
    link_url = blocks.URLBlock(required=False, help_text="Link to an external URL")

    class Meta:
        icon = "link"
        label = "Menu Item"


@register_setting
class NavigationSettings(BaseSiteSetting):
    menu_items = StreamField(
        [
            ("menu_item", MenuItem()),
        ],
        blank=True,
        use_json_field=True,
    )
    panels = [
        FieldPanel("menu_items"),
    ]


class ContactBlock(blocks.StructBlock):
    heading = blocks.CharBlock(
        required=True, default="Get in Touch!", help_text="Contact Me"
    )
    text = blocks.TextBlock(required=False, default="Lets work together.")

    class Meta:
        icon = "mail"
        label = "Contact Section (Auto Linked)"
        template = "home/contact_block.html"


class HeroBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Main Headline")
    subtitle = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = "user"
        label = "Hero Section"
        template = "home/hero_block.html"


class AboutBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text="About Me")
    content = blocks.RichTextBlock(required=False)

    class Meta:
        icon = "doc-full"
        label = "About Section"
        template = "home/about_block.html"


class ServiceBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    description = blocks.RichTextBlock(required=True)
    icon = ImageChooserBlock(required=False)

    class Meta:
        icon = "tick-inverse"
        label = "Single Service Card"
        template = "home/service_block.html"


class ServicesListBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, default="My Services")
    services = blocks.ListBlock(ServiceBlock())

    class Meta:
        icon = "list-ul"
        label = "Services Grid"
        template = "home/services_list_block.html"


class FeaturedProjectsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(default="Selected Projects", required=False)
    intro = blocks.TextBlock(required=False, default="Some of my recent projects.")
    projects = blocks.ListBlock(
        blocks.PageChooserBlock(target_model="portfolio.ProjectPage", required=False)
    )

    class Meta:
        icon = "pick"
        label = "Featured Projects"
        template = "home/featured_projects_block.html"


class HomePage(Page):
    body = StreamField(
        [
            ("hero", HeroBlock()),
            ("about", AboutBlock()),
            ("services", ServicesListBlock()),
            ("showcase", FeaturedProjectsBlock()),
            ("contact", ContactBlock()),
        ],
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
