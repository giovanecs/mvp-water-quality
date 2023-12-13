from sqlalchemy import Column, Integer, DateTime, Float
from datetime import datetime
from typing import Union
from model import Base

class Amostra(Base):
    __tablename__ = 'amostras'
    
    id = Column(Integer, primary_key=True)
    ph = Column(Float)
    hardness = Column(Float)
    solids = Column(Float)
    chloramines = Column(Float)
    sulfate = Column(Float)
    conductivity = Column(Float)
    organic_carbon = Column(Float)
    trihalomethanes = Column(Float)
    turbidity = Column(Float)
    potability = Column(Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, ph: float, hardness: float, solids: float, chloramines: float,
                 sulfate: float, conductivity: float, organic_carbon: float,
                 trihalomethanes: float, turbidity: float, potability: int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma instância de Amostra.

        Args:
            ph (float): Valor de pH da amostra.
            hardness (float): Dureza da amostra.
            solids (float): Concentração de sólidos na amostra.
            chloramines (float): Concentração de cloraminas na amostra.
            sulfate (float): Concentração de sulfato na amostra.
            conductivity (float): Condutividade da amostra.
            organic_carbon (float): Carbono orgânico na amostra.
            trihalomethanes (float): Concentração de trialometanos na amostra.
            turbidity (float): Turbidez da amostra.
            potability (int): Indicador de potabilidade da amostra (0 ou 1).
        """
        self.ph = ph
        self.hardness = hardness
        self.solids = solids
        self.chloramines = chloramines
        self.sulfate = sulfate
        self.conductivity = conductivity
        self.organic_carbon = organic_carbon
        self.trihalomethanes = trihalomethanes
        self.turbidity = turbidity
        self.potability = potability
        
        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
