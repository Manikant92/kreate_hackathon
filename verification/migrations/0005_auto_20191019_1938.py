# Generated by Django 2.2.6 on 2019-10-19 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0004_auto_20191019_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdata',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('PAN', 'PAN Card,'), ('AADHAR', 'Aadhar Card'), ('DRIVINGLICENCE', 'Driving License'), ('VOTERID', 'Voter ID'), ('BANKSTATEMENT', 'Bank Statements')], max_length=100),
        ),
    ]
