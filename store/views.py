import json
import random
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from drive import settings
from drive.settings import BASE_DIR
from store.models import ProfilePic, document, folders, size
from django.db.models import Q
import mimetypes
import os
from django.http.response import HttpResponse

# Create your views here.

def register(request):
    if(request.method=="POST"):
        body=json.loads(request.body)
        x=User.objects.filter(Q(username=body['user']) | Q(email=body['mail']))
        if(x.exists()):
            msg={'msg':'Username already exist'}
            return JsonResponse(msg, status=401, safe=False)
        global otp
        otp[body['mail']]=random.randint(1000,10000)
        send_mail(
                'OTP for registeration',
                '''Hello {name}.
                This mail is send by the company CloudBox. Your otp for sign up is {o}.
                \n\n\nThis message is generated by the server so do not reply back to it.'''.format(name=body['fname'], o=otp),
                'sudhanshu.2125it1056@kiet.edu',
                [body['mail']],
                fail_silently=False
                 )
        msg={'msg':'Success'}
        return JsonResponse(msg, status=200, safe=False)


def otpverify(request):
    if(request.method=="POST"):
        body=json.loads(request.body)
        if(body['otp']==otp[body['mail']]):
            otp.pop(body['otp'])
            user=User.objects.create_user(body['user'], body['mail'], body['pass1'])
            user.first_name=body['fname']
            user.last_name=body['lname']
            user.save()
            send_mail(
                'Account Created Succesfully',
                '''Hello {name}.
                You have succesfully signed up on the cloudbox server.
                This is the confirmation mail send you by Cloudbox.
                \n\n\n
                This message is generated by the server so do not reply back to it.'''.format(name=body['fname']),
                'sudhanshu.2125it1056@kiet.edu',
                [body['mail']],
                fail_silently=False
            )
            msg={'msg':'Account created'}
            return JsonResponse(msg, status=201, safe=False)
        else:
            msg={'msg':'OTP did not matched'}
            return JsonResponse(msg, status=401, safe=False)


def log_in(request):
    if(request.method=="POST"):
        body=json.loads(request.body)
        user=authenticate(username=body['user'], password=body['pass1'])
        if(user is not None):
            login(request, user)
            print(user.id)
            request.session['id']=user.id
            msg={'msg':'Success'}
            return JsonResponse(msg, status=200, safe=False)
        else:
            msg={'msg':'Wrong credentials'}
            return JsonResponse(msg, status=401, safe=False)


def upload(request):
    if(request.method=="POST"):
        if(request.user.is_authenticated):
            body=request.FILES
            p=request.POST
            print(p)
            print(body.keys())
            f=body['file']
            z=str(f)
            print(type(z))
            u=User.objects.get(id=request.user.id)
            x=folders.objects.get(id=p['id'])
            print(body['file'].size)
            if(z[-3:]=='jpg' or z[-4:]=='jpeg' or z[-3:]=='png' or z[-3:]=='svg'):
                a='images'
            elif(z[-3:]=='mp4'):
                a='videoes'
            else:
                a='files'
            doc=document(file=f, user=u, folder=x, byte=body['file'].size, type=a)
            doc.save()
            s=document.objects.filter(folder=x, user=u, delete=0)
            space=0
            for i in s:
                space=space+i.byte
            print(space)
            space=space/(1024*1024)
            x.s=space
            x.save()
            msg={'msg':'success'}
            return JsonResponse(msg, status=200, safe=False)
        else:
            msg={'msg':'Unauthorized'}
            return JsonResponse(msg, safe=False, status=401)


def details(request):
    if(request.user.is_authenticated):
        print(request.user)
        print(type(request))
        u=User.objects.get(request.user.id)
        pic=ProfilePic.objects.filter(user=u)
        if(not pic.exists()):
            p="No pic"
        else:
            p=pic[0].pic
        x={'fname':request.user.first_name,'lname':request.user.last_name,'user':request.user.username,'mail':request.user.email, 'pic':p}
        return JsonResponse(x, status=200, safe=False)
    else:
        msg={'msg':'Unauthorized'}
        return JsonResponse(msg, safe=False, status=401)


def fold(request):
    if(request.user.is_authenticated):
        u=User.objects.get(id=request.user.id)
        x=list(folders.objects.filter(user=u).distinct().values())
        print(x)
        return JsonResponse(x, safe=False, status=200)
    else:
        msg={'msg':'Unauthorized'}
        return JsonResponse(msg, safe=False, status=401)


