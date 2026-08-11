import requests
import logging
import time

# ================= CONFIG =================
BASE_URL = "https://middleware-prd.api.integra.do/prd/v1/product"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Im5hbWUiOiJHdWlsaGVybWUgQm92byAtIEludGVncmFkbyIsImVtYWlsIjoiZ3VpbGhlcm1lLmJvdm9AaW50ZWdyYS5kbyIsInR5cGUiOiJpbnRlZ3JhZG8iLCJyb2xlcyI6WyJhcHByb3ZlciIsImNyZWF0b3IiXSwicGVybWlzc2lvbnMiOnsidXNlciI6ImZ1bGwtYWNjZXNzIiwiYXR0cmlidXRlIjoiZnVsbC1hY2Nlc3MiLCJjYXRlZ29yeSI6ImZ1bGwtYWNjZXNzIiwiY3VzdG9tZXIiOiJmdWxsLWFjY2VzcyIsImNhbXBhaWduIjoiZnVsbC1hY2Nlc3MiLCJjbGllbnQiOiJmdWxsLWFjY2VzcyIsInNlcmlhbCI6ImZ1bGwtYWNjZXNzIiwiZnJlaWdodCI6ImZ1bGwtYWNjZXNzIiwic2hpcHBpbmdfY29tcGFueSI6ImZ1bGwtYWNjZXNzIiwiaW52b2ljZSI6ImZ1bGwtYWNjZXNzIiwib3JkZXIiOiJmdWxsLWFjY2VzcyIsInBheW1lbnQiOiJmdWxsLWFjY2VzcyIsInByb2R1Y3QiOiJmdWxsLWFjY2VzcyIsInByaWNlIjoiZnVsbC1hY2Nlc3MiLCJzdG9jayI6ImZ1bGwtYWNjZXNzIiwidHJhY2tpbmciOiJmdWxsLWFjY2VzcyIsImZpbmFuY2lhbCI6ImZ1bGwtYWNjZXNzIiwiZmlzY2FsIjoiZnVsbC1hY2Nlc3MifX0sImlhdCI6MTc3ODI1ODcwOSwiZXhwIjoxNzc4MzQ1MTA5LCJpc3MiOiJpbnRlZ3JhZG8tbWlkZGxld2FyZS1hcGkiLCJzdWIiOiI2ODYzZTIyNTNkMzQzM2NjOTU4YzU0NTcifQ.-6gGNv1pfFA00WBto10AoxUCUTyCTWhdKsypkGW7_gM"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

ENTITY_INTEGRATOR_ID = "647e3feed02bd87f86d27dff" # ID DO SISTEMA \\ Sistemas -> ID do Sistema 

# QUERY BASE (fixa)
QUERY_BASE = (
    "type[STARTS_WITH]=,"
    "sku[HAS]={sku},"
    "client_id[IN]=69975b279849d9b88045f531|69a899d23149f9e4cd025c7e|695d14d00db4166e16e6d3c6|"
    "69975b6f970deb1b531b779d|69172a59ebb6d0541a01e4ff|69b944136108df12ca467e44|"
    "6978f6b2f9b104e02be6b295|69a59d1a1f943cb8dd6f6c01|690a30663edfe92211c0c11c|"
    "6980cebfd928b094bf7a9652|6980ce96ba66c631fc9fab70|69a8a2d33a39958c54c1fae9|"
    "697a48ea37a19e8da0e00f8a|688cca5e19bebbc0c0269b8b|6888c916a699a18151c72396"
)

# Lista de SKUs/refs
SKUS = [
    "25387-0",
    "29531-0",
    "29900",
    "29933-3",
    "29933-9",
    "29959-0",
    "29931-0",
    "29970-0",
    "70435-3",
    "70435-9",
    "70436-3",
    "70436-9",
    "E0229-181",
    "E5006-9",
    "E5007-12",
    "E5012-9",
    "W0072-0",
    "W0460-9",
    "W0462-9",
    "W0455-9",
    "W0456-9",
    "E0207-495",
    "E0209-9",
    "E5006-9",
    "E5007-12",
    "E5012-9"
]

# ================= LOG =================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("resend_script.log"),
        logging.StreamHandler()
    ]
)

# ================= FUNÇÕES =================

def buscar_produto(sku):
    query = QUERY_BASE.format(sku=sku)

    url = f"{BASE_URL}?limit=1&query={query}"

    logging.info(f"[GET] SKU: {sku}")
    logging.debug(f"URL: {url}")

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        logging.error(f"Erro GET SKU {sku}: {response.status_code} - {response.text}")
        return None

    data = response.json()

    if not data.get("items"):
        logging.warning(f"SKU {sku} não encontrado")
        return None

    product_id = data["items"][0]["product_id"]
    logging.info(f"SKU {sku} -> product_id: {product_id}")

    return product_id


def resend_produto(product_id):
    url = f"{BASE_URL}/{product_id}/resend"

    payload = {
        "entity_integrator_id": ENTITY_INTEGRATOR_ID,
        "skip_validation": True,
        "use_seller_integrator": True
    }

    logging.info(f"[PUT] Resend product_id: {product_id}")

    response = requests.put(url, headers=HEADERS, json=payload)

    if response.status_code not in [200, 201]:
        logging.error(f"Erro PUT {product_id}: {response.status_code} - {response.text}")
        return False

    logging.info(f"Resend sucesso: {product_id}")
    return True


# ================= EXECUÇÃO =================

def main():
    for sku in SKUS:
        try:
            product_id = buscar_produto(sku)

            if not product_id:
                continue

            resend_produto(product_id)

            time.sleep(0.5)

        except Exception as e:
            logging.exception(f"Erro inesperado no SKU {sku}: {str(e)}")


if __name__ == "__main__":
    main()