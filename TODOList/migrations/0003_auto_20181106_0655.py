# Generated by Django 2.1.2 on 2018-11-06 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODOList', '0002_auto_20181106_0650'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MEMO', models.CharField(max_length=120)),
                ('CONDITION', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='What',
        ),
    ]