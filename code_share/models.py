from django.db import models


# 每个题的信息
class TestCode(models.Model):
    title = models.CharField(max_length=100, primary_key=True, verbose_name='标题')
    code = models.TextField(verbose_name='代码')
    status = models.CharField(max_length=20, verbose_name='题目状态', default='未完成')
    remark = models.CharField(max_length=200, verbose_name='备注', default='暂无说明')

    class Meta:
        verbose_name_plural = '题目信息'
        verbose_name = '题目信息'



