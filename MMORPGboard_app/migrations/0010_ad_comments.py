# Generated by Django 4.2.4 on 2023-08-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board_app', '0009_alter_ad_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='comments',
            field=models.ManyToManyField(related_name='ads_comments', to='bulletin_board_app.comment'),
        ),
    ]