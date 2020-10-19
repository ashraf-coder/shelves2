# Generated by Django 3.1 on 2020-09-30 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelvesapp', '0007_phone_addedon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('productName', models.CharField(max_length=30)),
                ('business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shelvesapp.business')),
            ],
        ),
    ]
