# Generated by Django 4.2.5 on 2023-09-15 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0004_remove_person_scripts'),
        ('movies', '0007_movie_scripts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cast.person'),
        ),
    ]
