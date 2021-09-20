from base.models import Product
from decimal import Decimal
class Basket():
    def __init__(self,request):
        self.session=request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket=self.session['skey']={}
        self.basket=basket    
    def add(self,product):
        product_id=product.id
        if product_id not in self.basket:
            if self.basket.get(str(product_id)) is None:
                self.basket[product_id]={'price':str(product.product_price),'qty':int(1)}
            else:
                qty=self.basket.get(str(product_id))
                qty=qty.get('qty')
                qty=qty+1 
                #self.basket[product_id]={'price':str(product.product_price),'qty':int(qty)}
                self.basket.update({str(product_id):{'price':str(product.product_price),'qty':int(qty)}})
                print(self.basket)   
        
        
        self.session.modified=True 
    """
    To get the total number of items in the basket
    """     
    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())
    """
    Function to itterate over the class
    """    
    def get_total_price(self):
        return sum(int(item['price'])*int(item['qty']) for item in self.basket.values())
    def __iter__(self):
        product_ids=self.basket.keys()
        products=Product.objects.all().filter(id__in=product_ids)
        basket=self.basket.copy()
        for product in products:
            basket[str(product.id)]['product']=product

        for item in basket.values():
            item['price']=Decimal(item['price'])
            item['total_price']=item['price']*item['qty']
            yield item    


    #funtion to reduce item quantity from the cart  
    def reduce(self,product):
        product_id=product.id
        qty=self.basket.get(str(product_id))
        qty=qty.get('qty')
        qty-=1 
        self.basket.update({str(product_id):{'qty':int(qty)}})
        print(self.basket)