from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.blocks import StructBlock, URLBlock, CharBlock, ChoiceBlock

from streams import blocks
# Create your models here.
class AssistPage(Page):
    
    hero_block = StreamField(
        [
            ("hero_block" , blocks.HeroBlock()) 
        ],
        null=True,
        blank=True,
        use_json_field=True
    )

    second_block = StreamField(
        [
            ("second_block" , blocks.SecondBlock()) 
        ],
        null=True,
        blank=True,
        use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_block"),
        FieldPanel("second_block")
    ]
