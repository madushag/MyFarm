# Generated by Django 3.2.9 on 2021-11-09 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farm', '0005_alter_farm_farmer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FarmerStub',
        ),
        migrations.AlterField(
            model_name='farm',
            name='farmer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
