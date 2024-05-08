from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,request
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from serviceapp.models import *
from .forms import CompanyForm,ProductForm,CustomerForm
import razorpay
from django.conf import settings 

# Create your views here.
def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())

def about(request):
     return render(request,"about.html")

def homelog(request):
    template=loader.get_template('homelog.html')
    return HttpResponse(template.render())

def aboutlog(request):
     return render(request,"aboutlog.html")

def register(request):
    if request.method == "POST": 
        form=CompanyForm(data=request.POST,files=request.FILES) 
        if form.is_valid(): 
            form.save() 
            obj=form.instance
            return render(request,"addsuccess.html",{"obj":obj}) 
    else: 
        form=CompanyForm() 
    return render(request,"register.html",{"form":form})


def company(request):
    template=loader.get_template('company.html')
    company=Company.objects.filter(status=0)
    context={
        'company':company
        }
    return HttpResponse(template.render(context,request))

def companyview(request,name):
  if(Company.objects.filter(company_name=name,status=0)):
      products=Product.objects.filter(company__company_name=name)
      return render(request,"product.html",{"products":products,"company_name":name})
  else:
    return redirect('company')

def oneproduct(request,cname,pname):
    if(Company.objects.filter(company_name=cname,status=0)):
      if(Product.objects.filter(product_name=pname,status=0)):
        products=Product.objects.filter(product_name=pname,status=0).first()
        return render(request,"oneproduct.html",{"products":products})
      else:
        return redirect('company')
    else:
      return redirect('company')

def centernewlog(request):
    template=loader.get_template('centernewlog.html')
    return HttpResponse(template.render())

@csrf_exempt
def centerprofile(request):
    if request.method=='POST':
        company_username=request.POST['company_username']
        company_create_password=request.POST['company_create_password']
        try:
            pro=Company.objects.get(company_username=company_username,company_create_password=company_create_password)
            context={
                'pro':pro
                }
            template=loader.get_template('centerprofile.html')
            return HttpResponse(template.render(context,request))
        except Company.DoesNotExist:
            template=loader.get_template('centerloginerror.html')
            return HttpResponse(template.render())
    
    
    
def centerpaycheck(request,obj):
    template=loader.get_template('centerpaycheck.html')
    pro=Company.objects.get(company_name=obj)
    context={
        'pro':pro
        }
    return HttpResponse(template.render(context,request))

