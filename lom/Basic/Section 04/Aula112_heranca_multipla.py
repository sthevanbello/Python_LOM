from classes.heranca_multipla import Pessoa, Cliente, ClienteVip, ClienteEspecial

cliente_vip = ClienteVip('Sthevan', 34, '12345678978', 121)
cliente_especial = ClienteEspecial('Home', 45, '45612378965', 9876, 6541)

cliente_especial.comprar()
cliente_vip.comprar()