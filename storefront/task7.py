# You run cmd and run the command below to start off
# source>python manage.py shell

# from playground.models import Product

# using our table:
# class Product(models.Model):
#    name = models.CharField(max_length=1000)
#    price = models.CharField(max_length=1000000)

# 1) to insert a new record into product model
# product(name="vitamin_c", price="#10")
# i) Assign a variable i.e;
# x = Product(name="vitamin_c", price="#10")
# Then save using;
# x.save()

# 2) Get all the records in the product table, run the command;
# Product.object.all()
# It should return a list in form of query set.
# QuerySet [<Product: x (1)>]

# 3) Filter products by their name:
# Product.object.filter(name="vitamin_c")
# It should also create a query list

# 4) Get a single record from the product table;
# Product.objects.filter(name="vitamin_c").last()

# 5) Change product price;
# assign a variable;
# x = Product.objects.filter(name="vitamin_c").filter(price="#10").last()
# To confirm we have chosen the right record;
# x.price
# It should return;
# "#10"
# to change price;
# x.price = "#20"
# save it;
# x.save()

