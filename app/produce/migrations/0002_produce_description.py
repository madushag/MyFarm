# Generated by Django 3.2.9 on 2021-11-18 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produce',
            name='description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
