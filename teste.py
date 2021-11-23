from models.cliente import Cliente
from models.conta import Conta


rafael: Cliente = Cliente('Rafael Maldivas','rafaelmaldivas@gmail.com','343.721.318-01','28/04/1987')
beatriz: Cliente = Cliente('Maria Beatriz', 'mbpaiva@gmail.com', '889.736.698-69', '05/03/2015')
print(beatriz)
print(rafael)

conta_r: Conta = Conta(rafael)
cont_b: Conta = Conta(beatriz)
conta_r.depositar(2215.55)
cont_b.sacar(50)

print(cont_b)

print(conta_r)