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
                self.basket[product_id]={'qty':int(1)}
            else:
                qty=self.basket.get(str(product_id))
                qty=qty.get('qty')
                qty+=1 
                self.basket.update({str(product_id):{'qty':int(qty)}})
                print(self.basket)   
        
        
        self.session.modified=True  

    def reduce(self,product):
        product_id=product.id
        qty=self.basket.get(str(product_id))
        qty=qty.get('qty')
        qty-=1 
        self.basket.update({str(product_id):{'qty':int(qty)}})
        print(self.basket)