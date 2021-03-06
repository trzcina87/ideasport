# Generated by Django 3.0 on 2020-11-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideasport_app', '0002_gallery_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
