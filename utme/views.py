# from django.db.models.query import QuerySet
# from django.core import paginator
from django.core import paginator
from django.http import request
from django.shortcuts import redirect, render
from .models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import User_Option

# Create your views here.

# homepage
def register(request):
    return render(request, 'candReg.html', {})


def pre_exam(request):
    opt = []
    
    
    # if request.method == 'POST':
    #     name = request.POST['users_name']
    #     print('my name is ' + name)
    form = User_Option()
    qu = English19.objects.filter()
    try:
        username = request.POST["users_name", False]
    except MultiValueDictKeyError:
        username = False
    existing_user = Candidate.objects.filter(user=username).exists()
    if existing_user:
        user = Candidate.objects.filter(user=username)
        print("user exists")
    else:
        user = Candidate.objects.create(user=username)
        user.save()
    # subj = request.POST["subject"]
    # sel = Candidate.objects.update(Test=subj)
    # print(user.user)
    paginator = Paginator(qu, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_qu = paginator.page(page)
    except PageNotAnInteger:
        paginated_qu = paginator.page(1)
    except EmptyPage:
        paginated_qu = paginator.page(paginator.num_pages)
    print(page_request_var)
    
    
    if request.method == "POST":
        try:
            option = request.POST['option']
            print(option)
            opt.append(option)
            paginated_qu.next_page_number
            # '?' + page_request_var + '=' + paginated_qu.previous_page_number
        except MultiValueDictKeyError:
            option = False
            paginated_qu.next_page_number
    num = 1
   
        # else:
        #     url = paginated_qu.number
    context = {
        "user": user,
        "queryset": paginated_qu,
        'queryset': paginator.page(num),
        'page_request_var': page_request_var,
        # 'form': form,
    }
    return render(request, 'exam.html', context)



def process(request):
    qu = English19.objects.filter()
    paginator = Paginator(qu, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_qu = paginator.page(page)
    except PageNotAnInteger:
        paginated_qu = paginator.page(1)
    except EmptyPage:
        paginated_qu = paginator.page(paginator.num_pages)
        
    if request == "POST":
        option = request.POST['option']
        print(option)
        if paginated_qu.has_previous:
            url = '?' + page_request_var + '=' + paginated_qu.previous_page_number
            redirect(pre_exam)
        if paginated_qu.has_next:
            url = '?' + page_request_var + '=' + paginated_qu.previous_page_number
            redirect(pre_exam)
        
    context = {
        
    }
    return render(request, context)


def index(request):
    return render(request, 'blog.html', {})
def postdet(request):
    return render(request, 'post.html', {})
    # pass