def addfolder(request):
    if(request.user.is_authenticated):
        body=json.loads(request.body)
        u=User.objects.get(id=request.user.id)
        f=folders.objects.create(user=u, name=body['name'])
        msg={'msg':'Success'}
        return JsonResponse(msg, status=200, safe=False)
    else:
        msg={'msg':'Unauthorized'}
        return JsonResponse(msg, safe=False, status=401)


def files(request):
    if(request.user.is_authenticated and request.method=="POST"):
        body=json.loads(request.body)
        u=User.objects.get(id=request.user.id)
        f=folders.objects.get(id=body['id'])
        l=list(document.objects.filter(folder=f, user=u, delete=0).values())
        return JsonResponse(l, safe=False, status=200)
    else:
        msg={'msg':'Unauthorized'}
        return JsonResponse(msg, safe=False, status=401)


def setsize(request):
    if(request.user.is_authenticated and request.user.is_superuser and request.method=="POST"):
        body=json.loads(request.body)
        if(body['type']=="" or body['size']==None):
            msg={'msg':'invalid'}
            return JsonResponse(msg, status=400, safe=False)
        s=size.objects.filter(type=body['type'])
        if(s.exists()):
            s.size=body['size']
            s.save()
            msg={'msg':'Success'}
            return JsonResponse(msg, safe=False, status=200)
        size.objects.create(type=body['type'], size=body['size'])
        msg={'msg':'Success'}
        return JsonResponse(msg, safe=False, status=200)


def recent_file(request):
    if(request.user.is_authenticated):
        u=User.objects.get(id=request.user.id)
        doc=list(document.objects.filter(user=u, delete=0).order_by('recent').values())
        return JsonResponse(doc, status=200, safe=False)


def log_admin(request):
    if(request.method=="POST"):
        if(request.user.is_authenticated and request.user.i_superuser):
            body=json.loads(request.body)
            user=authenticate(username=body['user'],password=body['pass1'])
            if(user is not None):
                login(request, user)
                msg={'msg':'Success'}
                return JsonResponse(msg, status=200, safe=False)
            else:
                msg={'msg':'Wrong credentials'}
                return JsonResponse(msg, status=401, safe=False)
                
                
def out(request):
    logout(request)
    msg={'msg':'Logout successfull'}
    return JsonResponse(msg, status=200, safe=False)


def download_file(request):
    if(request.user.is_authenticated and request.method=="POST"):
        body=json.loads(request.body)
        i=body['id']
        path=document.objects.get(id=i)
        path=path.file
        path=str(path)
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        mime_type, _ = mimetypes.guess_type(file_path)
        print(mime_type)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type=mime_type)
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        return HttpResponse('lol')  
    else:
        return HttpResponse('lol')


def trash(request):
    if(request.method=="POST"):
        if(request.user.is_authenticated):
            body=json.loads(request.body)
            doc=document.objects.get(id=body['id'])
            doc.delete=1
            doc.save()
            msg={'msg':'Success'}
            return JsonResponse(msg, status=200, safe=False)


def trash_files(request):
    if(request.user.is_authenticated):
        u=User.objects.get(id=request.user.id)
        doc=list(document.objects.filter(user=u, delete=1).values())
        return JsonResponse(doc, status=200, safe=False)


def path_file():
    def wrapper(user, filename):
        file_upload_dir = os.path.join(settings.MEDIA_ROOT, 'file_upload')
        if os.path.exists(file_upload_dir):
            import shutil
            shutil.rmtree(file_upload_dir)
        return os.path.join(file_upload_dir, filename)
    return wrapper


def profile(request):
    if(request.method=="POST"):
        if(request.user.is_authenticated):
            body=request.FILES
            u=User.objects.get(id=request.user.id)
            x=ProfilePic.objects.filter(user=u)
            if(x.exists()):
                x.pic=body['file']
                x.save()
            else:
                ProfilePic.objects.create(user=u, pic=body['file'])
            msg={'msg':'Success'}
            return JsonResponse(msg, status=200, safe=False)


def all_file(request):
    if(request.user.is_authenticated and request.user.is_superuser):
        doc=list(document.objects.filter(delete=0).order_by('recent').values())
        return JsonResponse(doc, status=200, safe=False)



