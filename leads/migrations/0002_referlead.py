# Generated by Django 3.1.4 on 2021-03-14 15:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferLead',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
