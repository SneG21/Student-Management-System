# Generated by Django 5.1.1 on 2024-10-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_num', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=100)),
                ('field_of_study', models.CharField(max_length=50)),
                ('ap_score', models.FloatField()),
            ],
        ),
    ]
