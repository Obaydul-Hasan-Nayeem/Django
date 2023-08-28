Django Mart
===========

Total Parts:
============
    - Design / Frontend
    - Logical / Backend
        - Logic
        - Database


Functionalities
================
    User
    ----
        - can create account
            (based on the first_name, last_name, email, password and the email will be sent to the given email, an gmail app must be set)

        - email varification
            (an gmail must be set)

        - can login

        - can add product to cart
            (working with cookies)

        - can give review
            (only authenticated user can review once)

        - can pay money to buy product
            (can pay through ssl commerze)


    Store
    -----
        - product categories
            (admin will add product from backend based on categories)

        - Product title and product price
            

        - filter product
            (user can filter products based on categories)

        - show review
            (unauthenticated users can only see reviews, authenticated users can see and update reviews)

        - searching products
            (in the search bar users can search a product)


Breaking down the project into smaller parts:
============================================

Frontend: (apps)
    - account
        - registration
        - login
        - logout
        - profile
        - pay
    
    - cart
        - item add
        - update

    - store
        - product details
        - search
        - filter
        - all item

    - order

    - category
