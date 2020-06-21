# Generated by Django 3.0.2 on 2020-06-18 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IndianCollegesApp', '0004_allcities'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(upload_to='all_images')),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IndianCollegesApp.AllColleges')),
            ],
        ),
    ]