# Generated by Django 4.1 on 2022-09-13 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=40)),
                ('preco', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=60)),
            ],
        ),
    ]
