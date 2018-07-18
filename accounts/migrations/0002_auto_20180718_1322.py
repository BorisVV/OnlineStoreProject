# Generated by Django 2.0.7 on 2018-07-18 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', verbose_name='Birth date'),
        ),
    ]