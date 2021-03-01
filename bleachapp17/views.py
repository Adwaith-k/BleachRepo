
from django.shortcuts import render, redirect
from bleachapp17.models import db_add_product,db_coslogin,ProductImages,db_create_account,db_category,db_service_form,db_coursemodules,db_servicevideo,db_admin_service_form,db_admin_service_form2,db_careers,db_careers_job,db_customer,db_custsignup,db_addcourse_table, db_addcoursevideo_table, db_addservice_table,db_coursecategory_table, db_offlinetraining_table,db_Governerate_table,db_Area_table,db_blog_table,db_blogfile_table,db_wishlist,db_wishlistproduct,db_cart,db_cartproduct,db_addjob,db_courseorder,db_productorder,db_orderr,db_orderritem,db_addaddresstable,db_orderstatus
from django.http import HttpResponse
from django.contrib.sessions.models import Session                             #session
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa
from django.views import View
from django.db import connection
from datetime import datetime
from django.views.decorators.cache import cache_control
from googletrans import Translator


# Create your views here.

def ADMININDEX(request):
    return render(request, "index.html")

#admin  #admin  #admin #admin #admin  #admin   #admin    #admin    #admin   #admin   #admin   #admin   #admin    #admin   #admin   #admin   #admin   #admin   #admin

def SIDEMENU(request):
    print("side menu executed.")
    return render(request, "sidebar.html")

def sidebar(request):
    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "sidebar.html",{'coslogin':tb})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "sidebar.html",{'admin':tbb})
    else:
        return redirect("else")



        
def search(request):
    ii=request.session['id']
    if request.method=='POST':
        name=request.POST['search']
        # cattt=request.POST['catt']
        # offer=request.POST['offer']

        a=db_add_product.objects.all().filter(product_name=name)
        
        # b=db_add_product.objects.all().filter(product_category=cattt,product_name=name)

        
        if a:
            return render(request,'newproduct.html',{'aa':a,'ob':a})
        else:
            obj = db_add_product.objects.filter(is_delete=0,status=1).exclude(quantity=0)
            
            return render(request,'newproduct.html',{'ob':obj,'msg':'Oooopz!! Incorrectt Search'})
       

    else:
        obj = db_add_product.objects.filter(is_delete=0,status=1).exclude(quantity=0)
            
        return render(request,'newproduct.html',{'ob':obj,'msg':'Oooopz!! Incorrectt Search'})


       
def searchcourse(request):
    ii=request.session['id']
    if request.method=='POST':
        name=request.POST['search']
        # cattt=request.POST['catt']
        # offer=request.POST['offer']

        a=db_addcourse_table.objects.all().filter(course_name=name)
        
        # b=db_add_product.objects.all().filter(product_category=cattt,product_name=name)

        
        if a:
            return render(request,'courselist.html',{'aa':a,'ob':a})
        else:
            obj = db_addcourse_table.objects.filter(is_delete=0,status=1).exclude(quantity=0)
            
            return render(request,'courselist.html',{'ob':obj,'msg':'Oooopz!! Incorrectt Search'})
       

    else:
        obj = db_addcourse_table.objects.filter(is_delete=0,status=1).exclude(quantity=0)
            
        return render(request,'courselist.html',{'ob':obj,'msg':'Oooopz!! Incorrectt Search'})





def sample(request, id):
    obj = db_addcourse_table.objects.get(id=id)
    print(obj,"obj")
    # obj1=db_coursemodules.objects.order_by('module').filter(course_id=id).distinct('module')
    obj1=db_coursemodules.objects.filter(course_id=id).values_list('module', flat=True).distinct()
    print(obj1,"obj1")
    obj2=db_coursemodules.objects.filter(course_id=id).values_list('chapter', flat=True).distinct()
    print(obj2,"obj2")
    obj3=db_coursemodules.objects.filter(course_id=id).values_list('level', flat=True).distinct()
    print(obj3,"obj3")

    return render(request,"sample.html",{'ob':obj,'ob1':obj1,'ob2':obj2,'ob3':obj3})
       



        





def NAVBAR(request):
    return render(request, "navbar.html")









def LOGIN(request):
    return render(request, "login.html")

# @cache_control(no_cache=True,must_revalidate=True,no_store=True)
def home(request):
    if request.session.has_key('id'):
        return render(request,'home.html')

    return render(request,'custlogin.html')





def fourhome(request):
    obj = db_add_product.objects.filter(is_delete=0,status=1).exclude(quantity=0)
    print(obj,"_______________________________________________________________________")
    obj1= db_category.objects.all()
    print(obj1,"+++++++++++++++++++++++++++++++++product categorieesss++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return render(request, "vvvv.html",{'ob':obj,'ob1':obj1})

def aboutus(request):
    return render(request, "aboutus.html")





# def BLOG(request):
#     obj = db_blog_table.objects.filter(is_delete=0)
#     return render(request, "blog.html", {'ob': obj})


# def CUSTBLOGVIDEOS(request,id):
#     obj1 = db_blog_table.objects.filter(is_delete=0,id=id)

#     obj = db_blogfile_table.objects.filter(video_id=id, is_delete=0)
#     return render(request, "custblogvideos.html", {'ob': obj,'obb':obj1})



def headerfooter(request):
    obj=db_add_product.objects.all().filter(is_delete=0,status=1).exclude(quantity=0)[0:3]
    return render(request, "headerfooter.html", {'ob': obj,'kk':"hgjhgj"})


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def blognew(request):
    if request.session.has_key('id'):

        obj = db_blog_table.objects.filter(is_delete=0)[0:3]
        
        return render(request, "blognew.html", {'ob': obj})
    else:
        return render(request, "custlogin.html")



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def blogsingle(request, id):
    if request.session.has_key('id'):
        obj = db_blog_table.objects.get(id=id)
        print(obj)
        obj1 = db_blogfile_table.objects.filter(video_id=id, is_delete=0)
        return render(request, "blogsingle.html", {'ob': obj,'ob1':obj1})
    else:
        return render(request, "custlogin.html")






def servicesnew(request):
    obj=db_addservice_table.objects.all()
    return render(request, "servicesnew.html",{'ob':obj})

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def servicesinglenew(request):
    if request.session.has_key('id'):

        gId = request.GET.get('gId')
        obj = db_Governerate_table.objects.filter(is_delete=0)
        obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)
        obj2 = db_addservice_table.objects.all().filter(id=1)
        obj3 = db_servicevideo.objects.all().filter(video_id=1)
        print(obj3,"hhhhhhhhh")

        print(obj2)
        return render(request, "servicesingle.html", {'ob': obj,'ob1':obj1,'ob2':obj2,'ob3':obj3})
    else:
        return render(request, "custlogin.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def servicesinglenew1(request):
    if request.session.has_key('id'):

        gId = request.GET.get('gId')
        obj = db_Governerate_table.objects.filter(is_delete=0)
        obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)
        obj2 = db_addservice_table.objects.all().filter(id=2)
        obj3 = db_servicevideo.objects.all().filter(video_id=2)
        print(obj2)
        return render(request, "servicesingle1.html", {'ob': obj,'ob1':obj1,'ob2':obj2,'ob3':obj3})
    else:
        return render(request, "custlogin.html")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def servicesinglenew2(request):
    if request.session.has_key('id'):

        gId = request.GET.get('gId')
        obj = db_Governerate_table.objects.filter(is_delete=0)
        obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)
        obj2 = db_addservice_table.objects.all().filter(id=3)
        obj3 = db_servicevideo.objects.all().filter(video_id=3)

        print(obj2)
        return render(request, "servicesingle2.html", {'ob': obj,'ob1':obj1,'ob2':obj2,'ob3':obj3})
    else:
        return render(request, "custlogin.html")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def servicesinglenew3(request):
    if request.session.has_key('id'):

        gId = request.GET.get('gId')
        obj = db_Governerate_table.objects.filter(is_delete=0)
        obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)
        obj2 = db_addservice_table.objects.all().filter(id=4)
        obj3 = db_servicevideo.objects.all().filter(video_id=4)

        print(obj2)
        return render(request, "servicesingle3.html", {'ob': obj,'ob1':obj1,'ob2':obj2,'ob3':obj3})
    else:
        return render(request, "custlogin.html")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def servicesinglenew4(request):
    if request.session.has_key('id'):

        gId = request.GET.get('gId')
        obj = db_Governerate_table.objects.filter(is_delete=0)
        obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)
        obj2 = db_addservice_table.objects.all().filter(id=5)
        obj3 = db_servicevideo.objects.all().filter(video_id=5)

        print(obj2)
        return render(request, "servicesingle4.html", {'ob': obj,'ob1':obj1,'ob2':obj2,'ob3':obj3})
    else:
        return render(request, "custlogin.html")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def servicesinglenew5(request):
    if request.session.has_key('id'):

        gId = request.GET.get('gId')
        obj = db_Governerate_table.objects.filter(is_delete=0)
        obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)
        obj2 = db_addservice_table.objects.all().filter(id=6)
        obj3 = db_servicevideo.objects.all().filter(video_id=6)

        print(obj2)
        return render(request, "servicesingle5.html", {'ob': obj,'ob1':obj1,'ob2':obj2,'ob3':obj3})
    else:
        return render(request, "custlogin.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def servicesinglenew6(request):
    if request.session.has_key('id'):

        gId = request.GET.get('gId')
        obj = db_Governerate_table.objects.filter(is_delete=0)
        obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)
        obj2 = db_addservice_table.objects.all().filter(id=7)
        obj3 = db_servicevideo.objects.all().filter(video_id=7)

        print(obj2)
        return render(request, "servicesingle5.html", {'ob': obj,'ob1':obj1,'ob2':obj2,'ob3':obj3})
    else:
        return render(request, "custlogin.html")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)    
def newproduct(request, id):
    if request.session.has_key('id'):
        obj4=db_category.objects.all()
        obj2= db_category.objects.get(id=id)
        obj3 = db_add_product.objects.filter(is_delete=0,status=1).exclude(quantity__lte=0)
        print(obj3,"obj3333333333333")

        if id==4:
            obj = db_add_product.objects.filter(is_delete=0,status=1).exclude(quantity__lte=0)
            return render(request, "newproduct.html", {'ob': obj,'ob2':obj2,'ob4':obj4})
        elif id==1:
            obj = db_addcourse_table.objects.filter(is_delete=0,status=1)
            return render(request, "courselist.html", {'ob': obj,'ob2':obj2,'ob4':obj4})




            
        else:
            obj = db_add_product.objects.filter(is_delete=0,status=1,category_id=id).exclude(quantity=0)
            return render(request, "newproduct.html", {'ob': obj,'ob2':obj2,'ob4':obj4})

          
        array=[]
        for i in obj3:
            print(i,"++++++++add_product objects++++++++++")
            var2=i.id
            array.append(var2)
            print(array,"+++++++++++++add_product id array++++++++")
        print(var2,"++++++++++add_product id+++++++++++")

        # obj1=ProductImages.objects.all().filter(product_id=var2)
        # print(obj1,"++++++++++++product images objects++++++++++++")
        # image=[]
        # for i in obj1:
        #     var1=i.images
        #     print(var1,"++++++++++++++images+++++++++++++++++")
        #     image.append(var1)
        #     print(image,"++++++++image++++++++++")
        #     cursor  = connection.cursor()
        #     obj8=cursor.execute('select a.id,b.id,b.images,b.product_id_id from db_add_product a,ProductImages b WHERE a.id=b.product_id_id and a.is_delete=0 and a.status=1 and a.quantity>0')
        #     print('select a.id,b.id,b.images,b.product_id_id from db_add_product a,ProductImages b WHERE a.id=b.product_id_id  and a.is_delete=0 and a.status=1  and a.quantity>0')
        #     print(obj8,"objjjjjjjjjj8")
        #     row = cursor.fetchall()
        #     print(row,"rowwwwwww")



            # return render(request, "newproduct.html", {'ob': obj,'ob1':row,'ob2':obj2})
    else:
        return render(request, "custlogin.html")



def megaproduct(request):
    if request.session.has_key('id'):
        obj = db_add_product.objects.filter(is_delete=0,status=1).exclude(quantity=0)
        
        return render(request, "newproduct.html", {'ob': obj})
    else:
        return render(request, "custlogin.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def courselist(request, id):
    if request.session.has_key('id'):

        obj = db_addcourse_table.objects.filter(is_delete=0,status=1)
        obj2= db_category.objects.get(id=id)
        print(obj,"obj3333333333333")
        
        return render(request, "courselist.html", {'ob': obj,'ob2':obj2})
    else:
        return render(request, "custlogin.html")




        
    






@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def productsingle(request, id):
    if request.session.has_key('id'):
        obj = db_add_product.objects.get(id=id)
        print(obj,"obj")
        obj1=ProductImages.objects.all().filter(product_id=id)
        print(obj1,"obj1")
        return render(request, "productsingle.html", {'ob': obj,'ob1':obj1})
    else:
        return render(request, "custlogin.html")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def cartnew(request):
    if request.session.has_key('id'):
        ii=request.session['id']
        gId = request.GET.get('gId')
        print(gId,"gid")


        obj2 = db_Governerate_table.objects.filter(is_delete=0)
        obj3 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)

        print(ii)
        obj1=db_custsignup.objects.all().filter(id=ii)  

        uid=db_custsignup.objects.get(id=ii)
        print(uid)
        jaid=request.GET['faid']
        print(jaid)
        var1=db_add_product.objects.get(id=jaid)
        print(var1)
        quantityy=request.GET["num"]
        print(quantityy)
        print("((((((((((((((((((((((((((((((((((((")
        if db_cart.objects.all().filter(user_id=uid,item_id=jaid,is_delete=0,status=0):
            ii=request.session['id']
            print(ii,"print ii")
            uid=db_custsignup.objects.get(id=ii)
            print(uid,"userid")
            jaid=request.GET['faid']
            var1=db_add_product.objects.get(id=jaid)
            obj = db_cart.objects.all().filter(user_id=ii,is_delete=0)
            sum1=0
            for i in obj:
                a=i.total
                sum1=sum1+a
            objj=db_cart.objects.all().filter(user_id=ii,is_delete=0).count()
            

            print("welcome============================")
            row=db_add_product.objects.all()

            return render(request,'cartneww.html',{'ob':obj,'ob1':obj1,'sum1':sum1,'count':objj,'ob2':obj2,'ob3':obj3})#,'ob1':obj2
            print("++++++++++++++++++++++++++++++++++++")
            # return redirect("/newproduct")


        else:
            ii=request.session['id']
            print(ii)
            uid=db_custsignup.objects.get(id=ii)
            print(uid)
            jaid=request.GET['faid']
            var1=db_add_product.objects.all().get(id=jaid)
            quantityy=request.GET["num"]
            print(quantityy,"product quantity")
            price=(var1.product_price)
            print(price,"product price")
            totall=float(price)*int(quantityy)
            print(totall,"product total")

            a=db_cart(user_id=uid,item_id=jaid,quantity=quantityy,total=totall,stage=0,status=0,product_id=var1)
            a.save()
            row=db_add_product.objects.all()
            obj=db_cart.objects.all().filter(user_id=ii,is_delete=0,stage=0)
            sum1=0
            for i in obj:
                a=i.total
                sum1=sum1+a
            objj=db_cart.objects.all().filter(user_id=ii,is_delete=0,stage=0).count()

           
            return render(request,'cartneww.html',{'ob':obj,'ob1':obj1,'sum1':sum1,'count':objj})#,'ob1':obj2
            print("++++++++++++++++++++++++++++++++++++")
            # return redirect("/newproduct")
            
    else:
        return render(request,'custlogin.html')
    


