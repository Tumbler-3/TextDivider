# Generated by Django 5.1.3 on 2024-11-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'ImageModel',
                'verbose_name_plural': 'ImageModels',
            },
        ),
    ]
