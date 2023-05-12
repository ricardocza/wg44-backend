from django.db import models


# Create your models here.
class Stocks(models.Model):
    class Meta:
        ordering = ["id"]

    ticker = models.CharField(max_length=12)
    ticker_name = models.CharField(max_length=100)
    closed_price = models.FloatField()
    pred_1 = models.FloatField()
    pred_2 = models.FloatField()
    pred_3 = models.FloatField()
    pred_4 = models.FloatField()
    pred_5 = models.FloatField()
    pred_6 = models.FloatField()
    diff_1 = models.FloatField(default=None, null=True)
    error_1 = models.FloatField(default=None, null=True)
    diff_2 = models.FloatField(default=None, null=True)
    error_2 = models.FloatField(default=None, null=True)
    diff_3 = models.FloatField(default=None, null=True)
    error_3 = models.FloatField(default=None, null=True)
    diff_4 = models.FloatField(default=None, null=True)
    error_4 = models.FloatField(default=None, null=True)
    diff_5 = models.FloatField(default=None, null=True)
    error_5 = models.FloatField(default=None, null=True)
    diff_6 = models.FloatField(default=None, null=True)
    error_6 = models.FloatField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