def invoice(request):
    if request.method == "POST":
        received_data = dict(request.POST)
        paytm_params = {}
        return render(request,"invoice.html",{'id':paytm_params})


    if request.method == "GET":
        b=request.GET.get('paymentid', )
        return render(request,"invoice.html",{'id':b})



   



def deletecartnew(request, id):
    tb=db_cart.objects.get(id=id)
    tb.delete()
    return redirect("/cartlist")


def videopage(request, id):
    obj = db_addcoursevideo_table.objects.filter(video_id=id, is_delete=0)
    return render(request, "videopage.html", {'ob': obj})






def VIEWCOURSE(request):
    if request.session.has_key('id'):
        obj = db_addcourse_table.objects.filter(is_delete=0,status=1)
        print(obj)
        return render(request, "course.html", {'ob': obj})
    else:
        return render(request, "custlogin.html")






@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def newcourse(request):
    if request.session.has_key('id'):
        obj = db_addcourse_table.objects.filter(is_delete=0,status=1)
        print(obj)
        return render(request, "sample.html", {'ob': obj})
    else:
        return render(request, "custlogin.html")




# def CUSTCOURSEVIDEOS(request,id):
#     obj = db_addcoursevideo_table.objects.filter(video_id=id, is_delete=0)
#     return render(request, "custcoursevideos.html", {'ob': obj})




def paymentnew(request):
    return render(request, "paymentnew.html")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewjobsclt(request):
    if request.session.has_key('id'):

        obj1 = db_addjob.objects.filter(is_delete=0)
        return render(request, "career.html",{'ob':obj1})
    else:
        return render(request, "custlogin.html")










# def productsingle(request, id):
#     if request.session.has_key('id'):
#         obj = db_add_product.objects.get(id=id)
#         return render(request, "productsingle.html", {'ob': obj})
#     else:
#         return render(request, "custlogin.html")





@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def coursesingle(request, id):
    if request.session.has_key('id'):
        obj = db_addcourse_table.objects.get(id=id)
        print(obj,"obj")
        obj1= db_coursemodules.objects.filter(course_id_id=id)
        print(obj1,"obj1")
        obj2=db_addcoursevideo_table.objects.get(id=id)
        print(obj2,"obj2")
        return render(request, "coursesingle.html", {'ob': obj,'ob1':obj1,'ob2':obj2})
    else:
        return render(request, "custlogin.html")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def fav(request):
    if request.session.has_key('id'):

        return render(request,"fav.html")
    else:
        return render(request, "custlogin.html")

def viewjobnew(request):
    return render(request,"viewjobnew.html")





def CUSTOMERREGFORM(request):
    gId = request.GET.get('gId')
    obj = db_Governerate_table.objects.filter(is_delete=0)
    obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)

    return render(request, "customerregform.html", {'ob': obj,'ob1':obj1})











def CUSTERREGINSERT(request):
    if request.method=="POST":
        print("----------------inside post--------------")
        FirstName = request.POST["FirstName"]
        LastName = request.POST["LastName"]
        Gender = request.POST["Gender"]
        Zipcode = request.POST["zipcode"]


        username = request.POST["username"]
        password = request.POST["password"]

        Phone_number = request.POST["Phone_number"]
        Nationality = request.POST["Nationality"]
        Apartment = request.POST["Apartment"]
        Floor = request.POST["Floor"]
        Building = request.POST["Building"]
        Block = request.POST["Block"]
        Street = request.POST["Street"]
        Avenue = request.POST["Avenue"]
        Governerate = request.POST.get("governarateid")
        Area = request.POST.get("Area")
        # Governerate = request.POST["Governerate"]
        # Area = request.POST["Area"]
        if db_custsignup.objects.filter(username=username):
            print("email is already exist")
            return render(request,'customerregform.html',{'msg':"email is already exist"})#message pass
        else:
            a=db_custsignup(FirstName=FirstName,LastName=LastName,Gender=Gender,username=username,password=password,Phone_number=Phone_number,Nationality=Nationality,Apartment=Apartment,Floor=Floor,Building=Building,Block=Block,Street=Street,Avenue=Avenue,Governerate=Governerate,zipcode=Zipcode,Area=Area)#,status='pending'
            a.save()
            return redirect("/custlogin")
        
    else:
        print("----------------inside else--------------")

        return render(request,'customerregform.html')




def admininsertacnt(request):
    tbb=db_coslogin.objects.all().filter(status=1)
    
    if request.method == "POST":
        ecom = 0
        servive = 0
        career = 0
        course = 0
        offline = 0
        blog = 0
        var2 = request.POST["name"]
        var4 = request.POST["email"]
        var5 = request.POST["password"]
        # var1 = request.POST["role"]
        var3 = request.POST.get("check[1]")
        if var3:
            var3=1
            print(var3,"service")
        else:
            var3=0
            print(var3,"service")
        var6 = request.POST.get("check[2]")
        if var6:
            var6=1
            print(var6,"career")
        else:
            var6=0
            print(var6,"career")

        var7 = request.POST.get("check[3]")
        if var7:
            var7=1
            print(var7,"course")
        else:
            var7=0
            print(var7,"course")

        var8 = request.POST.get("check[4]")
        if var8:
            var8=1
            print(var8,"offline")
        else:
            var8=0
            print(var8,"offline")

        var9 = request.POST.get("check[5]")
        if var9:
            var9=1
            print(var9,"blog")
            
        else:
            var9=0
            print(var9,"blog")
            

        var10 = request.POST.get("check[0]")
        if var10:
            var10=1
            print(var10,"ecom")
        else:
            var10=0
            print(var10,"ecom")
        if db_coslogin.objects.filter(username=var4):
            print("email is already exist")
            return render(request,'addaccount.html',{'admin':tbb,'msg':"email is already exist"})
        else:
            a=db_coslogin(password=var5,name=var2,username=var4,service=var3,career=var6,cource=var7,
            offline=var8,blog=var9,ecom=var10,status=2)#,type1=var1
            a.save()
            return render(request,'addaccount.html',{'admin':tbb})
            print("------------------------------")

        
    else:
        print("----------------without post--------------")

        return render(request,'addaccount.html',{'admin':tbb})







# def LOGIN1(request):
#     if request.method=="POST":
#         uname = request.POST.get("username")
#         passwrd = request.POST.get("password")
#         a = db_coslogin.objects.filter(username=uname,password=passwrd,status=1,type1="admin")
#         b = db_coslogin.objects.filter(username=uname,password=passwrd,status=2)
#         c = db_coslogin.objects.all().filter(status=2)
#         for opp in c:
#             id=opp.id
#             print(id,"id")

#         print("++++++++++++")
#         if a:
#             print("-----------")

#             return redirect("/adminindex")

#         elif b:
#             for i in b:
#                 request.session['sid']=i.id
#                 varr=i.id
#                 print(varr,"session id of subadmin")
#                 print("==============")

#             return redirect("/adminindex")
#         else:
#             return redirect("/login")


#     else:
#         return HttpResponse("noooooooooooo post")
#         print("###########")










def LOGIN1(request):
    if request.method == "POST":
        data = db_coslogin.objects.all()
        # data1 = db_custsignup.objects.all()

        username = request.POST.get("username")
        password = request.POST.get("password")
        flag = 0

        for i in data:
            if username == i.username and password == i.password:
                type = i.type1
                flag = 1
                if type == "admin":
                    request.session['aid'] = i.id                            #session
                    # request.session['type'] = "admin"
                    print(i.id,"session of admin")
                    print("========admin========")
                    return redirect("/adminindex")
                else:
                    # request.session['is_logged'] = True
                    request.session['sid']=i.id
                    varr=i.id
                    print(varr,"session id of subadmin")
                    print("========sub admin=========")

                    return redirect("/adminindex")
 

        if flag == 0:
            return HttpResponse("user not exist")

        # for i in b:
        #     request.session['sid']=i.id
        #     varr=i.id
        #     print(varr,"session id of subadmin")
        #     print("==============")
        #     return redirect("/adminindex")
        # return HttpResponse("aaaaaaaaaaaaaaaaa")
        





                

                
        




def CUSTLOGIN(request):
    
    if request.method=="POST":
        uname=request.POST["username"]
        psw=request.POST["password"]
        obj1= db_category.objects.all()
        b=db_custsignup.objects.all().filter(username=uname,password=psw,is_delete=0)
        obj = db_add_product.objects.filter(is_delete=0,status=1).exclude(quantity=0)

        if b:
            for i in b:
                request.session['id']=i.id
                print(i.id,"session of customer")
           
            return render(request,'vvvv.html',{'ob':obj,'ob1':obj1})
        else:
            return render(request,'custlogin.html')
        print("===========================================+")

        
    else:
        return render(request,'custlogin.html')
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
    # return render(request, "custlogin.html")


# def LOGIN1(request):
#     if request.method=="POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         b=db_coslogin.objects.all().filter(username=username,password=password,status=1)
#         if b:
#             for i in b:
#                 request.session['aid']=i.id
#                 print(i.id,"admin session")

           
#             return redirect("/adminindex")
#         else:
#             return redirect("/login")
            

        
#     else:
#         return redirect("/login")


# def LOGIN11(request):
#     if request.method=="POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         b=db_coslogin.objects.all().filter(username=username,password=password,status=2)
#         if b:
#             for i in b:
#                 request.session['sid']=i.id
#                 print(i.id,"subadmin session")
           
#             return redirect("/subadminindex")
#         else:
#             return redirect("/loginsub")
            

        
#     else:
#         return redirect("/loginsub")



def loginsub(request):
    return render(request, "loginsub.html")
        
def ADDCOURSE(request):
    obj = db_coursecategory_table.objects.filter(is_delete=0)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "add_course.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "add_course.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")

    
    



def ADMIN_INDEX(request):
    count= db_custsignup.objects.all().count()
    countp= db_cart.objects.all().filter(stage=1,status=0).count()
    countc= db_cart.objects.all().filter(stage=1,status=1).count()
    counts= db_service_form.objects.all().count()
    countj= db_addjob.objects.all().count()
    countcareer= db_addjob.objects.all().count()
    countorder= db_orderr.objects.all().count()
    countbuyer= db_orderr.objects.all().filter(stage=1).count()
    countcancel= db_orderr.objects.all().filter(stage=2).count()
    countasimah= db_custsignup.objects.all().filter(Governerate=4).count()
    countjahra= db_custsignup.objects.all().filter(Governerate=5).count()
    counthawali= db_custsignup.objects.all().filter(Governerate=6).count()
    countfarwaniya= db_custsignup.objects.all().filter(Governerate=7).count()
    countmubarak= db_custsignup.objects.all().filter(Governerate=8).count()
    countahmadi= db_custsignup.objects.all().filter(Governerate=9).count()

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")
        context= {'coslogin':tb,'countasimah':countasimah,'countjahra':countjahra,'counthawali':counthawali,'countfarwaniya':countfarwaniya,'countmubarak':countmubarak,'countahmadi':countahmadi,'countj':countj,'countcareer':countcareer,'count': count,'countp':countp,'countc':countc,'counts':counts,'counto':countorder,'countb':countbuyer,'countcancel':countcancel}#
        print(count,"++++++count++++++")     

        return render(request, "index.html", context)
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        context= {'admin':tbb,'countasimah':countasimah,'countjahra':countjahra,'counthawali':counthawali,'countfarwaniya':countfarwaniya,'countmubarak':countmubarak,'countahmadi':countahmadi,'countj':countj,'countcareer':countcareer,'count': count,'countp':countp,'countc':countc,'counts':counts,'counto':countorder,'countb':countbuyer,'countcancel':countcancel}#
        print(count,"++++++count++++++")     
        return render(request, "index.html", context)
    else:
        return redirect("else")



# def SUBADMIN_INDEX(request):
#     if request.session.has_key('sid'):
         
#         count= db_custsignup.objects.all().count()
#         countp= db_cart.objects.all().filter(stage=1,status=0).count()
#         countc= db_cart.objects.all().filter(stage=1,status=1).count()
#         counts= db_service_form.objects.all().count()
#         countj= db_addjob.objects.all().count()
#         countcareer= db_addjob.objects.all().count()
#         countorder= db_orderr.objects.all().count()
#         countbuyer= db_orderr.objects.all().filter(stage=1).count()
#         countcancel= db_orderr.objects.all().filter(stage=2).count()
#         countasimah= db_custsignup.objects.all().filter(Governerate=4).count()
#         countjahra= db_custsignup.objects.all().filter(Governerate=5).count()
#         counthawali= db_custsignup.objects.all().filter(Governerate=6).count()
#         countfarwaniya= db_custsignup.objects.all().filter(Governerate=7).count()
#         countmubarak= db_custsignup.objects.all().filter(Governerate=8).count()
#         countahmadi= db_custsignup.objects.all().filter(Governerate=9).count()

      
#         sid=request.session['sid']
#         tb = db_coslogin.objects.get(id=sid)
#         # th=db_coslogin.objects.all().filter(status=1)
#         item=sidebar(request)
        

#         context= {'coslogin':tb,'item':item,'countasimah':countasimah,'countjahra':countjahra,'counthawali':counthawali,'countfarwaniya':countfarwaniya,'countmubarak':countmubarak,'countahmadi':countahmadi,'count': count,'countp':countp,'countc':countc,'counts':counts,'countj':countj,'countcareer':countcareer,'counto':countorder,'countb':countbuyer,'countcancel':countcancel}#'ecom':a,'blog':b,'service':c,'offline':d,'career':e,'course':f
#         print(count,"++++++count++++++")                                  
#         return render(request, "index.html", context)
#     return redirect("/login")







                                                                                #session
def ADMIN_LOGOUT(request):
    request.session['aid']                                               #session
    request.session.flush();                                                   #session
    return redirect("/login")

def SUBADMIN_LOGOUT(request):
    request.session['sid']                                               #session
    request.session.flush();                                                   #session
    return redirect("/login")



def userlogout(request):
    if request.session.has_key('id'):
        del request.session['id']
        return redirect("/custlogin")


    

    


def ECOMMERCE(request):
    if request.session.has_key('is_logged'):                                   # session
        if request.session['type'] == "ecommerce":
            return render(request, "Ecommerce.html")
    return redirect("/login")

  


def CUSTOMMER(request):
    # if request.session.has_key('is_logged'):                                   #session                  #session
            return render(request, "CUSTOMMER.html")
            return redirect("/login")




@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def VIEWCUSTOMER(request):
    if request.session.has_key('aid'):
        tbb=db_coslogin.objects.all().filter(status=1)
        obj1 = db_custsignup.objects.filter(is_delete=0)
        return render(request, "viewcustomer.html", {'ob': obj1,'admin':tbb})
    else:
        return render(request,'login.html')



def CUSTOMERFORMDELETE(request, id):
    tb = db_custsignup.objects.get(id=id)
    tb.is_delete = True
    tb.save()
    return redirect("/viewcustomer")


def ADD_PRODECT(request):
    obj = db_category.objects.all()
    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "Addprodect.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "Addprodect.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")
    
    

def VIEW_PRODECT(request):
    obj1 = db_add_product.objects.filter(is_delete=0)
    obj2 = ProductImages.objects.all()
    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "Viewprodect.html",{'coslogin':tb,'ob': obj1, 'ob1' : obj2})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "Viewprodect.html",{'admin':tbb,'ob': obj1, 'ob1' : obj2})
    else:
        return redirect("else")
    
    

