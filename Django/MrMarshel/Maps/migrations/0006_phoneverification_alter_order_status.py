# Generated by Django 5.0.3 on 2024-05-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maps', '0005_master_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('verification_code', models.CharField(max_length=6)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'В очікуванні'), ('inProcess', 'В обробці'), ('completed', 'Завершено')], max_length=50),
        ),
    ]