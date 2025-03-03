import { check, sleep } from 'k6';
import http from 'k6/http';

// Caminho do arquivo de URLs
const urlFilePath = './base/rj.txt';

// Ler as URLs do arquivo
const urls = open(urlFilePath).split('\n').filter(url => url.trim() !== '');

// Configuração de execução
export const options = {
    stages: [
      { duration: '30s', target: 10 },
      { duration: '1m', target: 10 },
      { duration: '0s', target: 0 },
    ],
  };

export default function () {
    // Iterar sobre cada URL e fazer a requisição
    urls.forEach((url) => {

        // Realizar a requisição GET
        const response = http.get(url);

        console.log(url);

        console.log('Response status code:', response.status);

        // Verificar se o status da resposta é 200 OK
        check(response, {
            'status é 200': (r) => r.status === 200,
            'status é 404': (r) => r.status === 404,
            //'tempo de resposta é menor que 3s': (r) => r.timings.duration < 3000,
        });

        sleep(1); // Pausa de 1 segundo entre as requisições
    });

}
