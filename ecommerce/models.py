from django.db import models


class AdminModel(models.Model):

    id = models.AutoField(
        db_column='IdAdmin', primary_key=True
    )
