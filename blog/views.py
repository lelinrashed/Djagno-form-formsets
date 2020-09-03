from django.utils import timezone

from blog.forms import TestForm, PostModelForm
from django.shortcuts import render

# Create your views here.


def home(request):
    # initial_dict = {
    #     # "some_text": "Text",
    #     "boolean": True,
    #     "integer": "123"
    # }
    #
    # form = TestForm(request.POST or None)
    #
    # if form.is_valid():
    #     print(form.cleaned_data)

    # if request.method == "POST":
    #     form = TestForm(data=request.POST or None)
    #     print(request.POST)
    # elif request.method == "GET":
    #     form = TestForm(user=request.user)
    #     print(request.GET)


    form = PostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        print(obj.title)
        obj.title = "some random title"
        obj.publish = timezone.now()
        obj.save()
    if form.has_error:
        print(form.errors.as_json())
        print(form.errors.as_text())

    context = {
        "form": form
    }
    return render(request, "forms.html", context)
