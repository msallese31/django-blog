# Generated by Django 2.1.7 on 2019-03-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190319_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttype',
            name='display_name',
            field=models.CharField(default='Dummy', max_length=50),
        ),
    ]
