# Generated by Django 4.0.2 on 2022-02-02 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_answertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField(default=1, verbose_name='Этап вопроса')),
                ('question_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.question')),
            ],
        ),
        migrations.DeleteModel(
            name='AnswerType',
        ),
    ]
