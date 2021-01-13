# Generated by Django 3.1.4 on 2020-12-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utme', '0024_english19_has_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='english19',
            name='option1_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='english19',
            name='option2_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='english19',
            name='option3_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='english19',
            name='option4_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='english19',
            name='right_answer_img',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='english19',
            name='option1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='english19',
            name='option2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='english19',
            name='option3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='english19',
            name='option4',
            field=models.TextField(blank=True),
        ),
    ]
