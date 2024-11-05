# Generated by Django 4.2 on 2024-10-20 14:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0006_remove_delivery_client_qt_remove_delivery_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receiving',
            options={'verbose_name_plural': 'Receiving'},
        ),
        migrations.AlterField(
            model_name='receiving',
            name='collection',
            field=models.IntegerField(default=0, verbose_name='collection'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='Preparing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Preparing_Status', to='Orders.order_status'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Warehouse_Order', to='Orders.order'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='work',
            field=models.CharField(blank=True, choices=[('2', '2'), ('4', '4'), ('6', '6'), ('8', '8'), ('10', '10')], max_length=10, null=True),
        ),
    ]