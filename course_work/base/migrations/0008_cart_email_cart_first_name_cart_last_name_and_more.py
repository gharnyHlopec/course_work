# Generated by Django 4.2.11 on 2024-05-12 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_cart_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]