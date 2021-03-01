from django.db import models


# Create your models here.






class db_category(models.Model):

    id = models.AutoField(primary_key=True)


    product_category = models.CharField(max_length=100)

    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)
    image=models.FileField(upload_to="files")
    

    class Meta:
        db_table = "db_category"




class db_add_product(models.Model):
    # userid=models.ForeignKey(signuptable,on_delete=models.CASCADE,default="",null=True)
    

    id=models.AutoField(primary_key=True)

    id=models.AutoField(primary_key=True)

    


    product_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=30)
    product_price = models.FloatField() 

    image=models.FileField(upload_to="files")
    

    discription = models.CharField(max_length=5000)
    offer = models.IntegerField()
    status = models.BooleanField(default=False,blank=True)
    is_delete = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    is_trending = models.IntegerField(default=0)
    cart_status = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    org_price = models.FloatField() 
    category_id=models.IntegerField()





    



    class Meta:
        db_table = "db_add_product"


class ProductImages(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(db_add_product,on_delete=models.CASCADE)
    images=models.FileField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)

    class Meta:
        db_table = "ProductImages"



class db_coslogin(models.Model):
    id = models.AutoField(primary_key=True)


    name = models.CharField(max_length=100)
    
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    type1 = models.CharField(max_length=50)
    # last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)
    ecom = models.IntegerField(default=0)
    service = models.IntegerField(default=0)
    career = models.IntegerField(default=0)
    cource = models.IntegerField(default=0)
    offline = models.IntegerField(default=0)
    blog = models.IntegerField(default=0)
    status = models.IntegerField(default=0)


    

    class Meta:
        db_table = "db_coslogin"



class db_create_account(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)

    class Meta:
        db_table = "db_create_account"













class db_admin_service_form(models.Model):
    id = models.AutoField(primary_key=True)

    governerate = models.CharField(max_length=500)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)
    status = models.CharField(max_length=500)

    class Meta:
        db_table = "db_admin_service_form"

class db_admin_service_form2(models.Model):

    id = models.AutoField(primary_key=True)
    governerate_id = models.ForeignKey(db_admin_service_form, on_delete=models.CASCADE)

    Area = models.CharField(max_length=500)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)
    status = models.CharField(max_length=500)
    class Meta:
        db_table = "db_admin_service_form2"





class db_careers_job(models.Model):

    jobs = models.CharField(max_length=500)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)
    status = models.CharField(max_length=500)
    governerate_id = models.ForeignKey(db_admin_service_form, on_delete=models.CASCADE)
    

    class Meta:
        db_table = "db_careers_job"


class db_customer(models.Model):
    id = models.AutoField(primary_key=True)

    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=100)

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)
    status = models.CharField(max_length=500)

    class Meta:
        db_table = "db_customer"





# class db_order(models.Model):
#     id = models.AutoField(primary_key=True)

#     id = models.AutoField(primary_key=True)
#     category_id = models.ForeignKey(db_category, on_delete=models.CASCADE)

#     id = models.AutoField(primary_key=True)
#     customer_id = models.ForeignKey(db_customer, on_delete=models.CASCADE)
#     grand_tottal = models.IntegerField()
#     pending_status = models.IntegerField()
#     order_at = models.IntegerField()

#     last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#     is_delete = models.IntegerField(default=0)
#     status = models.CharField(max_length=500)


#     class Meta:
#         db_table = "db_order"     









# class db_order_item(models.Model):

#     id = models.AutoField(primary_key=True)
#     order_id = models.ForeignKey(db_order, on_delete=models.CASCADE)

#     id = models.AutoField(primary_key=True)
#     coslogin_id = models.ForeignKey(db_coslogin, on_delete=models.CASCADE)

#     id = models.AutoField(primary_key=True)
#     customer_id = models.ForeignKey(db_customer, on_delete=models.CASCADE)

#     id = models.AutoField(primary_key=True)
#     product_id = models.ForeignKey(db_add_product, on_delete=models.CASCADE)



#     quantity = models.IntegerField()
#     price = models.IntegerField()
#     order_at = models.IntegerField()

#     last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#     is_delete = models.IntegerField(default=0)
#     status = models.CharField(max_length=500)

#     class Meta:
#         db_table = "db_order_item"



