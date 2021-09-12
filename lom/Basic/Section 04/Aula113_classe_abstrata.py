from abstratas.poupanca import ContaPoupanca
from abstratas.corrente import ContaCorrente

cp = ContaPoupanca(1111, 2222, 1000)
cp.detalhes()
cp.sacar(500)
cp.detalhes()

cc = ContaCorrente(1234, 5678, 1500, 150)

cc.detalhes()
cc.sacar(1800)
cc.detalhes()
