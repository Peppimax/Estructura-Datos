class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.siguiente = None

class ListaAnimales:
    def __init__(self):
        self.cabeza = None
    
    def agregar_animal(self, animal):
        # Verificar que el animal no esté en la lista
        if self.buscar_animal(animal.nombre) is None:
            if self.cabeza is None:
                self.cabeza = animal
            else:
                actual = self.cabeza
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = animal
        else:
            print(f"El animal '{animal.nombre}' ya está en la lista.")

    def buscar_animal(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None

    def mostrar_con_bucle(self):
        actual = self.cabeza
        while actual:
            print(f"Nombre: {actual.nombre}, Edad: {actual.edad}, Tipo: {actual.tipo}")
            actual = actual.siguiente

    def mostrar_con_recursion(self, nodo):
        if nodo:
            print(f"Nombre: {nodo.nombre}, Edad: {nodo.edad}, Tipo: {nodo.tipo}")
            self.mostrar_con_recursion(nodo.siguiente)


zoologico = ListaAnimales()
animal1 = Animal("Águila", 5, "Ave")
animal2 = Animal("Pantera", 7, "Felino")
animal3 = Animal("Vaca", 3, "Mamífero")

zoologico.agregar_animal(animal1)
zoologico.agregar_animal(animal2)
zoologico.agregar_animal(animal3)
zoologico.agregar_animal(animal1)  


print("Lista usando bucle:")
zoologico.mostrar_con_bucle()


print("\nLista usando recursión:")
zoologico.mostrar_con_recursion(zoologico.cabeza)
