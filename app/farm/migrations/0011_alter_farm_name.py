# Generated by Django 3.2.9 on 2021-12-03 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0010_alter_farm_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='name',
            field=models.CharField(max_length=200, verbose_name='POS Name'),
        ),
    ]