# Generated by Django 4.2.11 on 2024-04-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_book_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='manual',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
