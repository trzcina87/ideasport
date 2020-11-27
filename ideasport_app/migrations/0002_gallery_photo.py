# Generated by Django 3.0 on 2019-12-20 09:53

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ideasport_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order', models.IntegerField(blank=True, db_index=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=1000)),
                ('order', models.IntegerField(blank=True, db_index=True, null=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ideasport_app.Gallery')),
            ],
        ),
    ]