def INSER_PRODECT(request):
    
    if request.method == "POST":
        # tb = db_add_product()

        product_name = request.POST.get("product_name")

        # photo = request.FILES['image']
        # img = FileSystemStorage()
        # filename = img.save(photo.name, photo)
        # uploaded_file_url = img.url(filename)
        # tb.image = uploaded_file_url

        product_category = request.POST.get("product_category")
        print(product_category,"vvvvvvvvv")
        category_id = request.POST.get("product_category")
        print(category_id,"bbbbbbbbbb")


        product_price = request.POST.get("product_price")
        status = request.POST.get("status")
        offer = request.POST.get("offer")
        discription = request.POST.get("discription")
        original = request.POST.get("org_price")
        is_delete = False
        newname=request.POST.get("file[]")
        print(newname,"newnameeeeeeeeeeeee")
        # tb.status = True

        status=request.POST.get("check[0]")
        
        var3 = request.POST.get("check[0]")
        if var3:
            var3=1
            print(var3,"check[0] if")
        else:
            var3=0
            print(var3,"check[0] else")
        images = request.FILES.getlist("file[]")
        print(images,"immmmm")

        for img in images:
            fs = FileSystemStorage()
            filename = fs.save(img.name, img)

            uploaded_file_url = fs.url(filename)
            images = uploaded_file_url
        quantityy=request.POST.get("num")
        print(quantityy,"qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")

        cursor  = connection.cursor()
        obj4=cursor.execute('select a.product_name,b.* from db_add_product a,db_category b WHERE a.category_id=b.id ')
        print('select a.product_name,b.* from db_add_product a,db_category b WHERE a.category_id=b.id ')
        print(obj4,"objjjjjjjjjj")
        row = cursor.fetchall()

        for x in row:
            print(x,"prooooooooooooo")

        a=db_add_product(status=var3,product_price=product_price,quantity=quantityy,product_name=product_name,offer=offer,discription=discription,image=images,org_price=original,category_id=category_id)
        a.save()
        




        images = request.FILES.getlist("file[]")
        print(images)

        for img in images:
            fs = FileSystemStorage()
            filename = fs.save(img.name, img)

            uploaded_file_url = fs.url(filename)
            images = uploaded_file_url

            pimage = ProductImages(product_id=a, images=images)
            pimage.save()
        return redirect("/addprodect")










def UPDATEDATA(request,id):
    obj=db_add_product.objects.get(id=id)
    obj2 = ProductImages.objects.filter(product_id=id,is_delete=0)
    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "Addproductupdate.html",{'coslogin':tb,'ob': obj,'img1': obj2})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "Addproductupdate.html",{'admin':tbb,'ob': obj,'img1': obj2})
    else:
        return redirect("else")
    
    
    






def PRODUCTUPDATEINSERT(request,id):
    
    if request.method == "POST":
        tb = db_add_product.objects.get(id=id)
        tb.product_name = request.POST.get("product_name")

        # photo = request.FILES['image']
        # img = FileSystemStorage()
        # filename = img.save(photo.name, photo)
        # uploaded_file_url = img.url(filename)
        # tb.image = uploaded_file_url

        # tb.product_category = request.POST.get("product_category")
        tb.product_price = request.POST.get("product_price")
        tb.offer = request.POST.get("offer")
        tb.status=request.POST.get("status")
        tb.quantity=request.POST.get("num")
        tb.discription=request.POST.get("discription")


        tb.save()

        images = request.FILES.getlist("file[]")
        print(images)
        for img in images:
            fs = FileSystemStorage()
            filename = fs.save(img.name, img)

            uploaded_file_url = fs.url(filename)
            images = uploaded_file_url

            pimage = ProductImages(product_id=tb, images=images)
            pimage.save()

        return redirect("/viewprodect")



def PRODUCTTABLEDELETE(request, id):
    
    tb = db_add_product.objects.get(id=id)
    tb.is_delete = True
    tb.save()
    return redirect("/viewprodect")






def VIEW_IMAGES(request,id):
    obj=ProductImages.objects.filter(product_id=id,is_delete=0)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewimagesB.html",{'coslogin':tb,'ob': obj, 'pageId':id})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewimagesB.html",{'admin':tbb,'ob': obj, 'pageId':id})
    else:
        return redirect("else")
    
    
def IMAGEDELETE(request,pageId,id):
    tb = ProductImages.objects.get(id=id)
    tb.is_delete = True
    tb.save()
    return redirect("/viewimages/"+pageId)

def IMAGEUPDATEDATA(request,pageId,id):
    obj=ProductImages.objects.get(id=id)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "Addimageupdate.html",{'coslogin':tb,'ob': obj,'pageId':pageId})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "Addimageupdate.html",{'admin':tbb,'ob': obj,'pageId':pageId})
    else:
        return redirect("else")
    

def IMAGEUPDATEINSERT(request,pageId,id):
    
    if request.method == "POST":
        tb = ProductImages.objects.get(id=id)

    photo = request.FILES['image']
    print (photo)
    img = FileSystemStorage()
    filename = img.save(photo.name, photo)
    uploaded_file_url = img.url(filename)
    print (uploaded_file_url)
    tb.images = uploaded_file_url
    tb.save()

    return redirect("/viewimages/"+pageId)


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def ADD_ACCOUNT(request):
    if request.session.has_key('aid'):
        # return render(request, "addaccount.html")
        tbb=db_coslogin.objects.all().filter(status=1)
        return render(request,'addaccount.html',{'admin':tbb})
    else:
        return render(request,'login.html')


# def UPDATECATEGORY(request,id):
#     obj=db_category.objects.get(id=id)
#     return render(request, "categoryupdate.html", {'ob': obj})

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def view_ACCOUNT(request):
    if request.session.has_key('aid'):

        tbb=db_coslogin.objects.all().filter(status=1)
        obj1 = db_coslogin.objects.all()
        return render(request, "viewaccount.html", {'ob': obj1,'admin':tbb})
    else:
        return render(request,'login.html')





def checkboxsub(request):

    if request.method == "POST":
        tb=db_coslogin()
        ecom=0
        career=0
        course=0
        offline=0
        blog=0
        tb.ecom = request.POST.get("checkbox[]")
        tb.service = request.POST.get("checkbox[]")
        tb.career = request.POST.get("checkbox[]")
        tb.course = request.POST.get("checkbox[]")
        tb.offline = request.POST.get("checkbox[]")
        tb.blog = request.POST.get("checkbox[]")
        tb.save()
        return redirect("/addaccount/")







@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def UPDATEACCOUNT(request,id):
    if request.session.has_key('aid'):

        tbb=db_coslogin.objects.all().filter(status=1)
        obj=db_coslogin.objects.get(id=id)
        return render(request, "accountupdate.html", {'ob': obj,'admin':tbb})
    else:
        return render(request,'login.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def ACCOUNTUPDATEINSERT(request,id):
    if request.session.has_key('aid'):

        if request.method == "POST":
            tb = db_coslogin.objects.get(id=id)
            tb.password = request.POST.get("name")
            # tb.type1 = request.POST.get("role")
            tb.username = request.POST.get("email")
            tb.ecom =request.POST.get("check[0]")
            tb.service =request.POST.get("check[1]")
            tb.career =request.POST.get("check[2]")
            tb.cource =request.POST.get("check[3]")
            tb.offline =request.POST.get("check[4]")
            tb.blog =request.POST.get("check[5]")

            tb.save()
            return redirect("/viewaccount")
        else:
            return render(request,'login.html')



def ACCOUNTDELETE(request, id):
    tbb=db_coslogin.objects.all().filter(status=1)
    tb = db_coslogin.objects.get(id=id)
    tb.delete()
    return redirect("/viewaccount")

    



def ADD_CATEGORY(request):
    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")
        return render(request, "addcategory.html",{'coslogin':tb})
        
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "addcategory.html",{'admin':tbb})
        
    else:
        return redirect("else")

def orderstatus(request,id):
     return render(request, "updateorderstatus.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def orderupdateinsert(request):
    if request.session.has_key('aid'):
        oid=request.GET.get('cid')
        var1=db_orderr.objects.get(id=oid)
        print(var1,"var1")
        print(oid,"oid")
        status=request.POST.get("statuss")

        if db_orderstatus.objects.all().filter(order_id=var1):
            return redirect("/vieworder")

            
        else:
            oid=request.GET.get('cid')
            var1=db_orderr.objects.get(id=oid)
            print(var1,"var1")
            print(oid,"oid")
            if request.method == "POST":

                status=request.POST.get("statuss")
                print(status,"statusssssssssssssssssssssssssssss")
                a=db_orderstatus(order_id=var1,status=status)#
                a.save()
                return redirect("/vieworder")
            return HttpResponse("not saved")
    else:
        return render(request,'login.html')




    # oid=request.GET.get('cid')
    # print(oid,"oid")
    # obj = db_orderr.objects.all()
    # for i in obj:
    #     id = i.id
    #     print(id,"id")
    # return render(request, "vieworder.html")

    



def ADD_CATEGORY_in_DATABASE(request):
    if request.method == "POST":
        product_category = request.POST.get("product_category")
        print(product_category,"product_category")
        images = request.FILES.getlist("file[]")
        print(images,"images")

        for img in images:
            fs = FileSystemStorage()
            filename = fs.save(img.name, img)

            uploaded_file_url = fs.url(filename)
            images = uploaded_file_url
            print(images,"imagess")

            a=db_category(product_category=product_category,image=images)
            a.save()
        return redirect("/addcategory")




def VIEW_CATEGORY(request):
    obj1 = db_category.objects.filter(is_delete=0)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewcategory.html",{'coslogin':tb,'ob': obj1})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewcategory.html",{'admin':tbb,'ob': obj1})
    else:
        return redirect("else")
    
def UPDATECATEGORY(request,id):
    obj=db_category.objects.get(id=id)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "categoryupdate.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "categoryupdate.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")
    



def CATEGORYUPDATEINSERT(request,id):
    if request.method == "POST":
        tb = db_category.objects.get(id=id)
        tb.product_category = request.POST.get("product_category")
        tb.save()
        return redirect("/viewcategory")

def addaddress(request):
    ii=request.session['id']

    gId = request.GET.get('gId')
    print(gId,"gid")


    obj = db_Governerate_table.objects.filter(is_delete=0)
    obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)
    obj2= db_addaddresstable.objects.filter(id=ii)
    print(obj2,"obj2")

    return render(request,'addaddress.html',{'ob':obj,'ob1':obj1,'ob2':obj2})



def editaddaddress(request):
    ii=request.session['id']

    gId = request.GET.get('gId')
    print(gId,"gid")


    obj = db_Governerate_table.objects.filter(is_delete=0)
    obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)
    obj2= db_addaddresstable.objects.filter(id=ii)
    print(obj2,"obj2")

    return render(request,'updateaddaddress.html',{'ob':obj,'ob1':obj1,'ob2':obj2})



def inserteditaddaddress(request):
    ii=request.session['id']
    uid=db_custsignup.objects.get(id=ii)
    if request.method == "POST":

        FirstName = request.POST["FirstName"]
        LastName = request.POST["LastName"]
        Email = request.POST["username"]
        phone = request.POST["Phone_number"]
        Nationality = request.POST["Nationality"]
        Address = request.POST["address"]
        Governerate = request.POST.get("governarateid")
        Area = request.POST.get("Area")
        Zipcode = request.POST["zipcode"]
        b=db_addaddresstable.objects.filter(user_id=uid).update(FirstName=FirstName,LastName=LastName,Area=Area,Email=Email,phone=phone,Governerate=Governerate,Zipcode=Zipcode)

   
    return render(request,"successnew.html") 








def insertaddaddress(request):
    ii=request.session['id']
    uid=db_custsignup.objects.get(id=ii)
    if request.method == "POST":

        FirstName = request.POST["firstname"]
        LastName = request.POST["lastname"]
        Email = request.POST["username"]
        phone = request.POST["Phone_number"]
        # Nationality = request.POST["Nationality"]
        Address = request.POST["address"]
        Governerate = request.POST.get("governarateid")
        Area = request.POST.get("Area")
        
        if db_addaddresstable.objects.filter(user_id=uid):
            return render(request,'submited.html')
        else:

            a=db_addaddresstable(user_id=uid,FirstName=FirstName,LastName=LastName,Email=Email,phone=phone,Address=Address,Governerate=Governerate,Area=Area)
            a.save()
            print("saveeeeeeeeeee address")

        
            obj=db_addaddresstable.objects.all().filter(user_id=ii)#.last()
            print(obj,"objjjj")
            obj1=db_cart.objects.all().filter(user_id=ii,is_delete=0,stage=0)
            sum1=0
            for i in obj1:
                a=i.total
                sum1=sum1+a
                print(sum1,"++++++++++++++")
            return render(request, "cartordernew.html",{'ob':obj,'bb':obj1,'sum1' : sum1})




def submitted(request):
    return render(request, "submited.html")


def viewcartorder(request,id):
    obj1 = db_custsignup.objects.filter(is_delete=0)
    return render(request, "cart.html", {'ob': obj1})

def deletecart(request, id):
    tb=db_cart.objects.get(id=id)
    tb.delete()
    return redirect("/cartorder")






def CATEGORYDELETE(request, id):
    tb = db_category.objects.get(id=id)
    tb.delete()
    return redirect("/viewcategory")






@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def orderreport(request):
    if request.session.has_key('aid'):
        tbb=db_coslogin.objects.all().filter(status=1)
        return render(request, "report.html",{'admin':tbb})
    else:
        return render(request,'login.html')



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def paymentreport(request):
    if request.session.has_key('aid'):
        tbb=db_coslogin.objects.all().filter(status=1)
        return render(request, "paymentreport.html",{'admin':tbb})
    else:
        return render(request,'login.html')





@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def cancelreport(request):
    if request.session.has_key('aid'):
        tbb=db_coslogin.objects.all().filter(status=1)
        return render(request, "cancelreport.html",{'admin':tbb})
    else:
        return render(request,'login.html')




@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def productreport(request):
    if request.session.has_key('aid'):

        tbb=db_coslogin.objects.all().filter(status=1)
        return render(request, "productreport.html",{'admin':tbb})
    else:
        return render(request,'login.html')




@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def coursereport(request):
    if request.session.has_key('aid'):

        tbb=db_coslogin.objects.all().filter(status=1)
        return render(request, "coursereport.html",{'admin':tbb})
    else:
        return render(request,'login.html')




def date(request):
    tbb=db_coslogin.objects.all().filter(status=1)
    if request.method=="POST":
        quantity=db_orderritem.objects.all().filter(stage=0)
        date_from=request.POST.get("date_from")
        print(date_from,"date frommmmmmmmmm==========")

        date_to=request.POST.get("date_to")
        print(date_to,"datetoooooooooooo=================")
        a=db_cart.objects.all().filter(updated_at__lte=date_to,updated_at__gte=date_from,stage=0)
        print(a,"aaaaaaaaaaaaaaaaa((((((((((((((((((((((((")
        b=db_orderr.objects.all().filter(timestamp__lte=date_to,timestamp__gte=date_from,stage=0)   
        cursor  = connection.cursor()
        obj=cursor.execute('select a.order_id_id, a.quantity, a.total, d.FirstName, b.product_name,c.course_name from db_orderritem a,db_add_product b,db_addcourse_table c, db_custsignup d WHERE a.user_id_id=d.id AND (a.item_order=b.id AND a.item_order=c.id) AND a.stage=0 AND a.timestamp<=\''+date_to+'\' AND a.timestamp>=\''+date_from+'\'')
        print('select a.item_order,b.product_name,c.course_name from db_orderritem a,db_add_product b,db_addcourse_table c WHERE (a.item_order=b.id OR a.item_order=c.id) AND a.stage=0 AND a.timestamp<='+date_to+' AND a.timestamp>='+date_from+'')
        print(obj,"objjjjjjjjjj")
        row = cursor.fetchall()

        for x in row:
            print(x,"prooooooooooooo")
    return render(request, "report.html",{'odl':a,'od':b,'join':a,'quantity':quantity,'admin':tbb})#,'vv':roww for x in roww: 



