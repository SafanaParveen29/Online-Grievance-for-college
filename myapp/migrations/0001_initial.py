# Generated by Django 3.2 on 2024-03-26 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffId', models.CharField(max_length=10)),
                ('sName', models.CharField(max_length=50)),
                ('Designation', models.CharField(max_length=50)),
                ('Department', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNo', models.CharField(max_length=10, unique=True)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(blank=True, max_length=50)),
                ('PhoneNumber', models.CharField(max_length=10)),
                ('studentEmail', models.EmailField(max_length=254)),
                ('studentPassword', models.CharField(max_length=50)),
                ('ConfirmPassword', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HostelGrievance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IssueType', models.CharField(max_length=50)),
                ('RoomNumber', models.CharField(max_length=10)),
                ('Issue', models.TextField()),
                ('Impact', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved'), ('Closed', 'Closed')], default='Pending', max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Counseling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Academic', 'Academic Counseling'), ('Emotional', 'Emotional Support'), ('Career', 'Career Guidance'), ('Other', 'Other')], default='Other', max_length=20)),
                ('Problem', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved'), ('Closed', 'Closed')], default='Pending', max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='CollegeGrievance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IssueType', models.CharField(max_length=50)),
                ('Location', models.CharField(blank=True, max_length=50, null=True)),
                ('Issue', models.TextField()),
                ('Impact', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved'), ('Closed', 'Closed')], default='Pending', max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_type', models.CharField(max_length=30)),
                ('Purpose', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Issued', 'Issued')], default='Pending', max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
    ]
