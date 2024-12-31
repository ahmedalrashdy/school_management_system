# Generated by Django 5.1.4 on 2024-12-27 22:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_due', models.FloatField(verbose_name='المبلغ المستحق')),
                ('fees_type', models.CharField(choices=[('tuition', 'رسوم دراسية'), ('registration', 'رسوم تسجيل'), ('books', 'رسوم كتب'), ('transportation', 'رسوم مواصلات'), ('activities', 'رسوم أنشطة'), ('uniform', 'رسوم زي موحد'), ('exam', 'رسوم امتحان'), ('other', 'رسوم أخرى')], max_length=20, verbose_name='نوع الرسوم')),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.academicyear', verbose_name='السنة الدراسية')),
                ('class_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.classlevel', verbose_name='الفصل الدراسي')),
            ],
            options={
                'verbose_name': 'رسوم دراسية',
                'verbose_name_plural': 'الرسوم الدراسية',
                'unique_together': {('class_level', 'academic_year', 'fees_type')},
            },
        ),
        migrations.CreateModel(
            name='Installment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='المبلغ المدفوع')),
                ('payment_date', models.DateField(verbose_name='تاريخ الدفع')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student', verbose_name='الطالب')),
                ('study_fees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fees.studyfees', verbose_name='الرسوم الدراسية')),
            ],
            options={
                'verbose_name': 'قسط',
                'verbose_name_plural': 'الأقساط',
            },
        ),
    ]