def paymentdate(request):
    tbb=db_coslogin.objects.all().filter(status=1)
    if request.method=="POST":
        date_from=request.POST.get("date_from")
        print(date_from,"date frommmmmmmmmm==========")

        date_to=request.POST.get("date_to")
        print(date_to,"datetoooooooooooo=================")
        a=db_orderritem.objects.all().filter(timestamp__lte=date_to,timestamp__gte=date_from,stage=1)
        print(a,"aaaaaaaaaaaaaaaaa((((((((((((((((((((((((")
        b=db_orderr.objects.all().filter(timestamp__lte=date_to,timestamp__gte=date_from,stage=1)
        cursor  = connection.cursor()
        obj=cursor.execute('select a.order_id_id, a.quantity, a.total, d.FirstName, b.product_name,c.course_name from db_orderritem a,db_add_product b,db_addcourse_table c, db_custsignup d WHERE a.user_id_id=d.id AND (a.item_order=b.id AND a.item_order=c.id) AND a.stage=1 AND a.timestamp<=\''+date_to+'\' AND a.timestamp>=\''+date_from+'\'')
        print(obj,"objjjjjjjjjj")
        row = cursor.fetchall()
        for x in row:
            print(x)
            print(row,"row========")
    return render(request, "paymentreport.html",{'odl':a,'od':b,'join':a,'admin':tbb})  #join:row for name  #'join':a for otems




def canceldate(request):
    tbb=db_coslogin.objects.all().filter(status=1)
    if request.method=="POST":
        date_from=request.POST.get("date_from")
        print(date_from,"date frommmmmmmmmm==========")

        date_to=request.POST.get("date_to")
        print(date_to,"datetoooooooooooo=================")
        a=db_orderritem.objects.all().filter(timestamp__lte=date_to,timestamp__gte=date_from,stage=2)
        print(a,"aaaaaaaaaaaaaaaaa((((((((((((((((((((((((")
        b=db_orderr.objects.all().filter(timestamp__lte=date_to,timestamp__gte=date_from,stage=2)
        

        return render(request, "cancelreport.html",{'odl':a,'od':b,'admin':tbb}) 




def productdate(request):
    tbb=db_coslogin.objects.all().filter(status=1)
    if request.method=="POST":
        date_from=request.POST.get("date_from")
        print(date_from,"date frommmmmmmmmm==========")

        date_to=request.POST.get("date_to")
        print(date_to,"datetoooooooooooo=================")
        select=request.POST.get("select")
        print(select,"selectttttt")
        # a=db_cart.objects.all().filter(timestamp__lte=date_to,timestamp__gte=date_from,stage=select,status=0)
        # print(a,"aaaaaaaaaaaaaaaaa((((((((((((((((((((((((")
        a=db_cart.objects.all().filter(updated_at__lte=date_to,updated_at__gte=date_from,stage=select,status=0)
        
        

        return render(request, "productreport.html",{'odl':a,'admin':tbb})




def coursedate(request):
    tbb=db_coslogin.objects.all().filter(status=1)
    if request.method=="POST":
        date_from=request.POST.get("date_from")
        print(date_from,"date frommmmmmmmmm==========")

        date_to=request.POST.get("date_to")
        print(date_to,"datetoooooooooooo=================")
        select=request.POST.get("select")
        print(select,"selectttttt")
        a=db_cart.objects.all().filter(updated_at__lte=date_to,updated_at__gte=date_from,stage=select,status=1)
        return render(request, "coursereport.html",{'odl':a,'admin':tbb})   




def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



class ViewiPDF(View):

    def get(self, request, *args, **kwargs):

            
            
        pdf = render_to_pdf('invoice.html')
        return HttpResponse(pdf, content_type='application/pdf')

class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        pdf=render_to_pdf('invoice.html')
        response=HttpResponse(pdf, content_type='application/pdf')
        filename="report%s.pdf"%("12341231")
        content="attachment; filename='%s'" %(filename)
        response['Content-Disposition']=content
        return response


##################################################################################






class ViewoPDF(View):

    def get(self, request, *args, **kwargs):
        obj1 = db_orderr.objects.all().filter(is_delete=0)

        
            
            
        pdf = render_to_pdf('vieworderpdf.html',{'ob1':obj1})
        return HttpResponse(pdf, content_type='application/pdf')


 ######################################################  order pdf     

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



class ViewPDF(View):

    def get(self, request, *args, **kwargs):

            
            
        pdf = render_to_pdf('reportpdf.html')
        return HttpResponse(pdf, content_type='application/pdf')

class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        pdf=render_to_pdf('reportpdf.html')
        response=HttpResponse(pdf, content_type='application/pdf')
        filename="report%s.pdf"%("12341231")
        content="attachment; filename='%s'" %(filename)
        response['Content-Disposition']=content
        return response


#########################################################payment pdf
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



class ViewpPDF(View):

    def get(self, request, *args, **kwargs):
        
        pdf = render_to_pdf('paymentreportpdf.html')
        return HttpResponse(pdf, content_type='application/pdf')

class DownloadpPDF(View):
    def get(self, request, *args, **kwargs):
        pdf=render_to_pdf('paymentreportpdf.html')
        response=HttpResponse(pdf, content_type='application/pdf')
        filename="report%s.pdf"%("12341231")
        content="attachment; filename='%s'" %(filename)
        response['Content-Disposition']=content
        return response

######################################################cancelpdf

def renderc_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



class ViewcPDF(View):

    def get(self, request, *args, **kwargs):
        
        pdf = render_to_pdf('cancelpdf.html')
        return HttpResponse(pdf, content_type='application/pdf')

class DownloadcPDF(View):
    def get(self, request, *args, **kwargs):
        pdf=render_to_pdf('cancelpdf.html')
        response=HttpResponse(pdf, content_type='application/pdf')
        filename="report%s.pdf"%("12341231")
        content="attachment; filename='%s'" %(filename)
        response['Content-Disposition']=content
        return response


###################################################################################


        














# def cartorder(request):
#     ii=request.session['id']
#     print(ii)
#     var1=db_carttt.objects.all()
#     obj=db_custsignup.objects.all().filter(id=ii)             #original
#     obj1=db_carttt.objects.all().filter(user_id=ii)

#     sum1=0
#     for i in obj1:
#         a=i.total
#         sum1=sum1+a
#         print(sum1,"++++++++++++++")
#     return render(request, "order.html",{'ob':obj,'bb':obj1,'jj':var1,'sum1' : sum1})

def ok(request):
    return render(request, "neworder.html")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def cartorder(request):
    if request.session.has_key('id'):
        ii=request.session['id']
        print(ii)
        uid=db_custsignup.objects.get(id=ii)

        var1=db_cart.objects.all()
        obj=db_custsignup.objects.all().filter(id=ii)            
        obj1=db_cart.objects.all().filter(user_id=ii,is_delete=0)

        sum1=0
        for i in obj1:
            a=i.total
            sum1=sum1+a
            print(sum1,"++++++++++++++")
            
        return render(request, "order.html",{'ob':obj,'bb':obj1,'sum1' : sum1})
    else:
        return render(request,'custlogin.html')





# def VIEW_CATEGORY(request):
#     obj1 = db_category.objects.filter(is_delete=0)
#     return render(request, "viewcategory.html", {'ob': obj1})



def save_model(self, request, obj, form, change):
        obj.cart.total += obj.quantity * obj.product.cost
        obj.cart.count += obj.quantity
        obj.cart.updated = datetime.now()
        obj.cart.save()
        super().save_model(request, obj, form, change)

def get_deal_total(self):
        price = self.product.deal_price
        quantity = self.quantity
        total = price*quantity
        print(total)

        return total

# def cartorder(request,self):
#     ii=request.session['id']

#     obj=db_custsignup.objects.all().filter(id=ii)
#     obj1=db_carttt.objects.all().filter(user_id=ii)
#     price = self.db_add_product.product_price
#     quantityy = self.quantity
#     total = price*quantityy
#     print(total)
#     return total
#     return render(request, "order.html",{'ob':obj,'bb':obj1})




# def total_price(self):
#         return self.quantity * self.unit_price
#     total_price = property(total_price)



    



def viewordercource(request):
    obj1 = db_order.objects.all()
    obj2 = db_customer.objects.all()
    obj3 = db_category.objects.all()
    obj4 = db_order_item.objects.filter(is_delete=0)


    return render(request, "viewordercource.html", {'ob1': obj1,'ob2': obj2, 'ob3': obj3, 'ob4': obj4,})

def ORDERITEMDELETE(request, id):
    tb = db_orderr.objects.get(id=id)
    tbb = db_orderritem.objects.all().filter(order_id=id).update(is_delete=1)
    tb.is_delete = True
    
    tb.save()
    
    
    return redirect("/vieworder")

# tbt=db_orderritem.objects.filter(order_id=id)
#     print(tbt,"tbtttt")
#     tbt.is_delete= True        
#     tbt.save()


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def VIEW_ORDER(request):
    if request.session.has_key('aid'):
        tbb=db_coslogin.objects.all().filter(status=1)
        
        
        obj1 = db_orderr.objects.all().filter(is_delete=0,stage=1)
        obj2 = db_orderstatus.objects.all()
       

        return render(request, "vieworder.html", {'ob1': obj1,'ob2':obj2,'admin':tbb})
    else:
        return render(request,'login.html')



def VIEW_ORDERC(request):
    tbb=db_coslogin.objects.all().filter(status=1)
    
    
    obj1 = db_orderr.objects.all()
    


    return render(request, "vieworderc.html", {'ob1': obj1,'admin':tbb})



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def VIEWALLORDER(request):
    if request.session.has_key('aid'):

        tbb=db_coslogin.objects.all().filter(status=1)
        

        obj1 = db_cart.objects.all().filter(status=0,stage=1)
        
        return render(request, "viewallbill.html", {'ob1': obj1,'admin':tbb})#, 'ob2': obj2
    else:
        return render(request,'login.html')





@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def VIEWALLORDERC(request):
    if request.session.has_key('aid'):

        tbb=db_coslogin.objects.all().filter(status=1)
        

        obj1 = db_cart.objects.all().filter(status=1,stage=1)
        
        return render(request, "viewallbillc.html", {'ob1': obj1,'admin':tbb})
    else:
        return render(request,'login.html')



def VIEW_BILL(request):
    tbb=db_coslogin.objects.all().filter(status=1)
    return render(request, "viewbill.html",{'admin':tbb})

def viewbillcource(request):
    return render(request, "viewbillcource.html",{'admin':tbb})





#admin
def ADDGOVERNERTE(request):
    return render(request, "addgovernerte.html")
def VIEWGOVERNERTE(request):
    obj1 = db_admin_service_form.objects.all()
    return render(request, "viewgovernerte.html", {'ob': obj1})
def DELETEGOVERNERTE(request, id):
    tb = db_admin_service_form.objects.get(id=id)
    tb.delete()
    return redirect("/viewgovernerte")
def UPDATEGOVERNERTE(request,id):
    obj=db_admin_service_form.objects.get(id=id)
    return render(request, "governorateupdate.html", {'ob': obj})
def GOVERNORATEUPDATINSERT(request,id):
    if request.method == "POST":
        tb = db_admin_service_form.objects.get(id=id)
        tb.governerate = request.POST.get("governerate")
        tb.save()
        return redirect("/viewgovernerte")


def GETAREABYiD(request):
    gId = request.GET.get('gId')
    obj2 = db_admin_service_form2.objects.filter(governerate_id=gId)
    print(obj2)
    return render(request, "areadropdown.html",{'ob':obj2})


def ADDAREA(request):
    obj1 = db_admin_service_form.objects.all()
    return render(request, "addarea.html", {'ob1': obj1})
def VIEWAREA(request):
    obj1 = db_admin_service_form2.objects.all()
    return render(request, "viewarea.html", {'ob': obj1})
def DELETEAREA(request, id):
    tb = db_admin_service_form2.objects.get(id=id)
    tb.delete()
    return redirect("/viewarea")
def UPDATEAREA(request,id):
    obj=db_admin_service_form2.objects.get(id=id)
    return render(request, "areaupdate.html", {'ob': obj})
def AREAUPDATINSERT(request,id):
    if request.method == "POST":
        tb = db_admin_service_form2.objects.get(id=id)
        tb.Area = request.POST.get("Area")
        tb.save()
        return redirect("/viewarea")










def INSERADMINPAGEFORM(request):
    if request.method == "POST":
        tbt = db_admin_service_form()
        tbt.governerate = request.POST.get("governerate")
        tbt.save()
        return redirect("/addgovernerte")

def INSERADMINPAGEFORM2(request):
    if request.method == "POST":

        governerate_id = request.POST.get("governerate")
        tb = db_admin_service_form.objects.get(id=governerate_id)

        area = request.POST.get("Area")
        tbt = db_admin_service_form2(Area=area, governerate_id=tb)
        tbt.save()
        return redirect("/addarea")






#clnt
def CLTSERVICEFORM(request):
    gId = request.GET.get('gId')
    obj = db_Governerate_table.objects.filter(is_delete=0)
    obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)


    return render(request, "cltserviceform.html", {'ob': obj,'ob1':obj1})
    




   

def INSERTSERVICEPAGE(request):
    ii=request.session['id']
    uid=db_custsignup.objects.all().filter(id=ii)
    if request.method == "POST":
        tbt = db_service_form()
        tbt.name = request.POST.get("name")
        tbt.gender = request.POST.get("gender")
        tbt.email = request.POST.get("email")
        tbt.phone_number = request.POST.get("phone_number")
        tbt.preferred_communication = request.POST.get("preferred_communication")
        tbt.evaluationtimeslot = request.POST.get("evaluationtimeslot")
        tbt.nationality = request.POST.get("nationality")


        tbt.customer_type = request.POST.get("customer_type")
        if tbt.customer_type == "Corporate":

            tbt.company = request.POST.get("company")
            tbt.job_title = request.POST.get("job_title")

        tbt.civil_id = request.POST.get("civil_id")
        tbt.other_mobile = request.POST.get("other_mobile")
        tbt.message_language = request.POST.get("message_language")
        tbt.apartment = request.POST.get("apartment")
        tbt.floor = request.POST.get("floor")
        tbt.building = request.POST.get("building")
        tbt.street = request.POST.get("street")
        tbt.avenue = request.POST.get("avenue")

        tbt.governerate = request.POST.get("governerate")
        tbt.Area = request.POST.get("Area")
        tbt.service_id_id = request.POST.get("hiddenid")

        


        
        tbt.date = request.POST.get("date")
        tbt.save()
        return redirect("/servicesinglenewurl")


        



def CLTCAREERS(request):
    obj1 = db_addjob.objects.all()
    return render(request, "cltcareers.html", {'ob': obj1})


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def custcltcareers(request):
    if request.session.has_key('id'):
        obj1 = db_addjob.objects.all()
        return render(request, "custcltcareer.html", {'ob': obj1})
    else:
        return render(request, "custlogin.html")



def appliedjob(request):
    ii=request.session['id']
    # var2=editprofiletable.objects.all().filter(userid=ii)
    var1=db_custsignup.objects.all().filter(id=ii)
    aview=db_careers.objects.all().filter(user_id=ii)
    return render(request,'appliedjob.html',{'av':aview,'aa':var1})



def VIEWCAREERS(request):
    obj1 = db_careers.objects.filter(is_delete=0)


    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewcareers.html",{'coslogin':tb,'ob': obj1})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewcareers.html",{'admin':tbb,'ob': obj1})
    else:
        return redirect("else")
    