class db_custsignup(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)


    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type1 = models.CharField(max_length=50)
    zipcode=models.CharField(max_length=20,default='')


    Phone_number = models.IntegerField()
    Nationality = models.CharField(max_length=30)
    Apartment = models.CharField(max_length=100)
    Floor = models.CharField(max_length=100)
    Building = models.CharField(max_length=100)
    Block = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    Avenue = models.CharField(max_length=100)
    Governerate = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)

    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)
    status = models.CharField(max_length=500)
    
    class Meta:
        db_table = "db_custsignup"


#shammas   #shammas   #shammas   #shammas   #shammas   #shammas   #shammas   #shammas   #shammas    #shammas    #shammas   #shammas   #shammas


class db_addcourse_table(models.Model):
    # userid=models.ForeignKey(db_custsignup,on_delete=models.CASCADE,default="",null=True)
    

    

    category_id = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    course_price = models.CharField(max_length=100)
    status = models.BooleanField(default=False,blank=True)
    videos = models.CharField(max_length=1000)
    # cart = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.IntegerField(default=0)
    cart_status = models.IntegerField(default=0)
    level = models.CharField(max_length=100)
    review = models.CharField(max_length=5000)
    
    




    class Meta:
        db_table = "db_addcourse_table"










class db_coursecategory_table(models.Model):
    category_name = models.CharField(max_length=50)
    is_delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "db_coursecategory_table"


class db_addcoursevideo_table(models.Model):
    # video_id = models.IntegerField()
    video = models.ForeignKey(db_addcourse_table, default=None, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_delete = models.IntegerField(default=0)

    class Meta:
        db_table = "db_addcoursevideo_table"



class db_coursemodules(models.Model):
    level = models.CharField(max_length=100)
    module = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    course_id = models.ForeignKey(db_addcourse_table, default=None, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=500)


    class Meta:
        db_table = "db_coursemodules"





class db_addservice_table(models.Model):

    service_name = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    service_price = models.CharField(max_length=100)
    # status = models.BooleanField()
    # cart = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_delete = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    query = models.CharField(max_length=100)
    notes = models.CharField(max_length=5000)
    feature1 = models.CharField(max_length=100)
    feature2 = models.CharField(max_length=100)
    feature3 = models.CharField(max_length=100)
    feature4= models.CharField(max_length=100)



    class Meta:
        db_table = "db_addservice_table"

class db_servicevideo(models.Model):
    video = models.ForeignKey(db_addservice_table, default=None, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_delete = models.IntegerField(default=0)


    class Meta:
        db_table = "db_servicevideo"





class db_service_form(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    phone_number = models.IntegerField()
    preferred_communication = models.CharField(max_length=100)
    nationality = models.CharField(max_length=500)
    customer_type = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=500)
    civil_id = models.IntegerField()
    other_mobile = models.IntegerField()
    message_language = models.CharField(max_length=500)
    apartment = models.CharField(max_length=500)
    floor = models.CharField(max_length=500)
    building = models.CharField(max_length=500)
    street = models.CharField(max_length=500)
    avenue = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    evaluationtimeslot = models.CharField(max_length=500)


    governerate = models.CharField(max_length=500)
    Area = models.CharField(max_length=500)
    date = models.CharField(max_length=500)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)
    service_id = models.ForeignKey(db_addservice_table, on_delete=models.CASCADE)

    class Meta:
        db_table = "db_service_form"








class db_serviceimage(models.Model):
    service_id = models.ForeignKey(db_addservice_table, default=None, on_delete=models.CASCADE)
    images = models.CharField(max_length=500)

    class Meta:
        db_table = "db_serviceimage"
     


class db_offlinetraining_table(models.Model):

    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Email = models.CharField(max_length=1000)
    Phone_number = models.IntegerField()
    Nationality = models.CharField(max_length=30)
    Customer_Type = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    Job_Title = models.CharField(max_length=100)
    Civil_ID = models.IntegerField()
    Other_Mobile = models.IntegerField()

    Apartment = models.CharField(max_length=100)
    Floor = models.CharField(max_length=100)
    Building = models.CharField(max_length=100)
    Block = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    Avenue = models.CharField(max_length=100)
    Governerate = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)

    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    is_delete = models.IntegerField(default=0)

    class Meta:
        db_table = "db_offlinetraining_table"


