from math import cos, sin, radians, atan, degrees

massa = float(input("Qual o valor da massa? (Digite 0 para calcular apenas a força)"))

Forca1 = float(input("Qual o módulo da primeira força? "))
angulo1 = float(input("Qual o primeiro ângulo? "))

Fx1 = Forca1 * cos(radians(angulo1))
Fy1 = Forca1 * sin(radians(angulo1))

Forca2 = float(input("Qual o módulo da segunda força? "))
angulo2 = float(input("Qual o segundo ângulo? "))

Fx2 = Forca2 * cos(radians(angulo2))
Fy2 = Forca2 * sin(radians(angulo2))


F_resultante_x = Fx1 + Fx2
F_resultante_y = Fy1 + Fy2

if massa == 0:
    print("Fx = {} Fy = {}.".format(F_resultante_x, F_resultante_y))
else:
    aceleracao_x = (F_resultante_x / massa)
    aceleracao_y = (F_resultante_y / massa)

    aceleracao = (((aceleracao_x)**2) + ((aceleracao_y)**2))**(1/2)

    div = (aceleracao_y / aceleracao_x)

    arctan = atan(div)
    arctan_graus = degrees(arctan)
    print("Fx = {} Fy = {}.".format(F_resultante_x, F_resultante_y))
    print("a_x = {} e a_y = {}.".format(aceleracao_x, aceleracao_y))
    print("O módulo da aceleração é {}.".format(aceleracao))
    print("O ângulo da aceleração é {}.".format(arctan_graus))

