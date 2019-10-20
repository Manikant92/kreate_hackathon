# Generated by Django 2.2.6 on 2019-10-19 11:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0002_auto_20191019_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccuracyDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=100)),
                ('doc_type1', models.CharField(blank=True, choices=[('PAN', 'PAN Card,'), ('AADHAR', 'Aadhar Card'), ('DRIVINGLICENCE', 'Driving License'), ('VOTERID', 'Voter ID,'), ('BANKSTATEMENT', 'Bank Statements,')], max_length=100)),
                ('doc_type2', models.CharField(blank=True, choices=[('PAN', 'PAN Card,'), ('AADHAR', 'Aadhar Card'), ('DRIVINGLICENCE', 'Driving License'), ('VOTERID', 'Voter ID,'), ('BANKSTATEMENT', 'Bank Statements,')], max_length=100)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('doc_id', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=100)),
                ('doc_type', models.CharField(blank=True, choices=[('PAN', 'PAN Card,'), ('AADHAR', 'Aadhar Card'), ('DRIVINGLICENCE', 'Driving License'), ('VOTERID', 'Voter ID,'), ('BANKSTATEMENT', 'Bank Statements,')], max_length=100)),
                ('data', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None), blank=True, size=None)),
            ],
        ),
    ]