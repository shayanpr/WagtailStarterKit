from django.db import models
from wagtail import blocks
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase, Tag
from blocks.models import CaseStudyBlock


class ProjectIndexPage(Page):
    hero_images = StreamField(
        [
            ("image", ImageChooserBlock()),
        ],
        blank=True,
        use_json_field=True,
    )
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("hero_images"),
        FieldPanel("intro", classname="Intro"),
    ]

    subpage_types = ["portfolio.ProjectPage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_projects = ProjectPage.objects.child_of(self).live().specific()
        projects = (
            ProjectPage.objects.child_of(self).live().specific().order_by("-date")
        )
        tag = request.GET.get("tag")
        if tag:
            projects = projects.filter(tags__slug=tag)
        context["projects"] = projects

        context["all_tags"] = (
            Tag.objects.filter(
                portfolio_projectpagetag_items__content_object__in=all_projects
            )
            .distinct()
            .order_by("name")
        )
        return context


class ProjectPageTag(TaggedItemBase):
    content_object = ParentalKey(
        "ProjectPage",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )


class ProjectPage(Page):
    client = models.CharField(max_length=200)
    date = models.DateField("Project date")
    body = StreamField(
        [
            ("case_study_block", CaseStudyBlock()),
            ("paragraph", blocks.RichTextBlock()),
        ],
        use_json_field=True,
        blank=True,
    )
    main_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_images = StreamField(
        [
            ("image", ImageChooserBlock()),
        ],
        blank=True,
        use_json_field=True,
    )
    tags = ClusterTaggableManager(through=ProjectPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("client"),
        FieldPanel("date"),
        FieldPanel(
            "main_image",
            help_text="Thumbnail image used on the 'Our Work' list page, also works as a hero image if the hero_images field is not set.",
        ),
        FieldPanel("hero_images", help_text="Cinematic background slideshow images."),
        FieldPanel("body"),
        FieldPanel("tags"),
        InlinePanel("gallery_images", label="Gallery images"),
    ]

    parent_page_types = ["portfolio.ProjectIndexPage"]


class ProjectGalleryImage(Orderable):
    page = ParentalKey(
        ProjectPage,
        on_delete=models.CASCADE,
        related_name="gallery_images",
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel("image"),
        FieldPanel("caption"),
    ]
