# Generated by Django 4.1.4 on 2023-01-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Institute_Management_App",
            "0002_common_student_teacher_alter_master_password_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Book_Name", models.CharField(max_length=40)),
                ("Author_Name", models.CharField(max_length=40)),
                ("Price", models.CharField(max_length=40)),
                ("Time_Period", models.CharField(max_length=40)),
            ],
            options={"db_table": "book",},
        ),
        migrations.CreateModel(
            name="Club",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Club_Name", models.CharField(max_length=50)),
                ("Open_Time", models.CharField(default="10:00 AM", max_length=50)),
                ("Close_Time", models.CharField(default="04:00 PM", max_length=50)),
                ("Head_Of_Club", models.CharField(default="", max_length=50)),
                ("Contact", models.CharField(default="", max_length=10)),
            ],
            options={"db_table": "club",},
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Role_Type",
                    models.CharField(
                        blank=True,
                        choices=[("T", "Teacher"), ("S", "Student")],
                        default="",
                        max_length=5,
                    ),
                ),
            ],
            options={"db_table": "role",},
        ),
        migrations.RemoveField(model_name="student", name="Master",),
        migrations.RemoveField(model_name="teacher", name="Master",),
    ]
