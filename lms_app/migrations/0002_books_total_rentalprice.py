# Generated by Django 4.0.4 on 2022-05-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='total_rentalprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]