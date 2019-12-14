import csv
from blog.serializers import BlogSerializer
from django.shortcuts import render,redirect
from blog.models import Blog,Entry,Author,Images
from blog.forms import BlogForm,SignupForm,LoginForm,UploadFileForm
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  

#REST API

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
'''
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))

def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])

def sample_api(request):
    data = {"message":"Hello World"}
    return Response(data, status=HTTP_200_OK)   

'''
'''
@csrf_exempt
@api_view(["GET"])

def sample_data(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs,many=True)
    return Response(serializer.data)    

'''
@csrf_exempt
@api_view(["PUT"])
def sample_put(request,blog_id):

    blog = Blog.objects.get(id=blog_id)
    serializer = BlogSerializer(blog,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)    
    
'''
#PDF FILES

def link_callback(uri, rel):

    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path 
'''
'''
def html_to_pdf_view(request):

    blog_objects = Blog.objects.all()

    template_path = 'blog/pdf_template.html'
    context = {"blogs":blog_objects}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback="")
    # if error then show some funy view
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

'''
'''
#CSV FILES

def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response
'''
'''
def sample_ajax_view(request):  
    blog = Blog.objects.all().values()
    data = list(blog)
    return JsonResponse(data,safe=False)

def sample_ajax_view(request):  
    
    data = {"name":"parvathy"}
    return JsonResponse(data)

def sample_view(request):
    return render(request,"blog/ajax_template.html")
'''
'''
def sendMailToUser(request):
    subject = "Subject:Hello"            
    message = "Good day!!"
    sender = "sender@example.com"
    recievers = ["receiver@example.com"]
    msg = EmailMessage(subject,message,sender,recievers)
    msg.content_subtype = "html"
    msg.send()  
    return HttpResponse("Mail send")

'''
'''
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Images(image=request.FILES['image'])
            instance.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully added')
            return HttpResponseRedirect('/blog/upload-file/')
    else:
        form = UploadFileForm()
    return render(request, 'blog/upload.html', {'form': form})

def showImage(request):
    img = Images.objects.get(id=1)
    return render(request, 'blog/image_preview.html', {"file":img})
 '''   
'''
def message_Add(request):
    count = 10
    messages.debug(request, ' statements were executed.' )
    messages.info(request, 'Three credits remain in your account.')
    messages.success(request, 'Profile details updated.')
    messages.warning(request, 'Your account expires in three days.')
    messages.error(request, 'Document deleted.')    
#add_message method    
    messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request,'blog/message-display.html')

'''

'''
def logout_view(request):
    logout(request)
    return HttpResponse("logout successfully")
    #Redirect to a success page.ss 
    '''
'''
def authen_web_request(request):
    if request.user.is_authenticated:
        return redirect('/blog/login_user/')  
    else:
        return redirect('/blog/signup/')  

def signup(request):
    if request.method == 'POST':
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                username = signup_form.cleaned_data['username'] 
                email = signup_form.cleaned_data['email']   
                password = signup_form.cleaned_data['password'] 
                if  User.objects.filter(username=username).exists():
                    return HttpResponse("Username or Email Already Exists")
                else:   
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    messages.info(request, 'Profile details updated.')
                    return render(request,'blog/signup.html')
                    
    else:
        signup_form = SignupForm(request.POST)
        messages.info(request, 'Please fill the form to sign-up')
    return render(request,'blog/signup.html',{"form":signup_form})                 
    
                  
    
def login_user(request):
    if request.user.is_authenticated:
        return HttpResponse('You Are already logged in')
    else:   
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():

                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                user = authenticate(username=username, password=password)
                                
                if user is not None:
                    if user.is_active:
                        login_user(request, user)    
                        return HttpResponse('Login Successful')
                    else:
                        return HttpResponse('Your account is not active')
                else:
                    return HttpResponse('The Account does not exists')
            else:
                login_form = LoginForm()
                return render(request, "blog/login.html",{"form":login_form})
        else:
            login_form = LoginForm()
        return render(request, "blog/login.html",{"form":login_form})

'''
'''
def authen_users(request):
    user = authenticate(username='john', password='new password')
    if user is not None:
        # A backend authenticated the credentials
        return HttpResponse("Authorised user...")
    else:
        # No backend authenticated the credentials  
        return HttpResponse("Non authorised user..")
'''
'''
def create_user(request):   
    user = User.objects.create_user('parvathy', 'parvathygs@gmail.com', '123456')
    user.save()
    return HttpResponse("user created")
'''
'''
def change_password(request):
    u = User.objects.get(username='parvathy')
    u.set_password('hellopassword')
    u.save()
    return HttpResponse("password created")
'''

