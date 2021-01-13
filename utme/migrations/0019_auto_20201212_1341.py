# Generated by Django 3.1.4 on 2020-12-12 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utme', '0018_candidate_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='user_answer',
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('answer', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utme.candidate')),
            ],
        ),
    ]
