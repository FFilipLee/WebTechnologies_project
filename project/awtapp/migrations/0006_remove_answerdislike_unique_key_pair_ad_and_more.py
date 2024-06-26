# Generated by Django 5.0.3 on 2024-05-21 07:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awtapp', '0005_rename_question_id_answer_question_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='answerdislike',
            name='unique_key_pair_ad',
        ),
        migrations.RemoveConstraint(
            model_name='answerlike',
            name='unique_key_pair_al',
        ),
        migrations.RemoveConstraint(
            model_name='questiondislike',
            name='unique_key_pair_qd',
        ),
        migrations.RemoveConstraint(
            model_name='questionlike',
            name='unique_key_pair_ql',
        ),
        migrations.RenameField(
            model_name='answerdislike',
            old_name='question',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='answerlike',
            old_name='question',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='questionlike',
            old_name='question_id',
            new_name='question',
        ),
        migrations.AddConstraint(
            model_name='answerdislike',
            constraint=models.UniqueConstraint(fields=('answer', 'user'), name='unique_key_pair_ad'),
        ),
        migrations.AddConstraint(
            model_name='answerlike',
            constraint=models.UniqueConstraint(fields=('answer', 'user'), name='unique_key_pair_al'),
        ),
        migrations.AddConstraint(
            model_name='questiondislike',
            constraint=models.UniqueConstraint(fields=('question', 'user'), name='unique_key_pair_qd'),
        ),
        migrations.AddConstraint(
            model_name='questionlike',
            constraint=models.UniqueConstraint(fields=('question', 'user'), name='unique_key_pair_ql'),
        ),
    ]
