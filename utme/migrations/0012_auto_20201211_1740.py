# Generated by Django 3.1.4 on 2020-12-11 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utme', '0011_auto_20201211_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='user_answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='english19',
            name='option1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='english19',
            name='option2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='english19',
            name='option3',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='english19',
            name='option4',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='english19',
            name='question',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='english19',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utme.candidate'),
        ),
    ]
