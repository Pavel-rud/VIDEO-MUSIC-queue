# Generated by Django 4.0.5 on 2022-07-07 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sait', '0010_alter_room_password_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name_room',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]