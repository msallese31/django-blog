# Generated by Django 2.1.7 on 2019-03-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_posttype_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttype',
            name='display_name',
            field=models.CharField(max_length=50),
        ),
    ]
