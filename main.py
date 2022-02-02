import csv

# PARENT CLASS -----------------------------------------------------------------------------------------------
class Item:
    #CLASS ATTRIBUTE 
    pay_rate = 0.8 # the pay rate after 20% discount

    all = []

    # los metodos (funciones dentro de las clases) siempre tienen que recibir al menos un parametro (self)

    # por cada instancia que haya, se va a correr el metodo init
    # se pueden poner default parametros (como el de quantity), en caso de que no tengamos ese dato en los instances
    # hay que validar los tipos de datos o values que estamos pasando en los parametros, por ej. "name" solo puede aceptar str type data
    # float: pasa int y numeros (cualquiera)

    def __init__(self, name: str, price: float, quantity=0) -> None:
        print(f"An intance createad: {name}")
        
        # Verificar y validar los datos recibidos. 
        # por ejemplo, que el precio y cantidad sean igual o mayor a cero
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # asignar atributos de cada instancia. 
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute. 
        Item.all.append(self)
        

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        #es mejor utilizar el self, que un objeto en especifico, da lugar a que se tome en cuenta el instance level
        self.price = self.price * self.pay_rate

    # 1.2 CLASS METHOD
    # Convertir este metodo en un class method, se usa un decorator (change the behavior of the functions by calling them before)
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=str(item.get('name')),          # If you want to copy the line to the line above itself, press Shift + Alt + Up Arrow Key.
                # price=float(item.get('price')),     # HAY UN PROBLEMA AQUI Y NO SE QUE ES, 1:00:00 tutorial
                quantity=int(item.get('quantity')),
            )
    # 1.3 STATIC METHOD
    @staticmethod
    def is_interger(num):
        # we will count out the floats that are point zero (ex: 2.5)
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Lista de las instancias con sus parametros
    def __repr__(self): 
        # intead of --> return f"Item('{self.name}','{self.price}', '{self.quantity}')" -->
        return f"{self.__class__.__name__}('{self.name}','{self.price}', '{self.quantity}')"

# PRINTS FROM CLASS ITEM --------------------------------------------------------------------------------------

#INSTANCE ATTRIBUTES 

# Objeto/instance; aun se pueden asignar atributos a instances especificos, individualmente

item1 = Item("phone", 100, 5)
# primero buscará el pay rate en el instance level (no hay dato), luego ira al class level (pay_rate = 0.8)
item1.apply_discount()
print(item1.price)

item2 = Item("laptop", 1000,3)
# primero buscará el pay rate en el instance level, tomará el 0.7
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price) 

# print(Item.__dict__) # Para saber all the attributes for class level
# print(item1.__dict__) # Para saber all the attributes for instance level

print(Item.all)

# Se pueden tomar solo algunos objetos de la lista (lista creada al principio de la clase []) 
for instance in Item.all:
    print(instance.name)

# 1.2 CLASS METHOD PRINT
# Item.instantiate_from_csv() #stores all the instances inside the list. AQUI HAY OTRO PROBLEMA
print(Item.all)

# 1.3 STATIC METHOD PRINT (def is_interger(num):)
print(Item.is_interger(7.0))

# 2.0 CHILD CLASS ----------------------------------------------------------------------------------------------

# Crear un Phone class (child class) separada que herede las funconalidad del Item class
# Queremos hacer un metodo que cuente los telefonos que no esten quebrados
# Mandamos a llamar a la clase "Item" dentro del parametro y copiamos el constructor para poder agregar mas parametros
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:
    
        # Call to super function to have access to all attributes and methods.
        super().__init__(
            name, price, quantity
        )

        # run validations.
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater or equal to zero!"

        # asignar atributos de cada instancia. 
        self.broken_phones = broken_phones

# PRINTS FROM CLASS PHONE --------------------------------------------------------------------------------------

phone1 = Phone("jscPhonev10",500,5, 1)
# Probamos con un method del parent class
print(phone1.calculate_total_price())

phone2 = Phone("jscPhonev20",700,5, 1)



# ---------------------------------------------------------------------------------------------------------------
# no entendi porque lo imprime con comillas y corchetes, deberia ser mas facil de leer como en el video 
print(Item.all)
print(Phone.all)


