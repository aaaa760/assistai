from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import StructBlock, TextBlock, StreamBlock, URLBlock, RichTextBlock, DecimalBlock, ListBlock, CharBlock
from wagtail.contrib.table_block.blocks import TableBlock

class HeroBlock(blocks.StructBlock):
    banner_title = blocks.CharBlock(required=True, help_text="Add you Heading")
    banner_sub_title = blocks.CharBlock(required=True, help_text="Add you Sub Heading")
    banner_image = ImageChooserBlock(required=False , help_text="Add your Image")
    
    class Meta:
        template = "streams/hero_block.html"
        icon = "placeholder"
        label = "Hero"


class SecondBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text="Add you Heading")
    question = blocks.CharBlock(required=True, help_text="Add you Question")
    answer = blocks.RichTextBlock(required=True, help_text="Add you Answer")
    image = ImageChooserBlock(required=False , help_text="Add your Image")
    
    class Meta:
        template = "streams/second_block.html"
        icon = "placeholder"
        label = "Second"
