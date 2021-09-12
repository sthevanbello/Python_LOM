from abstratas.poupanca import ContaPoupanca

cp = ContaPoupanca(1111, 2222, 1000)
print(cp.saldo)
cp.sacar(500)
print(cp.saldo)
