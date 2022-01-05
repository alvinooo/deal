# Generated by Django 4.0 on 2022-01-01 02:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ItemInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField()),
                ('price', models.FloatField()),
                ('quantity', models.FloatField()),
                ('unit', models.FloatField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prices.item')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prices.iteminstance')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prices.store')),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prices.iteminstance')),
            ],
        ),
        migrations.AddField(
            model_name='iteminstance',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prices.store'),
        ),
        migrations.CreateModel(
            name='CurrentBest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField()),
                ('price', models.FloatField()),
                ('quantity', models.FloatField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='best', to='prices.iteminstance')),
                ('next_best', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_best', to='prices.iteminstance')),
            ],
        ),
    ]