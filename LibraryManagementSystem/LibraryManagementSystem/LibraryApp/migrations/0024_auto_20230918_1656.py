# Generated by Django 3.0 on 2023-09-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0023_bookrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookrequest',
            name='bkd',
        ),
        migrations.RemoveField(
            model_name='bookrequest',
            name='bookname',
        ),
        migrations.RemoveField(
            model_name='bookrequest',
            name='bookno',
        ),
        migrations.RemoveField(
            model_name='bookrequest',
            name='usd',
        ),
        migrations.RemoveField(
            model_name='bookrequest',
            name='username',
        ),
        migrations.AddField(
            model_name='bookrequest',
            name='bookid',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookrequest',
            name='userid',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
