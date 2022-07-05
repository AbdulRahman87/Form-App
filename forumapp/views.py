from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Categories, user_details, Question, question_reply, ContactUs
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.
def index(request):
    categories = Categories.objects.all()[:5]
    users = User.objects.all()
    return render(request, 'index.html', {'categories': categories, 'users': users})


def categories(request):
    categories = Categories.objects.all()
    return render(request, 'categories.html', {'categories': categories})


class startDiscussion(View):
    def get(self, request, name):
        category = Categories.objects.filter(cat_name=name)
        questions = Question.objects.filter(ques_parent=category[0])
        context = {'category': category, 'name': name, 'questions': questions}
        return render(request, 'startDiscussion.html',context)

    def post(self, request, name):
        category = Categories.objects.get(cat_name = name)
        title = request.POST['title']
        if title.__contains__('?') or title.__contains__('/') or title.__contains__('.') or title.__contains__('#'):
            messages.warning(request, 'Title should not contain any special characters')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
        desc = request.POST['desc']
        user = request.user
        question = Question(ques_parent=category, ques_title=title, ques_desc=desc, ques_user=user)
        question.save()
        messages.success(request, 'Your question is uploaded Successfully!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class questionReply(View):
    def get(self,request, name, slug):
        question = Question.objects.filter(ques_title=slug)
        replies = question_reply.objects.filter(reply_parent=question[0])
        context = {'question': question, 'replies': replies, 'name': name, 'slug': slug}
        return render(request, 'replies.html', context)

    def post(self, request, name, slug):
        user = request.user
        parent_reply = Question.objects.filter(ques_title=slug)
        desc = request.POST['desc']
        reply = question_reply(reply_parent=parent_reply[0], reply_desc=desc, reply_user=user, reply_category=name)
        reply.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def handleSignUp(request):
    if request.method == 'POST':
        u_name = request.POST['u_name']
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        email = request.POST['email']

        check_user = User.objects.filter(username=u_name)
        check_email = User.objects.filter(email=email)
        if len(check_user) > 0:
            messages.error(request, 'Username already exist')
            return redirect('Home')
        if len(check_email) > 0:
            messages.error(request, 'Email Already Exist')
            return redirect('Home')

        password = request.POST['pass']
        user_img = request.FILES.get('user_img')

        newUser = User.objects.create_user(u_name, email, password)
        newUser.first_name = f_name
        newUser.last_name = l_name
        newUser.save()

        if user_img == None:
            _user = user_details(_user=newUser)
            _user.save()
        else:
            _user = user_details(_user = newUser, user_img=user_img)
            _user.save()
        messages.success(request, 'Your Account is created Successfully! Now you can login!')
        return redirect('Home')


def handleLogIn(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(username=user_name, password=password)

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Invalid username and password!')
            return redirect('Home')


def handleLogOut(request):
    logout(request)
    messages.success(request, 'You have been logged out.')  
    return redirect('Home')


def userProfile(request, user):
    if request.method == 'POST':
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        user_email = request.POST['email']
        try:
            user_object = User.objects.get(username=user)
            if f_name.isalpha() and l_name.isalpha():
                user_object.first_name = f_name
                user_object.last_name = l_name
                user_object.email = user_email
                user_object.save()
                messages.success(request, 'Details updated Successfully!')
                return HttpResponseRedirect(request.path_info)
            else:
                messages.warning(request, 'First Name and Last Name should not contain any digits.')
                return HttpResponseRedirect(request.path_info)
        except Exception as e:
            return redirect('Home')

    user__ = User.objects.filter(username=user)
    if (len(user__) == 0):
        return redirect('Home')
    isTrue = False
    if user__[0] == request.user:
       isTrue = True
    details = user_details.objects.filter(_user=user__[0])
    for i in details:
        isPrivate = i.private_profile
    questions = Question.objects.filter(ques_user=user__[0])
    replies = question_reply.objects.filter(reply_user=user__[0])
    context = {'user__': user__, 'details': details, 'questions':questions, 'replies': replies, 'isTrue': isTrue, 'user': user, 'isPrivate': isPrivate}
    return render(request, 'user_profile.html', context)


class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')
    def post(self, request):
        if request.user.is_authenticated:
            user = request.user
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            query = request.POST['query']
            query__ = ContactUs(user=user, name=name, email=email, phone=phone, query=query)
            query__.save()
            messages.success(request, 'Your Feedback is successfully submitted!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponse("<h1 style='text-align: center;'>Please Login to Feedback...</h1><h3 style='text-align: center; color:red;'>You are redirecting to the Home page.</h3> <p id='number' style='text-align: center; font-size: 8em;'></p> <script> setTimeout(() => {window.location.href='/';}, 5000);  let a = 4; function countdown(){ document.getElementById('number').innerHTML = a; a-- } setInterval(() => { countdown();}, 1000); </script>")

def About(request):
    return render(request, 'about.html')

def set_default_pic(request, user):
    try:
        user_object = User.objects.get(username=user)
        logged_in_user = request.user
        if user_object == logged_in_user:
            user_image = user_details.objects.get(_user=request.user)
            user_image.user_img = 'IMG/user.png'
            user_image.save()
        else: 
            return redirect('Home')
    except Exception as e:
        print(e)
        return redirect('Home')
    return redirect(f'/user_profile/{user}/')

def update_pic(request):
    if request.method == 'POST':
        user_image = user_details.objects.get(_user=request.user)
        image = request.FILES.get('image')
        user_image.user_img = image
        user_image.save()
        messages.success(request, 'Your profile pic updated Successfully!')
        return redirect(f'/user_profile/{request.user}/')
    else:
        return redirect('Home')

def update_question(request, name, slug):
    if request.method == 'POST':
        upd_title = request.POST['upd_ques_title']
        upd_desc = request.POST['upd_ques_desc']
        if upd_title.__contains__('?') or upd_title.__contains__('/') or upd_title.__contains__('#') or upd_title.__contains__('.'):
            messages.warning(request, 'Title should not contain any special characters')
            return redirect(f'/startDiscussion/{name}/{slug}')
        question = Question.objects.get(ques_title=slug)
        question.ques_title = upd_title
        question.ques_desc = upd_desc
        question.save()
        messages.success(request, 'Your Question is Successfully updated')
        return redirect(f'/startDiscussion/{name}/{slug}')
    else:
        return redirect('Home')

def update_reply(request, r_id, name, slug):
    if request.method == 'POST':
        upd_reply_desc = request.POST['upd_reply_desc']
        reply = question_reply.objects.get(reply_id=r_id)
        reply.reply_desc = upd_reply_desc
        reply.save()
        messages.success(request, 'Reply was updated Successfully')
        return redirect(f'/startDiscussion/{name}/{slug}')
    else:
        return redirect('Home')
    
def search(request):
    query = request.GET['query']
    categories = Categories.objects.filter(cat_name__icontains=query)
    questions = Question.objects.filter(ques_title__icontains=query)
    context = {'query': query, 'categories': categories, 'questions': questions}
    return render(request, 'search.html', context)


def privateProfile(request, user):
    if request.method == 'POST':
        try:
            user__ = User.objects.filter(username=user)
            try:
                details = user_details.objects.get(_user=user__[0])
            except Exception as e:
                return redirect('Home')
        except Exception as e:
            return redirect('Home')
        if details.private_profile == 'off':
            details.private_profile = 'on'
            details.save()
        else:
            details.private_profile = 'off'
            details.save()
        return redirect(f'/user_profile/{user}')