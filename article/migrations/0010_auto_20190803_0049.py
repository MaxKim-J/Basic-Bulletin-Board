# Generated by Django 2.2.3 on 2019-08-02 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20190803_0039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='delete',
            new_name='delo',
        ),
    ]