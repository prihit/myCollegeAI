# Generated by Django 3.1.5 on 2021-06-09 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0016_auto_20210608_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='admission_procedure',
            field=models.TextField(null=True),
        ),
    ]
