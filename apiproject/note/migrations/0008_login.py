# Generated by Django 3.2.19 on 2023-06-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0007_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('u_id', models.IntegerField()),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
    ]