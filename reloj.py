
class Reloj:
	def __init__(self,h,m):
		self.h=h
		self.m=m
	def mostrar(self):
		print('{}:{}'.format(self.h,self.m)
		return

	def agregar_minuto(self.m):
		self.m+=1
		if self.m>59:
			self.m=0
		return

	def agregar_hora(self.h):
		self.h+=1
		if self.h>23:
			self.h=0
		return

rolex = Reloj(horas=23, minutos=59)
rolex.mostrar() # -> 23:59
rolex.agregar_minuto()
rolex.mostrar() # -> 00:00
rolex.agregar_hora()
rolex.mostrar() # -> 00:01
