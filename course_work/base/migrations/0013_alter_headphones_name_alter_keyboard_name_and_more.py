# Generated by Django 4.2.11 on 2024-05-14 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_cart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headphones',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='keyboard',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]