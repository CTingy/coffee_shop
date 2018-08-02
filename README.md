# coffee_shop
## Intoduction

Deploy on Heroku.

Url: https://a-hui-coffee.herokuapp.com/

It is a E-commerce website built with Django.
The website sales many kinds of roast coffee beans and 
you can shop on this website and comment the products.

## Functions
(send_email function has been banned by Google security)

* Only for admin
  * Create, update, delete products on the product pages.
  * Create, update, delete news on the board page.
  * Receive notifications through email when user send "contact us". 

* Only for authenticated users
  * View user's profile.
  * View and delete orders.
  * Create, delete comments on product pages.
  * User Login and Logout
  * Make orders
  * Send email to users when they get their orders' checking process done.
  * Choose product receiving convenience stores with 'ezShip map API' in the order checking process.

* For guests
  * Add, update, delete products to the cart.
  * Search products with some keywords.
  * Send some questions to us with 'Contact us'.
  * User register
  * View the cart content

## Buid with
* Bootstrap 4
* Django 2.0
* Python 3.6
* HTML 5
* CSS 3
* Ajax
* jQuery
