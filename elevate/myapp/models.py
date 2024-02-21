from django.db import models

# Create your models here.
class pwd_emp(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=20)
    emp_cnic = models.BigIntegerField()
    office = models.CharField(max_length=20)
    class Meta:
        db_table="pwd_emp"

    def __str__(self):
        return self.emp_name
