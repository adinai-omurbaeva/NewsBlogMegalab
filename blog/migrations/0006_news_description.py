# Generated by Django 4.1.3 on 2023-01-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_rename_user_comment_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="description",
            field=models.CharField(default="text", max_length=255),
            preserve_default=False,
        ),
    ]