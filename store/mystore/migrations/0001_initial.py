# Generated by Django 3.2.3 on 2021-05-21 10:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phoneNumber', models.IntegerField()),
                ('posterName', models.CharField(max_length=100)),
                ('pubDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('city', models.CharField(max_length=20)),
                ('featured', models.BooleanField()),
            ],
        ),
    ]
