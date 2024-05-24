from tarea import Tarea

class Evento(Tarea):
    def __init__(self, id:int, tarea:str, estado:bool, fechaInicio, horaInicio, fechaFin, horaFin):
        super().__init__(id, tarea, estado)
        self.fechaInicio = fechaInicio
        self.horaInicio = horaInicio
        self.fechaFin = fechaFin
        self.horaFin = horaFin

    # Métodos CRUD
    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass