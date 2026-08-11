
# Importa as bibliotecas necessárias
import requests  # Para requisições HTTP
import logging   # Para logs de execução
import time      # Para delays entre requisições
from datetime import datetime  # Para manipulação de datas


# ================= CONFIGURAÇÕES =================


# URL base da API de produtos
BASE_URL = "https://middleware-prd.api.integra.do/prd/v1/product"

# Token de autenticação (substitua pelo seu token real)
TOKEN = "INSIRA_SEU_TOKEN_AQUI"

# Cabeçalhos padrão para as requisições
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Connection": "close"
}

# ID do integrador da entidade
ENTITY_INTEGRATOR_ID = "647e3feed02bd87f86d27dff"

# Tempo de espera entre requisições (em segundos)
REQUEST_DELAY = 4
# Número máximo de tentativas em caso de erro
MAX_RETRIES = 3


# ================= QUERY BASE =================


# Query base para busca de produtos, filtrando por SKU e client_id ( como aqui o produto deve ser buscado em todos fornecedores do cliente, o filtro de client_id é necessário para garantir que o produto seja encontrado mesmo que esteja associado a um fornecedor diferente do que fez a última atualização)
QUERY_BASE = (
    "type[STARTS_WITH]=," 
    "sku[HAS]={sku},"
    "client_id[IN]=69975b279849d9b88045f531|69a899d23149f9e4cd025c7e|695d14d00db4166e16e6d3c6|"
    "69975b6f970deb1b531b779d|69172a59ebb6d0541a01e4ff|69b944136108df12ca467e44|"
    "6978f6b2f9b104e02be6b295|69a59d1a1f943cb8dd6f6c01|690a30663edfe92211c0c11c|"
    "6980cebfd928b094bf7a9652|6980ce96ba66c631fc9fab70|69a8a2d33a39958c54c1fae9|"
    "697a48ea37a19e8da0e00f8a|688cca5e19bebbc0c0269b8b|6888c916a699a18151c72396"
)


# ================= LISTA DE SKUS =================


# Lista de SKUs a serem processados
SKUS = [
    "W0250-0",
    "W0250-9",
    "E5000-7",
    "E5003-226",
    "E0093-9"
]


# ================= CONFIGURAÇÃO DE LOG =================


# Nome do arquivo de log com data/hora
LOG_FILE = f"resend_script_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Configuração do logging para arquivo e console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)


# ================= FUNÇÕES PRINCIPAIS =================


# Busca um produto na API pelo SKU
def buscar_produto(sku):

    try:
        logging.info("=" * 80)
        logging.info(f"Buscando SKU: {sku}")

        # Monta a query para busca
        query = QUERY_BASE.format(sku=sku)
        url = f"{BASE_URL}?limit=1&query={query}"

        # Faz a requisição GET para buscar o produto
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=60
        )

        # Verifica se a resposta foi bem-sucedida
        if response.status_code != 200:
            logging.error(f"Erro ao buscar SKU {sku} | Status: {response.status_code}")
            return None

        data = response.json()
        items = data.get("items", [])

        # Se não encontrar o produto
        if not items:
            logging.warning(f"SKU não encontrado: {sku}")
            return None

        produto = items[0]

        logging.info(
            f"Produto encontrado | SKU: {sku} | "
            f"Tipo: {produto.get('type')} | "
            f"ID: {produto.get('product_id')}"
        )

        return produto

    except Exception as e:
        logging.exception(f"Erro na busca do SKU {sku}: {str(e)}")
        return None



# Reenvia (PUT) o produto para a API, podendo ser pai ou filho
def resend_produto(product_id, sku=None, tipo=None):


    url = f"{BASE_URL}/{product_id}/resend"

    # Payload padrão para o envio
    payload = {
        "entity_integrator_id": ENTITY_INTEGRATOR_ID,
        "skip_validation": True,
        "use_seller_integrator": True
    }

    # Tenta reenviar até o número máximo de tentativas
    for tentativa in range(MAX_RETRIES):
        try:
            logging.info(
                f"Enviando produto | SKU: {sku} | "
                f"Tipo: {tipo} | "
                f"Product ID: {product_id}"
            )

            # Faz a requisição PUT para reenviar o produto
            response = requests.put(
                url,
                headers=HEADERS,
                json=payload,
                timeout=60
            )

            # Verifica se o envio foi bem-sucedido
            if response.status_code not in [200, 201]:
                logging.error(
                    f"Falha no envio | SKU: {sku} | "
                    f"Status: {response.status_code}"
                )
                # Tenta novamente após um tempo, se ainda houver tentativas
                if tentativa < MAX_RETRIES - 1:
                    time.sleep(8)
                    continue
                return False

            logging.info(f"Envio realizado com sucesso | SKU: {sku}")
            return True

        except (
            requests.exceptions.SSLError,
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout
        ) as e:
            logging.warning(f"Erro de conexão no SKU {sku}: {str(e)}")
            if tentativa < MAX_RETRIES - 1:
                time.sleep(8)
                continue
            logging.error(f"Falha definitiva no SKU {sku}")
            return False

        except Exception as e:
            logging.exception(f"Erro inesperado no resend do SKU {sku}: {str(e)}")
            return False



# Processa as variações (filhos) de um produto configurável
def processar_variacoes(produto_pai):

    try:
        # Obtém as variações do produto pai
        variations = produto_pai.get("variations", [])

        if not variations:
            logging.warning("Produto configurable sem variações")
            return

        logging.info(f"Processando {len(variations)} variações")

        # Para cada variação (produto filho), faz o reenvio
        for variacao in variations:
            try:
                sku_filho = variacao.get("sku")
                product_id_filho = variacao.get("product_id")

                sucesso = resend_produto(
                    product_id=product_id_filho,
                    sku=sku_filho,
                    tipo="child"
                )

                if not sucesso:
                    logging.error(f"Falha ao enviar filho: {sku_filho}")

                time.sleep(REQUEST_DELAY)

            except Exception as e:
                logging.exception(f"Erro ao processar filho: {str(e)}")

    except Exception as e:
        logging.exception(f"Erro nas variações: {str(e)}")



# ================= EXECUÇÃO PRINCIPAL =================


# Função principal que executa o processamento de todos os SKUs
def main():


    logging.info("#" * 80)
    logging.info("INÍCIO DO PROCESSAMENTO")
    logging.info(f"Total de SKUs: {len(SKUS)}")
    logging.info("#" * 80)

    # Processa cada SKU da lista
    for index, sku in enumerate(SKUS, start=1):
        try:
            logging.info("")
            logging.info(f"[{index}/{len(SKUS)}] Processando SKU: {sku}")

            # Busca o produto pelo SKU
            produto = buscar_produto(sku)
            if not produto:
                continue

            product_id = produto.get("product_id")
            tipo = produto.get("type")

            # Reenvia o produto pai
            sucesso = resend_produto(
                product_id=product_id,
                sku=sku,
                tipo=tipo
            )
            if not sucesso:
                logging.error(f"Falha no produto pai: {sku}")
                continue

            # Se for um produto configurável, processa as variações (filhos)
            if tipo == "configurable":
                logging.info(f"Produto configurable detectado: {sku}")
                logging.info("Iniciando envio dos filhos")
                processar_variacoes(produto)

            time.sleep(REQUEST_DELAY)

        except Exception as e:
            logging.exception(f"Erro geral no SKU {sku}: {str(e)}")

    logging.info("")
    logging.info("#" * 80)
    logging.info("PROCESSAMENTO FINALIZADO")
    logging.info("#" * 80)



# ================= INÍCIO DO SCRIPT =================

if __name__ == "__main__":
    main()