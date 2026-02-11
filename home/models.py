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
    SocialFieldsMixin,
    ComparisonBlock,
    TestimonialBlock,
    FAQBlock,
    PartnerLogoBlock,
    TeamMemberBlock,
    StatsBlock,
    CallToActionBlock,
    CaseStudyBlock,
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
class SocialMediaSettings(BaseSiteSetting, SocialFieldsMixin):
    panels = [MultiFieldPanel(SocialFieldsMixin.social_panels, "Social Media Links")]

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


class BaseStreamBlockMixin(models.Model):
    body = StreamField(
        [
            ("hero_block", HeroBlock()),
            ("about_block", AboutBlock()),
            ("services_list_block", ServicesListBlock()),
            ("featured_projects_block", FeaturedProjectsBlock()),
            ("contact_block", ContactBlock()),
            ("contact_form_block", ContactFormBlock()),
            ("comparison_block", ComparisonBlock()),
            ("testimonial_block", TestimonialBlock()),
            ("faq_block", FAQBlock()),
            ("partner_logo_block", PartnerLogoBlock()),
            ("team_member_block", TeamMemberBlock()),
            ("grid_block", GridBlock()),
            ("stats_block", StatsBlock()),
            ("cta_block", CallToActionBlock()),
            ("case_study_block", CaseStudyBlock()),
        ],
        use_json_field=True,
    )

    class Meta:
        abstract = True


class HomePage(Page, BaseStreamBlockMixin):
    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class FlexPage(Page, BaseStreamBlockMixin):
    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    template = "home/home_page.html"


class AboutPage(Page, BaseStreamBlockMixin):
    hero_text = models.CharField(max_length=255, blank=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    description = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_text"),
                FieldPanel("hero_image"),
                FieldPanel("description"),
            ],
            heading="Hero Section",
        ),
        FieldPanel("body"),
    ]
