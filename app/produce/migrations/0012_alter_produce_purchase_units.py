# Generated by Django 3.2.9 on 2021-12-10 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produce', '0011_produce_purchase_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produce',
            name='purchase_units',
            field=models.CharField(choices=[('OUNCE', 'oz'), ('PINT', 'pt'), ('QUART', 'qt'), ('BUNCH', 'Bunch'), ('POUND', 'lbs')], max_length=20),
        ),
    ]
