# Generated by Django 5.0.7 on 2024-08-02 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signup",
            name="email",
            field=models.EmailField(db_index=True, max_length=100, unique=True),
        ),
    ]