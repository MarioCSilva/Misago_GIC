# Generated by Django 2.2.3 on 2019-09-28 21:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("misago_users", "0021_user_sso_id")]

    operations = [
        migrations.CreateModel(
            name="DeletedUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "deleted_on",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now
                    ),
                ),
                (
                    "deleted_by",
                    models.PositiveIntegerField(
                        choices=[(1, "By self"), (2, "By staff"), (3, "By system")],
                        db_index=True,
                    ),
                ),
            ],
            options={"ordering": ["-id"]},
        )
    ]
