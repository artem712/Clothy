# Generated by Django 2.2.7 on 2019-12-31 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20191231_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='chekouthistory',
            name='product',
            field=models.TextField(default='', max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chekouthistory',
            name='shipping_type',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]