def CAREERSFORMDELETE(request, id):
    tb = db_careers.objects.get(id=id)
    tb.is_delete = True
    tb.save()
    return redirect("/viewcareers")



def CAREERSFORMMM(request):
    if request.method == "POST":
        tbt = db_careers()
        tbt.name = request.POST.get("name")
        tbt.email = request.POST.get("email")
        tbt.phone_number = request.POST.get("phone_number")
        tbt.jobs = request.POST.get("jobs")
        tbt.about_your_self = request.POST.get("about_your_self")

        tbt.notesfile = request.FILES["notesfile"]

        tbt.save()
        return redirect("/cltcareers")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def custcareersform(request):
    if request.session.has_key('id'):

        if request.method == "POST":
            tbt = db_careers()
            tbt.name = request.POST.get("name")
            tbt.email = request.POST.get("email")
            tbt.phone_number = request.POST.get("phone_number")
            tbt.jobs = request.POST.get("jobs")
            tbt.about_your_self = request.POST.get("about_your_self")

            tbt.notesfile = request.FILES["notesfile"]

            tbt.save()
            return redirect("/custcltcareersurl")
    else:
        return render(request, "custlogin.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def applyjob(request):
    if request.session.has_key('id'):
        if request.method == "POST":
            ii=request.session['id']
            var1=db_addjob.objects.all()
            jaid=request.GET['jbid']
            print(jaid,"+++++++++++++++++++++++++++")
            notesfile = request.FILES["notesfile"]
            ii=request.session['id']
            uid=db_custsignup.objects.get(id=ii)
            jid=db_addjob.objects.get(id=jaid)
            print("---------------------------",jid)
            q=db_addjob.objects.all().filter(id=jaid)
            for x in q:
                eid=x.id
                print(eid,"EIDDDDDDDDDDDDDDDDD")
            if db_careers.objects.all().filter(job_id=eid,user_id=uid):
                ii=request.session['id']
                print("already saved+++++++++++++++")
                aview=db_careers.objects.all().filter(user_id=ii)
                return redirect("/viewjobsclt")

                
            else:

               
                # ii=request.session['id']
                print("save=======================")
                # var=jobapplytable.objects.all().filter(userid=ii)
                a=db_careers(job_id=jid,user_id=uid,notesfile=notesfile)#,Resume=var
                a.save()
                ii=request.session['id']
                var1=db_custsignup.objects.all().filter(id=ii)
                aview=db_careers.objects.all().filter(user_id=ii)
                # return render(request, "appliedjob.html",{'av':aview,'aa':var1})
                # return HttpResponse("SUCCESSFULL")
                return render(request,"successnew.html")     
    else:
        return render(request, "custlogin.html")




            
def successnew(request):
    return render(request,"successnew.html")     
    



def ADDJOB(request):

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "addjob.html",{'coslogin':tb})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "addjob.html",{'admin':tbb})
    else:
        return redirect("else")
    
def ADDINSERTJOB(request):
    
    if request.method == "POST":
        tbt = db_addjob()
        tbt.company = request.POST.get("comp")
        tbt.jobtitle = request.POST.get("title")
        tbt.description = request.POST.get("descri")
        tbt.jobtype = request.POST.get("selectt")
        tbt.save()
        return redirect("/addjob")
def VIEWJOBS(request):
    obj1 = db_addjob.objects.filter(is_delete=0)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewjobs.html",{'coslogin':tb,'ob': obj1})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewjobs.html",{'admin':tbb,'ob': obj1})
    else:
        return redirect("else")
    



def JOBDELETE(request, id):
    
    tb = db_addjob.objects.get(id=id)
    tb.delete()
    return redirect("/viewjobs")

def UPDATEJOB(request,id):
    obj=db_addjob.objects.get(id=id)

    
    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "jobupdate.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "jobupdate.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")
    
def JOBUPDATINSERT(request,id):
    
    if request.method == "POST":
        tb = db_addjob.objects.get(id=id)
        tb.company = request.POST.get("comp")
        tb.jobtitle = request.POST.get("title")
        tb.description = request.POST.get("descri")
        tb.jobtype = request.POST.get("selectt")

        tb.save()
        return redirect("/viewjobs")




















#templates   templates    templates    templates   templates    templates    templates    templates    templates    templates    templates    templates


def index(request):
    obj = db_add_product.objects.filter(is_delete=0,status=1).exclude(quantity=0)
    obj1= db_category.objects.all()
    return render(request, "vvvv.html",{'ob':obj,'ob1':obj1})

def SERVICES(request):
    return render(request, "services.html")
def BLOG(request):
    return render(request, "blog.html")
def HELP(request):
    return render(request, "help.html")


def SHOPNOW(request):
    return render(request, "shopnow.html")
# def CART(request):
#     return render(request, "cart.html")








    


# def addtocart(request):
#     ii=request.session['id']

#     print(ii)
#     uid=db_custsignup.objects.get(id=ii)
#     print(uid)
#     jaid=request.GET['faid']
#     print(jaid)
#     var1=db_addcourse_table.objects.get(id=jaid)
#     print(var1)
#     quantityy=request.GET["num"]
#     print(quantityy)
#     print("((((((((((((((((((((((((((((((((((((")
#     if db_carttt.objects.filter(user_id=uid,course_id=var1):     #original
#         var1=db_addcourse_table.objects.get(id=jaid)
#         quantityy=request.GET["num"]

#         price=(var1.course_price)
#         print(price)
#         totall=int(price)*int(quantityy)
#         print(totall)
#         ii=request.session['id']
#         print(ii)
#         uid=db_custsignup.objects.get(id=ii)
#         print(uid)
#         jaid=request.GET['faid']
#         obj = db_carttt.objects.all().filter(user_id=ii)
#         print("welcome============================")
#         return render(request, "cart.html", {'ob': obj})

#     else:
#         jaid=request.GET['faid']

#         var1=db_addcourse_table.objects.all().get(id=jaid)
#         quantityy=request.GET["num"]


#         price=(var1.course_price)
#         print(price)
#         totall=int(price)*int(quantityy)
#         print(totall)
#         ii=request.session['id']
#         print(ii)
#         uid=db_custsignup.objects.get(id=ii)
#         print(uid)
#         obj = db_carttt.objects.all()


#         a=db_carttt(user_id=uid,course_id=var1,quantity=quantityy,total=totall)
#         a.save()

#         ii=request.session['id']
#         obj=db_carttt.objects.all().filter(user_id=ii)
#         return render(request,'cart.html',{'ob':obj})
#         print("++++++++++++++++++++++++++++++++++++")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def cartlist(request):
    if request.session.has_key('id'):
        ii=request.session['id']
        gId = request.GET.get('gId')
        obj2 = db_Governerate_table.objects.filter(is_delete=0)
        obj3 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)
        uid=db_custsignup.objects.get(id=ii)
        obj1=db_custsignup.objects.all().filter(id=ii) 
        obj=db_cart.objects.all().filter(user_id=ii,is_delete=0,stage=0)
        obj = db_cart.objects.all().filter(user_id=ii,is_delete=0)
        sum1=0
        for i in obj:
            a=i.total
            sum1=sum1+a
        objj=db_cart.objects.all().filter(user_id=ii,is_delete=0).count()

        return render(request,'cartneww.html',{'ob':obj,'ob1':obj1,'sum1':sum1,'count':objj,'ob2':obj2,'ob3':obj3})
    else:
        return render(request,'custlogin.html')






@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def addtocartproduct(request):
    if request.session.has_key('id'):
        ii=request.session['id']

        print(ii)
        uid=db_custsignup.objects.get(id=ii)
        print(uid)
        jaid=request.GET['faid']
        print(jaid)
        var1=db_add_product.objects.get(id=jaid)
        print(var1)
        quantityy=request.GET["num"]
        print(quantityy)
        print("((((((((((((((((((((((((((((((((((((")
        if db_cart.objects.all().filter(user_id=uid,item_id=jaid,is_delete=0,status=0):
            ii=request.session['id']
            print(ii,"print ii")
            uid=db_custsignup.objects.get(id=ii)
            print(uid,"userid")
            jaid=request.GET['faid']
            var1=db_add_product.objects.get(id=jaid)
            obj = db_cart.objects.all().filter(user_id=ii,is_delete=0)
            print("welcome============================")
            row=db_add_product.objects.all()

            # for x in row:
            #     print(row,"rowww")
            #     varr=x.id
            #     print(varr,"varrrrrrrrrrrrrrrrrrrrrrrrrrr")
            #     obj2 = ProductImages.objects.filter(is_delete=0,id=varr)
            return render(request,'cart.html',{'ob':obj})#,'ob1':obj2
            print("++++++++++++++++++++++++++++++++++++")

        else:
            ii=request.session['id']
            print(ii)
            uid=db_custsignup.objects.get(id=ii)
            print(uid)
            jaid=request.GET['faid']
            var1=db_add_product.objects.all().get(id=jaid)
            quantityy=request.GET["num"]
            print(quantityy,"product quantity")
            price=(var1.product_price)
            print(price,"product price")
            totall=int(price)*int(quantityy)
            print(totall,"product total")

            a=db_cart(user_id=uid,item_id=jaid,quantity=quantityy,total=totall,status=0,product_id=var1)
            a.save()
            row=db_add_product.objects.all()
            obj=db_cart.objects.all().filter(user_id=ii,is_delete=0)

            # for x in row:
            #     print(row,"rowww")
            #     varr=x.id
            #     print(varr,"varrrrrrrrrrrrrrrrrrrrrrrrrrr")
            #     obj2 = ProductImages.objects.filter(is_delete=0,id=varr)
            return render(request,'cart.html',{'ob':obj})#,'ob1':obj2
            print("++++++++++++++++++++++++++++++++++++")
    else:
        return render(request,'custlogin.html')





@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def addtocart(request):
    if request.session.has_key('id'):

        ii=request.session['id']
        obj1=db_custsignup.objects.all().filter(id=ii)  
        print(ii)
        uid=db_custsignup.objects.get(id=ii)
        print(uid)
        jaid=request.GET['faid']
        print(jaid)
        var1=db_addcourse_table.objects.get(id=jaid)
        print(var1)
        
        print("((((((((((((((((((((((((((((((((((((")
        if db_cart.objects.filter(user_id=uid,item_id=jaid,is_delete=0,status=1):     #original
            var1=db_addcourse_table.objects.get(id=jaid)
            var2=db_add_product.objects.all().get(id=jaid)
            

            price=(var1.course_price)
            print(price)
            totall=int(price)
            print(totall)
            ii=request.session['id']
            print(ii)
            uid=db_custsignup.objects.get(id=ii)
            print(uid)
            jaid=request.GET['faid']
            # obj = db_cart.objects.all().filter(user_id=ii,is_delete=0)
            obj=db_cart.objects.all().filter(user_id=ii,is_delete=0)
            objj=db_cart.objects.all().filter(user_id=ii,is_delete=0).count()

            return render(request,'cartneww.html',{'ob':obj,'ob1':obj1,'count':objj})

        else:
            jaid=request.GET['faid']

            var1=db_addcourse_table.objects.all().get(id=jaid)

            price=(var1.course_price)
            print(price)
            totall=int(price)
            print(totall)
            ii=request.session['id']
            print(ii)
            uid=db_custsignup.objects.get(id=ii)
            print(uid)
                                                       


            a=db_cart(user_id=uid,item_id=jaid,total=totall,stage=0,status=1,course_id=var1,quantity=1)#
            a.save()

            ii=request.session['id']
            # obj=db_cart.objects.all().filter(user_id=ii,is_delete=0,stage=0)
            obj=db_cart.objects.all().filter(user_id=ii,is_delete=0)
            objj=db_cart.objects.all().filter(user_id=ii,is_delete=0).count()

            return render(request,'cartneww.html',{'ob':obj,'ob1':obj1,'count':objj})

    else:
        return render(request,'custlogin.html')






@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def checkout(request):
    if request.session.has_key('id'):
        ii=request.session['id']
        uid=db_custsignup.objects.get(id=ii)
        obj1=db_cart.objects.all().filter(user_id=uid,is_delete=0)
        sum1=0
        for i in obj1:
            a=i.total
            sum1=sum1+a
            print(sum1,"++++++++++++++")
        if db_cart.objects.all().filter(user_id=uid,is_delete=0):
            a=db_orderr(user_id=uid,total=sum1,stage=0)
            a.save()
            var1=db_cart.objects.all().filter(user_id=uid,is_delete=0)
            print(var1,"var1")
            for i in var1:
                itm=i.item_id
                print(itm,"item")
                prc=i.total
                qty=i.quantity
                prd=i.product_id
                print(prd,"product foreignkey")

                crs=i.course_id
                print(crs,"course foreignkey")
                oid=db_orderritem(order_id=a,user_id=uid,stage=0,item_order=itm,total=prc,quantity=qty,course_id=crs,product_id=prd)#
                oid.save()
                count= db_cart.objects.all().filter(is_delete=0,user_id=uid,stage=0).count()
                b=db_cart.objects.filter(user_id=uid,is_delete=0,stage=0).update(updated_at=datetime.now())


     
        else:
            return render(request, "checkout.html",{'ob':obj1,'sum1':sum1,'count':count})
        
        return render(request, "checkout.html",{'ob':obj1,'sum1':sum1,'count':count})
    else:
        return render(request,'custlogin.html')







# @cache_control(no_cache=True,must_revalidate=True,no_store=True)
# def cart_payment(request):
#     if request.session.has_key('id'):
#         ii=request.session['id']
#         uid=db_custsignup.objects.get(id=ii)
#         obj1=db_cart.objects.all().filter(user_id=uid,is_delete=0)
#         sum1=0
#         for i in obj1:
#             a=i.total
#             sum1=sum1+a
#             print(sum1,"++++++++++++++")
#         if db_cart.objects.all().filter(user_id=uid,is_delete=0):
#             a=db_orderr(user_id=uid,total=sum1,stage=0)
#             a.save()
#             var1=db_cart.objects.all().filter(user_id=uid,is_delete=0)
#             print(var1,"var1")
#             for i in var1:
#                 itm=i.item_id
#                 print(itm,"item")
#                 prc=i.total
#                 qty=i.quantity
#                 oid=db_orderritem(order_id=a,user_id=uid,stage=0,item_order=itm,total=prc,quantity=qty)#
#                 oid.save()
#                 count= db_cart.objects.all().filter(is_delete=0,user_id=uid,stage=0).count()
#                 b=db_cart.objects.filter(user_id=uid,is_delete=0,stage=0).update(updated_at=datetime.now())


     
#         else:
#             return render(request, "checkout.html",{'ob':obj1,'sum1':sum1,'count':count})
        
#         return render(request, "checkout.html",{'ob':obj1,'sum1':sum1,'count':count})
#     else:
#         return render(request,'custlogin.html')


def cart_payment(request):
    ii=request.session["id"]

    if request.method=="POST":
        ii=request.session['id']
        uid=db_custsignup.objects.get(id=ii)
        print(uid,"llll")

        amount=request.POST["subtotall"]

        obj1=db_cart.objects.all().filter(user_id=uid,is_delete=0)
        obj2=db_addaddresstable.objects.all().filter(user_id=uid)
        print(obj2,"obj2")

        id = db_addaddresstable.objects.only('id').get(user_id=uid).id
        print(id,"id")

        

        if db_cart.objects.all().filter(user_id=uid,is_delete=0):
            a=db_orderr(user_id=uid,total=amount,stage=0,address_id=id,status='pending')
            a.save()
            var1=db_cart.objects.all().filter(user_id=uid,is_delete=0)
            for i in var1:
                itm=i.item_id
                print(itm,"item")
                prc=i.total
                qty=i.quantity
                prd=i.product_id
                print(prd,"product foreignkey")

                crs=i.course_id
                print(crs,"course foreignkey")
                oid=db_orderritem(order_id=a,user_id=uid,stage=0,item_order=itm,total=prc,quantity=qty,course_id=crs,product_id=prd,status='pending')#
                oid.save()
                count= db_cart.objects.all().filter(is_delete=0,user_id=uid,stage=0).count()
                b=db_cart.objects.filter(user_id=uid,is_delete=0,stage=0).update(updated_at=datetime.now())
        else:
            return render(request, "checkout.html",{'ob':obj1,'amount':amount,'count':count,'ob1':uid})
        
        return render(request, "checkout.html",{'ob':obj1,'amount':amount,'count':count,'ob1':uid})
        # return render(request,'frontend/cart_payment.html',{'db':user,'amount':amount})
        
    else:
        return HttpResponse("elseeeeeeeeeeeeeeeeeeeeeeee")

