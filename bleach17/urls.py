"""bleach17 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from bleachapp17 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminindex/' ,views.ADMIN_INDEX),
    # path('subadminindex/' ,views.SUBADMIN_INDEX),

    path('sidemenu/', views.SIDEMENU),
    # path('subsidebar/', views.subsidebar),

    path('navbar/', views.NAVBAR),
    path('home/', views.home),
    path('fourhome/', views.fourhome),
    path('aboutusurl/', views.aboutus),
    path('blognewurl/', views.blognew),
    path('blogsingle/<int:id>', views.blogsingle),

    path('servicesnewurl/', views.servicesnew),
    path('servicesinglenewurl/', views.servicesinglenew),
    path('servicesinglenewurl1/', views.servicesinglenew1),
    path('servicesinglenewurl2/', views.servicesinglenew2),
    path('servicesinglenewurl3/', views.servicesinglenew3),
    path('servicesinglenewurl4/', views.servicesinglenew4),
    path('servicesinglenewurl5/', views.servicesinglenew5),
    path('servicesinglenewurl6/', views.servicesinglenew6),

    path('newproduct/<int:id>', views.newproduct),
    path('productsingle/<int:id>', views.productsingle),

    path('newcourse/', views.newcourse),
    path('viewjobsclt/', views.viewjobsclt),

    path('cartnew/', views.cartnew),
    path('paymentnew/', views.paymentnew),
    path('favurl/',views.fav),
    path('successnew/',views.successnew),
    path('videopage/<int:id>',views.videopage),
    path('cart_payment/',views.cart_payment),

    path('courselist/<int:id>',views.courselist),

    path('searchcourse/',views.searchcourse),
    




    path('coursemodule/', views.coursemodule),
    

    path('module/',views.module),
    









    path('wishlistproductlist/',views.wishlistproductlist),



    path('custlogin/',views.CUSTLOGIN),
    path('login/', views.LOGIN),
    path('login1/', views.LOGIN1),
    # path('loginsub/', views.loginsub),
    # path('login11/', views.LOGIN11),



    path('myprofile/', views.myprofile),
    




    path('logout/', views.ADMIN_LOGOUT),
    path('sublogout/', views.SUBADMIN_LOGOUT),
    path('userlogout/', views.userlogout),
    path('orderreporturl/', views.orderreport),
    path('paymentreporturl/', views.paymentreport),
    path('cancelreporturl/', views.cancelreport),


    path('dateurl/', views.date),
    path('paymentdateurl/', views.paymentdate),
    path('canceldateurl/', views.canceldate),
    path('productdateurl/', views.productdate),
    path('coursedateurl/', views.coursedate),
    path('productreporturl/', views.productreport),
    path('coursereporturl/', views.coursereport),




    path('pdf_view/', views.ViewPDF.as_view(),name="pdf_view"),
    path('pdf_viewp/', views.ViewpPDF.as_view(),name="pdf_viewp"),
    path('pdf_viewc/', views.ViewcPDF.as_view(),name="pdf_viewc"),
    path('pdf_viewo/', views.ViewoPDF.as_view(),name="pdf_viewo"),

    path('pdf_viewi/', views.ViewiPDF.as_view(),name="pdf_viewi"),


    path('pdf_download/', views.DownloadPDF.as_view(),name="pdf_download"),
    path('pdf_downloadp/', views.DownloadpPDF.as_view(),name="pdf_downloadp"),
    path('pdf_downloadc/', views.DownloadcPDF.as_view(),name="pdf_downloadc"),




   path('sample/<int:id>',views.sample),





    path('addprodect/', views.ADD_PRODECT),
    path('fazalinsert/', views.INSER_PRODECT),
    path('viewprodect/', views.VIEW_PRODECT),




    path('updatedata/<int:id>', views.UPDATEDATA),
    path('productupdateinsert/<int:id>', views.PRODUCTUPDATEINSERT),
    path('producttabledelete/<int:id>', views.PRODUCTTABLEDELETE),








    path('viewimages/<int:id>', views.VIEW_IMAGES),
    path('imagedelete/<str:pageId>/<int:id>', views.IMAGEDELETE),
    path('imageupdatedata/<str:pageId>/<int:id>', views.IMAGEUPDATEDATA),
    path('imageupdateinsert/<str:pageId>/<int:id>', views.IMAGEUPDATEINSERT),




    path('cartorder/', views.cartorder),
    path('cartlist/', views.cartlist),
    path('checkouturl/', views.checkout),
    path('paymenturl/', views.payment),#
    path('cancelurl/', views.cancel),
    path('terms/', views.terms),











    path('addaccount/', views.ADD_ACCOUNT),
    path('insertaccountadmin/', views.admininsertacnt),
    path('viewaccount/', views.view_ACCOUNT),
    path('updateaccount/<int:id>', views.UPDATEACCOUNT),
    path('accountupdateinsert/<int:id>', views.ACCOUNTUPDATEINSERT),
    path('accountdelete/<int:id>', views.ACCOUNTDELETE),



    path('addcategory/', views.ADD_CATEGORY),
    path('addactegoryindatabase/', views.ADD_CATEGORY_in_DATABASE),
    path('viewcategory/', views.VIEW_CATEGORY),
    path('updatecategory/<int:id>', views.UPDATECATEGORY),
    path('addaddressurl/', views.addaddress),
    path('editaddaddressurl/', views.editaddaddress),
    path('inserteditaddaddress/', views.inserteditaddaddress),

    path('insertaddaddressurl/', views.insertaddaddress),
    path('viewcartorderurl/<int:id>', views.viewcartorder),

    path('categoryupdateinsert/<int:id>', views.CATEGORYUPDATEINSERT),
    path('cayegorydelete/<int:id>', views.CATEGORYDELETE),

    

    

    
    










    







    path('viewstatus/<int:id>', views.viewstatus),
    path('statusupdate/<int:id>', views.statusupdate),
    path('orderitems/<int:id>', views.orderitems),
    path('buyedcourse/', views.buyedcourse),



    



    path('vieworder/', views.VIEW_ORDER),
    path('vieworderc/', views.VIEW_ORDERC),

    path('orderitemdelete/<int:id>', views.ORDERITEMDELETE),
    path('orderstatusurl/<int:id>', views.orderstatus),
    path('orderupdateinsert/', views.orderupdateinsert),


    path('viewallorder/', views.VIEWALLORDER),
    path('viewallorderc/', views.VIEWALLORDERC),




    path('viewbill/', views.VIEW_BILL),





    path('viewcustomer/', views.VIEWCUSTOMER),

    path('addgovernerte/', views.ADDGOVERNERTE),
    path('viewgovernerte/', views.VIEWGOVERNERTE),
    path("governertedelete/<int:id>", views.DELETEGOVERNERTE),
    path("updategevernorate/<int:id>", views.UPDATEGOVERNERTE),
    path('governerateupdateinsert/<int:id>', views.GOVERNORATEUPDATINSERT),



    path('getareabyId/', views.GETAREABYiD,  name="ajax_load_area"),

    path('addarea/', views.ADDAREA),
    path('viewarea/', views.VIEWAREA),
    path("areadelete/<int:id>", views.DELETEAREA),
    path("updatearea/<int:id>", views.UPDATEAREA),
    path('areaupdateinsert/<int:id>', views.AREAUPDATINSERT),




    path('custviewaddserviceurl/', views.custviewaddservice),







    path('viewservice/', views.VIEWSERVICE),
    path('viewcustserviceurl/', views.viewcustservice),

    path('servicedelete/<int:id>', views.SERVICEDELETE),


    path('insertadminpageform/', views.INSERADMINPAGEFORM),
    path('insertadminpageform2/', views.INSERADMINPAGEFORM2),





   path('applyjob/', views.applyjob),
   path('appliedjob/', views.appliedjob),



    path('cltserviceform/', views.CLTSERVICEFORM),
    path('insertservicepage/', views.INSERTSERVICEPAGE),

    path('cltcareers/', views.CLTCAREERS),
    path('custcltcareersurl/', views.custcltcareers),

    path('careersformmm/', views.CAREERSFORMMM),
    path('custcareersformurl/', views.custcareersform),
    path('viewcareers/', views.VIEWCAREERS),
    path("careersformdelete/<int:id>", views.CAREERSFORMDELETE),





    path('addjob/', views.ADDJOB),
    path('viewjobs/', views.VIEWJOBS),
    path("jobdelete/<int:id>", views.JOBDELETE),
    path("updatejob/<int:id>", views.UPDATEJOB),
    path('jobupdateinsert/<int:id>', views.JOBUPDATINSERT),
    path('addinsertjob/', views.ADDINSERTJOB),




    path('', views.index),

    path('services/', views.SERVICES),
    # path('blog/', views.BLOG),
    path('help/', views.HELP),

    path('shopnow/', views.SHOPNOW),
    # path('cart/', views.CART),
    # path('addtocarturl/',views.addtocart),
    path('addtocarturl/',views.addtocart),
    path('buycourseurl/',views.buycourse),
    path('buyproducturl/',views.buyproduct),
    path('deletecarturl/<int:id>',views.deletecart),
    path('deletecartnew/<int:id>',views.deletecartnew),


    path('wishlist/', views.WISH_LIST),
    path('wishlistproductdelete/<int:id>', views.wishlistproductdelete),
    path('wishlistproducturl/', views.wishlistproduct),

    path('addtocartproducturl/', views.addtocartproduct),

    path('trendingproducts/', views.TRENDINGPRODUCTS),

    path('customerregform/', views.CUSTOMERREGFORM),
    path('custreginsert/', views.CUSTERREGINSERT),



    path('CUSTOMMER/', views.CUSTOMMER),  #custemor demo page



    path('viewcustomer/', views.VIEWCUSTOMER),
    path("Customerformdelete/<int:id>", views.CUSTOMERFORMDELETE),











     path('coursesingle/<int:id>', views.coursesingle),
     path('search/', views.search),


     path('invoice/', views.invoice, name='invoice'),

    




     



    path('submitted/',views.submitted),
    path('addmodule/',views.addmodule),
    
    path('viewaddmodules/',views.viewaddmodules),
    path('viewaddmoduleupdate/<int:id>',views.viewaddmoduleupdate),
    path('viewaddmoduleupdateinsert/<int:id>',views.viewaddmoduleupdateinsert),
    path('viewaddmodulevideos/<int:id>',views.viewaddmodulevideos),

    path('orderitemdeleteclt/<int:id>',views.orderitemdeleteclt),
    



    



    path('addcourse/',views.ADDCOURSE),
    path('courseinsert/', views.COURSEINSERT),
    path('viewaddcourses/', views.VIEWADDCOURSES),
    path('viewaddcoursesupdate/<int:id>', views.VIEWADDCOURSESUPDATE),
    path('viewaddcoursesupdateinsert/<int:id>', views.VIEWADDCOURSESUPDATEINSERT),
    path('viewaddcoursesdelete/<int:id>', views.VIEWADDCOURSESDELETE),
    path('viewaddcoursesvideos/<int:id>', views.VIEWADDCOURSESVIDEOS),
    path('viewaddcoursesvideosdelete/<int:pageId>/<int:id>', views.VIEWADDCOURSESVIDEOSDELETE),
    path('viewaddcoursescart/<int:id>', views.VIEWADDCOURSESCART),

    path('coursecategory/', views.COURSECATEGORY),
    path('coursecategoryinsert/', views.COURSECATEGORYINSERT),
    path('viewcoursecategory/', views.VIEWCOURSECATEGORY),
    path('viewcoursecategoryupdate/<int:id>', views.VIEWCOURSECATEGORYUPDATE),
    path('viewcoursecategoryupdateinsert/<int:id>', views.VIEWCOURSECATEGORYUPDATEINSERT),
    path('viewcoursecategorydelete/<int:id>', views.COURSECATEGORYDELETE),


















    path('addservices/', views.ADDSERVICES),
    path('serviceinsert/', views.SERVICEINSERT),
    path('viewaddservice/', views.VIEWADDSERVICE),
    path('viewaddservicesupdate/<int:id>', views.VIEWADDSERVICESUPDATE),
    path('viewaddservicesupdateinsert/<int:id>', views.VIEWADDSERVICESUPDATEINSERT),
    path('viewaddservicesdelete/<int:id>', views.VIEWADDSERVICESDELETE),



    path('viewcustserviceupdate/<int:id>', views.viewcustserviceupdate),
    path('viewcustserviceupdateinsert/<int:id>', views.viewcustserviceupdateinsert),


    path('offlinetraining/', views.OFFLINETRAINING),
    path('offlinetraininginsert/', views.OFFLINETRAININGINSERT),
    path('viewofflinetraining/', views.VIEWOFFLINETRAINING),
    path('viewofflinetrainingdelete/<int:id>', views.VIEWOFFLINETRAININGDELETE),
    path('viewofflineupdateinserturl/<int:id>', views.VIEWOFFLINEUPDATEINSERT),
    path('viewofflineupdate/<int:id>', views.VIEWOFFLINEUPDATE),

    path('governerate/', views.GOVERNERATE),
    path('governerateinsert/', views.GOVERNERATEINSERT),
    path('viewgovernerate/', views.VIEWGOVERNERATE),
    path('viewgovernerateupdate/<int:id>', views.VIEWGOVERNERATEUPDATE),
    path('viewgovernerateupdateinsert/<int:id>', views.VIEWGOVERNERATEUPDATEINSERT),
    path('viewgoverneratedelete/<int:id>', views.COURSEGOVERNERATEDELETE),

    path('getareabyId/', views.GETAREABYiD, name="ajax_load_area"),

    path('area/', views.AREA),
    path('areainsert/', views.AREAINSERT),
    path('viewarea/', views.VIEWAREA),
    path('viewareaupdate/<int:id>', views.VIEWAREAUPDATE),
    path('viewareaupdateinsert/<int:id>', views.VIEWAREAUPDATEINSERT),
    path('viewareadelete/<int:id>', views.VIEWAREADELETE),



    path('product/',views.VIEWPRODUCT),
    path('megaproduct/',views.megaproduct),

    path('viewproduct/', views.VIEWPRODUCT),
    path('viewcustimages/<int:id>', views.VIEW_CUSTIMAGES),



    path('okurl/',views.ok),


    path('checkboxsuburl/',views.checkboxsub),
   



    path('course/',views.VIEWCOURSE),
    path('viewcourse/', views.VIEWCOURSE),
    path('custcoursevideos/<int:id>',views.CUSTCOURSEVIDEOS),



    path('blog/',views.BLOG),
    path('addblog/',views.ADDBLOG),
    path('bloginsert/', views.BLOGINSERT),
    path('viewaddblog/', views.VIEWADDBLOG),
    path('viewaddblogupdate/<int:id>', views.VIEWADDBLOGUPDATE),
    path('viewaddblogupdateinsert/<int:id>', views.VIEWADDBLOGUPDATEINSERT),
    path('viewaddblogdelete/<int:id>', views.VIEWADDBLOGDELETE),
    path('viewaddblogfile/<int:id>', views.VIEWADDBLOGFILE),
    path('viewaddblogfiledelete/<int:pageId>/<int:id>', views.VIEWADDBLOGFILEDELETE),
    path('custblogvideos/<int:id>',views.CUSTBLOGVIDEOS),


    path('cartordernew/',views.cartordernew),
    path('viewjobnew/',views.viewjobnew),


    








#sham  #sham  #sham  #sham   #sham   #sham   #sham   #sham   #sham   #sham     #sham  #sham   #sham   #sham   #sham  #sham   #sham  #sham

]
if settings.DEBUG:
   urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)