# Generated by Django 4.2 on 2024-10-10 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('APP_DATA', '0001_initial'),
        ('Technical', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_kind', models.CharField(max_length=30, verbose_name='نوع السيارة')),
                ('car_number', models.CharField(max_length=30, verbose_name='رقم السيارة')),
                ('car_model', models.CharField(max_length=30, verbose_name='موديل السيارة')),
                ('car_motor', models.CharField(default='Motor_No', max_length=50, verbose_name=' رقم الماتور')),
                ('car_chassis', models.CharField(default='Chassis_No', max_length=50, verbose_name='رقم الشاسية ')),
                ('record_date', models.DateField(verbose_name='بداية الترخيص')),
                ('end_date', models.DateField(verbose_name='انتهاء الترخيص')),
                ('ADS_date', models.DateField(verbose_name='بداية الاعلان')),
                ('ADS_END', models.DateField(verbose_name='انتهاء الاعلان')),
                ('note', models.CharField(default='NO_NOTE', max_length=20, verbose_name='ملاحظات')),
                ('Officer', models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='car_officer', to='APP_DATA.delevry_officer', verbose_name='مندوب التسليم')),
                ('car_tank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_tank', to='APP_DATA.car_tank', verbose_name='نوع الوقود')),
            ],
            options={
                'verbose_name_plural': 'السيارات',
            },
        ),
        migrations.CreateModel(
            name='Oil_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_amount', models.IntegerField(verbose_name='مبلغ الوقود')),
                ('Car_meter', models.IntegerField(verbose_name='قراءة العداد')),
                ('date', models.DateField(verbose_name='التاريخ')),
                ('lastMeter', models.IntegerField(blank=True, null=True, verbose_name='عداد سابق')),
                ('metres', models.IntegerField(blank=True, null=True, verbose_name='عدد الكيلو')),
                ('Officer', models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Oil_Detail_officer', to='APP_DATA.delevry_officer', verbose_name='مندوب التسليم')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_Oil_Detail', to='DELVERY.car', verbose_name='السيارة')),
            ],
            options={
                'verbose_name_plural': 'استهلاك الوقود',
            },
        ),
        migrations.CreateModel(
            name='Oil_Change',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oil_kind', models.CharField(choices=[('700', '700'), ('1000', '1000'), ('3000', '3000'), ('5000', '5000'), ('10000', '10000')], max_length=50, verbose_name='نوع الزيت')),
                ('oil_name', models.CharField(max_length=100, verbose_name=' الزيت')),
                ('Car_meter', models.IntegerField(default=0, verbose_name='قراءة العداد')),
                ('date', models.DateField(verbose_name='التاريخ')),
                ('note', models.CharField(default='no note', max_length=300, verbose_name='ملاحظات')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_Oil_Change', to='DELVERY.car', verbose_name='السيارة')),
            ],
            options={
                'verbose_name_plural': 'تغيير الزيت',
            },
        ),
        migrations.CreateModel(
            name='Missions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=100, verbose_name='الاوردر')),
                ('author', models.CharField(max_length=100, verbose_name='المسئول')),
                ('detail', models.TextField(max_length=300, verbose_name='تفاصيل العملية')),
                ('date', models.DateField(auto_now_add=True, verbose_name='تاريخ ')),
                ('Officer', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.PROTECT, related_name='Mission_officer', to='APP_DATA.delevry_officer', verbose_name='المندوب')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Missions_car', to='DELVERY.car', verbose_name='رقم السيارة')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Missions_company', to='Technical.vendor', verbose_name=' الشركة')),
                ('mission', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.PROTECT, related_name='Mission_Kind', to='APP_DATA.mission_kind', verbose_name='نوع العملية')),
            ],
            options={
                'verbose_name_plural': 'العمليات',
            },
        ),
        migrations.CreateModel(
            name='Expenses_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=300, verbose_name='تفاصيل المصروف')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='التكلفة')),
                ('file', models.FileField(blank=True, null=True, upload_to='expenses_files', verbose_name='تحميل ملف')),
                ('date', models.DateField(auto_now_add=True, verbose_name='تاريخ المصروفات')),
                ('note', models.CharField(default='no-note', max_length=50, verbose_name='ملاحظات')),
                ('Officer', models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.PROTECT, to='APP_DATA.delevry_officer', verbose_name='مندوب التسليم')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='car_Expenses', to='DELVERY.car', verbose_name='السيارة')),
                ('expenses_kind', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='expenses_name', to='APP_DATA.expenses_kind', verbose_name='نوع المصروف')),
            ],
            options={
                'verbose_name_plural': 'تفاصيل المصروفات',
            },
        ),
        migrations.CreateModel(
            name='Company_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('مخزن', 'مخزن'), ('الإدارة', 'الإدارة'), ('محل', 'محل')], max_length=50, verbose_name='المكان')),
                ('address', models.CharField(max_length=500, verbose_name='عنوان الشركة')),
                ('location', models.CharField(max_length=500, verbose_name='موقع الشركة')),
                ('phone', models.CharField(blank=True, max_length=14, null=True, verbose_name='تليفون المسؤول')),
                ('response', models.CharField(blank=True, max_length=25, null=True, verbose_name='اسم المسؤول')),
                ('work_hours', models.CharField(blank=True, max_length=25, null=True, verbose_name='مواعيد العمل')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='company_details', to='Technical.vendor', verbose_name='اسم الشركة')),
            ],
            options={
                'verbose_name_plural': 'مواقع الشركات',
            },
        ),
    ]
