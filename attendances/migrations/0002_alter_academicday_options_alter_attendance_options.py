# Generated by Django 5.1.4 on 2024-12-28 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academicday',
            options={'verbose_name': 'اليوم الأكاديمي', 'verbose_name_plural': 'الأيام الأكاديمية'},
        ),
        migrations.AlterModelOptions(
            name='attendance',
            options={'verbose_name': 'تحضير', 'verbose_name_plural': 'تحضير'},
        ),
    ]
