# Generated by Django 3.2.19 on 2023-05-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='bakers_tip',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(max_length=250),
        ),
    ]