def viewstatus(request, id):
    obj = db_orderr.objects.get(id=id)
    print(obj,"objj")

    return render(request,'viewstatus.html',{'ob':obj})

def statusupdate(request, id):
    ii=request.session['id']
    uid=db_custsignup.objects.get(id=ii)
    tb = db_orderr.objects.get(id=id)
    if request.method == "POST":
        tb.status = request.POST.get("status")
        status = request.POST.get("status")
        tb.save()
        tbb = db_orderritem.objects.all().filter(order_id=id,user_id=uid).update(status=status)

        return redirect("/vieworder")



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def cancel(request):
    if request.session.has_key('id'):
        ii=request.session['id']
        uid=db_custsignup.objects.get(id=ii)
        # if db_orderr.objects.all().filter(user_id=uid,stage=2):
        #         return HttpResponse("u already canceled the order")

            
        if db_cart.objects.all().filter(user_id=uid,is_delete=0):
            sum1=0
            obj1=db_cart.objects.all().filter(user_id=uid,is_delete=0)      ###order cencel

            for i in obj1:
                a=i.total
                sum1=sum1+a
                a=db_orderr(user_id=uid,total=sum1,stage=2)
                a.save()
            obj1= db_category.objects.all()
            b=db_cart.objects.filter(user_id=uid,is_delete=0,stage=0).update(stage=2,updated_at=datetime.now())
            return render(request,'vvvv.html',{'ob1':obj1})
    else:
        return render(request,'custlogin.html')

            


                # obj=db_cart.objects.all().filter(user_id=ii,is_delete=1,stage=2)
                # return render(request,'cart.html',{'ob':obj})


def terms(request):
    return render(request,"termscondition.html")



#,id1,id2,id3
def payment(request):
    aid=request.GET['paymentid']
    print(aid,"aiddddddddddddddddd")
    bid=request.GET['result']
    print(bid,"aiddddddddddddddddd")

    cid=request.GET['auth']
    print(cid,"aiddddddddddddddddd")

    did=request.GET['avr']
    print(did,"aiddddddddddddddddd")

    eid=request.GET['ref']
    print(eid,"aiddddddddddddddddd")

    fid=request.GET['tranid']
    print(fid,"aiddddddddddddddddd")

    gid=request.GET['postdate']
    hid=request.GET['trackid']
    amount=request.GET['amt']
    print(amount,"amount")





    ii=request.session['id']
    uid=db_custsignup.objects.get(id=ii)
    tb = db_cart.objects.all().filter(stage=0,user_id=uid)


    
    # if db_orderritem.objects.all().filter(user_id=uid,stage=1):
    #     return HttpResponse("YOU ALREADY PAID FOR THIS payment")
    # else:
    obj=db_orderr.objects.all().filter(user_id=uid,stage=0)

    c=db_orderr.objects.all().filter(user_id=uid,stage=0).update(stage=1)
    d=db_cart.objects.all().filter(user_id=uid,stage=0).update(stage=1,is_delete=1,updated_at=datetime.now())
    e=db_orderritem.objects.all().filter(user_id=uid,stage=0).update(stage=1)
    f=db_orderr.objects.all().filter(user_id=uid,stage=1)
    for i in f:
        var1=i.id
    g=db_orderritem.objects.all().filter(user_id=uid,order_id=var1,stage=1).values_list('item_order', flat=True)
    print(g,"item order")
    b=db_orderritem.objects.all().filter(user_id=uid,order_id=var1,stage=1)
    for i in b:
        var2=i.item_order
        print(var2,"item orderrr")
    print(var2,"item hghghgh")

    k = db_add_product.objects.filter(status=1,is_delete=0,id=var2).values_list('id', flat=True)
    print(k,"product id")


    
        
    l = db_add_product.objects.filter(status=1,is_delete=0,id=var2).values_list('quantity', flat=True)
    for i in l:
        var10=i
        
        print(var10,"qUA-var10")


    print(l,"total quantity from product table-object")

    b=db_orderritem.objects.all().filter(user_id=uid,order_id=var1,stage=1)
    for i in b:
        var5=i.quantity
        print(var5," taken quantity")
    

        newqty=var10 - var5
        print(newqty,"newwwwwwquantity")
        i=db_add_product.objects.all().filter(id=var2,is_delete=0,status=1).update(quantity=newqty)
        obj = db_add_product.objects.filter(is_delete=0,status=1).exclude(quantity__lte=0)
        obj1= db_category.objects.all()
        return render(request,'invoice.html',{'aid':aid,'bid':bid,'cid':cid,'did':did,'eid':eid,'fid':fid,'gid':gid,'hid':hid,'amount':amount})#
        # return render(request,"vvvv.html")
    else:




    
        print("YOUR CART IS EMPTY....U PAID FOR THIS")
        # return HttpResponse("PAYMENT SUCCESSFULL..... THANK YOU/goback/")
        obj = db_add_product.objects.filter(is_delete=0,status=1).exclude(quantity=0)
        obj1= db_category.objects.all()
        return render(request,'vvvv.html',{'ob':obj,'ob1':obj1})

        # obj = db_cart.objects.all().filter(user_id=ii,is_delete=0)
        # return render(request, "cart.html", {'ob': obj})
   
    # obj=db_orderr.objects.all().filter(user_id=uid,stage=0)
    # if obj:
        



    # else:
    #     # obj=db_orderr.objects.all().filter(user_id=uid,stage='paid')
    #     # return HttpResponse("ALREADY DONE")
    #     obj = db_cart.objects.all().filter(user_id=ii,is_delete=0,stage=0)
    #     print("welcome============================")
    #     return render(request, "cart.html", {'ob': obj})

        






def buyproduct(request):
    ii=request.session['id']
    print(ii)
    uid=db_custsignup.objects.get(id=ii)
    print(uid)
    jaid=request.GET['faid']
    print(jaid)
    var1=db_add_product.objects.get(id=jaid)
    print(var1)
    
    print("((((((((((((((((((((((((((((((((((((")
    if db_productorder.objects.filter(user_id=uid,product_id=var1):   
        var1=db_add_product.objects.get(id=jaid)
        var2=db_add_product.objects.all().get(id=jaid)
        

        price=(var1.product_price)
        print(price)
        totall=int(price)
        print(totall)
        ii=request.session['id']
        print(ii)
        uid=db_custsignup.objects.get(id=ii)
        print(uid)
        jaid=request.GET['faid']
        obj = db_productorder.objects.all().filter(user_id=ii,product_id=var1)
        obj1=db_custsignup.objects.all().filter(id=ii)           

        print("welcome============================")
        return render(request, "order.html", {'ob':obj1,'bb':obj,'total':totall})

    else:
        jaid=request.GET['faid']

        var1=db_add_product.objects.all().get(id=jaid)

        quantityy=request.GET["num"]
        print(quantityy,"product quantity")
        price=(var1.product_price)
        print(price,"product price")
        totall=int(price)*int(quantityy)
        print(totall,"product total")
        ii=request.session['id']
        print(ii)
        uid=db_custsignup.objects.get(id=ii)
        print(uid)
        


        a=db_productorder(user_id=uid,product_id=var1,total=totall,stage='unpaid')
        a.save()

        ii=request.session['id']
        obj=db_productorder.objects.all().filter(user_id=ii,product_id=var1)
        obj1=db_custsignup.objects.all().filter(id=ii)           

        return render(request,'order.html',{'ob':obj1,'bb':obj,'total':totall})
        print("++++++++++++++++++++++++++++++++++++")



def buycourse(request):
    ii=request.session['id']
    print(ii)
    uid=db_custsignup.objects.get(id=ii)
    print(uid)
    jaid=request.GET['faid']
    print(jaid)
    var1=db_addcourse_table.objects.get(id=jaid)
    print(var1)
    
    print("((((((((((((((((((((((((((((((((((((")
    if db_courseorder.objects.filter(user_id=uid,course_id=var1):     #original
        var1=db_addcourse_table.objects.get(id=jaid)
        var2=db_add_product.objects.all().get(id=jaid)
        

        price=(var1.course_price)
        print(price)
        totall=int(price)
        print(totall)
        ii=request.session['id']
        print(ii)
        uid=db_custsignup.objects.get(id=ii)
        print(uid)
        jaid=request.GET['faid']
        obj = db_courseorder.objects.all().filter(user_id=ii,course_id=var1,stage='unpaid')
        obj1=db_custsignup.objects.all().filter(id=ii)           

        print("welcome============================")
        return render(request, "order.html", {'ob':obj1,'bb':obj,'total':totall})

    else:
        jaid=request.GET['faid']

        var1=db_addcourse_table.objects.all().get(id=jaid)

        price=(var1.course_price)
        print(price)
        totall=int(price)
        print(totall)
        ii=request.session['id']
        print(ii)
        uid=db_custsignup.objects.get(id=ii)
        print(uid)
        


        a=db_courseorder(user_id=uid,course_id=var1,total=totall,stage='unpaid')
        a.save()

        ii=request.session['id']
        obj=db_courseorder.objects.all().filter(user_id=ii,course_id=var1)
        obj1=db_custsignup.objects.all().filter(id=ii)           

        return render(request,'order.html',{'ob':obj1,'bb':obj,'total':totall})
        print("++++++++++++++++++++++++++++++++++++")







# def VIEWCOURSE(request):
#     obj = db_addcourse_table.objects.filter(is_delete=0)
#     print(obj)
#     return render(request, "course.html", {'ob': obj})

    



# def VIEWCOURSE(request):
#     obj = db_addcourse_table.objects.filter(is_delete=0)
#     print(obj)
#     return render(request, "course.html", {'ob': obj})




def WISH_LIST(request):
    ii=request.session['id']
    jaid=request.GET['fali']
    uid=db_custsignup.objects.get(id=ii)
    var1=db_addcourse_table.objects.get(id=jaid)
    if db_wishlist.objects.filter(userid=uid,course_id=var1):
        ii=request.session['id']
        jaid=request.GET['fali']
        var1=db_addcourse_table.objects.get(id=jaid)
        obj=db_wishlist.objects.all().filter(userid=ii)
        return render(request,'fav.html',{'ob':obj})
    else:
        ii=request.session['id']
        uid=db_custsignup.objects.get(id=ii)
        jaid=request.GET['fali']
        var1=db_addcourse_table.objects.all().get(id=jaid)
        obj = db_wishlist.objects.all()
        a=db_wishlist(userid=uid,course_id=var1)
        a.save()
        ii=request.session['id']
        obj=db_wishlist.objects.all().filter(userid=ii)
        return render(request,'fav.html',{'ob':obj})

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def wishlistproductlist(request):
    if request.session.has_key('id'):

        ii=request.session['id']
        obj=db_wishlistproduct.objects.all().filter(userid=ii,is_delete=0)

        return render(request,'fav.html',{'ob':obj})
    else:
        return render(request, "custlogin.html")
        


def wishlistproduct(request):
    ii=request.session['id']
    jaid=request.GET['pali']
    uid=db_custsignup.objects.get(id=ii)
    var1=db_add_product.objects.get(id=jaid)
    if db_wishlistproduct.objects.filter(userid=uid,product_id=var1,is_delete=0):
        ii=request.session['id']
        jaid=request.GET['pali']
        var1=db_add_product.objects.get(id=jaid)
        obj=db_wishlistproduct.objects.all().filter(userid=ii,is_delete=0)
        return redirect("/newproduct/4")
        
    else:
        ii=request.session['id']
        uid=db_custsignup.objects.get(id=ii)
        jaid=request.GET['pali']
        var1=db_add_product.objects.all().get(id=jaid)
        obj = db_wishlistproduct.objects.all()
        a=db_wishlistproduct(userid=uid,product_id=var1)
        a.save()
        ii=request.session['id']
        obj=db_wishlistproduct.objects.all().filter(userid=ii,is_delete=0)
        return redirect("/newproduct/4")
        


def wishlistproductdelete(request, id):
    tb = db_wishlistproduct.objects.get(id=id)
    tb.is_delete = 1
    tb.save()
    ii=request.session['id']

    obj=db_wishlistproduct.objects.all().filter(userid=ii,is_delete=0)
    return render(request,'fav.html',{'ob':obj})


    











    



def TRENDINGPRODUCTS(request):
    return render(request, "trendingproducts.html")





#sham  #sham  #sham  #sham   #sham   #sham   #sham   #sham   #sham   #sham     #sham  #sham   #sham   #sham   #sham  #sham   #sham  #sham

#cource #cource  #cource #cource #cource  #cource  #cource #cource  #cource  #cource #cource  #cource   #cource #cource  #cource #cource #cource  #cource


def COURCESIDEMENU(request):
    return render(request, "courcesidemenu.html")
def POWCOURCE(request):
    return render(request, "powcource.html")
def AVATARCOURCE(request):
    return render(request, "avatarcource.html")

def NAVBARCOURCE(request):
    return render(request, "navbarcource.html")

def COURCEPAGE(request):
    if request.session.has_key('is_logged'):                                   # session
        if request.session['type'] == "COURCEPAGE":
            return render(request, "COURCEPAGE.html")
    return redirect("/login")
    #session
def CCOURCELOGOUT(request):
    request.session['is_logged']                                               #session
    request.session.flush();                                                   #session
    return redirect("/login")




def addcoursecource(request):
    obj = db_coursecategory_table.objects.filter(is_delete=0)
    return render(request, "addcoursecource.html", {'ob': obj})



        
def ADDCOURSE(request):
    obj = db_coursecategory_table.objects.filter(is_delete=0)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "add_course.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "add_course.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")

def addmodule(request):
    obj=db_addcourse_table.objects.all()
    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")
        return render(request, "coursemodule.html",{'coslogin':tb,'ob':obj})

    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "coursemodule.html",{'admin':tbb,'ob':obj})
    else:
        return redirect("else")


def coursemodule(request):
    obj=db_addcourse_table.objects.all()
    course=request.POST.get("course_id")
    print(course,"course")
    level = request.POST.get("level")
    print(level,"level")

    module = request.POST.get("module")
    print(module,"module")

    chapter = request.POST.get("chapter")
    print(chapter,"chapter")


    videos = request.FILES.getlist("file[]")
    print(videos)
   

    
    for vid in videos:
        fs = FileSystemStorage()
        filename = fs.save(vid.name, vid)
        uploaded_file_url = fs.url(filename)

        course=db_coursemodules(level=level,module=module,chapter=chapter,course_id_id =course,video_name=uploaded_file_url)
        course.save()
        return render(request, "coursemodule.html",{'ob':obj})
    return render(request, "coursemodule.html",{'ob':obj})