class db_Governerate_table(models.Model):
    Governerate_name = models.CharField(max_length=50)
    is_delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "db_Governerate_table"




class db_Area_table(models.Model):
    id = models.AutoField(primary_key=True)
    governerate_id = models.ForeignKey(db_Governerate_table, on_delete=models.CASCADE)
    Area_name = models.CharField(max_length=50)
    is_delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "db_Area_table"

class db_blog_table(models.Model):
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    description1 = models.CharField(max_length=5000)
    description2 = models.CharField(max_length=5000)
    videos = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.IntegerField(default=0)
    category = models.CharField(max_length=100)


class Meta:
        db_table = "db_blog_table"

class db_blogfile_table(models.Model):
    video = models.ForeignKey(db_blog_table, default=None, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_delete = models.IntegerField(default=0)

    class Meta:
        db_table = "db_blogfile_table"









# class db_carttt(models.Model):
#     user_id = models.ForeignKey(db_custsignup, default=None, on_delete=models.CASCADE)
#     course_id = models.ForeignKey(db_addcourse_table, default=None, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     total = models.CharField(max_length=500)
#     is_delete = models.IntegerField(default=0)
#     total = models.IntegerField(default=0)



    # product_id = models.ForeignKey(db_add_product, default=None, on_delete=models.CASCADE)


    #employerid=models.ForeignKey(employersign_uptable,on_delete=models.CASCADE,default="",null=True)


    # class Meta:
    #     db_table = "db_carttt"


class db_cart(models.Model):
    user_id = models.ForeignKey(db_custsignup, default=None, on_delete=models.CASCADE,blank=True,null=True)
    # cart_item = models.CharField(max_length=100)
    status = models.BooleanField(default=False,blank=True)
    quantity = models.IntegerField(blank=True,null=True)

    total = models.FloatField() 
    is_delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stage = models.IntegerField(default=0)
    item_id = models.IntegerField(default=0)
    course_id = models.ForeignKey(db_addcourse_table, default=None, on_delete=models.CASCADE,blank=True,null=True)
    product_id = models.ForeignKey(db_add_product, default=None, on_delete=models.CASCADE,blank=True,null=True)


    
    
    class Meta:
        db_table = "db_cart"


# class db_placeorder(models.Model):
#     user_id = models.ForeignKey(db_custsignup, default=None, on_delete=models.CASCADE,blank=True,null=True)
#     # cart_item = models.CharField(max_length=100)
#     status = models.BooleanField(default=False,blank=True)
#     product_id = models.ForeignKey(db_add_product, default=None, on_delete=models.CASCADE,blank=True,null=True)
#     course_id = models.ForeignKey(db_addcourse_table, default=None, on_delete=models.CASCADE,blank=True,null=True)

#     total = models.IntegerField(default=0)
#     last_updated = models.DateTimeField(auto_now_add=False,auto_now=True)
#     timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    
    


    # class Meta:
    #     db_table = "db_placeorder"



class db_courseorder(models.Model):
    id = models.AutoField(primary_key=True)

    user_id = models.ForeignKey(db_custsignup, default=None, on_delete=models.CASCADE,blank=True,null=True)
    status = models.BooleanField(default=False,blank=True)
    
    course_id = models.ForeignKey(db_addcourse_table, default=None, on_delete=models.CASCADE,blank=True,null=True)

    total = models.FloatField() 
    last_updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)

    stage = models.CharField(max_length=30,default='')


    
    


    class Meta:
        db_table = "db_courseorder"


class db_productorder(models.Model):
    user_id = models.ForeignKey(db_custsignup, default=None, on_delete=models.CASCADE,blank=True,null=True)
    status = models.BooleanField(default=False,blank=True)
    
    product_id = models.ForeignKey(db_add_product, default=None, on_delete=models.CASCADE,blank=True,null=True)
    total = models.FloatField() 
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    is_delete = models.IntegerField(default=0)
    stage = models.CharField(max_length=30,default='')


    
    
    


    class Meta:
        db_table = "db_productorder"







