# Generated by Django 4.0.2 on 2022-02-02 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_alter_questionstep_answer_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HitCount',
        ),
        migrations.RenameField(
            model_name='dialogitem',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='dialogitem',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='questionstep',
            old_name='question_id',
            new_name='question',
        ),
    ]
