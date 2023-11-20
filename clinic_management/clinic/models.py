from django.db import models
from django.utils import timezone

class Clinic(models.Model):
    name = models.CharField(max_length=255, verbose_name='诊所备案名称')
    address = models.CharField(max_length=255, verbose_name='地址')
    legal_representative = models.CharField(max_length=255, verbose_name='法定代表人')
    main_person_in_charge = models.CharField(max_length=255, verbose_name='主要负责人')
    medical_subjects = models.CharField(max_length=255, verbose_name='诊疗科目')
    service_mode = models.CharField(max_length=255, verbose_name='服务方式')
    record_number = models.CharField(max_length=255, verbose_name='备案编号')
    ownership_form = models.CharField(max_length=255, verbose_name='所有制形式')
    business_nature = models.CharField(max_length=255, verbose_name='经营性质')
    administrative_approval_authority = models.CharField(max_length=255, verbose_name='行政审批机关')
    record_date = models.DateField(verbose_name='备案日期')
    record_validity_period = models.PositiveIntegerField(verbose_name='备案有效期（年）')
    record_expiry_date = models.DateField(blank=True, null=True, verbose_name='备案到期')

    def save(self, *args, **kwargs):
        if not self.record_expiry_date:
            self.record_expiry_date = self.record_date + timezone.timedelta(days=self.record_validity_period * 365)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
