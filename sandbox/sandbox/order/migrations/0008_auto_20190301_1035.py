# Generated by Django 2.2.5 on 2019-09-26 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20190926_1152'),
        ('communication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationevent',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communication.CommunicationEventType', verbose_name='Event Type'),
        ),
    ]