from django.shortcuts import render, HttpResponse
from . import models
from django.template import RequestContext
import json
# Create your views here.

def students(request):
    cls_list = models.Classes.objects.all()
    stu_list = models.Student.objects.all()
    return render(request, 'school/students.html', {'stu_list': stu_list, 'cls_list': cls_list})

def add_student(request):
    response = {'status': True, 'message': None, 'data': None}
    print("Si se ejecuta")
    try:
        print(request.POST.get('username'))
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cls_id')
        obj = models.Student.objects.create(
            username = u,
            age = a,
            gender = g,
            cs_id = c
        )

        obj.save()

        response['data'] = obj.id
    except Exception as e:
        print(e)
        response['status'] = False
        response['mensaje'] = 'Error de entrada del usuario'
    
    result = json.dumps(response, ensure_ascii= False)

    return HttpResponse(result)

def del_student(request):
    ret = {'status': True}

    try:
        nid = request.get('nid')
        models.Student.objects.filter(id=nid).delete()
    except Exception as e:
        ret['status': False]
    
    return HttpResponse(json.dumps(ret))

def edit_student(request):
    response = {'code': 1000, 'message': None}

    try:
        nid = request.POST.get('nid')
        user = request.POST.get('user')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cls_id = request.POST.get('cls_id')

        models.Student.objects.filter(id=nid).update(
            username = user,
            age = age,
            gender = gender,
            cs_id=cls_id

        )
    except Exception as e:
        response['code'] = 1001
        response['message'] = str(e)
    
    return HttpResponse(json.dumps(response))
