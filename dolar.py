cometa = input("Nombre del comisionista: ")
tc = input("Cuál es la cotización?: ")
ammount = input("Cuantos USD desea cambiar el cliente?: ")
cchica = input("Ingrese la cantidad de dolares cara chica si no hay ninguno ingrese 0: ")
porcentajec = input ("A que porcentaje se tomaran los biletes cara chica?  -%: ")
tc_f = float(tc)
ammount_i = int(ammount)
icchica = int(cchica)
carachicaperc =  (float(porcentajec)*icchica)/100
totalpesos = tc_f * ammount_i
totalpesoscchica = (totalpesos- (icchica*tc_f)) + (((icchica)- carachicaperc)*tc_f)

def getcot():
    if icchica <= 0 :
        print(f"""{cometa} realizo una operacion por {ammount_i} a {tc_f:.2f}, el equivalente en pesos es de  
{tc_f*ammount_i}""")
    else :
        print(f"""{cometa} realizo una operación por {ammount_i} a {tc_f:.2f}, el equivalente en pesos es de
{totalpesoscchica}""")

getcot()