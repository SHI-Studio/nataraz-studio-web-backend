# Generated by Django 5.1.2 on 2024-10-29 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='media_type',
            new_name='media_text',
        ),
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to='media/general/'),
        ),
    ]
