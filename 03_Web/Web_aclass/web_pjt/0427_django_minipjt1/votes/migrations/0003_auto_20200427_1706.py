# Generated by Django 2.1.15 on 2020-04-27 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0002_choice_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=140, verbose_name='보기1 문항')),
                ('count', models.IntegerField(default=0, verbose_name='보기1 투표수')),
                ('vote', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='votes.Vote')),
            ],
        ),
        migrations.CreateModel(
            name='Choice2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=140, verbose_name='보기2 문항')),
                ('count', models.IntegerField(default=0, verbose_name='보기2 투표수')),
                ('vote', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='votes.Vote')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='vote',
        ),
        migrations.AlterField(
            model_name='comment',
            name='choice',
            field=models.CharField(max_length=140, verbose_name='선택'),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