class db_cartproduct(models.Model):
    user_id = models.ForeignKey(db_custsignup, default=None, on_delete=models.CASCADE)
    product_id = models.ForeignKey(db_add_product, default=None, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.IntegerField(default=0)

    # product_id = models.ForeignKey(db_add_product, default=None, on_delete=models.CASCADE)
    




    class Meta:
        db_table = "db_cartproduct"




class db_wishlist(models.Model):
    userid = models.ForeignKey(db_custsignup, default=None, on_delete=models.CASCADE)
    courseid = models.ForeignKey(db_addcourse_table, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.IntegerField(default=0)


    class Meta:
        db_table = "db_wishlist"



class db_wishlistproduct(models.Model):
    userid = models.ForeignKey(db_custsignup, default=None, on_delete=models.CASCADE)
    course_id = models.ForeignKey(db_addcourse_table, default=None, on_delete=models.CASCADE,blank=True,null=True)
    product_id = models.ForeignKey(db_add_product, default=None, on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.IntegerField(default=0)

    class Meta:
        db_table = "db_wishlistproduct"


class db_addjob(models.Model):
    company=models.CharField(max_length=30,default='')
    jobtitle=models.CharField(max_length=50,default='')
    description=models.CharField(max_length=5000,default='')
    jobtype=models.CharField(max_length=30,default='')
    is_delete = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    # timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

    class Meta:
        db_table = "db_addjob"



 
class db_careers(models.Model):

    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    about_your_self = models.CharField(max_length=500)
    jobs = models.CharField(max_length=500)

    notesfile = models.FileField(null=True)

    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)
    status = models.CharField(max_length=500)
    job_id=models.ForeignKey(db_addjob, default=None, on_delete=models.CASCADE)
    user_id=models.ForeignKey(db_custsignup, default=None, on_delete=models.CASCADE)



    class Meta:
        db_table = "db_careers"



class db_addaddresstable(models.Model):
    
    FirstName = models.CharField(max_length=500)
    LastName = models.CharField(max_length=500)
    Email = models.CharField(max_length=500)
    phone = models.IntegerField()
    
    Nationality = models.CharField(max_length=500)
    Address = models.CharField(max_length=500)
    Governerate = models.CharField(max_length=500)
    Zipcode = models.CharField(max_length=500)
    Area = models.CharField(max_length=500)
    user_id=models.ForeignKey(db_custsignup, on_delete=models.CASCADE)
    class Meta:
        db_table = "db_addaddresstable"


class db_orderr(models.Model):
    user_id=models.ForeignKey(db_custsignup, on_delete=models.CASCADE)
    total = models.CharField(max_length=500)
    stage = models.CharField(max_length=30,default='')
    
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)
    address = models.ForeignKey(db_addaddresstable, default=None, on_delete=models.CASCADE,blank=True,null=True)
    status = models.CharField(max_length=30,default='')
    

    
    # is_delete = models.IntegerField(default=0)


    class Meta:
        db_table = "db_orderr" 


class db_orderritem(models.Model):
    user_id=models.ForeignKey(db_custsignup, on_delete=models.CASCADE)
    order_id=models.ForeignKey(db_orderr, on_delete=models.CASCADE)
    item_order=models.IntegerField(default=0)
    
    quantity = models.IntegerField(blank=True,null=True)
    total = models.CharField(max_length=500)
    stage = models.CharField(max_length=30,default='')
    
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_delete = models.IntegerField(default=0)
    course_id = models.ForeignKey(db_addcourse_table, default=None, on_delete=models.CASCADE,blank=True,null=True)
    product_id = models.ForeignKey(db_add_product, default=None, on_delete=models.CASCADE,blank=True,null=True)
    status = models.CharField(max_length=30,default='')

    
    # is_delete = models.IntegerField(default=0)


    class Meta:
        db_table = "db_orderritem" 




class db_orderstatus(models.Model):
    order_id=models.ForeignKey(db_orderr, on_delete=models.CASCADE)
    status = models.CharField(max_length=500)
    
    
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    # is_delete = models.IntegerField(default=0)


    class Meta:
        db_table = "db_orderstatus"




    # user_id = models.ForeignKey(db_custsignup, on_delete=models.CASCADE)


    


   
# id = models.AutoField(primary_key=True)
#     course_id = models.ForeignKey(db_addcourse_table, on_delete=models.CASCADE)#









