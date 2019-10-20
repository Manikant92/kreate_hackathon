# Generated by Django 2.2.6 on 2019-10-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('doc_type', models.CharField(blank=True, choices=[('PAN', 'PAN Card,'), ('AADHAR', 'Aadhar Card'), ('DRIVINGLICENCE', 'Driving License'), ('VOTERID', 'Voter ID,'), ('BANKSTATEMENT', 'Bank Statements,')], max_length=100, null=True)),
                ('doc_id', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]