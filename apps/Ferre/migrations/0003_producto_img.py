# Generated by Django 2.0.6 on 2021-09-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ferre', '0002_auto_20210928_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img',
            field=models.URLField(default='https://i.postimg.cc/Hk439n1v/no-found.jpg', max_length=8000),
        ),
    ]