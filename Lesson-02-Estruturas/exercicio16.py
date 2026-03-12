### Exercício 16 – Decomposição de Jornada para Fechamento de Folha
"""
Um técnico de som trabalhou em um set de filmagem por um total de 1527 minutos. Para o fechamento do contrato, o RH precisa que o tempo seja discriminado separando as horas completas dos minutos excedentes, pois as horas e os minutos possuem valores de pagamento distintos. O impacto esperado é a transparência e conformidade com os acordos sindicais. Para este contrato cada hora completa trabalhada é paga a R$ 60,00 e cada minuto excedente é pago a R$ 1,20. O impacto esperado é conseguir definir com precisão o valor que deverá ser pago.

**Tarefa:** A partir do total de 1527 minutos, calcule a quantidade de horas inteiras trabalhadas e a quantidade de minutos restantes. Em seguida calcule o valor total referente às horas e o valor total referente aos minutos excedentes. 

Exiba no terminal devidamente sinalizada:
   - horas trabalhadas  
   - minutos excedentes  
   - valor pago pelas horas  
   - valor pago pelos minutos  
   - valor total a receber  
   """


total_minutos = 1527

horas = total_minutos // 60
minutos = total_minutos % 60

valor_horas = horas * 60.00
valor_minutos = minutos * 1.20

valor_total = valor_horas + valor_minutos

print("Horas trabalhadas:", horas)
print("Minutos excedentes:", minutos)
print("Valor pago pelas horas:", f"{valor_horas:.2f}")
print("Valor pago pelos minutos:", f"{valor_minutos:.2f}")
print("Valor total a receber:", f"{valor_total:.2f}")






