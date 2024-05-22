class Tarea:
    def __init__(self, id:int, tarea:str, estado:bool) -> None:
        self.id     = id
        self.tarea  = tarea
        self.estado = estado

    # Métodos CRUD
    def read(self) -> str:
        return f"{self.id}|&&|{self.tarea}|&&|{self.estado}"

    def update(self, id, tarea, estado) -> None:
        self.id = id
        self.tarea = tarea
        self.estado = estado

    def delete(self):
        self.id     = None
        self.tarea  = None
        self.estado = None