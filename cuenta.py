class CuentaCorriente:
	def __init__(self,saldo):
		self.saldo=saldo

	def depositar(self,deposito):
		if deposito<0:
			return
		self.saldo+=deposito

	def transferir(self,user,cantidad):
		if cantidad<0 or cantidad>self.saldo:
			return
		self.saldo-=cantidad
		user.depositar(cantidad)

keiko = CuentaCorriente(100)
print(keiko.saldo) # 32847
keiko.depositar(10)
print(keiko.saldo) # 32857

AG = CuentaCorriente(10)
AG.transferir(keiko, 1)
print(AG.saldo) # disminuido
print(keiko.saldo) # aumentado