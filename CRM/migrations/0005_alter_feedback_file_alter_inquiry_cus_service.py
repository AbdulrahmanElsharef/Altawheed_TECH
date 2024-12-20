# Generated by Django 4.2 on 2024-10-23 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0004_cus_service_inquiry_cus_service_alter_feedback_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='file',
            field=models.FileField(max_length=50, upload_to='CRM/Files/<function user_directory at 0x000001D67A911800>', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='Cus_Service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Inquiry_Cus_Service', to='CRM.cus_service'),
        ),
    ]
