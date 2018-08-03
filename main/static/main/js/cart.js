$(document).ready(function(){

    // add cart in products' page
    var productForm = $(".form-product-ajax")
    productForm.submit(function(event){
        event.preventDefault();
        var thisForm = $(this)
        var actionEndpoint = thisForm.attr("action"); // /cart/update/
        var httpMethod = thisForm.attr('method'); // post
        var formData = thisForm.serialize();

        $.ajax({
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function(data){
                var navbarCount = $('.navbar-cart-count');
                navbarCount.text(data.cartItemCount);
                alert("商品已加入購物車");
            },
            error: function(errorData){
                console.log('error')
            }
        })
    })


    // ezShip api
    var orderForm = $(".ship-ajax")
    orderForm.submit(function(event){
        event.preventDefault();
        var thisForm = $(this)
        var actionEndpoint = thisForm.attr("action");
        var httpMethod = thisForm.attr('method');
        var formData = thisForm.serialize();

        $.ajax({
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function(data){
                console.log('success')
            },
            error: function(errorData){
                console.log('error')
            }
        })
    })


    // change cart quantity input
    var input = $("input.input-ajax")
    input.on("input", function(event){
        var actionEndpoint = $(this).attr("data-href");
        var inputData = event.delegateTarget.value;
        var cartId = '#' + $(this).attr("name");
        var cartTotalEle = $(cartId);
        $.ajax({
            url: actionEndpoint,
            method: 'POST',
            data: {'quantity': inputData},
            success: function(data){
                var navbarCount = $('.navbar-cart-count');
                navbarCount.text(data.cartItemCount);
                cartTotalEle.text(data.cartTotal);
            },
            error: function(errorData){
                console.log('error')
            }
        })
    });


    // delete cart button
    var btn = $("input.btn-outline-danger")
    btn.on('click', function(){
        var actionEndpoint = $(this).attr("data-href");
        var cartId = '.' + $(this).attr("name");

        $.ajax({
            url: actionEndpoint,
            method: 'POST',
            success: function(data){
                var navbarCount = $('.navbar-cart-count');
                navbarCount.text(data.cartItemCount);
                $(cartId).remove();
            },
            error: function(errorData){
                console.log('error')
            }
        })
    });
 })
