# Dicionário de Dados das Incrições dos Participantes vida Eventbrite 

Dados: [../inscrições-particiantes.csv](../inscricoes-particiantes.csv)

Os dados informa a quantidade total de pessoas inscritas no evento, não importando se realizaram check-in válido.

- Colunas removidas:
```
Nº do pedido, Data do pedido, Nome, Sobrenome, E-mail, Quantidade, Nível de preço, Participante nº, Grupo, Tipo do pedido, Moeda, Total pago, Processamento de Pagamentos da Eventbrite, Taxas pagas, Status do participante, Endereço residencial 1, Endereço residencial 2, Cidade de residência, Estado de residência, CEP residencial, País de residência, Código Conduta / Código Conducta, Direitos de conteúdo e imagem,	Termo de consentimento para tratamento de dados pessoais / Consentimiento al tratamiento de datos personales, Tamanho de camiseta - apenas para pessoas que participarão presencialmente, Tem interesse em trazer crianças para ficar no espaço kids? O Espaço Kids terá vagas limitadas que serão distribuídas de acordo com a ordem de compra de ingressos, apenas para pessoas que participarão presencialmente, Quantas crianças utilizariam o espaço kids?, Qual a idade das crianças?, Endereço, Complemento, Cidade, Localidade, CEP, País

```

| column                                        | data_value                                                                                                                                             |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| tipo_ingresso                                 | Tipo de ingresso do evento. Os ingressos "inteira" e "meia-entrada" correspondem a inscrição no evento presencial. O "ingresso online" corresponde a inscrição no evento online.                                                                                                               |
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
| camiseta_tamanho                              | Tamanho de camiseta. Util para gerenciar % de camisetas de cada tamanho para prox eventos.                                                             |

