# Generated by Django 4.2.5 on 2023-09-14 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('reviews', '0008_rename_object_type_review_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reviews', to='contenttypes.contenttype'),
        ),
    ]