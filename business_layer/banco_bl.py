import random
from typing import List
from dtos.Banco import NumeroDeBancoDto, PlazaDto, SolicitudDeClabeDto
from repositories.plaza_repository import get_all, get_random_plaza
from repositories.codigo_de_banco_repository import get_all as get_all_bancos


def create_clabe(solicitud: SolicitudDeClabeDto):
    # def create_clabe(numero_de_cuenta: str, banco: int, plaza: int):
    factorDePeso = [3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7]
    pad = "00000000000"
    pad = pad[len(solicitud.depositoId) : len(pad)]
    numero_de_cuenta = pad + solicitud.depositoId
    clabe = str(solicitud.numeroDeBanco) + str(solicitud.plaza) + numero_de_cuenta
    producto = []
    i = 0
    for number in clabe:
        producto.append(int(number) * factorDePeso[i])
        i = i + 1
    print(producto)
    suma = sum(producto)
    suma = suma % 10
    digito_verificador = (10 - suma) % 10
    clabe = clabe + str(digito_verificador)

    return clabe


def create_number_card(numero_de_cuenta: str = None):
    # Ejemplo de IIN/BIN (los primeros 6 dígitos)
    bin = "400000"  # Esto es un ejemplo y debería ser un BIN válido
    if numero_de_cuenta == None:
        # Generar el número de cuenta (del 7 al 15)
        numero_de_cuenta = get_numero_de_cuenta()
    else:
        pad = "000000000"
        pad = pad[len(numero_de_cuenta) : len(pad)]
        numero_de_cuenta = pad + numero_de_cuenta
    partial_card_number = bin + numero_de_cuenta
    check_digit = calculate_luhn(partial_card_number)

    return partial_card_number + str(check_digit)


def calculate_luhn(partial_card_number):
    sum = 0
    alternate = False
    for item in reversed(partial_card_number):
        number = int(item)
        if alternate:
            number = number * 2
            if number > 9:
                number = number - 9
        sum = sum + number
        if alternate:
            alternate = False
        else:
            alternate = True
    # El dígito de control es el número que hace que la suma sea múltiplo de 10
    check_digit = (10 - (sum % 10)) % 10

    return check_digit


def get_numero_de_cuenta():
    numero_de_cuenta = ""
    i = 0
    while i < 9:
        numero_de_cuenta = numero_de_cuenta + random.randint(1, 9)
        i = i + 1

    return numero_de_cuenta


def get_plazas() -> List[PlazaDto]:
    inventory = get_all()
    plazas = []
    for item in inventory:
        # print(item)
        plazas.append({"id": item["id"], "nombre": item["nombre"]})

    return plazas


def get_numeros_de_bancos() -> List[NumeroDeBancoDto]:
    inventory = get_all_bancos()
    lista = []
    for item in inventory:
        print(item)
        data = {
            "numero": item["Numero"],
            "nombreAbreviado": item["NombreAbreviado"],
            "nombreDeLaInstitucion": "",
        }
        if item.get("NombreDeLaInstitucion") != None:
            data["nombreDeLaInstitucion"] = item["NombreDeLaInstitucion"]
        lista.append(data)

    return lista
