# Generated by Django 3.0.8 on 2020-08-02 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200802_1707'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='category',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Location'),
        ),
    ]
