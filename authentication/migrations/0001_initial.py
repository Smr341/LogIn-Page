# Generated by Django 4.0.2 on 2022-02-11 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptype', models.CharField(max_length=122)),
                ('psummary', models.CharField(max_length=122)),
                ('pdescription', models.CharField(max_length=122)),
                ('kanalysis', models.CharField(max_length=122)),
                ('kinsights', models.CharField(max_length=250)),
                ('owner', models.CharField(max_length=250)),
            ],
        ),
    ]
