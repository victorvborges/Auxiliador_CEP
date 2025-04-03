from crewai import Agent, Task, Crew
import logging
import os

os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ChapterAgent:
    def __init__(self, role, goal, backstory):
        self.agent = Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            verbose=True
        )

def create_chapter_agents():
    agents = {
        'Introdução / Referencial Teórico': ChapterAgent(
    role='Especialista em Introdução e Revisão de Literatura Científica',
    goal=(
        "Elaborar o capítulo de Introdução e Revisão de Literatura, contextualizando o tema com base em "
        "referências teóricas relevantes e atuais. Apresentar citações no corpo do texto, seguindo as normas da ABNT, "
        "mas sem listar a seção de Referências. A lista de referências completa será gerada separadamente."
    ),
    backstory=(
        "Pesquisador especializado em redação acadêmica, com vasta experiência na elaboração de introduções e revisões "
        "de literatura para projetos de pesquisa científica, seguindo as normas ABNT e respeitando as exigências dos comitês de ética."
    )
    ).agent,

        'Problematização': ChapterAgent(
            role='Especialista em Formulação de Problemas de Pesquisa',
            goal=(
                "Delimitar um problema de pesquisa que decorra de um aprofundamento sobre o tema, "
                "formulando uma pergunta clara e precisa que guiará a investigação científica."
            ),
            backstory=(
                "Pesquisador com vasta experiência em formulação de problemas científicos. "
                "Especialista em metodologia de pesquisa com foco na construção de perguntas de pesquisa "
                "claras, objetivas e relevantes para a área do conhecimento."
            )
        ).agent,

        'Justificativa': ChapterAgent(
            role='Especialista em Elaboração de Justificativas de Pesquisa',
            goal=(
                "Descrever com clareza e profundidade a relevância do tema e da pesquisa, "
                "destacando as razões que justificam a realização do estudo. "
                "Explicar como a pesquisa contribui para a compreensão, intervenção ou solução do problema. "
                "Convencer o leitor sobre a importância e os benefícios que o estudo trará para a área de conhecimento e a sociedade."
            ),
            backstory=(
                "Pesquisador experiente em redação de justificativas de projetos científicos. "
                "Especialista em argumentação acadêmica, com foco em demonstrar a relevância, a atualidade e o impacto positivo de uma pesquisa. "
                "Capaz de convencer avaliadores de comitês de ética e de financiamento da necessidade e importância de realizar um estudo."
            )
        ).agent,

        'Objeto de estudo': ChapterAgent(
            role='Especialista em Delimitação de Objeto de Estudo',
            goal=(
                "Definir de forma clara e precisa o objeto de estudo da pesquisa, "
                "demonstrando sua relevância não apenas para o pesquisador, mas também para a comunidade acadêmica e a sociedade. "
                "O objeto de estudo deve representar o foco e o eixo central da investigação científica."
            ),
            backstory=(
                "Pesquisador experiente em metodologia científica, especializado em delimitação de objeto de estudo. "
                "Capaz de identificar e descrever o foco central de investigações com clareza e pertinência acadêmica."
            )
        ).agent,

        'Hipótese': ChapterAgent(
            role='Especialista em Formulação de Hipóteses Científicas',
            goal=(
                "Elaborar hipóteses científicas claras, que representem uma resposta suposta e provisória ao problema de pesquisa. "
                "A hipótese deve apresentar uma suposição fundamentada que será testada para verificar sua validade, "
                "indicando as variáveis principais que serão analisadas no processo de investigação científica."
            ),
            backstory=(
                "Cientista com experiência em pesquisa quantitativa e qualitativa, especializado na formulação de hipóteses testáveis. "
                "Capaz de estruturar hipóteses claras, provisórias e alinhadas com o problema de pesquisa para guiar investigações rigorosas."
            )
        ).agent,

        'Objetivos': ChapterAgent(
            role='Especialista em Definição de Objetivos de Pesquisa',
            goal=(
                "Definir com clareza os objetivos gerais e específicos da pesquisa. "
                "O objetivo geral deve apresentar uma visão ampla e global do que se deseja alcançar com o estudo, "
                "expressando a meta principal da investigação. Os objetivos específicos devem desdobrar o objetivo geral "
                "em etapas ou ações concretas que orientem a realização da pesquisa. Ambos devem ser escritos com verbos no infinitivo."
            ),
            backstory=(
                "Pesquisador com vasta experiência na elaboração de projetos de pesquisa, especializado em estruturar objetivos gerais e específicos "
                "de maneira clara, concisa e alinhada às normas acadêmicas. Focado em garantir que os objetivos sejam compreensíveis, viáveis e mensuráveis."
            )
        ).agent,

        'Metodologia': ChapterAgent(
            role='Especialista em Metodologia de Pesquisa Científica',
            goal=(
                "Elaborar o capítulo de Metodologia detalhado, organizado em subtópicos obrigatórios, "
                "apresentando o desenho da pesquisa, local, amostra, critérios de inclusão e exclusão, recrutamento, "
                "instrumentos de coleta e procedimentos, todos descritos no tempo verbal futuro do infinitivo, "
                "de acordo com as normas do CEP."
            ),
            backstory=(
                "Pesquisador experiente em metodologia científica, especializado na construção de projetos de pesquisa "
                "com foco na aprovação ética pelo Comitê de Ética em Pesquisa (CEP). Expert em redação acadêmica formal "
                "e elaboração de metodologias para estudos qualitativos e quantitativos."
            )
        ).agent,

        'Aspectos éticos': ChapterAgent(
            role='Especialista em Ética na Pesquisa com Seres Humanos',
            goal=(
                "Elaborar o capítulo Aspectos Éticos de um projeto de pesquisa científica, "
                "obedecendo às diretrizes do Conselho Nacional de Saúde, Resoluções 466/12 ou 510/16. "
                "Descrever claramente os riscos e benefícios aos participantes, "
                "e informar sobre o armazenamento seguro dos dados coletados sob responsabilidade do pesquisador responsável."
            ),
            backstory=(
                "Pesquisador membro de Comitê de Ética em Pesquisa com ampla experiência na elaboração e revisão de projetos "
                "que atendem às normativas éticas brasileiras. Especialista em assegurar a proteção dos participantes e a integridade científica da pesquisa."
            )
        ).agent,

        'Análise e Interpretação dos Dados': ChapterAgent(
            role='Especialista em Análise e Interpretação de Dados Científicos',
            goal=(
                "Elaborar a seção de Análise e Interpretação dos Dados, descrevendo com precisão os métodos de análise "
                "quantitativa ou qualitativa que serão utilizados. A análise deve estar alinhada aos objetivos da pesquisa, "
                "permitindo a comparação e o confronto de dados e evidências para a confirmação ou rejeição de hipóteses "
                "ou pressupostos do estudo."
            ),
            backstory=(
                "Especialista em estatística aplicada e análise qualitativa de dados, com experiência na interpretação de resultados "
                "de pesquisas científicas. Conhecedor de técnicas avançadas de análise, como estatística inferencial, análise temática e "
                "métodos mistos para pesquisas quantitativas e qualitativas."
            )
        ).agent,

        'Cronograma': ChapterAgent(
            role='Especialista em Planejamento e Gestão de Projetos Científicos',
            goal=(
                "Elaborar um cronograma detalhado para um projeto de pesquisa científica, "
                "dividido em etapas claras e específicas, dimensionadas mês a mês, considerando "
                "a possibilidade de algumas etapas ocorrerem simultaneamente e outras dependerem de etapas anteriores."
            ),
            backstory=(
                "Pesquisador e gestor de projetos acadêmicos, especializado em planejamento estratégico e desenvolvimento de cronogramas para propostas científicas, "
                "com foco em organização eficiente de etapas e recursos temporais."
            )
        ).agent,

        'Orçamento': ChapterAgent(
            role='Especialista em Elaboração de Orçamentos de Pesquisa Científica',
            goal=(
                "Elaborar um orçamento detalhado para a execução de um projeto de pesquisa científica, "
                "listando todos os custos previstos com materiais, serviços e recursos necessários à realização da pesquisa."
            ),
            backstory=(
                "Consultor financeiro com experiência em orçamentação de projetos acadêmicos, especializado em planejamento financeiro "
                "para pesquisa científica, considerando os requisitos exigidos por órgãos de financiamento e comitês de ética."
            )
        ).agent,

        'Referências': ChapterAgent(
            role='Especialista em Normalização de Referências',
            goal='Listar e formatar referências conforme as normas ABNT',
            backstory='Bibliotecário especializado em normalização e referências acadêmicas.'
        ).agent,

        'Anexos/Apêndices': ChapterAgent(
            role='Especialista em Documentação de Projetos de Pesquisa Científica',
            goal=(
                "Organizar e listar todos os documentos anexos e apêndices necessários para a submissão de um projeto de pesquisa ao CEP, "
                "incluindo carta de anuência, termos de consentimento, instrumentos de coleta de dados e outros documentos exigidos."
            ),
            backstory=(
                "Especialista em documentação técnica de projetos científicos, com ampla experiência em preparar documentos de suporte "
                "para submissão a comitês de ética e órgãos financiadores, garantindo conformidade ética e legal."
            )
        ).agent
    }

    return agents

