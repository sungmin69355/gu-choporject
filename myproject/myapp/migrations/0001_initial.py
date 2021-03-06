# Generated by Django 3.0.7 on 2020-07-26 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20200726_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('content', models.CharField(max_length=4000)),
                ('published', models.DateTimeField(auto_now=True)),
                ('weather', models.CharField(max_length=15)),
                ('emotion', models.CharField(max_length=15)),
                ('timeout', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]
