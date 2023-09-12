# Generated by Django 4.2.5 on 2023-09-12 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0002_character'),
        ('cast', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(default='', verbose_name=20000)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.character')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cast.person')),
            ],
        ),
    ]
