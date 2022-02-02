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

    # Lista de las instancias con sus parametros
    def __repr__(self): 
        return f"Item('{self.name}','{self.price}', '{self.quantity}')"

#INSTANCE ATTRIBUTES 

# crear un objeto (instance/object)
# aun se pueden asignar atributos a instances especificos, individualmente

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

#SEGUNDA PARTE DEL TUTORIAL

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

# Se pueden tomar solo algunos objetos de la lista (lista creada al principio de la clase []) 
for instance in Item.all:
    print(instance.name)

csv common separated value

