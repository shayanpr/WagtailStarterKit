from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from blocks.models import (
    BlogGridBlock,
    TestimonialBlock,
    ComparisonBlock,
    FAQBlock,
    CallToActionBlock,
    StatsBlock,
    PartnerLogoBlock,
    ServicesListBlock,
    CaseStudyBlock,
    FeaturedProjectsBlock,
    ContactFormBlock,
    TeamMemberBlock,
)


class BlogStreamBlockMixin(models.Model):
    body = StreamField(
        [
            ("heading", blocks.CharBlock(from_classname="title")),
            ("paragraph", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("services_list_block", ServicesListBlock()),
            ("featured_projects_block", FeaturedProjectsBlock()),
            ("contact_form_block", ContactFormBlock()),
            ("comparison_block", ComparisonBlock()),
            ("testimonial_block", TestimonialBlock()),
            ("faq_block", FAQBlock()),
            ("partner_logo_block", PartnerLogoBlock()),
            ("team_member_block", TeamMemberBlock()),
            ("blog_grid_block", BlogGridBlock()),
            ("stats_block", StatsBlock()),
            ("cta_block", CallToActionBlock()),
            ("case_study_block", CaseStudyBlock()),
        ],
        use_json_field=True,
    )

    class Meta:
        abstract = True


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        help_text="The URL friendly name for this category(e.g. 'news').",
    )
    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"


class BlogPage(Page, BlogStreamBlockMixin):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    main_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    category = models.ForeignKey(
        "blog.BlogCategory",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="blog_pages",
    )

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("main_image"),
        FieldPanel("category"),
        FieldPanel("body"),
    ]

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="Intro"),
    ]
    subpage_types = ["blog.BlogPage"]