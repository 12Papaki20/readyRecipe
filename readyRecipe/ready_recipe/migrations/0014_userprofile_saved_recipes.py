# Generated by Django 2.1.5 on 2020-03-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ready_recipe', '0013_auto_20200303_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='saved_Recipes',
            field=models.ManyToManyField(to='ready_recipe.Recipe'),
        ),
    ]