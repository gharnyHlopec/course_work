# Generated by Django 4.2.11 on 2024-05-12 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_cart_email_cart_first_name_cart_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('-', '-'), ('В обработке', 'В обработке'), ('Принят', 'Принят'), ('Отменен', 'Отменен'), ('Завершен', 'Завершен')], default='-', max_length=20),
        ),
    ]
