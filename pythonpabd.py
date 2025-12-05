from conta import Conta
from cliente import Cliente

cliente1 = Cliente('Elvis Presley', '111.222.333.45')
conta1 = Conta(cliente1, 1, 123, 'elvisplays@gmail.com', 1234545)
cliente2 = Cliente('John Lennon', '222.333.444.56')
conta2 = Conta(cliente2, 2, 234, 'johnlenno@gmail.com', 2345656)
conta1.extrato()
conta1.deposita(100000)
