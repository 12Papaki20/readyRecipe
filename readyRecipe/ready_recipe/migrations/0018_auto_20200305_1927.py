# Generated by Django 2.1.5 on 2020-03-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ready_recipe', '0017_auto_20200305_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
