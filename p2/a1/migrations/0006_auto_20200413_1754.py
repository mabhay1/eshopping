# Generated by Django 3.0.4 on 2020-04-13 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0005_auto_20200413_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returnorder',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='returns', to='a1.Order'),
        ),
    ]
