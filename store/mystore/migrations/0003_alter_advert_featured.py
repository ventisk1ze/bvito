# Generated by Django 3.2.3 on 2021-05-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0002_advert_viewsamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='featured',
            field=models.BooleanField(null=True),
        ),
    ]
