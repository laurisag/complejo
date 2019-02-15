class Fraccion():
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def suma_fraccion(self, otro):
        suma_numerador = self.numerador + otro.numerador
        suma_denominador = self.denominador + otro.denominador
        resultado = (suma_numerador, suma_denominador)
        return resultado

    def multiplicacion_fraccion(self, otro):
        mult_numerador = self.numerador * otro.numerador
        mult_denominador = self.denominador * otro.denominador
        resultado_2 = (mult_numerador, mult_denominador)
        return resultado_2

    def division_fraccion(self, otro):
        div_numerador = self.numerador / otro.numerador
        div_denominador = self.denominador / otro.denominador
        resultado_3 = (div_numerador, div_denominador)
        return resultado_3
