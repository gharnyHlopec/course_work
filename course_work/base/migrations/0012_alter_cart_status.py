# Generated by Django 4.2.11 on 2024-05-13 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_cart_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('-', '-'), ('В обработке', 'В обработке'), ('Принят', 'Принят'), ('Отменен', 'Отменен'), ('Отменен системой (на складе недостаточно товара)', 'Отменен системой (на складе недостаточно товара)'), ('Завершен', 'Завершен')], default='-', max_length=50),
        ),
    ]
