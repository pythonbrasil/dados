# Usage

## Gerar CSV original

1. Acesse o Eventbrite como administrador do evento
2. Vá em "Relatórios" > "Relatório de Participantes"
3. Selecione todas as colunas disponíveis
4. Clique em "Gerar Relatório" 
5. Faça o download do arquivo CSV gerado
6. Salve o arquivo como `inscricoes-participantes-original.csv` na pasta do ano correspondente

O arquivo original contém dados sensíveis que precisam ser tratados antes de serem publicados. Use os comandos abaixo para fazer a limpeza dos dados.

## Ambiente local
- Python: 3.12.1
- Criar um virtualenv com Python 3.12.1
- Instalar as dependências com `pip install -r requirements.txt`

## Comandos

### Normaliza os nomes das colunas


Normaliza os nomes das colunas do CSV para um formato padronizado:
- Converte para minúsculas
- Substitui espaços por underscores
- Remove caracteres especiais
- Mantém apenas letras, números e underscores

Por exemplo:
- "Nome do Participante" -> "nome_do_participante"
- "E-mail" -> "email"
- "Endereço Residencial 1" -> "endereco_residencial_1"


```python data-cleaner.py normalize-columns-cmd ../dados/python-brasil-2024/inscricoes-participantes-original.csv ../dados/python-brasil-2024/inscricoes-participantes.csv```

E use o output para como base para o dicionario de dados ;)

#### Remove colunas desnecessárias & sensíveis

Remove colunas sensíveis e desnecessárias do CSV, como dados pessoais dos participantes (nome, email, endereço etc). Por padrão remove as seguintes colunas se não forem especificadas outras:
   - nome
   - sobrenome 
   - email
   - participante_n
   - endereço residencial
   - cidade
   - estado
   - CEP
   - país
   - número do pedido


```python data-cleaner.py remove-columns-cmd ../dados/python-brasil-2024/inscricoes-participantes.csv ../dados/python-brasil-2024/inscricoes-participantes.csv```

### No caso de precisar alterar o separador de colunas

O arquivo CSV original do Eventbrite usa ponto e vírgula (;) como separador de colunas. Para manter a consistência com outros arquivos CSV do repositório, podemos alterar o separador para vírgula (,) usando o comando:


```python data-cleaner.py replace-separator-cmd ../dados/python-brasil-2024/inscricoes-participantes.csv ../dados/python-brasil-2024/inscricoes-participantes.csv```