def COURSEINSERT(request):
    
    
    category_id = request.POST.get("category_id")
    course_name = request.POST.get("course_name")
    

    level = request.POST.get("level")
    course_price = request.POST.get("course_price")
    description = request.POST.get("description")
    review = request.POST.get("review")

    status = True
    photo = request.FILES.get("photo")
    fs = FileSystemStorage()
    filename = fs.save(photo.name, photo)
    uploaded_file_url = fs.url(filename)
    #
    # name=request.POST.get("name")
    # desc=request.POST.get("desc")
    videos = request.FILES.getlist("file[]")
    print(videos)

    product = db_addcourse_table(category_id=category_id, course_name=course_name,
                                 course_price=course_price, description=description, status=status,
                                 photo=uploaded_file_url,level=level,review=review)
    product.save()
   


    for vid in videos:
        fs = FileSystemStorage()
        filename = fs.save(vid.name, vid)
        uploaded_file_url = fs.url(filename)

        pimage = db_addcoursevideo_table(video=product, video_name=uploaded_file_url)
        pimage.save()
    # return HttpResponse("File Uploaded")
    return redirect("/addcourse")



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def module(request):
    if request.session.has_key('id'):
        if request.method=="POST":
            level=request.POST["level"]
            print(level,"level")
            module=request.POST["module"]
            print(module,"module")
            chapter=request.POST["chapter"]
            print(chapter,"chapter")




            obj=db_coursemodules.objects.filter(level=level,module=module,chapter=chapter)
            print(obj,"obj")
            id = db_coursemodules.objects.only('id').get(level=level,module=module,chapter=chapter).id
            print(id,"idddddddddd")
           
            obj1=db_coursemodules.objects.filter(id=id)
            print(obj1,"obj1")
            return render(request,"newcourse.html", {'ob': obj1,'ob1':obj})


            
            
            

                

    else:
        return render(request, "custlogin.html")


def courseinsertcource(request):
    category_id = request.POST.get("category_id")
    course_name = request.POST.get("course_name")
    course_price = request.POST.get("course_price")
    description = request.POST.get("description")
    status = True
    photo = request.FILES.get("photo")
    fs = FileSystemStorage()
    filename = fs.save(photo.name, photo)
    uploaded_file_url = fs.url(filename)
    #
    # name=request.POST.get("name")
    # desc=request.POST.get("desc")
    videos = request.FILES.getlist("file[]")
    print(videos)

    product = db_addcourse_table(category_id=category_id, course_name=course_name,
                                 course_price=course_price, description=description, status=status,
                                 photo=uploaded_file_url)
    product.save()

    for vid in videos:
        fs = FileSystemStorage()
        filename = fs.save(vid.name, vid)
        uploaded_file_url = fs.url(filename)

        pimage = db_addcoursevideo_table(video=product, video_name=uploaded_file_url)
        pimage.save()
    # return HttpResponse("File Uploaded")
    # return redirect("/addcourse")
    return render(request, "addcoursecource.html")


def viewaddmodules(request):
    obj = db_coursemodules.objects.all()
    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")
        return render(request, "viewaddmodule.html",{'ob':obj,'coslogin':tb})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewaddmodule.html",{'ob':obj,'admin':tbb})
    else:
        return redirect("else")


def viewaddmoduleupdate(request, id):
    obj = db_coursemodules.objects.get(id=id)
    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")
        return render(request, "viewaddmoduleupdate.html",{'ob':obj,'coslogin':tb})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewaddmoduleupdate.html",{'ob':obj,'admin':tbb})

    else:
        return redirect("else")

def viewaddmoduleupdateinsert(request, id):
     if request.method == "POST":
        tb = db_coursemodules.objects.get(id=id)

        tb.level = request.POST.get("level")
        tb.module = request.POST.get("module")
        tb.chapter = request.POST.get("chapter")


        videos = request.FILES.getlist("file[]")
        tb.save()
        
        b=db_addcourse_table.objects.all().filter(id=tb.course_id_id).update(level=tb.level)
        

        # for vid in videos:
        #     fs = FileSystemStorage()
        #     filename = fs.save(vid.name, vid)
        #     uploaded_file_url = fs.url(filename)

        #     pimage = db_coursemodules(video_name=uploaded_file_url)
        #     pimage.save()
        print("uuuuuuuuuuuu")

        return redirect("/viewaddmodules")


def viewaddmodulevideos(request, id):
    obj = db_coursemodules.objects.filter(id=id)
    return render(request, "viewaddmodulevideo.html",{'ob': obj})





def VIEWADDCOURSES(request):
    obj = db_addcourse_table.objects.filter(is_delete=0)


    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewaddcourses.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewaddcourses.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")
    

def viewaddcoursecource(request):
    obj = db_addcourse_table.objects.filter(is_delete=0)
    return render(request, "viewaddcoursecource.html", {'ob': obj})







def VIEWADDCOURSESUPDATE(request, id):
    obj = db_addcourse_table.objects.get(id=id)
    vid = db_addcoursevideo_table.objects.filter(video_id=id,is_delete=0)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewaddcoursesupdate.html",{'coslogin':tb,'ob': obj, 'vid': vid})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewaddcoursesupdate.html",{'admin':tbb,'ob': obj, 'vid': vid})
    else:
        return redirect("else")
    
    

def viewaddcoursesupdate(request, id):
    
    obj = db_addcourse_table.objects.get(id=id)
    vid = db_addcoursevideo_table.objects.filter(video_id=id,is_delete=0)
    return render(request, "viewaddcoursesupdatecource.html", {'ob': obj, 'vid': vid})


def VIEWADDCOURSESUPDATEINSERT(request, id):
    if request.method == "POST":
        tb = db_addcourse_table.objects.get(id=id)
        tb.category_id = request.POST.get("category_id")
        tb.course_name = request.POST.get("course_name")
        # tb.description = request.POST.get("discription")


        photo = request.FILES.get("photo")
        if photo:
            fs = FileSystemStorage()
            filename = fs.save(photo.name, photo)
            uploaded_file_url = fs.url(filename)
            tb.photo = uploaded_file_url

        tb.course_price = request.POST.get("course_price")
        tb.description = request.POST.get("discription")
        tb.review = request.POST.get("review")

        tb.status = request.POST.get("status")
        videos = request.FILES.getlist("file[]")
        tb.save()

        for vid in videos:
            fs = FileSystemStorage()
            filename = fs.save(vid.name, vid)
            uploaded_file_url = fs.url(filename)

            pimage = db_addcoursevideo_table(video=tb, video_name=uploaded_file_url)
            pimage.save()
        return redirect("/viewaddcourses")


def VIEWADDCOURSESDELETE(request, id):
    tb = db_addcourse_table.objects.get(id=id)
    tb.is_delete = 1
    tb.save()
    return redirect("/viewaddcourses")


def VIEWADDCOURSESVIDEOS(request, id):
    obj = db_addcoursevideo_table.objects.filter(video_id=id, is_delete=0)


    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewaddcoursesvideos.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewaddcoursesvideos.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")


def VIEWADDCOURSESVIDEOSDELETE(request, pageId, id):
    tb = db_addcoursevideo_table.objects.get(id=id)
    tb.is_delete = 1
    tb.save()
    return redirect("/viewaddcoursesvideos/" + str(pageId))


def VIEWADDCOURSESCART(request, id):
    obj = db_addcourse_table.objects.get(id=id)
    return render(request, "viewaddcoursescart.html", {'ob': obj})


def COURSECATEGORY(request):

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "coursecategory.html",{'coslogin':tb})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "coursecategory.html",{'admin':tbb})
    else:
        return redirect("else")
    


def COURSECATEGORYINSERT(request):
    if request.method == "POST":
        tb = db_coursecategory_table()
        tb.category_name = request.POST.get("category_name")
        tb.save()

    return redirect("/coursecategory")
 


def VIEWCOURSECATEGORY(request):
    obj = db_coursecategory_table.objects.filter(is_delete=0)

    
    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewcoursecategory.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewcoursecategory.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")
    
    



def VIEWCOURSECATEGORYUPDATE(request, id):
    obj = db_coursecategory_table.objects.get(id=id)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewcoursecategoryupdate.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewcoursecategoryupdate.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")
    


def VIEWCOURSECATEGORYUPDATEINSERT(request, id):
    
    if request.method == "POST":
        tb = db_coursecategory_table.objects.get(id=id)

        tb.category_name = request.POST.get("category_name")

        tb.save()
        return redirect("/viewcoursecategory")


def COURSECATEGORYDELETE(request, id):
    tb = db_coursecategory_table.objects.get(id=id)
    tb.is_delete = 1
    tb.save()
    return redirect("/viewcoursecategory")



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def VIEWSERVICE(request):
    if request.session.has_key('aid'):
        tbb=db_coslogin.objects.all().filter(status=1)
        obj1 = db_service_form.objects.filter(is_delete=0)
        return render(request, "viewservice.html", {'ob': obj1,'admin':tbb})
    else:
        return render(request, "login.html")




@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcustservice(request):
    if request.session.has_key('id'):
        obj1 = db_service_form.objects.filter(is_delete=0)
        return render(request, "viewcustservice.html", {'ob': obj1})
    else:
        return render(request, "custlogin.html")

def SERVICEDELETE(request, id):
    tb = db_service_form.objects.get(id=id)
    tb.is_delete = True
    tb.save()
    return redirect("/viewservice")





def ADDSERVICES(request):

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "addservices.html",{'coslogin':tb})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "addservices.html",{'admin':tbb})
    else:
        return redirect("else")
    


def SERVICEINSERT(request):
    
    if request.method == "POST":
        tb = db_addservice_table()
        tb.service_name = request.POST.get("service_name")
        tb.category = request.POST.get("cat_name")
        tb.service_price = request.POST.get("service_price")
        tb.description = request.POST.get("description")
        tb.status = request.POST.get("status")
        tb.query = request.POST.get("query")
        tb.notes = request.POST.get("notes")
        tb.feature1 = request.POST.get("feature1")
        tb.feature2 = request.POST.get("feature2")
        tb.feature3 = request.POST.get("feature3")
        tb.feature4 = request.POST.get("feature4")


        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        uploaded_file_url = fs.url(filename)
        tb.photo = uploaded_file_url
        videos = request.FILES.getlist("file[]")
        print(videos)

        tb.save()
        for vid in videos:
            fs = FileSystemStorage()
            filename = fs.save(vid.name, vid)
            uploaded_file_url = fs.url(filename)
            pimage = db_servicevideo(video=tb, video_name=uploaded_file_url)
            pimage.save()
        return redirect("/addservices")


def myprofile(request):
    ii=request.session['id']
    print(ii,"ii")
    uid=db_custsignup.objects.get(id=ii)
    print(uid,"uid")
    obj1 = db_orderr.objects.all().filter(is_delete=0,stage=1,user_id=ii)
    obj2= db_cart.objects.all().filter(user_id=uid,stage=1,status=1)
    a=db_orderritem.objects.all().filter(stage=1,is_delete=0,user_id=uid)
    print(a,"aa")

    cursor  = connection.cursor()
    obj4=cursor.execute('select a.status,b.* from db_orderstatus a,db_orderritem b WHERE a.order_id_id=b.order_id_id ')
    print('select a.status,b.* from db_orderstatus a,db_orderritem b WHERE a.order_id_id=b.order_id_id ')
    print(obj4,"objjjjjjjjjj")
    row = cursor.fetchall()
    print(row,"rowwww---------------")

    for x in row:
        print(x,"prooooooooooooo")
    # print(x,"oooo")


    # obj3=db_orderstatus.objects.all().filter(order_id=id)
       
    return render(request, "myprofile.html",{'uid':uid,'ob1':obj1,'ob2':obj2,'item':a,'row':row})
    


def orderitemdeleteclt(request, id):
    ii=request.session['id']
    uid=db_custsignup.objects.get(id=ii)
    tbb = db_orderritem.objects.all().filter(order_id=id,user_id=uid).update(is_delete=1)
    print(tbb,"tbb")
    tb = db_orderr.objects.get(id=id)
    tb.is_delete = True
    
    tb.save()
    
    
    return redirect("/myprofile")


def orderitems(request, id):
    ii=request.session['id']
    uid=db_custsignup.objects.get(id=ii)
    countbuyer= db_orderr.objects.all().filter(stage=1,user_id=ii).count()
    countcancel= db_orderr.objects.all().filter(stage=2,user_id=ii).count()

    a=db_orderritem.objects.all().filter(stage=1,user_id=ii)
    b=db_orderstatus.objects.all().filter(order_id=id)
    print(a,"aa")
    
    

   


    return render(request,'myprofile.html',{'uid':uid,'count':countbuyer,'countc':countcancel,'join':a,'status':b})



def buyedcourse(request):
    return render(request, "buyedcourse.html")










def VIEWADDSERVICE(request):
    obj = db_addservice_table.objects.filter(is_delete=0)


    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewaddservice.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewaddservice.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")
    


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def custviewaddservice(request):
    if request.session.has_key('id'):
        obj = db_addservice_table.objects.filter(is_delete=0)
        return render(request, "service.html", {'ob': obj})
    else:
        return render(request, "course.html", {'ob': obj})


def VIEWADDSERVICESUPDATE(request, id):
    obj = db_addservice_table.objects.get(id=id)
    vid = db_servicevideo.objects.filter(video_id=id,is_delete=0)
    

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewaddservicesupdate.html",{'coslogin':tb,'ob': obj,'vid':vid})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewaddservicesupdate.html",{'admin':tbb,'ob': obj,'vid':vid})
    else:
        return redirect("else")
    
    


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcustserviceupdate(request, id):
    if request.session.has_key('id'):
        gId = request.GET.get('gId')
        obj2 = db_Governerate_table.objects.filter(is_delete=0)
        obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)
        obj = db_service_form.objects.get(id=id)
        return render(request, "viewcustservicesupdate.html", {'ob': obj,'ok':obj2})
    else:
        return render(request, "custlogin.html")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcustserviceupdateinsert(request, id):
    if request.session.has_key('id'):

        if request.method == "POST":
            tbt = db_service_form.objects.get(id=id)
            tbt.name = request.POST.get("name")
            tbt.gender = request.POST.get("gender")
            tbt.email = request.POST.get("email")
            tbt.phone_number = request.POST.get("phone_number")
            tbt.preferred_communication = request.POST.get("preferred_communication")
            tbt.evaluationtimeslot = request.POST.get("evaluationtimeslot")
            tbt.nationality = request.POST.get("nationality")


            tbt.customer_type = request.POST.get("customer_type")
            if tbt.customer_type == "Corporate":

                tbt.company = request.POST.get("company")
                tbt.job_title = request.POST.get("job_title")

            tbt.civil_id = request.POST.get("civil_id")
            tbt.other_mobile = request.POST.get("other_mobile")
            tbt.message_language = request.POST.get("message_language")
            tbt.apartment = request.POST.get("apartment")
            tbt.floor = request.POST.get("floor")
            tbt.building = request.POST.get("building")
            tbt.street = request.POST.get("street")
            tbt.avenue = request.POST.get("avenue")

            tbt.governerate = request.POST.get("governerate")
            tbt.Area = request.POST.get("Area")

            
            tbt.date = request.POST.get("date")
            tbt.save()
            return redirect("/viewcustserviceurl")
    else:
        return render(request, "custlogin.html")





