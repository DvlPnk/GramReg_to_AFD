# Delta
def delta(estado, simbolo):
    conjunto = []
    for i in range(0, n):
        if (datos[i][0] == estado and datos[i][1] == simbolo):
            conjunto += [datos[i][2]]
    conjunto = list(dict.fromkeys(conjunto))
    return conjunto

def clausura(estado):
    conjunto = []
    for i in range(len(estado)):
        conjunto += [estado[i]]
    for i in range(0, n):
        for j in range(len(estado)):
            if (datos[i][0] == estado[j] and datos[i][1] == 'e'):
                conjunto += [datos[i][2]]
    conjunto = list(dict.fromkeys(conjunto))
    return conjunto

        
print("PROGRAMA: Conversión de una gramática regular a AFD")
print("===================================================================")
print("INGRESO DE DATOS")
s = int(input("Ingrese la cantidad de símbolos no terminales: "))
estados2=[]
for i in range(s):
    estados2+=input("Ingrese ΣN" + str(i + 1) + ": ")
entrada=estados2[0]
estados2+='Z'
p = int(input("Ingrese la cantidad de terminales: "))
simbolo = []
for i in range(p):
    simbolo += [input("Ingrese terminal #" + str(i + 1) + ": ")]

print()
print("ΣN: { ",end='')
for i in range(len(estados2)):
    print(estados2[i],end=' ')
print("}")

print("ΣT: { ",end='')
for i in range(len(simbolo)):
    print(simbolo[i],end=' ')
print("}")

i = 0
datos = []
tran = []

print("--------------------------------------------------------")
n = int(input("Ingrese la cantidad de reglas: "))
print("-> Para regla de la forma A::=bC, ingresar: A b C")
print("-> Para regla de la forma A::=a, ingresar: A a Z")
conte=0
while (i < n):
    tran = input("Ingrese la regla #" + str(i + 1) + ": ")
    tran = tran.split(" ")
    if(tran[1]=='e'):
        conte+=1
    datos.append(tran)
    i += 1
print("--------------------------------------------------------")
print(conte)
if(conte>0):
    simbolo+='e'

print("\nEl Dtran AF es: ")
for i in range(len(simbolo)):
    print("\t",simbolo[i],end="\t")
print()
for i in range(len(estados2)):
    print(estados2[i],end= "\t")
    for j in range(len(simbolo)):
        print(delta(estados2[i],simbolo[j]),end="\t\t")
    print()
print("Estado de entrada: ",entrada)
print("Estado de aceptación: Z")

if(conte==0):
    q0 = [entrada]
    estados = [q0]
    cont = 0
    contq = 0
    k = 0
    q1 = []
    Dtran = []
    aceptacion=[]
    print("===================================================================")
    print("###PROCEDIMIENTO###")
    while (True):
        print("--------------------------------------------------------")
        for i in range(len(simbolo)):
            flag = 1
            del_U = []
            print("\nEstado: ", estados[k])
            print("Con el simbolo: ", simbolo[i])
            for j in range(len(estados[k])):
                del_U += delta(estados[k][j], simbolo[i])
                del_U = list(dict.fromkeys(del_U))
            q1 = clausura(del_U)
            q1.sort()
            print("Del_U es: ", end="")
            print(del_U)
            Dtran += [[estados[k], simbolo[i], q1]]
            for j in range(len(estados)):
                if (estados[j] == q1):
                    flag = 0
            if (flag == 1):
                estados += [q1]
                cont += 1
                for i in range(len(q1)):
                    if (q1[i]=='Z'):
                        aceptacion+=[[q1]]
        k += 1
        contq += 1
        print("--------------------------------------------------------")
        if k > cont:
            break;
    print("\nEstados: ")
    for i in range(len(estados)):
        print(estados[i])
    print("\nEl Dtran AFD es: ")
    contq2 = 0
    cont2 = 0
    for i in range (len(simbolo)):
        print("\t",simbolo[i], end= "\t")
    print()
    while(cont2 < (len(estados)*len(simbolo))):
        print(estados[contq2],":",end="\t")
        while(cont2 < (len(simbolo)*(contq2+1))):
            print(Dtran[cont2][2],end="\t")
            cont2 += 1
        print()
        contq2 += 1
        
    print("Estado de entrada: ",entrada)
    print("Estado de aceptación: ",aceptacion)
    
else:
    q0 = []
    q0 = clausura([entrada])
    q0.sort()
    estados = [q0]
    cont = 0
    contq = 0
    k = 0
    q1 = []
    Dtran = []
    print("===================================================================")
    print("###PROCEDIMIENTO###")
    while (True):
        print("--------------------------------------------------------")
        for i in range(len(simbolo)):
            flag = 1
            del_U = []
            print("\nEstado q",contq," es: ", estados[k])
            print("Con el simbolo: ", simbolo[i])
            for j in range(len(estados[k])):
                del_U += delta(estados[k][j], simbolo[i])
                del_U = list(dict.fromkeys(del_U))
            q1 = clausura(del_U)
            q1.sort()
            print("Del_U es:")
            print(del_U)
            print("Q es: ")
            print(q1)
            Dtran += [[estados[k], simbolo[i], q1]]
            for j in range(len(estados)):
                if (estados[j] == q1):
                    flag = 0
            if (flag == 1):
                estados += [q1]
                cont += 1
        k += 1
        contq += 1
        print("--------------------------------------------------------")
        if k > cont:
            break;
    print("\nEstados: ")
    for i in range(len(estados)):
        print("q",i,": ",estados[i])
    print("\nEl Dtran AFD es: ")
    contq2 = 0
    cont2 = 0
    for i in range (len(simbolo)):
        print("\t",simbolo[i], end= "\t")
    print()
    while(cont2 < (len(estados)*len(simbolo))):
        print("q",contq2,": ",end="\t")
        while(cont2 < (len(simbolo)*(contq2+1))):
            print(Dtran[cont2][2],end="\t")
            cont2 += 1
        print()
        contq2 += 1  
