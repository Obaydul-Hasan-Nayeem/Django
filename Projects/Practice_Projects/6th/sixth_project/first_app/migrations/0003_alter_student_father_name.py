# Generated by Django 4.2.3 on 2023-08-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_student_father_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.TextField(),
        ),
    ]
