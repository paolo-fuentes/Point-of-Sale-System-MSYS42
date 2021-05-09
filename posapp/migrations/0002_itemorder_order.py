# Generated by Django 3.2 on 2021-04-25 12:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_amount', models.IntegerField(default=None)),
                ('order_date', models.DateField(default=django.utils.timezone.now)),
                ('payment_type', models.CharField(choices=[('Cash', 'Cash'), ('Credit Card', 'Credit Card')], default='Cash', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_total', models.IntegerField(default=None)),
                ('quantity', models.IntegerField(default=None)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posapp.item')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posapp.order')),
            ],
        ),
    ]
