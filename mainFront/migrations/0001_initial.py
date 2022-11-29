# Generated by Django 3.2.9 on 2022-11-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('text', models.TextField()),
                ('text_en', models.TextField(null=True)),
                ('text_ru', models.TextField(null=True)),
                ('text_uk', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
    ]
