from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from manager.models import *


class WorkerListView(TemplateView):
    template_name = "worker_list.html"

    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        workers = Worker.objects.all()  # データベースからオブジェクトを取得して
        # workers = Worker.objects.filter(person__sex=Person.MAN) # 男だけデータ取得
        context['workers'] = workers  # 入れ物に入れる
        return render(self.request, self.template_name, context)

# 新しいhomeビューを追加
def home(request):
    return render(request, 'home.html')