'''
#Pagination

def listBlogs(request):

    blogs_list = Blog.objects.all()
    paginator = Paginator(blogs_list,2)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)

    return render(request,"blog/list-blogs.html",{"blogs":blogs})

# Create your views here.

#MySQL SELECT


def showBlog(request,requested_blog_id):
    blog_details = Blog.objects.get(id=requested_blog_id)
    context = {"blog":blog_details}
    return render(request,"blog/show-blog.html",context)        
    # return render(request,'blog/view-blog.html', {'blog':blog_details,'blog_id':requested_blog_id,}) 

def showAll(request):
    #blog_details = Blog.objects.filter(name="Blog").first()
    #blog_details = Blog.objects.filter(name="blog").first()
    blog_details = Blog.objects.all()
    context = {"blog":blog_details}
    return render(request,'blog/show-blog.html',context) 

def showBlogDetails(request,requested_blog_id):
    blog_details = Entry.objects.prefetch_related("blog").get(id=requested_blog_id)
    context = {"blog_details":blog_details}
    return render(request,"blog/view-blog-details.html",context)

def showFilter(request): 
    blog_details = Blog.objects.filter(name="Blog")
    context = {"blog":blog_details}
    return render(request,'blog/show-filter.html',context) 
'''

'''

#MySQLUpdate

def sqlUpdate(request):
    blog_details = Blog.objects.get(id=1)  
    blog_details.name = "Updated Blog Name "
    blog_details.tagline = "Updated blog tagline"
    blog_details.save() 
    context = {"blog_details" : blog_details}
    return render(request,'blog/blog-update.html',context)

'''
#MYSQL EDIT

'''
def edit_blog(request,requested_blog_id):
    if request.method == 'POST':

        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            blog_details = Blog.objects.get(id=requested_blog_id) # this will select datafrom database 
            blog_details.name = blog_form.cleaned_data['blog_name']
            blog_details.tagline = blog_form.cleaned_data['blog_tag_line']
            blog_details.save()                
            return HttpResponse('Data Edited successfully')
    else:
        blog_details = Blog.objects.get(id=requested_blog_id) # this will select datafrom database 
        blog_form = BlogForm(initial={"blog_name":blog_details.name,"blog_tag_line":blog_details.tagline}) # this will set initial values in the form from selected data

    return render(request,'blog/edit-blog.html', {'form': blog_form,'blog_id':requested_blog_id,})  
'''

#MYSQL DELETE

'''
def delete_blog(request,requested_blog_id):
    blog_details = Blog.objects.get(id=requested_blog_id)
    blog_details.delete()

#MYSQL Delete with link/button

def showAll(request):
    blog_details = Blog.objects.all()
    context = {"blog":blog_details}
    return render(request,'blog/view-blog.html',context) 


def delete_entry(request,requested_blog_id):
    blog_details = Blog.objects.get(id=requested_blog_id)  
    blog_details.delete()
    return HttpResponse('blog deleted')
    #return render(request,'view-blog.html')
    '''
'''

#MySQL INSERT

def insert_blog(request):
    if request.method == 'POST':

        blog_form = BlogForm()
        if blog_form.is_valid():
            
            blog_name_from_user = blog_form.cleaned_data['blog_name'] 
            blog_tagline_from_user = blog_form.cleaned_data['blog_tag_line'] 

            blog_object = Blog(name=blog_name_from_user, tagline=blog_tagline_from_user)
            blog_object.save() # will save the data from the form to database
           
            # blog_object = Blog()
            # blog_object.name = blog_name_from_user
            # blog_object.tagline =  blog_tagline_from_user
            # blog_object.save()

                            
            return HttpResponse('Data Inserted successfully')

    else:
        
        entry_object = Entry()
        blog_object = Blog()


        blog_object.name = "Blog"
        blog_object.tagline =  "Lorem ipsum dolor sit amet"
        blog_object.save() # will save the data from the form to database table blog

        entry_object.headline = "Lorum Ipsum"
        entry_object.body_text = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
        entry_object.pub_date = "2018-07-04"
        entry_object.mod_date = "2018-07-04"
        entry_object.n_comments = 0
        entry_object.n_pingbacks = 0
        entry_object.rating = 5
        entry_object.blog = blog_object # will insert the blog id into blog_entry
        entry_object.save()

        return HttpResponse('Data Inserted successfully')

        john = Author.objects.create(name="John") # will create new author in blog_authers table
        paul = Author.objects.create(name="Paul") # will create new author in blog_authers table
        george = Author.objects.create(name="George") # will create new author in blog_authers table

        entry_object.authors.add(john, paul, george) # will add data to blog_entry_authors

        blog_form = BlogForm()
        return render(request, 'blog-insert-form.html', {'form': blog_form})  

         
        '''

#xml format
        # <person>
        #     <name>parvathy</name>
        #     <email>parvathy@gmail.com</email>
        # </person>

#json format
        # person={'name':"parvathy",'email':"parvathy@gmail.com"}