client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY,settings.RAZORPAY_API_SECRET_KEY))
def centerpay(request):
    data = { "amount": 150000, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    razorpay_payment_id=payment['id']
    context={'amount':100,
    'api_key':settings.RAZORPAY_API_KEY,
    'order_id':razorpay_payment_id
    }
    return render(request,"centerpay.html",context)

def addproduct(request):
    if request.method == "POST": 
        form=ProductForm(data=request.POST,files=request.FILES) 
        if form.is_valid(): 
            form.save() 
            obj=form.instance
            return render(request,"productsuccess.html",{"obj":obj}) 
    else: 
        form=ProductForm() 
    return render(request,"addproduct.html",{"form":form})

def centerupdate(request,id):
    template=loader.get_template('centerupdate.html')
    person = Company.objects.get(id=id)
    context={
        'person':person
    }
    return HttpResponse(template.render(context,request))

@csrf_exempt
def centerupdateperson(request,id):
    if request.method=='POST':
        company_name=request.POST['company_name']
        company_username=request.POST['company_username']
        company_create_password=request.POST['company_create_password']
        company_email=request.POST['company_email']
        company_description=request.POST['company_description']
        company_contact=request.POST['company_contact']
        company_address=request.POST['company_address']

    person = Company.objects.get(id=id)
    person.company_name=company_name
    person.company_username=company_username
    person.company_create_password=company_create_password
    person.company_email=company_email
    person.company_description=company_description
    person.company_contact=company_contact
    person.company_address=company_address
    person.save()
    context={
        'person':person
    }
    template=loader.get_template('cenupdatesuccess.html')
    
    return HttpResponse(template.render())

def centerdelete(request, id):
    per = Company.objects.get(id=id)
    per.delete()
    template=loader.get_template('centerdelete.html')
    return HttpResponse(template.render())

def signup(request):
    if request.method == "POST": 
        form=CustomerForm(data=request.POST,files=request.FILES) 
        if form.is_valid(): 
            form.save() 
            obj=form.instance
            return render(request,"userlogin.html",{"obj":obj}) 
    else: 
        form=CustomerForm() 
    return render(request,"signup.html",{"form":form})

def userlogin(request):
    template=loader.get_template('userlogin.html')
    return HttpResponse(template.render())

@csrf_exempt
def userprofile(request):
    
    if request.method=='POST':
        user_fname=request.POST['user_fname']
        user_create_password=request.POST['user_create_password']
        try:
            pro=Customer.objects.get(user_fname=user_fname,user_create_password=user_create_password)
            context={
                'pro':pro
                }
            template=loader.get_template('userprofile.html')
            return HttpResponse(template.render(context,request))
        except Customer.DoesNotExist:
            template=loader.get_template('userloginerror.html')
            return HttpResponse(template.render())

def userupdate(request,id):
    template=loader.get_template('userupdate.html')
    person = Customer.objects.get(id=id)
    context={
        'person':person
    }
    return HttpResponse(template.render(context,request))

@csrf_exempt
def userupdateperson(request,id):
    if request.method=='POST':
        user_fname=request.POST['user_fname']
        user_lname=request.POST['user_lname']
        user_create_password=request.POST['user_create_password']
        user_email=request.POST['user_email']
        user_dob=request.POST['user_dob']
        user_contact=request.POST['user_contact']
        user_city=request.POST['user_city']
        user_state=request.POST['user_state']
        user_pincode=request.POST['user_pincode']

    person = Customer.objects.get(id=id)
    person.user_fname=user_fname
    person.user_lname=user_lname
    person.user_email=user_email
    person.user_create_password=user_create_password
    person.user_dob=user_dob
    person.user_contact=user_contact
    person.user_city=user_city
    person.user_state=user_state
    person.user_pincode=user_pincode
    person.save()
    context={
        'person':person
    }
    template=loader.get_template('userupdatesuccess.html')
    return HttpResponse(template.render())

def userdelete(request,id):
    per = Customer.objects.get(id=id)
    per.delete()
    template=loader.get_template('userdelete.html')
    return HttpResponse(template.render())

def userpaycheck(request,name):
    template=loader.get_template('userpaycheck.html')
    pro=Product.objects.get(product_name=name)
    context={
        'pro':pro
        }
    return HttpResponse(template.render(context,request))

def userpay(request,price,id):
    data = { "amount":price*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    razorpay_payment_id=payment['id']
    pro=Product.objects.get(id=id)
    context={'amounts':100,
    'api_key':settings.RAZORPAY_API_KEY,
    'order_id':razorpay_payment_id,
    'pro':pro
    }
    return render(request,"userpay.html",context)

def orders(request,id):
    template=loader.get_template('orders.html')
    pro=Product.objects.get(id=id)
    context={
        'pro':pro
        }
    return HttpResponse(template.render(context,request))

@csrf_exempt
def ordered(request):

    if request.method=='POST':
        oduserfname=request.POST['oduserfname']
        odcomname=request.POST['odcomname']
        odproname=request.POST['odproname']
        odprocolor=request.POST['odprocolor']
        odprostorage=request.POST['odprostorage']
        odproprice=request.POST['odproprice']
        odprobattery=request.POST['odprobattery']
        odproscreen=request.POST['odproscreen']
        odpronetwork=request.POST['odpronetwork']
    person=Order(oduserfname=oduserfname,odcomname=odcomname,odproname=odproname,odprocolor=odprocolor,odprostorage=odprostorage,odproprice=odproprice,odprobattery=odprobattery,odproscreen=odproscreen,odpronetwork=odpronetwork)
    person.save()
    template=loader.get_template('companyorder.html')
    return HttpResponse(template.render())
    

def myorders(request,userfname):
    template=loader.get_template('myorders.html')
    orders=Order.objects.filter(oduserfname=userfname)
    context={
        'orders':orders
        }
    return HttpResponse(template.render(context,request))

def centerorder(request,comname):
    template=loader.get_template('centerorder.html')
    orders=Order.objects.filter(odcomname=comname)
    context={
        'orders':orders
        }
    return HttpResponse(template.render(context,request))