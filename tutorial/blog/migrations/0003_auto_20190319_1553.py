# Generated by Django 2.1.7 on 2019-03-19 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190319_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.PostType'),
        ),
        migrations.AlterField(
            model_name='posttype',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
