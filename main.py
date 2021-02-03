menu = [
     {
        'food_type' : 'pescado',
        'food_name': 'salmon',
        'sale_price': 50,
        
    },
     {
        'food_type' : 'postre',
        'food_name': 'pie de limon',
        'sale_price': 15,
        
    },
     {
        'food_type' : 'aperitivo',
        'food_name': 'pan de ajo',
        'sale_price': 5,
        
    },
     {
        'food_type' : 'carne',
        'food_name': 'lagarto',
        'sale_price': 70,
        
    },
     {
        'food_type' : 'postre',
        'food_name': 'torta 3 leches',
        'sale_price': 18,
        
    },
     {
        'food_type' : 'aperitivo',
        'food_name': 'caviar',
        'sale_price': 500,
        
    },

]

#de aqui para arriba esta el menu ------------------------------------
orden = []
#para las ordenes
def create_food(food):
    if food not in menu:
        menu.append(food)
    

def update_food_menu(food, index):
    index_num = index
    index = menu[index]
    if index in menu:
        menu.pop(index_num)
        create_food(food)
        


def delete_food_menu(food):
    menu.pop(index)


def food_list():
    for idx, keys in enumerate(menu):
        print('{uid} | {type} | {name} |{price}'.format(uid = idx, type = keys['food_type'],
            name = keys['food_name'], price = keys['sale_price']))


def orden_food(index):
    index = menu[index]
    if index in menu:
        orden.append(index)
        print(orden)
    

def total_price():
    for carta in orden:
        for valor in carta.values():
            total = '{price}'.format(price = valor['sale_price'])
                
            print(total)
            



#ayudas para no repetir codigo 

def _get_food_field(field_food):
    type_food = None
       
    while not type_food:
        type_food = input(" tipo nombre precio {}  ".format(field_food))

        return type_food



def main():
    print("Bienvenido al restaurant")
    print("*" * 50)
    print(""" Menu

    [L]ista de comidas
    [A]agregar platos
    [M]odificar platos   
    [E]liminar platos
    [O]ordenar 
    
    
    """)




if __name__=='__main__':
    main()

    commands = input("que quieres hacer? ")
    commands = commands.capitalize()
    
    print("*" * 50)
    if commands == "L":
        food_list()
    
    elif commands == "A":
        food = {
        'food_type': _get_food_field(''),
        'food_name': _get_food_field(''),
        'sale_price': _get_food_field(''),
        }
        print("*" * 50)
        create_food(food)
        food_list()
        main()

    elif commands == "M":
         
        food_list() 
        print("*" * 50)
        index = int(input("cual plato quieres modificar: "))
        print("dime el typo el nombre y el precio del nuevo plato")
        food = {
        'food_type': _get_food_field(''),
        'food_name': _get_food_field(''),
        'sale_price': _get_food_field(''),
        }
        print("*" * 50)
        update_food_menu(food, index)
        food_list()

    elif commands =="E":
        food_list()
        print("*" * 50)
        index = int(input("cual plato quieres eliminar: "))
        print("*" * 50)
        delete_food_menu(index)
        food_list()
    
    elif commands == "O":
        food_list()
        print("*" * 50)
        index = (int(input("que deseas ordenar: ")))
        orden_food(index)
        other_index = "si"
        while other_index == "si":
            other_index = input("deseas algo mas? ")
            if other_index == "si":
                index = (int(input("que deseas? ")))
                orden_food(index)
            else:
                break
        total_price()




