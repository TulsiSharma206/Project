# Generated by Django 3.0.3 on 2020-11-25 11:34

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201125_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='Details',
        ),
        migrations.AddField(
            model_name='home',
            name='Designation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='home',
            name='Email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='home',
            name='Phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AddField(
            model_name='home',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]
