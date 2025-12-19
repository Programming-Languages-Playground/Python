
## DataTypes Python
    - Types of data
    - How to manipulate data
    - Mutability - Non Mutability

    Object and Mutability
       
       - Everything is object in python

        Object 
            - identity
            - type
            - value

        - Mutable   -> changeable
        - Immutalbe -> NOT changeable

        We look for mutability through identity and not value.

        sugar_amount = 2
        sugar_amouunt = 12

        We change the `reference` -> we are not changing the actual value (unlike other programming languages)


    Numbers # Immutable
        - Integers
            Integer division (//)
            Exponent (**)

        - Boolean
            0 and None -> False
            Everything else -> True


        - Real (Floating -> Decimal)
        - Complex Number (2 + 3j)


    Strings # Immutable
        core
        

        indexing, slicing, encoding and decoding

            sring_name[startingIdx:endingIdx]
            sring_name[::-1] # Reverse a string
        
            string_name.ecode("utf-8")
            string_name.decode("utf-8")

    Tuples -> () # Immutable 

        spices = ("cardomom", "cloves", "cinnamon")
        (spice1, spice2, spice3) = spices

        ginger_ratio, cardramom_ratio = 2, 1
        ginger_ratio, cardramom_ratio = cardramom_ratio, ginger_ratio

        # membership
        'ginger' in spices # returns True or Flase - case sensitive


    # Mutable
    
    List (/Array)
        - append
        - pop (removes and returns the value), remove
        - extent -> array1.extend(array2)
        - insert[2, "water"]
        - reverse
        - sort





        
