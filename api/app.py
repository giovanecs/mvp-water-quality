from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from model import Session, Amostra, Model
from logger import logger
from schemas import *
from flask_cors import CORS

# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
amostra_tag = Tag(name="Amostra", description="Operações relacionadas a amostras")

# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota de listagem de amostras
@app.get('/amostras', tags=[amostra_tag],
         responses={"200": AmostraViewSchema, "404": ErrorSchema})
def get_amostras():
    """Lista todas as amostras cadastradas na base
    Retorna uma lista de amostras cadastradas na base.
    
    Returns:
        list: lista de amostras cadastradas na base
    """
    session = Session()
    
    # Buscando todas as amostras
    amostras = session.query(Amostra).all()
    
    if not amostras:
        logger.warning("Não há amostras cadastradas na base :/")
        return {"message": "Não há amostras cadastradas na base :/"}, 404
    else:
        logger.debug(f"%d amostras encontradas" % len(amostras))
        return apresenta_amostras(amostras), 200

# Rota de adição de amostra
@app.post('/amostra', tags=[amostra_tag],
          responses={"200": AmostraViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def add_amostra(form: AmostraSchema):
    """Adiciona uma nova amostra à base de dados
    Retorna uma representação das amostras.
    
    Args:
        ph (float): valor do pH
        hardness (float): dureza da amostra
        solids (float): sólidos totais dissolvidos
        chloramines (float): quantidade de cloraminas
        sulfate (float): quantidade de sulfato
        conductivity (float): condutividade
        organic_carbon (float): quantidade de carbono orgânico
        trihalomethanes (float): quantidade de trihalometanos
        turbidity (float): turbidez
            
    Returns:
        dict: representação da amostra
    """
    
    # Carregando modelo
    ml_path = 'ml_model/model.pkl'
    modelo = Model.carrega_modelo(ml_path)

    amostra = Amostra(
        ph=form.ph,
        hardness=form.hardness,
        solids=form.solids,
        chloramines=form.chloramines,
        sulfate=form.sulfate,
        conductivity=form.conductivity,
        organic_carbon=form.organic_carbon,
        trihalomethanes=form.trihalomethanes,
        turbidity=form.turbidity,
        potability=Model.preditor(modelo, form)
    )
    logger.debug(f"Adicionando amostra de ID: '{amostra.id}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Adicionando amostra
        session.add(amostra)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionada amostra de ID: '{amostra.id}'")
        return apresenta_amostra(amostra), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar nova amostra :/"
        logger.warning(f"Erro ao adicionar amostra, {error_msg}")
        return {"message": error_msg}, 400

# Métodos baseados em ID
# Rota de busca de amostra por ID
@app.get('/amostra', tags=[amostra_tag],
         responses={"200": AmostraViewSchema, "404": ErrorSchema})
def get_amostra(query: AmostraBuscaSchema):
    """Faz a busca por uma amostra cadastrada na base a partir do ID

    Args:
        id (int): ID da amostra
        
    Returns:
        dict: representação da amostra
    """
    
    amostra_id = query.id;

    logger.debug(f"Coletando dados sobre amostra de ID: #{amostra_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    amostra = session.query(Amostra).filter(Amostra.id == amostra_id).first()
    
    if not amostra:
        # se a amostra não foi encontrada
        error_msg = f"Amostra {amostra_id} não encontrada na base :/"
        logger.warning(f"Erro ao buscar amostra '{amostra_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Amostra encontrada: ID {amostra.id}")
        # retorna a representação da amostra
        return apresenta_amostra(amostra), 200

# Rota de remoção de amostra por ID
@app.delete('/amostra', tags=[amostra_tag],
            responses={"200": AmostraViewSchema, "404": ErrorSchema})
def delete_amostra(query: AmostraDelSchema):
    """Remove uma amostra cadastrada na base a partir do ID

    Args:
        id (int): ID da amostra
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    amostra_id = query.id

    logger.debug(f"Deletando dados sobre amostra de ID: #{amostra_id}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando amostra
    amostra = session.query(Amostra).filter(Amostra.id == amostra_id).first()
    
    if not amostra:
        error_msg = f"Amostra de ID {amostra_id} não encontrada na base :/"
        logger.warning(f"Erro ao deletar amostra de ID '{amostra_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(amostra)
        session.commit()
        logger.debug(f"Deletada amostra de ID: #{amostra_id}")
        return {"message": f"Amostra de ID {amostra_id} removida com sucesso!"}, 200
