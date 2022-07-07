# Generated by Django 3.2.7 on 2021-12-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cource',
            name='bought',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cource',
            name='clicks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cource',
            name='image',
            field=models.ImageField(default='default.png', upload_to='../static/images/cource_img'),
        ),
        migrations.AlterField(
            model_name='cource',
            name='impresions',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cource',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='../static/pdf'),
        ),
        migrations.AlterField(
            model_name='cource',
            name='preview_video',
            field=models.FileField(blank=True, null=True, upload_to='../static/preview_video'),
        ),
        migrations.AlterField(
            model_name='cource_user',
            name='image',
            field=models.ImageField(default='default.png', upload_to='static/profile_images'),
        ),
    ]