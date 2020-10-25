# Generated by Django 3.0.8 on 2020-08-02 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200802_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Location'),
        ),
    ]
