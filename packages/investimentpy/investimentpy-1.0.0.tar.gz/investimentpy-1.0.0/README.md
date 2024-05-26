# InvestPy

InvestPy é uma biblioteca Python para análise de investimentos. Ela permite obter dados de ações, calcular indicadores financeiros e visualizar gráficos de desempenho.

## Funcionalidades

- Obter dados históricos de ações usando a API do Alpha Vantage.
- Calcular retorno diário das ações.
- Visualizar gráficos de preços de fechamento das ações.

## Requisitos

- Python 3.6+
- pandas
- matplotlib
- requests
- pytest

## Instalação


1. Navegue até o diretório do projeto:
    ```sh
    cd investpy
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Configuração

Obtenha uma chave de API do [Alpha Vantage](https://www.alphavantage.co/support/#api-key) e substitua `'your_api_key'` pela sua chave de API nos exemplos abaixo.

#### Testes

Os testes são escritos usando `pytest`. Para rodar os testes, execute:
    ```sh
    pytest aula4/tests
    ```

## Estrutura do Projeto

    ```
    investpy/
    │
    ├── investpy/
    │   ├── __init__.py
    │   ├── dados.py
    │   ├── calculos.py
    │   └── visualizacao.py
    │
    ├── tests/
    │   └── test_investpy.py
    │
    ├── README.md
    ├── requirements.txt
    └── setup.py
    ```

## Contribuindo

1. Faça um fork do repositório
2. Crie uma nova branch (`git checkout -b feature/foobar`)
3. Commit suas mudanças (`git commit -am 'Add some feature'`)
4. Push para a branch (`git push origin feature/foobar`)
5. Abra um Pull Request

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.