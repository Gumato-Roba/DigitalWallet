# Generated by Django 4.0.6 on 2022-07-31 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_alter_customer_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='currency',
            field=models.CharField(max_length=50, null=True),
        ),
    ]