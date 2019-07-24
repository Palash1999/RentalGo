# Generated by Django 2.2.1 on 2019-07-23 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('dprice', models.PositiveIntegerField()),
                ('wprice', models.PositiveIntegerField()),
                ('mprice', models.PositiveIntegerField()),
                ('img1', models.ImageField(null=True, upload_to='images/')),
                ('img2', models.ImageField(null=True, upload_to='images/')),
                ('available_for_selling', models.CharField(choices=[('y', 'YES'), ('n', 'NO')], default='n', max_length=1)),
                ('sprice', models.PositiveIntegerField(default=0)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=64)),
                ('zip_code', models.PositiveIntegerField()),
                ('contact', models.CharField(max_length=10)),
                ('order_date', models.DateField()),
                ('date_range', models.CharField(max_length=128)),
                ('cost', models.PositiveIntegerField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='products.Product')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iorder', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myorder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BuyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=64)),
                ('zip_code', models.PositiveIntegerField()),
                ('contact', models.CharField(max_length=10)),
                ('order_date', models.DateField()),
                ('cost', models.PositiveIntegerField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyorder', to='products.Product')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyiorder', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buymyorder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]