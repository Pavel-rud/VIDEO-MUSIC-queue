# Generated by Django 4.0.5 on 2022-07-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tg_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
