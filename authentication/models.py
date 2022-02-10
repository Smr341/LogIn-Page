from django.db import models


# Create your models here.
class Add(models.Model):
    ptype = models.CharField(max_length=122)
    psummary = models.CharField(max_length=122)
    pdescription = models.CharField(max_length=122)
    # p = models.BigIntegerField(models.BigIntegerField > 3)
    kanalysis = models.CharField(max_length=122)
    kinsights = models.CharField(max_length=250)
    owner = models.CharField(max_length=250)

    #   "ptype": ptype,
    #     "psummary": psummary,
    #     "pdescription": pdescription,
    #     "kanalysis": kanalysis,
    #     "kinsights": kinsights,
    #     "owner": owner

    def __str__(self):
        return self.name