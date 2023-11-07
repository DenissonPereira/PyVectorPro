from math import cos, sin, radians, atan, degrees

massa = float(input("Digite o valor da massa: "))
qnt_F = int(input("Qual a quantidade de forças no sistema? "))

contador = 1
F_x_resultante = 0
F_y_resultante = 0

while contador <= qnt_F:
    F = float(input("Qual o módulo de F{}? ".format(contador)))
    teta = float(input("Qual o \u03B8{}? ".format(contador)))

    Fx = F * cos(radians(teta))
    Fy = F * sin(radians(teta))

    F_x_resultante += Fx
    F_y_resultante += Fy
    contador += 1

a_x = F_x_resultante / massa
a_y = F_y_resultante / massa
a = (((a_x)**2) + ((a_y)**2))**(1/2)
print("Fx = {} e Fy = {}.".format(F_x_resultante, F_y_resultante))