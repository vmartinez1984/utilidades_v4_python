from repositories.plaza_repository import get_random_plaza


def get_clabe(numero_de_cuenta: str, banco: str):
    plaza = get_random_plaza()
    plazaId = ""
    if plaza["id"] < 100:
        plazaId = "0" + plaza["id"]
    else:
        plazaId = plaza["id"]
    #if banco == None:
        
    #create_clabe(numero_de_cuenta, plazaId, banco)

