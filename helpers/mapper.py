def serial_codigo_postal(codigo_postal) -> dict:
    return {
        "codigoPostal": codigo_postal["CodigoPostal"],
        "alcaldiaId": codigo_postal["AlcaldiaId"],
        "estado": codigo_postal["Estado"],
        "estadoId": codigo_postal["EstadoId"],
        "alcaldia": codigo_postal["Alcaldia"],
        "tipoDeAsentamiento": codigo_postal["TipoDeAsentamiento"],
        "asentamiento": codigo_postal["Asentamiento"],
    }

def serial_codigos_postales(codigos)-> list:
    return [serial_codigo_postal(cp) for cp in codigos]