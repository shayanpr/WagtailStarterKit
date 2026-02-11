from django.db import models
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField


class FAQItemBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True)
    answer = blocks.RichTextBlock(required=True)

    class Meta:
        icon = "question"
        label = "Question and Answer"


class FAQBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, default="Frequently Asked Questions")
    description = blocks.TextBlock(required=False)
    items = blocks.ListBlock(FAQItemBlock())

    class Meta:
        icon = "help"
        label = "FAQ Section"
        template = "blocks/faq_block.html"


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
        template = "blocks/tier_block.html"


class ComparisonBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    tiers = blocks.ListBlock(TierBlock(), min_num=1, max_num=4)

    class Meta:
        template = "blocks/comparison_block.html"
        icon = "table"
        label = "Comparison/Pricing Table"


@register_snippet
class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    website = models.URLField(blank=True, null=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("logo"),
        FieldPanel("website"),
    ]

    def __str__(self):
        return self.name


class PartnerLogoBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, default="Trusted By")
    partners = blocks.ListBlock(SnippetChooserBlock(Partner))

    class Meta:
        template = "blocks/partner_logo_block.html"
        icon = "group"
        label = "Partner Logo Block"


class SocialFieldsMixin(models.Model):
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
    facebook = models.URLField(
        blank=True, null=True, help_text="Enter your Facebook profile URL"
    )
    instagram = models.URLField(
        blank=True, null=True, help_text="Enter your Instagram profile URL"
    )
    phone = models.CharField(
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
    social_panels = [
        FieldPanel("email"),
        FieldPanel("linkedin"),
        FieldPanel("github"),
        FieldPanel("twitter"),
        FieldPanel("facebook"),
        FieldPanel("instagram"),
        FieldPanel("phone"),
        FieldPanel("telegram_username"),
        FieldPanel("extra_links"),
    ]

    class Meta:
        abstract = True


@register_snippet
class TeamMember(SocialFieldsMixin):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    biography = models.TextField(blank=True)
    panels = [
        FieldPanel("name"),
        FieldPanel("role"),
        FieldPanel("image"),
        FieldPanel("biography"),
        MultiFieldPanel(SocialFieldsMixin.social_panels, "Social"),
    ]

    def __str__(self):
        return self.name


class TeamMemberBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, default="My Team")
    team_members = blocks.ListBlock(SnippetChooserBlock(TeamMember))

    class Meta:
        template = "blocks/team_member_block.html"
        icon = "user"
        label = "Team Member Block"


class StatItemBlock(blocks.StructBlock):
    value = blocks.CharBlock()
    text = blocks.CharBlock()
    icon = ImageChooserBlock(required=False)

    class Meta:
        icon = "pick"
        label = "Stat Item"


class StatsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, default="My Stats")
    stats = blocks.ListBlock(StatItemBlock())

    class Meta:
        template = "blocks/stats_block.html"
        icon = "order"
        label = "Stats Block"


class CallToActionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, default="Ready to get started?")
    subtitle = blocks.TextBlock(required=False)
    button_text = blocks.CharBlock(required=False)
    button_link = blocks.PageChooserBlock(required=False)
    background_image = ImageChooserBlock(required=False)
    is_dark = blocks.BooleanBlock(required=False, default=True)

    class Meta:
        template = "blocks/call_to_action_block.html"
        icon = "link"
        label = "Call to Action Block"


class CaseStudyBlock(blocks.StructBlock):
    problem = blocks.RichTextBlock(required=False)
    solution = blocks.RichTextBlock(required=False)
    results = blocks.RichTextBlock(required=False)
    is_featured = blocks.BooleanBlock(required=False, default=False)

    class Meta:
        template = "blocks/case_study_block.html"
        icon = "doc-full"
        label = "Case Study Block"


class ColumnBlock(blocks.StreamBlock):
    hero_block = HeroBlock(icon="user")
    about_block = AboutBlock(icon="doc-full")
    heading = blocks.CharBlock(icon="title")
    paragraph = blocks.RichTextBlock(icon="pilcrow")
    image = ImageChooserBlock(icon="image")
    contact_form_block = ContactFormBlock(icon="mail")
    testimonial_block = TestimonialBlock(icon="openquote")
    featured_projects_block = FeaturedProjectsBlock(icon="pick")
    service_block = ServiceBlock(icon="tick-inverse")
    services_list_block = ServicesListBlock(icon="list-ul")
    tier_block = TierBlock(icon="pick")
    comparison_block = ComparisonBlock(icon="table")
    faq_block = FAQBlock(icon="help")
    partner_logo_block = PartnerLogoBlock(icon="group")
    team_member_block = TeamMemberBlock(icon="user")
    stats_block = StatsBlock(icon="order")
    cta_block = CallToActionBlock(icon="link")
    case_study_block = CaseStudyBlock(icon="doc-full")

    class Meta:
        label = "Columns Content"


class GridBlock(blocks.StructBlock):
    grid_title = blocks.CharBlock(required=False, help_text="Optional Section Heading.")
    columns = blocks.ListBlock(ColumnBlock(), label="Columns", min_num=1, max_num=4)

    class Meta:
        icon = "table"
        label = "Grid Section"
        template = "blocks/grid_block.html"
