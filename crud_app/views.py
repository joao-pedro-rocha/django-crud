from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import CrudModel
from .forms import CrudForm

# Create your views here.
def create_view(request):
    form = CrudForm(request.POST or None)

    if form.is_valid():
        form.save()
    
    return render(request, 'create_view.html', locals())


def list_view(request):
    dataset = CrudModel.objects.all()

    return render(request, 'list_view.html', locals())


def detail_view(request, id):
    data = CrudModel.objects.get(id=id)

    return render(request, 'detail_view.html', locals())


def update_view(request, id):
    obj = get_object_or_404(CrudModel, id=id)
    form = CrudForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect('/'+id)

    return render(request, 'update_view.html', locals())


def delete_view(request, id):
    obj = get_object_or_404(CrudModel, id=id)

    if request.method == 'POST':
        obj.delete()

        return HttpResponseRedirect('/')

    return render(request, 'delete_view.html', locals())
