from datetime import datetime

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
        self.siguiente = None

class ListaTareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, tarea):
        if self.cabeza is None:
            self.cabeza = tarea
        else:
            actual = self.cabeza
            anterior = None
            while actual and (actual.prioridad < tarea.prioridad or
                              (actual.prioridad == tarea.prioridad and actual.fecha_vencimiento < tarea.fecha_vencimiento)):
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                tarea.siguiente = self.cabeza
                self.cabeza = tarea
            else:
                anterior.siguiente = tarea
                tarea.siguiente = actual

    def eliminar_tarea(self, descripcion):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.descripcion == descripcion:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                print(f"Tarea '{descripcion}' eliminada.")
                return
            anterior = actual
            actual = actual.siguiente
        print(f"Tarea '{descripcion}' no encontrada.")

    def mostrar_tareas(self):
        actual = self.cabeza
        while actual:
            print(f"Descripción: {actual.descripcion}, Prioridad: {actual.prioridad}, Fecha de vencimiento: {actual.fecha_vencimiento.date()}")
            actual = actual.siguiente

    def buscar_tarea(self, descripcion):
        actual = self.cabeza
        while actual:
            if actual.descripcion == descripcion:
                print(f"Tarea encontrada: {actual.descripcion}, Prioridad: {actual.prioridad}, Fecha de vencimiento: {actual.fecha_vencimiento.date()}")
                return actual
            actual = actual.siguiente
        print(f"Tarea '{descripcion}' no encontrada.")
        return None

    def marcar_completada(self, descripcion):
        self.eliminar_tarea(descripcion)


tareas = ListaTareas()
tarea1 = Tarea("Hacer la compra", 1, "2024-09-25")
tarea2 = Tarea("Estudiar para el examen", 2, "2024-09-20")
tarea3 = Tarea("Llamar al médico", 1, "2024-09-19")

tareas.agregar_tarea(tarea1)
tareas.agregar_tarea(tarea2)
tareas.agregar_tarea(tarea3)


print("Lista de tareas:")
tareas.mostrar_tareas()


tareas.buscar_tarea("Estudiar para el examen")


tareas.marcar_completada("Llamar al médico")


print("\nLista de tareas actualizada:")
tareas.mostrar_tareas()
