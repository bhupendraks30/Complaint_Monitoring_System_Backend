
# Generated by Django 5.0.6 on 2024-07-02 12:54

# Generated by Django 5.0.6 on 2024-06-22 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(editable=False, max_length=12, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=1000)),
                ('pin_code', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/profile_Images/')),
                ('role', models.IntegerField(choices=[(0, 'User'), (1, 'Admin')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TourPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='Images/Dam/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='Images/Dam/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='Images/Dam/')),
                ('video1_link', models.CharField(blank=True, max_length=1200, null=True)),
                ('video2_link', models.CharField(blank=True, max_length=1200, null=True)),
                ('video3_link', models.CharField(blank=True, max_length=1200, null=True)),
                ('video4_link', models.CharField(blank=True, max_length=1200, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('popular', models.BooleanField()),
                ('categoty_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint.category')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=1000)),
                ('pin_code', models.CharField(max_length=10)),
                ('category', models.CharField(choices=[('technical', 'Technical Issues'), ('service_quality', 'Service Quality'), ('data_security', 'Data Security'), ('training_support', 'Training and Support'), ('feedback_suggestions', 'Feedback and Suggestions'), ('general_inquiries', 'General Inquiries'), ('Land Records', 'Land Records'), ('Public Distribution System', 'Public Distribution System'), ('Election', 'Election'), ('Social Welfare', 'Social Welfare'), ('Health Services', 'Health Services'), ('Taxation', 'Taxation'), ('Law and Order', 'Law and Order'), ('Education', 'Education'), ('Public Transport', 'Public Transport'), ('Water Transport', 'Water Transport'), ('Water Supply', 'Water Supply'), ('Electricity', 'Electricity'), ('Sanitation', 'Sanitation'), ('Environmental Issues', 'Environmental Issues'), ('Infrastructure', 'Infrastructure'), ('Public', 'Public'), ('Visitor', 'Visitor')], max_length=50, verbose_name='Category')),
                ('description', models.TextField(verbose_name='Description')),
                ('date_submitted', models.DateTimeField(auto_now_add=True, verbose_name='Date Submitted')),
                ('status', models.CharField(default='Pending', max_length=50, verbose_name='Status')),
                ('cid', models.CharField(editable=False, max_length=12, unique=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint.user')),
            ],
            options={
                'verbose_name': 'Complaint',
                'verbose_name_plural': 'Complaints',
            },
        ),
    ]