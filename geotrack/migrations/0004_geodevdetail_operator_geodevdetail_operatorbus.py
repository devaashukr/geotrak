# Generated by Django 4.2.5 on 2023-10-06 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
        ("geotrack", "0003_remove_geodevdetail_operator_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="geodevdetail",
            name="operator",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="geodevdetails",
                to="users.operator",
            ),
        ),
        migrations.AddField(
            model_name="geodevdetail",
            name="operatorbus",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="geodevdetails",
                to="users.operatorbuses",
            ),
        ),
    ]
