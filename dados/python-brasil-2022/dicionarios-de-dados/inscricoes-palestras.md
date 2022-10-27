# Dicionário de Dados das Incrições dos Participantes vida Eventbrite 

Dados: [../inscrições-palestras.csv](../inscricoes-palestras.csv)

Os dados informa a quantidade total de pessoas inscritas no evento, não importando se realizaram check-in válido.

- Colunas removidas:
```
Nº do pedido, Data do pedido, Nome, Sobrenome, E-mail, Quantidade, Nível de preço, Participante nº, Grupo, Tipo do pedido, Moeda, Total pago, Processamento de Pagamentos da Eventbrite, Taxas pagas, Status do participante, Endereço residencial 1, Endereço residencial 2, Cidade de residência, Estado de residência, CEP residencial, País de residência, Código Conduta / Código Conducta, Direitos de conteúdo e imagem,	Termo de consentimento para tratamento de dados pessoais / Consentimiento al tratamiento de datos personales, Tamanho de camiseta - apenas para pessoas que participarão presencialmente, Tem interesse em trazer crianças para ficar no espaço kids? O Espaço Kids terá vagas limitadas que serão distribuídas de acordo com a ordem de compra de ingressos, apenas para pessoas que participarão presencialmente, Quantas crianças utilizariam o espaço kids?, Qual a idade das crianças?, Endereço, Complemento, Cidade, Localidade, CEP, País

```

| column                                        | data_value                                                                                                                                             |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| tipo_ingresso                                 | Tipo de ingresso do evento. Os ingressos "geral" e "meia-entrada" correspondem a inscrição no evento presencial. O "ingresso online" corresponde a inscrição no evento online.                                                                                                               |
| como_voce_se_define                           | Como você se define / ¿Cómo te defines?                                                                                                                |
| como_voce_se_define_se_outro                  | Se outro, qual? / ¿Cuál?                                                                                                                               |
| como_voce_se_indentifica                      | Como você se identifica? / ¿Cómo te identificas?                                                                                                       |
| como_voce_se_indentifica_se_outro             | Se outro, qual? / ¿Cuál?                                                                                                                               |
| faz_parte_da_populacao_t                      | Faz parte da população T (pessoa transgênera, travesti)? / ¿Eres parte de la población transgénero?                                                    |
| orientaca_sexual                              | Orientação sexual / Orientación sexual                                                                                                                 |
| orientaca_sexual_se_outro                     | Se outro, qual? / ¿Cuál?                                                                                                                               |
| pessoa_com_necessidade_especifica             | Pessoa com necessidades específicas? / Persona con necesidades especiales                                                                              |
| pessoa_com_necessidade_especifica_se_sim_qual | Se sim, qual? / ¿Cuál?                                                                                                                                 |
| uf                                            | Em qual UF você reside? / ¿Dónde vives?                                                                                                                |
| pais                                          | Em qual país você reside? / ¿Cuál país?                                                                                                                |
| edicoes_anteriores_pybr                       | De quais edições da Python Brasil você já participou? / ¿Cuáles ediciones de Python Brasil ya asistiese?                                               |
| eventos_pybr                                  | Você já participou de algum outro evento Python? / ¿Has participado de alguno otro evento de la comunidad Python?                                      |
| eventos_online                                | Você participou de outros eventos online durante a pandemia de covid-19? / ¿Has participado de otros eventos en línea durante la pandemia de covid-19? |
| programa_em_python                            | Você programa em Python? / ¿Programas con Python?                                                                                                      |
| nivel_python                                  | Como você classificaria seu nível de conhecimento em Python? / ¿Cómo clasificas tu nivel de conocimiento en Python?                                    |
| estudante                                     | Você é estudante? / ¿Eres estudiante?                                                                                                                  |
| trabalha_com_python                           | Você trabalha com Python? / ¿Trabajas con Python?                                                                                                      |
| parte_de_alguma_comunidade                    | Você faz parte de alguma comunidade local? (grupy, PUG, PyLadies, AfroPython) / ¿Haces parte de alguna comunidad? (grupy, PUG, PyLadies, AfroPython)   |
| comunidade_qual                               | Se sim; qual? / ¿Cuál?                                                                                                                                 |