def VIEWADDSERVICESUPDATEINSERT(request, id):
    
    if request.method == "POST":
        tb = db_addservice_table.objects.get(id=id)
        tb.service_name = request.POST.get("service_name")
        tb.service_price = request.POST.get("service_price")
        tb.description = request.POST.get("description")
        tb.query = request.POST.get("query")
        tb.category = request.POST.get("cat_name")
        tb.notes = request.POST.get("notes")
        print("yuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuhgfbn")
        print(request.POST.get("status"))
        # if request.POST.get("status")=="true":
        tb.status = request.POST.get("status")
        # else:
        #    tb.status=0
        photo = request.FILES.get("photo")
        if photo:
            fs = FileSystemStorage()
            filename = fs.save(photo.name, photo)
            uploaded_file_url = fs.url(filename)
            tb.photo = uploaded_file_url

        videos = request.FILES.getlist("file[]")
        tb.save()

        for vid in videos:
            fs = FileSystemStorage()
            filename = fs.save(vid.name, vid)
            uploaded_file_url = fs.url(filename)

            pimage = db_servicevideo(video=tb, video_name=uploaded_file_url)
            pimage.save()
        return redirect("/viewaddservice")









 








def VIEWADDSERVICESDELETE(request, id):
    tb = db_addservice_table.objects.get(id=id)
    tb.is_delete = 1
    tb.save()
    return redirect("/viewaddservice")


def OFFLINETRAINING(request):
    gId = request.GET.get('gId')
    print(gId,"gid")


    obj = db_Governerate_table.objects.filter(is_delete=0)
    obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)
    print(obj1,"obj1")


    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "offlinetraining.html",{'coslogin':tb,'ob': obj,'ob1':obj1})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "offlinetraining.html",{'admin':tbb,'ob': obj,'ob1':obj1})
    else:
        return redirect("else")
    
    





 


def OFFLINETRAININGINSERT(request):
    
    if request.method == "POST":
        tb = db_offlinetraining_table()
        tb.Name = request.POST.get("Name")
        tb.Gender = request.POST.get("Gender")
        tb.Email = request.POST.get("Email")
        tb.Phone_number = request.POST.get("Phone_number")
        tb.Nationality = request.POST.get("Nationality")

        customer_Type = request.POST.get("Customer_Type")
        tb.Customer_Type = customer_Type

        if customer_Type == "Corporate":
            tb.Company = request.POST.get("Company")
            tb.Job_Title = request.POST.get("Job_Title")

        tb.Civil_ID = request.POST.get("Civil_ID")
        tb.Other_Mobile = request.POST.get("Other_Mobile")

        tb.Apartment = request.POST.get("Apartment")
        tb.Floor = request.POST.get("Floor")
        tb.Building = request.POST.get("Building")
        tb.Block = request.POST.get("Block")
        tb.Street = request.POST.get("Street")
        tb.Avenue = request.POST.get("Avenue")
        # tb.status = request.POST.get("status")

        tb.date = request.POST.get("date")
        tb.Governerate = request.POST.get("governarateid")
        tb.Area = request.POST.get("Area")
        tb.save()
        return redirect("/offlinetraining")


def VIEWOFFLINETRAINING(request):
    obj = db_offlinetraining_table.objects.filter(is_delete=0)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewofflinetraining.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewofflinetraining.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")
    
    
    


def VIEWOFFLINETRAININGDELETE(request, id):
    
    tb = db_offlinetraining_table.objects.get(id=id)
    tb.is_delete = 1
    tb.save()
    return redirect("/viewofflinetraining")


def VIEWOFFLINEUPDATE(request, id):
    gId = request.GET.get('gId')
    print(gId,"gid")


    obj = db_Governerate_table.objects.filter(is_delete=0)
    obj1 = db_Area_table.objects.filter(is_delete=0,governerate_id=gId)
    print(obj1,"obj1")

    obj2 = db_offlinetraining_table.objects.get(id=id)
    obj = db_coursecategory_table.objects.filter(is_delete=0)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewofflineupdate.html",{'coslogin':tb,'ob': obj,'ob1':obj1,'ob2':obj2})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewofflineupdate.html",{'admin':tbb,'ob': obj,'ob1':obj1,'ob2':obj2})
    else:
        return redirect("else")
    
    












# def VIEWADDSERVICESUPDATEINSERT(request, id):
#     if request.method == "POST":
#         tb = db_addservice_table.objects.get(id=id)
#         tb.service_name = request.POST.get("service_name")
#         tb.service_price = request.POST.get("service_price")
#         tb.description = request.POST.get("description")
#         print("yuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuhgfbn")
#         print(request.POST.get("status"))
#         # if request.POST.get("status")=="true":
#         tb.status = request.POST.get("status")
#         # else:
#         #    tb.status=0
#         photo = request.FILES.get("photo")
#         if photo:
#             fs = FileSystemStorage()
#             filename = fs.save(photo.name, photo)
#             uploaded_file_url = fs.url(filename)
#             tb.photo = uploaded_file_url

#         tb.save()
#         return redirect("/viewaddservice")

def VIEWOFFLINEUPDATEINSERT(request, id):
    
    if request.method == "POST":
        tb = db_offlinetraining_table.objects.get(id=id)
        tb.Name = request.POST.get("Name")
        tb.Gender = request.POST.get("Gender")
        tb.Email = request.POST.get("Email")
        tb.Phone_number = request.POST.get("Phone_number")
        tb.Nationality = request.POST.get("Nationality")

        customer_Type = request.POST.get("Customer_Type")
        tb.Customer_Type = customer_Type

        if customer_Type == "Corporate":
            tb.Company = request.POST.get("Company")
            tb.Job_Title = request.POST.get("Job_Title")

        tb.Civil_ID = request.POST.get("Civil_ID")
        tb.Other_Mobile = request.POST.get("Other_Mobile")

        tb.Apartment = request.POST.get("Apartment")
        tb.Floor = request.POST.get("Floor")
        tb.Building = request.POST.get("Building")
        tb.Block = request.POST.get("Block")
        tb.Street = request.POST.get("Street")
        tb.Avenue = request.POST.get("Avenue")
        # tb.status = request.POST.get("status")

        tb.date = request.POST.get("date")
        tb.Governerate = request.POST.get("governarateid")
        tb.Area = request.POST.get("Area")
        tb.save()
        return redirect("/viewofflinetraining")



        



def GOVERNERATE(request):
    return render(request, "governerate.html")


def GOVERNERATEINSERT(request):
    if request.method == "POST":
        tb = db_Governerate_table()
        tb.Governerate_name = request.POST.get("Governerate_name")
        tb.save()

    return redirect("/governerate")

def VIEWGOVERNERATE(request):
    obj = db_Governerate_table.objects.filter(is_delete=0)


    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewgovernerate.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewgovernerate.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")

def VIEWGOVERNERATEUPDATE(request, id):
    obj = db_Governerate_table.objects.get(id=id)
    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewgovernerateupdate.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewgovernerateupdate.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")


def VIEWGOVERNERATEUPDATEINSERT(request, id):
    if request.method == "POST":
        tb = db_Governerate_table.objects.get(id=id)

        tb.Governerate_name = request.POST.get("Governerate_name")

        tb.save()
        return redirect("/viewgovernerate")


def COURSEGOVERNERATEDELETE(request, id):
    tb = db_Governerate_table.objects.get(id=id)
    tb.is_delete = 1
    tb.save()
    return redirect("/viewgovernerate")


def AREA(request):
    obj = db_Governerate_table.objects.filter(is_delete=0)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "area.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "area.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")

def AREAINSERT(request):
    if request.method == "POST":
        Area_name = request.POST.get("Area_name")
        governerate_id = request.POST.get("Governerate_name")
        tb = db_Governerate_table.objects.get(id=governerate_id)
        tbt = db_Area_table(Area_name=Area_name,governerate_id=tb)
        tbt.save()

        return redirect("/area")

def VIEWAREA(request):
    obj = db_Area_table.objects.filter(is_delete=0)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewarea1.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewarea1.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")


def VIEWAREAUPDATE(request, id):
    obj = db_Area_table.objects.get(id=id)

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewareaupdate.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewareaupdate.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")


def VIEWAREAUPDATEINSERT(request, id):
    if request.method == "POST":
        tb = db_Area_table.objects.get(id=id)

        tb.Area_name = request.POST.get("Area_name")

        tb.save()
        return redirect("/viewarea")


def VIEWAREADELETE(request, id):
    tb = db_Area_table.objects.get(id=id)
    tb.is_delete = 1
    tb.save()
    return redirect("/viewarea")

def GETAREABYiD(request):
    gId = request.GET.get('gId')
    obj2 = db_Area_table.objects.filter(governerate_id=gId)
    print(obj2)
    return render(request, "areadropdown1.html",{'ob':obj2})













def PRODUCT(request):
    return render(request, "product.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def VIEWPRODUCT(request):
    if request.session.has_key('id'):
    # row=db_add_product.objects.all()
    # for x in row:
    #     print(row,"rowww")
    #     varr=x.id
    #     print(varr,"varrrrrrrrrrrrrrrrrrrrrrrrrrr")
        obj = db_add_product.objects.filter(is_delete=0,status=1)
        return render(request, "product.html", {'ob': obj})
    # obj2 = ProductImages.objects.filter(is_delete=0,product_id=varr)
    else:
        return render(request, "custlogin.html")#,'img1': obj2

def VIEW_CUSTIMAGES(request,id):
    obj=ProductImages.objects.filter(product_id=id,is_delete=0)
    return render(request, "viewcustimages.html", {'ob': obj, 'pageId':id})


def COURSE(request):
    return render(request, "course.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def VIEWCOURSE(request):
    if request.session.has_key('id'):
        obj = db_addcourse_table.objects.filter(is_delete=0,status=1)
        print(obj)
        return render(request, "course.html", {'ob': obj})
    else:
        return render(request, "custlogin.html")



def CUSTCOURSEVIDEOS(request,id):
    obj = db_addcoursevideo_table.objects.filter(video_id=id, is_delete=0)
    return render(request, "custcoursevideos.html", {'ob': obj})



def BLOG(request):
    obj = db_blog_table.objects.filter(is_delete=0)
    return render(request, "blog.html", {'ob': obj})


def CUSTBLOGVIDEOS(request,id):
    obj1 = db_blog_table.objects.filter(is_delete=0,id=id)

    obj = db_blogfile_table.objects.filter(video_id=id, is_delete=0)
    return render(request, "custblogvideos.html", {'ob': obj,'obb':obj1})








def ADDBLOG(request):

    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "addblog.html",{'coslogin':tb})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "addblog.html",{'admin':tbb})
    else:
        return redirect("else")

def BLOGINSERT(request):
    
    name = request.POST.get("name")
    description = request.POST.get("description")
    description1 = request.POST.get("description1")
    description2 = request.POST.get("description2")

    photo = request.FILES.get("photo")
    category = request.POST.get("category")
    fs = FileSystemStorage()
    filename = fs.save(photo.name, photo)
    uploaded_file_url = fs.url(filename)
    #
    # name=request.POST.get("name")
    # desc=request.POST.get("desc")
    videos = request.FILES.getlist("file[]")
    print(videos)

    product = db_blog_table(name=name, description=description, photo=uploaded_file_url,category=category,description1=description1,description2=description2)
    product.save()

    for vid in videos:
        fs = FileSystemStorage()
        filename = fs.save(vid.name, vid)
        uploaded_file_url = fs.url(filename)

        pimage = db_blogfile_table(video=product, video_name=uploaded_file_url)
        pimage.save()
    # return HttpResponse("File Uploaded")

    return redirect("/addblog")


def VIEWADDBLOG(request):
    obj = db_blog_table.objects.filter(is_delete=0)


    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewaddblog.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewaddblog.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")
 
def VIEWADDBLOGUPDATE(request, id):
    obj = db_blog_table.objects.get(id=id)
    vid = db_blogfile_table.objects.filter(video=id,is_delete=0)
    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewaddblogupdate.html",{'coslogin':tb,'ob': obj, 'vid': vid})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewaddblogupdate.html",{'admin':tbb,'ob': obj, 'vid': vid})
    else:
        return redirect("else")
    
    


def VIEWADDBLOGUPDATEINSERT(request, id):
    
    if request.method == "POST":
        tb = db_blog_table.objects.get(id=id)

        tb.name = request.POST.get("name")

        photo = request.FILES.get("photo")
        if photo:
            fs = FileSystemStorage()
            filename = fs.save(photo.name, photo)
            uploaded_file_url = fs.url(filename)
            tb.photo = uploaded_file_url

        tb.description = request.POST.get("discription")
        videos = request.FILES.getlist("file[]")
        tb.save()

        for vid in videos:
            fs = FileSystemStorage()
            filename = fs.save(vid.name, vid)
            uploaded_file_url = fs.url(filename)

            pimage = db_blogfile_table(video=tb, video_name=uploaded_file_url)
            pimage.save()
        return redirect("/viewaddblog")


def VIEWADDBLOGDELETE(request, id):
    tb = db_blog_table.objects.get(id=id)
    tb.is_delete = 1
    tb.save()
    return redirect("/viewaddblog")


def VIEWADDBLOGFILE(request, id):
    obj = db_blogfile_table.objects.filter(video_id=id, is_delete=0)


    try:
        sid=request.session['sid']
        tb = db_coslogin.objects.get(id=sid)
        print("tryyyyyyy")

        return render(request, "viewaddblogfile.html",{'coslogin':tb,'ob': obj})
    except:
        aid=request.session['aid']
        tbb=db_coslogin.objects.get(id=aid)
        print("excepttttt")
        return render(request, "viewaddblogfile.html",{'admin':tbb,'ob': obj})
    else:
        return redirect("else")
    


def VIEWADDBLOGFILEDELETE(request, pageId, id):
    tb = db_blogfile_table.objects.get(id=id)
    tb.is_delete = 1
    tb.save()
    return redirect("/viewaddblogfile/" + str(pageId))








            # quantityy=request.GET["num"]
            # print(quantityy,"product quantity")
            # price=(var1.product_price)
            # print(price,"product price")
            # totall=int(price)*int(quantityy)
            # print(totall,"product total")




@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def cartordernew(request):
    if request.session.has_key('id'):
        ii=request.session['id']
        uid=db_custsignup.objects.get(id=ii)
        if request.method=='POST':
                quantityy=request.POST["num"]
                cartid=request.POST["id"]
                price=request.POST["price"]
        
        if db_cart.objects.all().filter(user_id=uid,quantity=quantityy,id=cartid,is_delete=0,status=0):
            obj=db_custsignup.objects.all().filter(id=ii)
                 
            obj1=db_cart.objects.all().filter(user_id=ii,is_delete=0)
            print(obj1,"obj11111111")
            sum1=0
            for i in obj1:
                a=i.total
                sum1=sum1+a

            return render(request, "cartordernew.html",{'ob':obj,'bb':obj1,'sum1' : sum1})
        else:
            ii=request.session['id']
            print(ii)
            uid=db_custsignup.objects.get(id=ii)
            var1=db_cart.objects.all()
            obj=db_custsignup.objects.all().filter(id=ii)
                     
            obj1=db_cart.objects.all().filter(user_id=ii,is_delete=0)

            sum1=0
            for i in obj1:
                a=i.total
                print(a,"aaaa")
                sum1=sum1+a
                print(sum1,"++++++sum1++++++++")
            if request.method=='POST':
                quantityy=request.POST["num"]
                print(quantityy,"qq")
                cartid=request.POST["id"]
                price=request.POST["price"]
                print(cartid,"cartid")
                k = db_cart.objects.filter(status=0,is_delete=0,id=cartid).update(quantity=quantityy)
                totall=float(price)*int(quantityy)
                print(totall,"totall")
                u = db_cart.objects.filter(status=0,is_delete=0,id=cartid,stage=0).update(total=totall)

                print(k,"quantity k")   
            
                
            return render(request, "cartordernew.html",{'ob':obj,'bb':obj1,'sum1' : sum1})
    else:
        return render(request,'custlogin.html')









#sham  #sham  #sham  #sham   #sham   #sham   #sham   #sham   #sham   #sham     #sham  #sham   #sham   #sham   #sham  #sham   #sham  #sham
