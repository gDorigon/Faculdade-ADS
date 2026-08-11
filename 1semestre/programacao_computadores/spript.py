import requests
import xml.etree.ElementTree as ET
from collections import defaultdict

URL = "http://webapi.microvix.com.br/1.0/api/integracao"

XML_BODY = """<?xml version="1.0" encoding="ISO 8859-1" ?>
<LinxMicrovix>
    <Authentication user="linx_b2c"  password="linx_b2c" />
    <ResponseFormat>xml</ResponseFormat>
    <Command>
        <Name>B2CConsultaProdutosCodebar</Name>
        <Parameters> 
            <Parameter id="chave">1396f9d7-ca03-427e-bc11-c266d95c603e</Parameter> 
            <Parameter id="cnpjEmp">48386545000104</Parameter> 
            <Parameter id="timestamp">1</Parameter> 
        </Parameters>
    </Command>
</LinxMicrovix>
"""

HEADERS = {
    "Content-Type": "text/xml"
}

def fetch_data():
    try:
        response = requests.post(
            URL,
            data=XML_BODY.encode("ISO-8859-1"),
            headers=HEADERS,
            timeout=30
        )

        response.raise_for_status()

        # Força decoding correto
        text = response.content.decode("ISO-8859-1", errors="ignore")

        # Debug inicial (ajuda muito)
        print("\n=== RESPOSTA BRUTA (primeiros 500 chars) ===\n")
        print(text[:500])

        return text

    except requests.exceptions.RequestException as e:
        print("Erro na requisição:", e)
        return None


def sanitize_xml(xml_text):
    """
    Remove lixo antes do XML (muito comum na Microvix)
    """
    if not xml_text:
        return None

    start = xml_text.find("<")
    if start == -1:
        return None

    return xml_text[start:]


def parse_xml(xml_text):
    xml_text = sanitize_xml(xml_text)

    if not xml_text:
        print("Resposta inválida (não contém XML).")
        return []

    try:
        root = ET.fromstring(xml_text)

        columns_node = root.find(".//C")
        if columns_node is None:
            print("Estrutura inesperada: nó <C> não encontrado.")
            return []

        columns = [d.text for d in columns_node.findall("D")]

        data = []
        for row in root.findall(".//R"):
            values = [d.text for d in row.findall("D")]
            record = dict(zip(columns, values))
            data.append(record)

        return data

    except ET.ParseError as e:
        print("Erro ao fazer parse do XML:", e)
        return []


def check_duplicates(data):
    codebar_map = defaultdict(list)

    for item in data:
        codebar = item.get("codebar")
        codproduto = item.get("codigoproduto")

        if codebar and codproduto:
            codebar_map[codebar].append(codproduto)

    # duplicidades reais (mesmo codebar em vários produtos)
    duplicates = {
        codebar: produtos
        for codebar, produtos in codebar_map.items()
        if len(produtos) > 1
    }

    # inconsistência lógica (produto != codebar)
    inconsistencies = [
        item for item in data
        if item.get("codigoproduto") != item.get("codebar")
    ]

    return duplicates, inconsistencies


def main():
    xml = fetch_data()

    if not xml:
        print("Nenhuma resposta recebida.")
        return

    data = parse_xml(xml)

    if not data:
        print("Nenhum dado válido encontrado.")
        return

    duplicates, inconsistencies = check_duplicates(data)

    print("\n=== DUPLICIDADES (MESMO CODEBAR EM VÁRIOS PRODUTOS) ===")
    if duplicates:
        for codebar, produtos in duplicates.items():
            print(f"Codebar: {codebar} -> Produtos: {produtos}")
    else:
        print("Nenhuma duplicidade encontrada.")

    print("\n=== INCONSISTÊNCIAS (codigoproduto != codebar) ===")
    if inconsistencies:
        for item in inconsistencies:
            print(f"Produto: {item['codigoproduto']} | Codebar: {item['codebar']}")
    else:
        print("Nenhuma inconsistência encontrada.")


if __name__ == "__main__":
    main()
    