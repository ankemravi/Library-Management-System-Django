# Generated by Django 3.0 on 2023-09-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(blank=True, max_length=100, null=True)),
                ('authname', models.CharField(blank=True, max_length=100, null=True)),
                ('isbn', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
