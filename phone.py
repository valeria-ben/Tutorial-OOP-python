from item import Item

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