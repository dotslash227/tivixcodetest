# Generated by Django 2.2.6 on 2019-10-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remarks',
            name='favorite',
            field=models.CharField(choices=[('True', 'Yes'), ('False', 'No')], default='False', max_length=10),
        ),
    ]
