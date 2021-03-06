# Generated by Django 4.0.3 on 2022-03-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0007_distance_bundle_quantity_bundle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_col', models.DateField(verbose_name='Date')),
                ('name_col', models.CharField(max_length=200, verbose_name='Name')),
                ('quantity_col', models.CharField(max_length=100, verbose_name='Quantity')),
                ('distance_col', models.CharField(max_length=100, verbose_name='Distance')),
            ],
        ),
        migrations.RemoveField(
            model_name='distance',
            name='bundle',
        ),
        migrations.RemoveField(
            model_name='name',
            name='bundle',
        ),
        migrations.RemoveField(
            model_name='quantity',
            name='bundle',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.DeleteModel(
            name='Distance',
        ),
        migrations.DeleteModel(
            name='Name',
        ),
        migrations.DeleteModel(
            name='Quantity',
        ),
    ]
