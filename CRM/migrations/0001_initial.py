# Generated by Django 4.2 on 2024-10-15 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Technical', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Brand')),
                ('note', models.CharField(blank=True, max_length=50, null=True, verbose_name='Note')),
            ],
            options={
                'verbose_name_plural': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Category')),
                ('note', models.CharField(blank=True, max_length=50, null=True, verbose_name='Note')),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='FeedBack_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=50, unique=True, verbose_name='feedback')),
                ('note', models.CharField(blank=True, max_length=50, null=True, verbose_name='Note')),
            ],
            options={
                'verbose_name_plural': 'FeedBack_Status',
            },
        ),
        migrations.CreateModel(
            name='inquiry_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inquiry', models.CharField(max_length=50, unique=True, verbose_name='Inquiry')),
                ('note', models.CharField(blank=True, max_length=50, null=True, verbose_name='Note')),
            ],
            options={
                'verbose_name_plural': 'inquiry_Status',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Source')),
                ('note', models.CharField(blank=True, max_length=50, null=True, verbose_name='Note')),
            ],
            options={
                'verbose_name_plural': 'Source',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Status')),
                ('note', models.CharField(blank=True, max_length=50, null=True, verbose_name='Note')),
            ],
            options={
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InquiryId', models.IntegerField(blank=True, null=True)),
                ('Details', models.CharField(max_length=250, verbose_name='Details')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Note', models.CharField(default='No_Note', max_length=50, verbose_name='Note')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Inquiry_brand', to='CRM.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Inquiry_category', to='CRM.category')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Inquiry_client', to='Technical.end_user')),
                ('inquiry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inquiry_Status', to='CRM.inquiry_status')),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='request_Inquiry', to='Technical.request')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Inquiry_Source', to='CRM.source')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Status_client', to='CRM.status')),
            ],
            options={
                'verbose_name_plural': 'Inquiry',
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Details', models.CharField(max_length=250, verbose_name='FeedBack')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('note', models.CharField(default='No_Note', max_length=50, verbose_name='Note')),
                ('Inquiry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='FeedBack_Inquiry', to='CRM.inquiry')),
                ('Status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Feedback_Status', to='CRM.feedback_status')),
            ],
            options={
                'verbose_name_plural': 'FeedBack',
            },
        ),
    ]
