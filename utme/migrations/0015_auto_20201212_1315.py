# Generated by Django 3.1.4 on 2020-12-12 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utme', '0014_auto_20201212_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='test',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='utme.english19'),
        ),
    ]