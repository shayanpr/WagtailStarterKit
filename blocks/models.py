from django.db import models
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel


class ContactFormBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True)
    description = blocks.TextBlock(required=False)
    # We use a PageChooser to tell the block which Contact Page to use
    form_page = blocks.PageChooserBlock(target_model="home.ContactPage")

    class Meta:
        template = "blocks/contact_form_block.html"
        icon = "mail"
        label = "Embedded Contact Form"


class SocialLinkBlock(blocks.StructBlock):
    platform_name = blocks.CharBlock(required=True, help_text="e.g. Telegram Channel")
    url = blocks.URLBlock(required=True)
    icon = ImageChooserBlock(required=False, help_text="Upload a logo/icon")

    class Meta:
        icon = "link"
        label = "Custom Social Link"


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
        template = "blocks/contact_block.html"


class HeroBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Main Headline")
    subtitle = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = "user"
        label = "Hero Section"
        template = "blocks/hero_block.html"


class AboutBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text="About Me")
    content = blocks.RichTextBlock(required=False)

    class Meta:
        icon = "doc-full"
        label = "About Section"
        template = "blocks/about_block.html"


class ServiceBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    description = blocks.RichTextBlock(required=True)
    icon = ImageChooserBlock(required=False)

    class Meta:
        icon = "tick-inverse"
        label = "Single Service Card"
        template = "blocks/service_block.html"


class ServicesListBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, default="My Services")
    services = blocks.ListBlock(ServiceBlock())

    class Meta:
        icon = "list-ul"
        label = "Services Grid"
        template = "blocks/services_list_block.html"


class FeaturedProjectsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(default="Selected Projects", required=False)
    intro = blocks.TextBlock(required=False, default="Some of my recent projects.")
    projects = blocks.ListBlock(
        blocks.PageChooserBlock(target_model="portfolio.ProjectPage", required=False)
    )
    link_target = blocks.PageChooserBlock(required=False, help_text="Link to View All")

    class Meta:
        icon = "pick"
        label = "Featured Projects"
        template = "blocks/featured_projects_block.html"


@register_snippet
class Testimonial(models.Model):
    author_name = models.CharField(max_length=255)
    author_role = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    quote = models.TextField()
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("author_name"),
        FieldPanel("author_role"),
        FieldPanel("company"),
        FieldPanel("quote"),
        FieldPanel("image"),
    ]

    def __str__(self):
        return f"{self.author_name} - {self.company}"


class TestimonialBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    testimonials = blocks.ListBlock(SnippetChooserBlock(Testimonial))

    class Meta:
        template = "blocks/testimonial_block.html"
        icon = "openquote"
        label = "Testimonial Block"


class ColumnBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(icon="title")
    paragraph = blocks.RichTextBlock(icon="pilcrow")
    image = ImageChooserBlock(icon="image")
    contact_form = ContactFormBlock(icon="mail")
    testimonial = TestimonialBlock(icon="openquote")

    class Meta:
        label = "Columns Content"


class GridBlock(blocks.StructBlock):
    grid_title = blocks.CharBlock(required=False, help_text="Optional Section Heading.")
    columns = blocks.ListBlock(ColumnBlock(), label="Columns", min_num=1, max_num=4)

    class Meta:
        icon = "table"
        label = "Grid Section"
        template = "blocks/grid_block.html"


class TierBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    description = blocks.CharBlock(required=False)
    price_or_label = blocks.CharBlock(required=False, help_text="e.g. $10/mo or Free")
    features = blocks.ListBlock(blocks.CharBlock(), label="Feature List")
    button_text = blocks.CharBlock(required=False, default="Get Started")
    button_link = blocks.PageChooserBlock(required=False)
    is_featured = blocks.BooleanBlock(required=False, help_text="Highlight this plan?")

    class Meta:
        icon = "pick"
        label = "Individual Tier"


class ComparisonBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    tiers = blocks.ListBlock(TierBlock(), min_num=1, max_num=4)

    class Meta:
        template = "blocks/comparison_block.html"
        icon = "table"
        label = "Comparison/Pricing Table"
