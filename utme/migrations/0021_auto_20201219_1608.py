# Generated by Django 3.1.4 on 2020-12-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utme', '0020_remove_candidate_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='english19',
            name='has_img',
            field=models.BooleanField(default='False'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='english19',
            name='question_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='english19',
            name='option1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='english19',
            name='option2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='english19',
            name='option3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='english19',
            name='option4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='english19',
            name='question',
            field=models.TextField(blank=True),
        ),
    ]