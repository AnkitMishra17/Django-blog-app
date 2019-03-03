# Generated by Django 2.1.5 on 2019-01-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
