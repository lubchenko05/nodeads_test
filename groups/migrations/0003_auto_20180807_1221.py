# Generated by Django 2.1 on 2018-08-07 09:21

from django.db import migrations, models
import groups.validators


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20180807_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='icon',
            field=models.ImageField(default='images/None/no-group-icon.jpg', upload_to='images/Elements/', validators=[groups.validators.validate_image_extension]),
        ),
        migrations.AlterField(
            model_name='group',
            name='icon',
            field=models.ImageField(default='images/None/no-element-icon.jpg', upload_to='images/Groups/', validators=[groups.validators.validate_image_extension]),
        ),
    ]