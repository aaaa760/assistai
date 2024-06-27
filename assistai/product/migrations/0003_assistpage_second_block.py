# Generated by Django 5.0.6 on 2024-06-27 09:09

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_assistpage_hero_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistpage',
            name='second_block',
            field=wagtail.fields.StreamField([('second_block', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(help_text='Add you Heading', required=True)), ('question', wagtail.blocks.CharBlock(help_text='Add you Question', required=True)), ('answer', wagtail.blocks.RichTextBlock(help_text='Add you Answer', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Add your Image', required=False))]))], blank=True, null=True),
        ),
    ]
