# Generated by Django 4.2.4 on 2023-08-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categoryType',
            field=models.TextField(choices=[('Танки', 'Танки'), ('Хилы', 'Хилы'), ('ДД', 'ДД'), ('Торговцы', 'Торговцы'), ('Гилдмастеры', 'Гилдмастеры'), ('Квестгиверы', 'Квестгиверы'), ('Кузнецы', 'Кузнецы'), ('Кожевники', 'Кожевники'), ('Зельевары', 'Зельевары'), ('Мастера заклинаний', 'Мастера заклинаний')], default='Торговцы'),
        ),
    ]
