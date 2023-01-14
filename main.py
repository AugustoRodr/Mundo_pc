from orden import Orden
from computadora import Computadora
from monitor import Monitor
from teclado import Teclado
from raton import Raton

teclado_hp= Teclado('hp','USB')
raton_hp=Raton('hp','USB')
monitor_hp=Monitor('hp', '21 Pulgadas')
computadora_hp= Computadora('hp',monitor_hp,teclado_hp,raton_hp)

teclado_genius= Teclado('hp','PS/2')
raton_genius=Raton('hp','USB')
monitor_acer=Monitor('acer', '15 Pulgadas')
computadora_acer= Computadora('acer',monitor_hp,teclado_hp,raton_hp)

teclado_gamer= Teclado('gamer','bluetooth')
raton_gamer=Raton('gamer','bluetooth')
monitor_gamer=Monitor('gamer', '30 Pulgadas')
computadora_gamer= Computadora('gamer',monitor_hp,teclado_hp,raton_hp)

computadoras1=[computadora_acer,computadora_hp]

orden1= Orden(computadoras1)
orden1.agregar(computadora_gamer)
print(orden1)

computadora_armada= Computadora('armada', monitor_gamer, teclado_genius, raton_gamer)

computadoras2=[computadora_armada,computadora_gamer,computadora_hp]

orden2=Orden(computadoras2)
print(orden2)