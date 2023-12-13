from pydantic import BaseModel
from typing import List
from model.amostra import Amostra
from pydantic import BaseModel

class AmostraSchema(BaseModel):
    """Define como uma amostra a ser inserida deve ser representada
    """
    ph: float = 7.0
    hardness: float = 150.0
    solids: float = 300.0
    chloramines: float = 10.0
    sulfate: float = 100.0
    conductivity: float = 500.0
    organic_carbon: float = 10.0
    trihalomethanes: float = 50.0
    turbidity: float = 5.0

class AmostraViewSchema(BaseModel):
    """Define como uma amostra será retornada
    """
    id: int = 1
    ph: float = 7.0
    hardness: float = 150.0
    solids: float = 300.0
    chloramines: float = 10.0
    sulfate: float = 100.0
    conductivity: float = 500.0
    organic_carbon: float = 10.0
    trihalomethanes: float = 50.0
    turbidity: float = 5.0
    potability: int = 1

class AmostraBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no id da amostra.
    """
    id: int = 1

class ListaAmostrasSchema(BaseModel):
    """Define como uma lista de amostras será representada
    """
    amostras: list[AmostraSchema]

class AmostraDelSchema(BaseModel):
    """Define como uma amostra para deleção será representada
    """
    id: int = 1

# Apresenta apenas os dados de uma amostra
def apresenta_amostra(amostra: Amostra):
    """Retorna uma representação da amostra seguindo o schema definido em
       AmostraViewSchema.
    """
    return {
        "id": amostra.id,
        "ph": amostra.ph,
        "hardness": amostra.hardness,
        "solids": amostra.solids,
        "chloramines": amostra.chloramines,
        "sulfate": amostra.sulfate,
        "conductivity": amostra.conductivity,
        "organic_carbon": amostra.organic_carbon,
        "trihalomethanes": amostra.trihalomethanes,
        "turbidity": amostra.turbidity,
        "potability": amostra.potability
    }

# Apresenta uma lista de amostras
def apresenta_amostras(amostras: list[Amostra]):
    """Retorna uma representação das amostras seguindo o schema definido em
       AmostraViewSchema.
    """
    result = []
    for amostra in amostras:
        result.append({
            "id": amostra.id,
            "ph": amostra.ph,
            "hardness": amostra.hardness,
            "solids": amostra.solids,
            "chloramines": amostra.chloramines,
            "sulfate": amostra.sulfate,
            "conductivity": amostra.conductivity,
            "organic_carbon": amostra.organic_carbon,
            "trihalomethanes": amostra.trihalomethanes,
            "turbidity": amostra.turbidity,
            "potability": amostra.potability
        })

    return {"amostras": result}
