from classes.escritor import Escritor
from classes.caneta import Caneta
from classes.maquina import MaquinaDeEscrever

escritor1 = Escritor('Homer')
caneta1 = Caneta('Bic')
maquina1 = MaquinaDeEscrever('Olivete')

print('\nEscritor\n')

print(f'Escritor: {escritor1.nome}')
print(f'Marca da caneta: {caneta1.marca}')
print(f'Marca da máquina: {maquina1.marca}')

# ferramenta recebe um objeto e utiliza os métodos desse objeto
escritor1.ferramenta = caneta1
escritor1.ferramenta.escrever()
print()
escritor1.ferramenta = maquina1
escritor1.ferramenta.escrever()
