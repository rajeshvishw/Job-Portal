# Generated by Django 4.2.5 on 2023-10-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_candidate_country_candidate_education_lavel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='profile_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]