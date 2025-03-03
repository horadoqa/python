# Status_Code

## **Documentação do Processo de Teste: Teste de Performance de Páginas Web**

### 1. **Objetivo**
O objetivo deste teste de performance é verificar como as páginas de um conjunto de URLs se comportam sob diferentes condições de carga, tempo de resposta e consumo de recursos. A partir dessa avaliação, será possível identificar gargalos de desempenho e potenciais melhorias para otimizar a experiência do usuário e a infraestrutura de servidores.

### 2. **Requisitos**

#### 2.1 **Requisito Funcional**
- O sistema deve ser capaz de testar a performance das páginas Web listadas em um arquivo de entrada contendo as URLs.
- Para cada URL, o sistema deve medir o tempo de resposta, a quantidade de recursos consumidos e a estabilidade da página sob diferentes cargas.

#### 2.2 **Requisito Técnico**
- O teste deve ser automatizado para permitir a execução de múltiplas simulações de carga.
- O sistema de testes deverá ser configurado para registrar os resultados de cada URL de forma clara e acessível, preferencialmente em um arquivo de relatório gerado automaticamente.
- O desempenho das páginas será analisado em relação a métricas como:
  - **Tempo de Resposta (Response Time)**: Tempo que a página leva para carregar completamente.
  - **Taxa de Transferência**: Quantidade de dados transferidos entre o servidor e o cliente.
  - **Uso de CPU e Memória**: Consumo de recursos do servidor durante o carregamento da página.
  - **Taxa de Sucesso/Erro**: Porcentagem de carregamentos bem-sucedidos em comparação com falhas.

#### 2.3 **Ferramentas Necessárias**
- **Ferramenta de Teste de Performance**: K6
- **Ferramenta de Monitoramento de Recursos**: Como o New Relic, Prometheus, ou ferramentas de monitoramento nativas do servidor.
- **Arquivo de Entrada**: Arquivo CSV ou TXT contendo uma lista de URLs para testar.

### 3. **Escopo do Teste**

#### 3.1 **URLs a Serem Testadas**
- O teste de performance será realizado em uma lista de URLs fornecidas em um arquivo `.csv` ou `.txt`. Cada URL deve representar uma página da web cujos tempos de resposta e estabilidade serão analisados.

#### 3.2 **Parâmetros de Teste**
- **Carga Simulada**: A carga será simulada com base em um número específico de usuários virtuais acessando simultaneamente as URLs. O número de usuários variará de acordo com o nível de teste (ex.: 10, 50, 100, 500 usuários).
- **Durabilidade do Teste**: O teste de carga será executado por um período pré-definido, por exemplo, 30 minutos, para verificar a estabilidade da página durante esse tempo.

#### 3.3 **Métricas a Serem Coletadas**
- **Tempo de Resposta**: Tempo total para que a página carregue completamente, desde a requisição inicial até a resposta final.
- **Taxa de Erros**: Número de erros 4xx (erro do cliente) ou 5xx (erro do servidor).
- **Throughput**: Taxa de transferência de dados entre o servidor e o cliente durante a execução do teste.
- **Utilização de Recursos do Servidor**: Monitoramento do uso de CPU e memória durante o carregamento das páginas.

### 4. **Procedimento de Execução**

#### 4.1 **Pré-Teste**
1. **Preparar Ambiente**: Certificar-se de que o ambiente de testes está pronto, ou seja, as URLs estão acessíveis e o servidor está configurado para monitoramento de performance.
2. **Carregar Lista de URLs**: Importar o arquivo `.csv` ou `.txt` com as URLs a serem testadas.
3. **Configuração do Sistema de Testes**: Definir o número de usuários virtuais, a duração do teste e outros parâmetros conforme o escopo do teste.
4. **Definir Objetivos do Teste**: Estabelecer benchmarks, como tempo máximo de resposta esperado (ex.: tempo de resposta inferior a 3 segundos).

#### 4.2 **Execução do Teste**
1. **Iniciar o Teste de Performance**: Começar a execução das simulações de carga nas URLs listadas.
2. **Monitoramento de Recursos**: Durante o teste, coletar dados sobre a utilização de CPU, memória e largura de banda dos servidores.
3. **Registrar Resultados**: Durante cada execução, registrar:
   - Tempo de resposta para cada URL.
   - Taxa de sucesso ou falha na resposta.
   - Erros identificados (se houver).
4. **Escalonamento da Carga**: Gradualmente aumentar o número de usuários virtuais para avaliar como o sistema lida com maiores cargas de tráfego.

#### 4.3 **Pós-Teste**
1. **Análise dos Resultados**: Após o teste, analisar os dados coletados, identificando possíveis gargalos de desempenho, erros e comportamento inesperado.
2. **Relatório de Desempenho**: Gerar um relatório detalhado, incluindo:
   - Tempos médios de resposta por URL.
   - Percentual de sucesso versus falhas.
   - Desempenho do servidor (uso de CPU, memória e throughput).
3. **Recomendações**: Fornecer recomendações de otimização baseadas nos resultados do teste, como redução do tempo de resposta ou balanceamento de carga.

### 5. **Critérios de Aceitação**
- **Tempo de Resposta**: O tempo de resposta deve ser inferior a um valor pré-definido (por exemplo, 3 segundos para 90% das requisições).
- **Taxa de Erros**: A taxa de erro deve ser inferior a 5%.
- **Capacidade de Suporte de Carga**: O sistema deve ser capaz de suportar a carga definida sem degradação significativa de desempenho.
- **Estabilidade**: O servidor deve manter um uso estável de recursos, sem picos ou falhas durante o teste.

### 6. **Riscos e Contingências**
- **Riscos Técnicos**: Falha na conexão com as URLs, problemas de rede durante os testes ou limitações da ferramenta de teste.
- **Contingências**: Caso ocorram falhas no ambiente de teste, será necessário realizar um novo teste em um ambiente controlado ou em uma URL específica para identificar a causa raiz.

### 7. **Conclusão**
Este processo de teste de performance ajudará a identificar quaisquer problemas de desempenho nas páginas da web fornecidas e garantir que o sistema possa suportar o tráfego esperado de usuários sem falhas ou lentidão excessiva. Baseado nos resultados, serão fornecidas sugestões para otimização do desempenho e melhorias na infraestrutura do servidor.