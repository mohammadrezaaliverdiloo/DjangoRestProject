# Generated by Django 4.2 on 2024-03-07 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_slug_alter_file_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='product.product', verbose_name='product'),
        ),
    ]
