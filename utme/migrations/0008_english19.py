# Generated by Django 3.1.4 on 2020-12-11 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utme', '0007_auto_20201211_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='English19',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option1', models.TextField()),
                ('option2', models.TextField()),
                ('option3', models.TextField()),
                ('option4', models.TextField()),
            ],
        ),
    ]