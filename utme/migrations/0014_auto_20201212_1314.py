# Generated by Django 3.1.4 on 2020-12-12 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utme', '0013_auto_20201212_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='english19',
            name='user',
        ),
        migrations.AddField(
            model_name='candidate',
            name='test',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='utme.english19'),
        ),
    ]