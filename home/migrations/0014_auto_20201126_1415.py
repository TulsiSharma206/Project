# Generated by Django 3.0.3 on 2020-11-26 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_home_add_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Add_Event',
        ),
        migrations.AddField(
            model_name='event',
            name='Event_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eventname', to='home.Home'),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
