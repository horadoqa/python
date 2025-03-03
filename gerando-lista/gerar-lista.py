import csv

# Função para gerar o arquivo .txt com as URLs formatadas
def gerar_urls(input_csv, output_txt):
    # Abrir o arquivo CSV para leitura
    with open(input_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        
        # Abrir o arquivo TXT para escrita
        with open(output_txt, mode='w', encoding='utf-8') as output_file:
            for row in reader:
                uf = row['uf']
                capital = row['capital']
                municipio = row['municipio']
                
                # Formatar a URL
                url = f"https://g1.globo.com/{uf}/{capital}/eleicoes/2024/resultado-das-apuracoes/{municipio}.ghtml\n"
                
                # Escrever a URL no arquivo .txt
                output_file.write(url)

    print(f"Arquivo '{output_txt}' gerado com sucesso!")

# Chamar a função passando os nomes dos arquivos de entrada e saída
input_csv = 'brasil.csv'  # Nome do arquivo CSV de entrada
output_txt = 'urls_resultado.txt'  # Nome do arquivo TXT de saída

gerar_urls(input_csv, output_txt)