| column                  | data_value                                                                 |
|------------------------------------------|------------------------------------------------------------------------------------------|
| n_do_pedido                              | Nº do pedido                                                                                         |
| data_do_pedido                           | Data do pedido                                                                                       |
| nome                                     | Nome                                                                                                 |
| sobrenome                                | Sobrenome                                                                                            |
| email                                    | E-mail                                                                                               |
| quantidade                               | Quantidade                                                                                           |
| nvel_de_preo                             | Nível de preço                                                                                       |
| tipo_de_ingresso                         | Tipo de ingresso                                                                                     |
| participante_n                           | Participante nº                                                                                      |
| grupo                                    | Grupo                                                                                                |
| tipo_do_pedido                           | Tipo do pedido                                                                                       |
| moeda                                    | Moeda                                                                                                |
| total_pago                               | Total pago                                                                                           |
| taxas_pagas                              | Taxas pagas                                                                                          |
| taxas_da_eventbrite                      | Taxas da Eventbrite                                                                                  |
| processamento_de_pagamentos_da_eventbrite | Processamento de Pagamentos da Eventbrite                                                            |
| status_do_participante                   | Status do participante                                                                               |
| endereo_residencial_1                    | Endereço residencial 1                                                                               |
| endereo_residencial_2                    | Endereço residencial 2                                                                               |
| cidade_de_residncia                      | Cidade de residência                                                                                 |
| estado_de_residncia                      | Estado de residência                                                                                 |
| cep_residencial                          | CEP residencial                                                                                      |
| pas_de_residncia                         | País de residência                                                                                   |
| como_voc_se_define__cmo_te_defines       | Como você se define / ¿Cómo te defines?                                                              |
| como_voc_se_identifica__cmo_te_identificas_ | Como você se identifica? / ¿Cómo te identificas?                                                     |
| faz_parte_da_populao_t_pessoa_transgnera_travesti__eres_parte_de_la_poblacin_transgnero_ | Faz parte da população T (pessoa transgênera, travesti)? / ¿Eres parte de la población transgénero?  |
| orientao_sexual__orientacin_sexual       | Orientação sexual / Orientación sexual                                                               |
| pessoa_com_necessidades_especficas__persona_con_necesidades_especiales_ | Pessoa com necessidades específicas? / Persona con necesidades especiales                            |
| em_qual_uf_voc_reside__dnde_vives_       | Em qual UF você reside? / ¿Dónde vives?                                                              |
| de_quais_edies_da_python_brasil_voc_j_participou__cules_ediciones_de_python_brasil_ya_asistiese | De quais edições da Python Brasil você já participou? / ¿Cuáles ediciones de Python Brasil ya asistiese? |
| voc_j_participou_de_algum_outro_evento_python__has_participado_de_alguno_otro_evento_de_la_comunidad_python | Você já participou de algum outro evento Python? / ¿Has participado de alguno otro evento de la comunidad Python? |
| voc_participou_de_outros_eventos_online_durante_a_pandemia_de_covid19__has_participado_de_otros_eventos_en_lnea_durante_la_pandemia_de_covid19 | Você participou de outros eventos online durante a pandemia de covid-19? / ¿Has participado de otros eventos en línea durante la pandemia de covid-19? |
| voc_programa_em_python__programas_con_python_ | Você programa em Python? / ¿Programas con Python?                                                    |
| como_voc_classificaria_seu_nvel_de_conhecimento_em_python__cmo_clasificas_tu_nivel_de_conocimiento_en_python_ | Como você classificaria seu nível de conhecimento em Python? / ¿Cómo clasificas tu nivel de conocimiento en Python?  |
| voc__estudante__eres_estudiante          | Você é estudante? / ¿Eres estudiante?                                                                |
| voc_trabalha_com_python__trabajas_con_python_ | Você trabalha com Python? / ¿Trabajas con Python?                                                    |
| voc_faz_parte_de_alguma_comunidade_local_grupy_pug_pyladies_afropython__haces_parte_de_alguna_comunidad_grupy_pug_pyladies_afropython_ | Você faz parte de alguma comunidade local? (grupy, PUG, PyLadies, AfroPython) / ¿Haces parte de alguna comunidad? (grupy, PUG, PyLadies, AfroPython)  |
| tamanho_de_camiseta                      | Tamanho de camiseta                                                                                  |
| de_qual_tutorial_voc_ir_participar_os_tutoriais_sero_exclusivamente_presenciais | De qual tutorial você irá participar? Os tutoriais serão exclusivamente PRESENCIAIS                  |
| regras_adicionais_sobre_tutoriais__leia_atentamente | Regras adicionais sobre tutoriais - leia atentamente                                                 |
| aplicabilidade_do_ingresso               | Aplicabilidade do ingresso                                                                           |
| termo_de_consentimento_para_tratamento_de_dados_pessoais__consentimiento_al_tratamiento_de_datos_personales | Termo de consentimento para tratamento de dados pessoais / Consentimiento al tratamiento de datos personales |
| direitos_de_contedo_e_imagem             | Direitos de conteúdo e imagem                                                                        |
| cdigo_conduta__cdigo_conducta            | Código Conduta / Código Conducta                                                                     |
| se_outro_qual__cul                       | Se outro, qual? / ¿Cuál?                                                                             |
| se_outro_qual__cul1                      | Se outro, qual? / ¿Cuál?.1                                                                           |
| se_outro_qual__cul2                      | Se outro, qual? / ¿Cuál?.2                                                                           |
| se_sim_qual__cul                         | Se sim, qual? / ¿Cuál?                                                                               |
| em_qual_pas_voc_reside__cul_pas          | Em qual país você reside? / ¿Cuál país?                                                              |
| se_sim_qual__cul1                        | Se sim, qual? / ¿Cuál?.1                                                                             |
| endereo                                  | Endereço                                                                                             |
| complemento                              | Complemento                                                                                          |
| cidade                                   | Cidade                                                                                               |
| localidade                               | Localidade                                                                                           |
| cep                                      | CEP                                                                                                  |
| pas                                      | País                                                                                                 |

