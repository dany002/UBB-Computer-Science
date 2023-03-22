# Generated by Django 4.1.7 on 2023-03-20 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nameOfProject', models.CharField(max_length=200)),
                ('clientName', models.CharField(max_length=200)),
                ('budget', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nameOfTeam', models.CharField(max_length=100)),
                ('freePlaces', models.IntegerField()),
                ('purpose', models.CharField(max_length=200)),
                ('admin', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nameOfTask', models.CharField(max_length=200)),
                ('daysToImplement', models.IntegerField()),
                ('difficulty', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=100)),
                ('taken', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectTask', to='employee.project')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamTask', to='employee.team')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('employmentDate', models.DateField()),
                ('phoneNumber', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('wage', models.IntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamEmployee', to='employee.team')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
