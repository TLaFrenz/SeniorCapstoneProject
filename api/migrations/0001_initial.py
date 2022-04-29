# Generated by Django 4.0.3 on 2022-04-28 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('credit_info', models.CharField(max_length=16)),
                ('CSV', models.CharField(max_length=6)),
                ('logged_in', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('mechanic_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('checking_account', models.CharField(max_length=32)),
                ('ASE_certified', models.BooleanField(default=True)),
                ('available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('cost', models.FloatField(default=24.99)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(default='', max_length=16)),
                ('lname', models.CharField(default='', max_length=32)),
                ('address', models.CharField(default='', max_length=64)),
                ('user_type', models.CharField(default='C', max_length=1)),
                ('DOB', models.DateField()),
                ('email', models.CharField(max_length=30, unique=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(default='', max_length=32)),
                ('model', models.CharField(default='', max_length=32)),
                ('year', models.IntegerField(default=2022)),
                ('last_oil_change', models.DateField()),
                ('last_state_inspection', models.DateField()),
                ('registration_number', models.IntegerField(default=1)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=140)),
                ('rating', models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)])),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
                ('m_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mechanic')),
            ],
        ),
        migrations.CreateModel(
            name='Mechanic_Service_Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mechanic')),
                ('s_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.services')),
            ],
        ),
        migrations.AddField(
            model_name='mechanic',
            name='u_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AddField(
            model_name='customer',
            name='u_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.CreateModel(
            name='Current_Jobs',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(choices=[('1', 'Open'), ('2', 'In Progress'), ('3', 'Complete')], max_length=16)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
                ('s_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.services')),
            ],
        ),
    ]