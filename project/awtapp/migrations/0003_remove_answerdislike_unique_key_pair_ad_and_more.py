# Generated by Django 5.0.3 on 2024-05-12 23:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awtapp', '0002_userprofile_alter_question_user_alter_comment_user_and_more'),
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
            model_name='answer',
            old_name='question',
            new_name='question_id',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='answerdislike',
            old_name='question',
            new_name='question_id',
        ),
        migrations.RenameField(
            model_name='answerdislike',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='answerlike',
            old_name='question',
            new_name='question_id',
        ),
        migrations.RenameField(
            model_name='answerlike',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='answer',
            new_name='answer_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='questiondislike',
            old_name='question',
            new_name='question_id',
        ),
        migrations.RenameField(
            model_name='questiondislike',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='questionlike',
            old_name='question',
            new_name='question_id',
        ),
        migrations.RenameField(
            model_name='questionlike',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='questiontag',
            old_name='question',
            new_name='question_id',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='upvotes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='upvotes',
        ),
        migrations.AddConstraint(
            model_name='answerdislike',
            constraint=models.UniqueConstraint(fields=('question_id', 'user_id'), name='unique_key_pair_ad'),
        ),
        migrations.AddConstraint(
            model_name='answerlike',
            constraint=models.UniqueConstraint(fields=('question_id', 'user_id'), name='unique_key_pair_al'),
        ),
        migrations.AddConstraint(
            model_name='questiondislike',
            constraint=models.UniqueConstraint(fields=('question_id', 'user_id'), name='unique_key_pair_qd'),
        ),
        migrations.AddConstraint(
            model_name='questionlike',
            constraint=models.UniqueConstraint(fields=('question_id', 'user_id'), name='unique_key_pair_ql'),
        ),
    ]
