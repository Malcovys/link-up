# Generated by Django 4.2.3 on 2023-07-15 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absences', '0005_student_number_student_token_teachermodule'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachermodule',
            name='group',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='absences.group'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_begin', models.TimeField()),
                ('time_ending', models.TimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absences.teachermodule')),
            ],
        ),
    ]