# Generated by Django 4.1.2 on 2022-10-29 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_sepet_fiyat'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='stok',
            field=models.IntegerField(default=1, verbose_name='Stok'),
            preserve_default=False,
        ),
    ]