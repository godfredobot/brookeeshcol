# Generated by Django 4.1.1 on 2022-11-10 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0004_alter_member_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
    ]