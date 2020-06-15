from django.shortcuts import render
from . import models


# 展示主页
def show_index(request):
    # 取出所有题目的信息
    test_codes = models.TestCode.objects.all()
    # 打包发送前端
    context = {
        'test_codes': test_codes,
    }
    return render(request, 'index.html', context=context)


# 展示题目代码详情
def show_code(request, title):
    # 根据title取出此题目的信息
    test_code = models.TestCode.objects.get(title=title)
    # 将题目信息打包到前端
    context = {
        'test_code': test_code,
    }
    return render(request, 'test_code.html', context=context)
