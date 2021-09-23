$(document).on('click','.add-cart',function(e){
               
                e.preventDefault();
                
                $.ajax({
                    type:'POST',
                    url: '{% url "basket:basket_add" %}',
                    data:{
                        productid:$(this).attr('value'),
                        csrfmiddlewaretoken: "{{csrf_token}}",
                        action:'post'
                    
                },
                success:function(json){
                    $("#checkout_items").text(json.test)
                    
                },
                error: function(xhr,errmsg,err){}
            });  
                             
            })