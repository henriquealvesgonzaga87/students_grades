# Generated by Django 4.1.4 on 2022-12-19 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_studend_thirdquarter_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='AverageGrades',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('a_math', models.Field(verbose_name='Average Math')),
                ('a_natural_sciences', models.Field(verbose_name='Average Natural Sciences')),
                ('a_human_sciences', models.Field(verbose_name='Average Human Sciences')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]