from django.db import models

class Data(models.Model):
    account_date = models.DateField()
    shop = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    account = models.IntegerField(default=0)
    
    def __str__(self):
        return 'ID:' + str(self.id) + ',' + str(self.account_date) + ',' + self.shop + ',' +  \
            self.category + ',' + str(self.account) + '円'
