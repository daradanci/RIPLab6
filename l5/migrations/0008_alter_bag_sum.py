# Generated by Django 4.1.2 on 2022-11-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l5', '0007_alter_bag_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='sum',
            field=models.IntegerField(default=0, null=True),
        ),
    ]