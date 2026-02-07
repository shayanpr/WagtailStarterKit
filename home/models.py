from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail import blocks
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from blocks.models import (
    ContactFormBlock,
    GridBlock,
    HeroBlock,
    ServicesListBlock,
    AboutBlock,
    FeaturedProjectsBlock,
    ContactBlock,
    SocialLinkBlock,
)


class FormField(AbstractFormField):
    page = ParentalKey(
        "ContactPage", on_delete=models.CASCADE, related_name="form_fields"
    )


class ContactPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address", classname="col6"),
                        FieldPanel("to_address", classname="col6"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email Configuration",
        ),
    ]


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

    google_analytics_id = models.CharField(
        blank=True, null=True, max_length=50, help_text="Google Analytics ID"
    )

    panels = [
        FieldPanel("logo"),
        FieldPanel("favicon"),
        FieldPanel("google_analytics_id"),
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


class HomePage(Page):
    body = StreamField(
        [
            ("hero", HeroBlock()),
            ("about", AboutBlock()),
            ("services", ServicesListBlock()),
            ("showcase", FeaturedProjectsBlock()),
            ("contact", ContactBlock()),
            ("contact_form", ContactFormBlock()),
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
            ("contact_form", ContactFormBlock()),
            ("grid", GridBlock()),
        ],
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    template = "home/home_page.html"
