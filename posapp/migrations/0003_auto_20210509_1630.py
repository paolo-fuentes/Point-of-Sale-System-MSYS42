# Generated by Django 3.0.14 on 2021-05-09 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posapp', '0002_itemorder_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_quantity',
            new_name='stock_quantity',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_amount',
            new_name='total_amount',
        ),
        migrations.RemoveField(
            model_name='itemorder',
            name='item',
        ),
        migrations.RemoveField(
            model_name='itemorder',
            name='order',
        ),
        migrations.AddField(
            model_name='itemorder',
            name='item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posapp.Item'),
        ),
        migrations.AddField(
            model_name='itemorder',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posapp.Order'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='itemorder',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='itemorder',
            name='line_total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.IntegerField(choices=[(1, 'Cash'), (2, 'Card')]),
        ),
    ]
