# Generated by Django 4.1.5 on 2023-01-29 20:43

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_place_options_remove_image_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together={('place', 'order')},
        ),
    ]