# import threading
# import time

# class Hilo(threading.Thread):
#     def __init__(self, nombre, intervalo):
#         super().__init__()
#         self.nombre = nombre
#         self.intervalo = intervalo

#     def run(self):
#         print(f"El hilo {self.nombre} ha comenzado")
#         for i in range(5):
#             print(f"El hilo {self.nombre} se encuentra en la iteración {i}")
#             time.sleep(self.intervalo)
#         print(f"El hilo {self.nombre} ha finalizado")

# # Crear instancias de los hilos
# hilo1 = Hilo("Hilo1", 2)
# hilo2 = Hilo("Hilo2", 4)

# # Iniciar los hilos
# hilo1.start()
# hilo2.start()

# # Esperar a que los hilos finalicen
# hilo1.join()
# hilo2.join()

import asyncio
async def tarea (nombre):
    print(f'{nombre}inicia')
    qwait asyncio.sleep(2)
    print
