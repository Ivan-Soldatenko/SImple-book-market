# Generated by Django 3.1.2 on 2020-11-01 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("books", "0006_auto_20201101_2006")]

    operations = [
        migrations.AlterModelOptions(name="book", options={"ordering": ("title",)})
    ]
