from django.db import models
from wagtail.models import Page
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


class SocialLinkBlock(blocks.StructBlock):
    platform_name = blocks.CharBlock(required=True, help_text="e.g. Telegram Channel")
    url = blocks.URLBlock(required=True)
    icon = ImageChooserBlock(required=False, help_text="Upload a logo/icon")

    class Meta:
        icon = "link"
        label = "Custom Social Link"


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
    whatsapp = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        help_text="International format (e.g. +12345234567)",
    )
    telegram_username = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        help_text="Your username without the @ (e.g. username)",
    )
    extra_links = StreamField(
        [
            ("social_link", SocialLinkBlock()),
        ],
        blank=True,
        use_json_field=True,
    )
    panels = [
        FieldPanel("email"),
        FieldPanel("linkedin"),
        FieldPanel("github"),
        FieldPanel("twitter"),
        FieldPanel("whatsapp"),
        FieldPanel("telegram_username"),
        FieldPanel("extra_links"),
    ]

    class Meta:
        verbose_name = "Social Media Settings"
        verbose_name_plural = "Social Media Settings"


@register_setting
class BrandingSettings(BaseSiteSetting):
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Brand logo used in the navbar",
    )
    favicon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Favicon used in the browser tab (recommended 32x32)",
    )

    panels = [
        FieldPanel("logo"),
        FieldPanel("favicon"),
    ]

    class Meta:
        verbose_name = "Branding Settings"


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
    illustration = ImageChooserBlock(
        required=False, help_text="Side illustration image"
    )

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
    link_target = blocks.PageChooserBlock(requqired=False, help_text="Link to View All")

    class Meta:
        icon = "pick"
        label = "Featured Projects"
        template = "home/featured_projects_block.html"


class ColumnBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(icon="title")
    paragraph = blocks.RichTextBlock(icon="pilcrow")
    image = ImageChooserBlock(icon="image")

    class Meta:
        label = "Columns Content"


class GridBlock(blocks.StructBlock):
    grid_title = blocks.CharBlock(required=False, help_text="Optional Section Heading.")
    columns = blocks.ListBlock(ColumnBlock(), label="Columns", min_num=1, max_num=4)

    class Meta:
        icon = "table"
        label = "Grid Section"
        template = "home/grid_block.html"


class HomePage(Page):
    body = StreamField(
        [
            ("hero", HeroBlock()),
            ("about", AboutBlock()),
            ("services", ServicesListBlock()),
            ("showcase", FeaturedProjectsBlock()),
            ("contact", ContactBlock()),
            ("grid", GridBlock()),
        ],
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class FlexPage(Page):
    body = StreamField(
        [
            ("hero", HeroBlock()),
            ("about", AboutBlock()),
            ("services", ServicesListBlock()),
            ("showcase", FeaturedProjectsBlock()),
            ("contact", ContactBlock()),
            ("grid", GridBlock()),
        ],
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    template = "home/home_page.html"