def create_task_for_chapter(capitulo_nome, tema, contexto_anterior, agente_capitulo):
    contexto = f"Texto anterior do projeto:\n{contexto_anterior}\n\n" if contexto_anterior else ""

    if capitulo_nome == 'Referências':
        prompt = (
            f"{contexto}"
            "Agora, escreva exclusivamente o conteúdo do capítulo 'Referências'.\n"
            "Liste todas as referências bibliográficas mencionadas nos capítulos anteriores.\n"
            "Formate as referências de acordo com as normas ABNT.\n"
            "Inclua apenas as referências, sem comentários ou explicações adicionais.\n"
        )
    elif capitulo_nome == 'Introdução / Referencial Teórico':
        prompt = (
            f"{contexto}"
            f"Agora, escreva exclusivamente o conteúdo do capítulo '{capitulo_nome}'.\n"
            f"O tema do projeto é: {tema}.\n\n"

            "O capítulo deve conter uma introdução teórica sobre o tema abordado, com base em revisão de literatura atualizada.\n"
            "Faça citações no corpo do texto, conforme as normas da ABNT (ex: AUTOR, ano), mas NÃO insira a lista de referências bibliográficas ao final.\n\n"

            "A Introdução deve situar o tema dentro da área de pesquisa, contextualizando-o, justificando sua relevância e apresentando os objetivos do estudo.\n"
            "Elabore um texto coeso e coerente, mantendo a linguagem formal e científica.\n\n"

            "Importante:\n"
            "- NÃO escreva 'Referências' ao final do capítulo.\n"
            "- As referências completas serão listadas no capítulo específico de Referências Bibliográficas.\n"
    )
    elif capitulo_nome == 'Problematização':
        prompt = (
            f"{contexto}"
            f"Agora, escreva exclusivamente o conteúdo do capítulo '{capitulo_nome}'.\n"
            f"O tema do projeto é: {tema}.\n"
            "Este capítulo deve conter:\n"
            "- Uma explicação que demonstre o aprofundamento sobre o tema;\n"
            "- A formulação de uma pergunta clara e precisa que expressa o problema de pesquisa;\n"
            "- A justificativa lógica que conduza à pergunta formulada;\n"
            "- Evite repetições de conteúdo de outros capítulos e mantenha a coesão textual.\n"
            "Use linguagem formal, objetiva e acadêmica.\n"
        )
    elif capitulo_nome == 'Justificativa':
        prompt = (
            f"{contexto}"
            f"Agora, escreva exclusivamente o conteúdo do capítulo '{capitulo_nome}'.\n"
            f"O tema do projeto é: {tema}.\n"
            "Este capítulo deve conter:\n"
            "- A demonstração clara da relevância do tema escolhido;\n"
            "- As razões que justificam a realização desta pesquisa;\n"
            "- As contribuições que a pesquisa pode trazer para a compreensão, intervenção ou solução do problema de pesquisa;\n"
            "- Argumentos convincentes que destaquem a importância da pesquisa proposta em relação a outros temas;\n"
            "- Vantagens, benefícios e impactos esperados a partir da realização do estudo;\n"
            "- Linguagem persuasiva, formal e acadêmica para convencer o leitor da importância de efetivar a pesquisa.\n"
        )
    elif capitulo_nome == 'Objeto de estudo':
        prompt = (
            f"{contexto}"
            f"Agora, escreva exclusivamente o conteúdo do capítulo '{capitulo_nome}'.\n"
            f"O tema do projeto é: {tema}.\n"
            "Este capítulo deve conter:\n"
            "- A definição clara e objetiva do objeto de estudo;\n"
            "- A demonstração de que o objeto de estudo é relevante não apenas para o pesquisador, mas também para a comunidade acadêmica e para a sociedade;\n"
            "- A explicação de que o objeto representa o foco e o eixo central da investigação científica;\n"
            "- Linguagem formal, objetiva e acadêmica.\n"
        )
    elif capitulo_nome == 'Hipótese':
        prompt = (
            f"{contexto}"
            f"Agora, escreva exclusivamente o conteúdo do capítulo '{capitulo_nome}'.\n"
            f"O tema do projeto é: {tema}.\n"
            "Este capítulo deve conter:\n"
            "- A formulação de uma hipótese clara e objetiva, que represente uma resposta provisória ao problema de pesquisa;\n"
            "- Uma explicação de como a hipótese será testada para verificar sua validade;\n"
            "- A identificação das variáveis que serão analisadas para legitimar ou não a hipótese;\n"
            "- Reforçar que a hipótese é provisória e faz parte do processo de investigação científica;\n"
            "- Linguagem formal, objetiva e acadêmica.\n"
        )
    elif capitulo_nome == 'Objetivos':
        prompt = (
            f"{contexto}"
            f"Agora, escreva exclusivamente o conteúdo do capítulo '{capitulo_nome}'.\n"
            f"O tema do projeto é: {tema}.\n"
            "Este capítulo deve conter duas seções claramente separadas:\n\n"
            "OBJETIVOS\n\n"
            "1 Geral:\n"
            "- Defina o objetivo geral da pesquisa.\n"
            "- O objetivo geral deve expressar uma visão ampla e global da meta principal do estudo.\n"
            "- Descreva o que se deseja alcançar ao término da investigação.\n"
            "- Utilize verbos no infinitivo (por exemplo: Analisar, Investigar, Avaliar, Identificar).\n\n"
            "2 Específicos:\n"
            "- Liste pelo menos 3 a 5 objetivos específicos que detalhem e desdobrem o objetivo geral.\n"
            "- Cada objetivo específico deve ser uma meta a ser alcançada ao final da investigação.\n"
            "- Use verbos no infinitivo em todos os objetivos específicos (por exemplo: Analisar, Verificar, Compreender, Avaliar).\n\n"
            "Seja claro, objetivo e utilize linguagem formal científica.\n"
        )
    elif capitulo_nome == 'Metodologia':
        prompt = (
            f"{contexto}"
            f"Agora, escreva exclusivamente o conteúdo do capítulo '{capitulo_nome}'.\n"
            f"O tema do projeto é: {tema}.\n\n"

            "O capítulo Metodologia deve ser redigido obrigatoriamente no tempo verbal FUTURO DO INFINITIVO, "
            "porque a pesquisa só poderá ser realizada após a aprovação do projeto pelo CEP.\n\n"

            "Organize o texto com os seguintes subtópicos, respeitando a estrutura abaixo:\n\n"

            "METODOLOGIA\n\n"

            "1 Desenho da Pesquisa (tipo de estudo):\n"
            "- Identificar o tipo de abordagem metodológica que se utilizará para responder à questão de pesquisa.\n"
            "- Exemplos: pesquisa observacional, descritiva, explicativa, analítica; quantitativa, qualitativa; transversal, longitudinal; ensaios clínicos, estudos de coorte, etc.\n\n"

            "2 Local da pesquisa:\n"
            "- Descrever onde os dados serão coletados.\n"
            "- Exemplo: A pesquisa será realizada em instituições de ensino superior localizadas na cidade de XYZ.\n\n"

            "3 Amostra de Participantes:\n"
            "- Estimar o número de participantes.\n"
            "- Descrever a previsão de amostra e mencionar que o cálculo amostral será de competência do pesquisador responsável.\n"
            "- Recomendar o contato com um estatístico.\n\n"

            "4 Critérios de Inclusão e Exclusão:\n"
            "- Critérios de Inclusão: Definir as principais características da população alvo e acessível.\n"
            "- Critérios de Exclusão: Indicar o subgrupo de indivíduos que, mesmo preenchendo os critérios de inclusão, apresentem características que possam interferir na qualidade dos dados.\n\n"

            "5 Recrutamento dos Participantes:\n"
            "- Descrever como será feito o recrutamento dos participantes ou a seleção de dados secundários.\n"
            "- Exemplo: O recrutamento será realizado por meio de convites em redes sociais, e-mails institucionais, etc.\n\n"

            "6 Instrumentos de Coleta de Dados:\n"
            "- Detalhar todos os instrumentos físicos e critérios de classificação que serão utilizados.\n"
            "- Exemplo: Serão utilizados questionários validados, entrevistas semiestruturadas, etc.\n\n"

            "7 Procedimentos para a coleta de dados:\n"
            "- Descrever detalhadamente o passo a passo de como a coleta será realizada.\n"
            "- Exemplo: Após a assinatura do Termo de Consentimento Livre e Esclarecido (TCLE), os participantes responderão a um questionário eletrônico.\n\n"

            "Importante:\n"
            "- Todo o texto deve ser formal, técnico, detalhado e escrito no tempo verbal futuro do infinitivo.\n"
        )
    elif capitulo_nome == 'Aspectos éticos':
        prompt = (
            f"{contexto}"
            f"Agora, escreva exclusivamente o conteúdo do capítulo '{capitulo_nome}'.\n"
            f"O tema do projeto é: {tema}.\n\n"

            "O capítulo deve seguir as normas do Conselho Nacional de Saúde e estar de acordo com a Resolução 466/12 ou 510/16.\n\n"
            "Estruture o texto com as seguintes seções:\n\n"

            "ASPECTOS ÉTICOS\n\n"

            "Introdução:\n"
            "- Informar que a pesquisa obedecerá aos preceitos éticos da Resolução 466/12 ou 510/16 do Conselho Nacional de Saúde.\n"
            "- Exemplo: A realização da presente pesquisa obedecerá aos preceitos éticos da Resolução 466/12 ou 510/16 do Conselho Nacional de Saúde (CNS).\n\n"

            "Riscos:\n"
            "- Descrever quais riscos os procedimentos da pesquisa poderão oferecer aos participantes.\n"
            "- Explicar como tais riscos serão minimizados.\n"
            "- Exemplo: Os riscos serão mínimos e relacionados ao desconforto emocional durante entrevistas. Para minimizar, os participantes poderão interromper sua participação a qualquer momento.\n\n"

            "Benefícios:\n"
            "- Descrever os benefícios diretos ou indiretos aos participantes.\n"
            "- Exemplo: Os participantes poderão se beneficiar de uma reflexão crítica sobre a temática abordada, além de contribuir para o avanço do conhecimento científico.\n\n"

            "Armazenamento dos dados coletados:\n"
            "- Informar que os dados coletados serão armazenados de maneira segura.\n"
            "- Especificar o tipo de dados (ex: entrevistas gravadas, formulários online, etc.).\n"
            "- Informar o local e meio de armazenamento (ex: servidor criptografado, arquivos físicos em local seguro).\n"
            "- Declarar o responsável pelo armazenamento, o endereço completo e o período mínimo de guarda de 5 anos.\n"
            "- Exemplo: Os dados coletados (entrevistas gravadas em áudio e questionários eletrônicos) ficarão armazenados em servidor criptografado, sob a responsabilidade do pesquisador [NOME DO PESQUISADOR], no endereço [ENDEREÇO COMPLETO], pelo período mínimo de 5 anos.\n\n"

            "Importante:\n"
            "- Seja claro, objetivo e utilize linguagem formal e acadêmica.\n"
        )
    elif capitulo_nome == 'Análise e Interpretação dos Dados':
        prompt = (
            f"{contexto}"
            f"Agora, escreva exclusivamente o conteúdo do capítulo '{capitulo_nome}'.\n"
            f"O tema do projeto é: {tema}.\n\n"

            "Este capítulo deve descrever detalhadamente os métodos de análise dos dados coletados na pesquisa.\n"
            "A estrutura do capítulo deve incluir os seguintes pontos:\n\n"

            "ANÁLISE E INTERPRETAÇÃO DOS DADOS\n\n"

            "Métodos de Análise de Dados:\n"
            "- Explicar como os dados coletados serão analisados.\n"
            "- Indicar se será uma análise quantitativa, qualitativa ou mista.\n"
            "- Exemplo: A análise quantitativa será realizada utilizando estatística descritiva e inferencial para testar as hipóteses levantadas.\n\n"

            "Relação com os Objetivos da Pesquisa:\n"
            "- Demonstrar como a análise dos dados permitirá atingir os objetivos do estudo.\n"
            "- Exemplo: A categorização dos dados permitirá avaliar padrões de comportamento entre os participantes.\n\n"

            "Comparação e Confrontação dos Dados:\n"
            "- Explicar como os dados serão comparados e confrontados com a literatura existente.\n"
            "- Destacar a relação dos resultados com os pressupostos e hipóteses do estudo.\n"
            "- Exemplo: Os dados coletados serão analisados estatisticamente e comparados com estudos prévios para verificar a consistência das conclusões.\n\n"

            "Validação dos Resultados:\n"
            "- Indicar se serão utilizadas técnicas de triangulação de dados ou métodos de validação estatística.\n"
            "- Exemplo: Os resultados qualitativos serão validados por meio da triangulação de fontes e revisão por pares.\n\n"

            "Importante:\n"
            "- O texto deve ser acadêmico, claro e seguir as normas metodológicas da área de pesquisa.\n"
            "- Evite repetições de conteúdo e mantenha a coesão textual.\n"
        )
    elif capitulo_nome == 'Cronograma':
        prompt = (
            f"{contexto}"
            f"Agora, escreva exclusivamente o conteúdo do capítulo '{capitulo_nome}'.\n"
            f"O tema do projeto é: {tema}.\n\n"

            "O cronograma deve ser apresentado de forma detalhada, contemplando as seguintes regras:\n\n"

            "- A pesquisa deve ser dividida em partes (etapas) detalhadas, de acordo com as atividades necessárias para a sua execução.\n"
            "- Cada etapa deve conter a previsão do tempo necessário, mês a mês.\n"
            "- Algumas etapas podem ser executadas simultaneamente; outras só podem ser iniciadas após a conclusão de etapas anteriores.\n"
            "- O cronograma deve refletir o tempo disponível para a execução da pesquisa.\n"
            "- Apresente as informações de forma clara, objetiva e organizada.\n\n"

            "Sugestão de etapas (pode adaptar ao tema específico do projeto):\n"
            "1. Levantamento bibliográfico\n"
            "2. Definição da metodologia\n"
            "3. Submissão e aprovação no CEP\n"
            "4. Coleta de dados\n"
            "5. Análise de dados\n"
            "6. Interpretação e discussão dos resultados\n"
            "7. Redação do relatório final\n"
            "8. Revisão e ajustes\n"
            "9. Apresentação ou defesa do projeto\n\n"

            "Exemplo de formatação do cronograma:\n\n"
            "| Etapas                                    | Mês 1 | Mês 2 | Mês 3 | Mês 4 | Mês 5 | Mês 6 | Mês 7 | Mês 8 |\n"
            "|-------------------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|\n"
            "| Levantamento bibliográfico                |   X   |   X   |       |       |       |       |       |       |\n"
            "| Definição da metodologia                  |       |   X   |   X   |       |       |       |       |       |\n"
            "| Submissão e aprovação no CEP              |       |       |   X   |       |       |       |       |       |\n"
            "| Coleta de dados                           |       |       |       |   X   |   X   |       |       |       |\n"
            "| Análise de dados                          |       |       |       |       |   X   |   X   |       |       |\n"
            "| Interpretação e discussão dos resultados  |       |       |       |       |       |   X   |   X   |       |\n"
            "| Redação do relatório final                |       |       |       |       |       |       |   X   |   X   |\n"
            "| Revisão e ajustes                         |       |       |       |       |       |       |       |   X   |\n"
            "| Apresentação ou defesa do projeto         |       |       |       |       |       |       |       |   X   |\n\n"

            "Importante:\n"
            "- O cronograma deve ser realista e coerente com as exigências do Comitê de Ética em Pesquisa (CEP).\n"
            "- Utilize linguagem formal e objetiva.\n"
        )
    elif capitulo_nome == 'Orçamento':
        prompt = (
            f"{contexto}"
            f"Agora, escreva exclusivamente o conteúdo do capítulo '{capitulo_nome}'.\n"
            f"O tema do projeto é: {tema}.\n\n"

            "Elabore um orçamento detalhado, prevendo todos os gastos necessários para a realização da pesquisa.\n\n"

            "O orçamento deve conter:\n"
            "- A lista dos itens e serviços necessários para a realização do projeto.\n"
            "- A quantidade de cada item.\n"
            "- O valor estimado de cada item.\n"
            "- O custo total previsto para a execução do projeto.\n"
            "- Os valores devem ser apresentados em moeda corrente (R$).\n"
            "- Incluir materiais de consumo (papel, canetas, lápis), serviços (hora/computador, xerox, encadernação, revisão, formatação, artes gráficas), "
            "equipamentos (se necessário), e quaisquer outras especificidades relacionadas ao projeto.\n\n"

            "Exemplo de estrutura:\n\n"
            "| Item                      | Quantidade | Valor Unitário (R$) | Custo Total (R$) |\n"
            "|---------------------------|------------|---------------------|------------------|\n"
            "| Papel A4 (resma)          | 5          | 35,00               | 175,00           |\n"
            "| Canetas                   | 10         | 3,00                | 30,00            |\n"
            "| Lápis                     | 5          | 2,50                | 12,50            |\n"
            "| Hora/computador (locação) | 20         | 15,00               | 300,00           |\n"
            "| Xerox (cópias)            | 200        | 0,20                | 40,00            |\n"
            "| Encadernação (relatório)  | 3          | 25,00               | 75,00            |\n"
            "| Revisão e formatação      | 1          | 500,00              | 500,00           |\n"
            "| Artes gráficas (posters)  | 2          | 150,00              | 300,00           |\n"
            "| Equipamento (gravador)    | 1          | 250,00              | 250,00           |\n\n"

            "Ao final, some o custo total previsto e informe o valor final do orçamento.\n\n"

            "Importante:\n"
            "- Use linguagem formal e técnica.\n"
            "- Deixe claro que os valores são previsões.\n"
        )
    elif capitulo_nome == 'Anexos/Apêndices':
        prompt = (
            f"{contexto}"
            f"Agora, escreva exclusivamente o conteúdo do capítulo '{capitulo_nome}'.\n"
            f"O tema do projeto é: {tema}.\n\n"

            "O capítulo deve listar e descrever brevemente todos os documentos que serão anexados ou apresentados como apêndices no projeto de pesquisa.\n\n"

            "Exemplos de documentos que devem ser mencionados:\n"
            "- Carta de Anuência: documento assinado pela instituição onde será realizada a pesquisa, autorizando sua execução.\n"
            "- Termo de Consentimento Livre e Esclarecido (TCLE) e Termo de Assentimento Livre e Esclarecido (TALE): documentos que asseguram que os participantes estão cientes dos objetivos e riscos do estudo.\n"
            "- Termo de Confidencialidade: documento que garante o sigilo e a proteção dos dados dos participantes.\n"
            "- Instrumentos de Coleta de Dados: questionários, roteiros de entrevista, fichas de avaliação ou qualquer outro instrumento utilizado para a coleta de dados.\n\n"

            "Estruture o texto da seguinte forma:\n\n"
            "ANEXOS / APÊNDICES\n\n"
            "Anexo A - Carta de Anuência\n"
            "Documento emitido pela instituição parceira, autorizando a realização da pesquisa em suas dependências.\n\n"

            "Anexo B - Termo de Consentimento Livre e Esclarecido (TCLE)\n"
            "Documento que informa os participantes sobre os objetivos, riscos e benefícios da pesquisa, garantindo sua participação voluntária.\n\n"

            "Anexo C - Termo de Assentimento Livre e Esclarecido (TALE)\n"
            "Documento voltado para participantes menores de idade ou legalmente incapazes, garantindo a compreensão e o consentimento para participação.\n\n"

            "Anexo D - Termo de Confidencialidade\n"
            "Documento que assegura a confidencialidade das informações obtidas durante a pesquisa.\n\n"

            "Anexo E - Instrumento de Coleta de Dados\n"
            "Cópias dos questionários, roteiros de entrevistas ou fichas de avaliação que serão utilizados na coleta de dados.\n\n"

            "Importante:\n"
            "- Seja formal e objetivo.\n"
            "- Não insira os documentos completos, apenas a descrição de que eles compõem os anexos/apêndices.\n"
            "- Siga as normas da ABNT.\n"
        )
    else:
        prompt = (
            f"{contexto}"
            f"Agora, escreva exclusivamente o conteúdo do capítulo '{capitulo_nome}'.\n"
            f"O tema do projeto é: {tema}.\n"
            "O texto deve ser coeso, sem repetir informações dos capítulos anteriores.\n"
            "Não inclua a lista de referências bibliográficas neste capítulo.\n"
            "Não escreva 'Referências' ou qualquer menção a fontes no final.\n"
            "Siga rigorosamente as normas acadêmicas e referências da ABNT.\n"
            "Seja claro, objetivo e mantenha a linguagem formal científica.\n"
        )

    task = Task(
        description=prompt,
        expected_output=f"Conteúdo completo para o capítulo '{capitulo_nome}' com profundidade acadêmica.",
        agent=agente_capitulo
    )

    return [task]

def run_chapter_crew(capitulo_nome, tema, contexto_anterior):
    agents = create_chapter_agents()
    agente_capitulo = agents.get(capitulo_nome)

    if not agente_capitulo:
        raise ValueError(f"Agente para o capítulo '{capitulo_nome}' não encontrado.")

    tasks = create_task_for_chapter(capitulo_nome, tema, contexto_anterior, agente_capitulo)

    crew = Crew(
        agents=[agente_capitulo],
        tasks=tasks,
        verbose=True
    )

    logging.info(f"Iniciando CrewAI para o capítulo: {capitulo_nome}")

    resultado = crew.kickoff()

    if hasattr(resultado, 'result'):
        return resultado.result

    return str(resultado)
