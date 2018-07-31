# Generated by Django 2.0.5 on 2018-07-31 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('total', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('phone', models.CharField(blank=True, max_length=120, null=True)),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('subtotal', models.IntegerField(default=0)),
                ('shipping', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('pay', models.CharField(choices=[('面交自取', '面交自取'), ('超商取貨付款', '超商取貨付款')], default='', max_length=120)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('新建立', '新建立'), ('已寄出', '已寄出'), ('退貨', '退貨')], default='新建立', max_length=120)),
                ('done', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='cart.Order'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product'),
        ),
    ]
