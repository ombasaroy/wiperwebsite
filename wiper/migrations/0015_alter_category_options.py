# Generated by Django 5.1.6 on 2025-03-10 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiper', '0014_alter_category_options_remove_post_custom_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
