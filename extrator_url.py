import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida")

        print("A URL é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url


extrator_url = ExtratorURL("https://bytebank.com/cambio?moedaDestino=real&moedaOrigem=dolar&quantidade=6500")
print("O tamanho da URL: ", len(extrator_url))
valor_quantidade = extrator_url.get_valor_parametro("quantidade");
print(extrator_url);

cotacao_dolar = 5.50
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = float(extrator_url.get_valor_parametro("quantidade"))

if moeda_origem is 'dolar':
    res = quantidade * cotacao_dolar
    cifra_origem = "$"
    cifra_destino = "R$"
else:
    res = quantidade / cotacao_dolar
    cifra_origem = "R$"
    cifra_destino = "$"

print("============== Dados da Conversão ==============")
print("Moeda Origem: " + moeda_origem)
print("Moeda Destino: " + moeda_destino)
print('Valor na Moeda de Origem: ' + cifra_origem + f'{round(quantidade,2)}')
print('Valor na Moeda de Destino: ' + cifra_destino + f'{round(res, 2)}')
print("============== Fim da Conversão ================")


