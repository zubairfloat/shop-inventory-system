# Generated by Django 2.2.7 on 2019-12-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased '), ('SOLD ', 'Item Sold'), ('RESTOCKING ', 'Item restocking in few days ')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues ', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Datacabels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased '), ('SOLD ', 'Item Sold'), ('RESTOCKING ', 'Item restocking in few days ')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues ', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Handfree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased '), ('SOLD ', 'Item Sold'), ('RESTOCKING ', 'Item restocking in few days ')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues ', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased '), ('SOLD ', 'Item Sold'), ('RESTOCKING ', 'Item restocking in few days ')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues ', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MemmoryCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased '), ('SOLD ', 'Item Sold'), ('RESTOCKING ', 'Item restocking in few days ')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues ', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased '), ('SOLD ', 'Item Sold'), ('RESTOCKING ', 'Item restocking in few days ')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues ', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased '), ('SOLD ', 'Item Sold'), ('RESTOCKING ', 'Item restocking in few days ')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues ', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased '), ('SOLD ', 'Item Sold'), ('RESTOCKING ', 'Item restocking in few days ')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues ', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
