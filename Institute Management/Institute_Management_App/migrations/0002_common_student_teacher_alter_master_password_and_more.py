# Generated by Django 4.1.4 on 2022-12-28 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Institute_Management_App", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Common",
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
                ("Name", models.CharField(max_length=50)),
                ("DateOfBirth", models.DateField(default="2022-11-21")),
                ("DateOfJoining", models.DateField(default="2022-11-21")),
                ("Address", models.CharField(max_length=100)),
            ],
            options={"db_table": "common",},
        ),
        migrations.CreateModel(
            name="Student",
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
                ("Roll_Number", models.CharField(max_length=20)),
                (
                    "Common",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Institute_Management_App.common",
                    ),
                ),
            ],
            options={"db_table": "student",},
        ),
        migrations.CreateModel(
            name="Teacher",
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
                ("Compensation", models.CharField(max_length=10)),
                (
                    "Common",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Institute_Management_App.common",
                    ),
                ),
            ],
            options={"db_table": "teacher",},
        ),
        migrations.AlterField(
            model_name="master",
            name="Password",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.DeleteModel(name="UserProfile",),
        migrations.AddField(
            model_name="teacher",
            name="Master",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Institute_Management_App.master",
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="Master",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Institute_Management_App.master",
            ),
        ),
        migrations.AddField(
            model_name="common",
            name="Master",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Institute_Management_App.master",
            ),
        ),
    ]
