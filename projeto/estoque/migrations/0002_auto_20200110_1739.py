# Generated by Django 3.0.1 on 2020-01-10 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='movimento',
            field=models.CharField(choices=[('e', 'entrada'), ('s', 'saida')], max_length=1),
        ),
    ]
