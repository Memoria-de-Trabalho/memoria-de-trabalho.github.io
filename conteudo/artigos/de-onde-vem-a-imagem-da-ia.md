---
titulo: De onde vem a imagem que a IA desenha
linha_fina: Por trás de cada "foto de estúdio" gerada em dez segundos tem bilhões de imagens raspadas da internet, gente ganhando menos de dois dólares por hora para limpar a sujeira e uma pilha de processos sem dono definido.
eixo: Trabalho
data: 2026-11-01
ordem: 5
conferido: 2026-11-01
resumo: O LAION e os bilhões de imagens raspadas, os trabalhadores invisíveis que rotulam dados, os processos de Getty e de artistas, e quem é dono do que a IA gera no Brasil e nos EUA.
---

## Para quem tem pressa

- Os geradores de imagem aprenderam com bilhões de pares de imagem e texto raspados da web. Um dos maiores conjuntos, o LAION-5B, tem 5,85 bilhões de pares, e o próprio LAION avisa que as imagens continuam protegidas pelo direito autoral de quem as fez.
- Em 2023, pesquisadores de Stanford acharam links para material de abuso sexual infantil no LAION-5B. O conjunto saiu do ar e voltou limpo em 2024.
- Para deixar a IA apresentável, alguém precisa olhar o pior da internet e rotular. Uma investigação da revista TIME mostrou trabalhadores no Quênia ganhando menos de US$ 2 por hora para isso.
- Nos Estados Unidos, obra feita só por IA não tem direito autoral. No Brasil, a lei diz que autor é pessoa física, e o projeto que regula a IA está parado na Câmara desde que passou no Senado, em dezembro de 2024.

## Uma raspagem do tamanho da internet

O LAION é uma organização sem fins lucrativos alemã que monta conjuntos de dados abertos. Em março de 2022, ela publicou o LAION-5B: 5,85 bilhões de pares de imagem e texto. O método é quase engraçado de tão simples. Pega-se o Common Crawl (um arquivo gigante de páginas da web) e extrai-se toda tag de imagem que tenha texto alternativo. O `alt` que o seu time de acessibilidade pediu para preencher virou legenda de treino de IA.

O LAION distribui só os links e as legendas, sob licença aberta. Sobre as imagens em si, o aviso é direto: elas continuam sob o direito autoral de quem as fez. Ou seja, o conjunto aponta para bilhões de obras e deixa o problema jurídico para quem baixar.

Quem baixou foi muita gente. O Stable Diffusion 1.4, por exemplo, foi ajustado num subconjunto do LAION chamado "laion-aesthetics", segundo a própria ficha do modelo.

## A sujeira que ninguém filtrou

Raspar a internet inteira traz a internet inteira junto, com tudo de pior que ela tem. Em dezembro de 2023, o Observatório da Internet de Stanford encontrou no LAION-5B 1.008 links para material de abuso sexual infantil confirmado ou provável. O LAION tirou os conjuntos do ar logo em seguida.

Em agosto de 2024 saiu o Re-LAION-5B, limpo com listas de verificação de organizações de proteção à infância. No total, foram removidos 2.236 links suspeitos. E o próprio LAION passou a recomendar com todas as letras que esses conjuntos não sejam usados em produto comercial. Recomendação feita, claro, depois que vários produtos comerciais já tinham sido treinados.

## Os trabalhadores invisíveis

Para um modelo não devolver o pior da internet, alguém precisa ensinar o que é o pior. Isso é feito por gente, imagem por imagem e texto por texto.

Em janeiro de 2023, a revista TIME mostrou que a OpenAI contratou a empresa Sama para rotular textos tóxicos usando trabalhadores no Quênia. Eles levavam para casa entre US$ 1,32 e US$ 2 por hora, enquanto a OpenAI pagava à Sama US$ 12,50 por hora de trabalho, segundo os contratos. A Sama contestou parte dos números. Em fevereiro de 2022, a Sama também testou para a OpenAI a coleta de imagens sexuais e violentas, num lote de 1.400 imagens. A própria TIME diz que esse trabalho com imagens parece não ter relação com o ChatGPT. A Sama encerrou o contrato antes do previsto.

Rotular dado e moderar conteúdo é trabalho de tecnologia, feito em grande parte no Sul Global e pago por tarefa, sem vínculo nenhum. Se esse podcast é sobre quem trabalha com tecnologia, essa gente está no centro da conversa.

## Quem processou quem

**Getty Images contra Stability AI, no Reino Unido.** O banco de imagens acusou a dona do Stable Diffusion de usar o seu acervo no treino. Em novembro de 2025, a Alta Corte da Inglaterra decidiu que a Stability não cometeu violação de direito autoral, segundo o resumo da Wikipedia, que cita a revista The Economist. Nos Estados Unidos, em abril de 2026, um tribunal federal deixou seguir a maior parte das acusações da Getty, incluindo as de direito autoral e de marca.

**Artistas contra Stability, Midjourney e DeviantArt.** Em janeiro de 2023, as ilustradoras Sarah Andersen, Kelly McKernan e Karla Ortiz abriram uma ação coletiva nos Estados Unidos. Em agosto de 2024, o juiz deixou seguir as acusações de direito autoral e de marca. O processo continuava em 2026, ainda sem julgamento.

**Autores contra a Anthropic.** Em 2025, a empresa fechou um acordo de US$ 1,5 bilhão com autores de livros por causa de cópias não licenciadas usadas na formação do seu acervo. É texto e não imagem, mas virou a referência de quanto custa treinar com material que não é seu.

## E de quem é a imagem que a IA gera?

**Nos Estados Unidos**, a resposta curta é: de ninguém, se não houver autoria humana. O Escritório de Direitos Autorais publicou em janeiro de 2025 um relatório sobre a proteção do que a IA gera. Em março de 2025, um tribunal de apelação confirmou, no caso Thaler contra Perlmutter, que obra feita só por máquina não tem registro. Seleção e arranjo feitos por uma pessoa podem ser protegidos. O prompt sozinho, em geral, não basta.

**No Brasil**, a Lei de Direitos Autorais (Lei 9.610, de 1998) diz no artigo 11 que autor é a pessoa física criadora da obra. A lei é de antes da IA generativa, mas, pela letra dela, máquina não é autora. O resto vai ser decidido em tribunal ou em lei nova.

E a lei nova está empacada. O projeto de lei 2338/2023, o marco da inteligência artificial, foi aprovado pelo Senado em 10 de dezembro de 2024. O texto do Senado prevê que sistemas comerciais que usem obras protegidas paguem os titulares de direitos. Na Câmara, segundo a ficha oficial em 1º de novembro de 2026, o projeto aguarda o parecer do relator numa comissão especial. E o capítulo de direitos autorais, segundo quem acompanha a tramitação, é justamente o ponto de maior briga.

## E eu com isso?

Muita gente que trabalha com tecnologia está dos dois lados dessa história. Tem quem escreva o scraper e o pipeline de treino, e tem quem faça freela de rotulagem e avaliação de modelo para pagar as contas. Os dois são trabalho de tecnologia, e só um deles aparece no LinkedIn com foto sorrindo.

Algumas perguntas valem para o seu próximo projeto: de onde vêm os dados, quem consentiu, quem recebeu e quem limpou a sujeira. E, se você trabalha com rotulagem ou avaliação, a precarização desse serviço foi escrita num contrato por alguém. Contrato se renegocia, e em grupo se renegocia melhor.

## Para conversar

- O seu time já treinou ou ajustou modelo com dado raspado? Alguém perguntou de onde vinha?
- Quem deveria receber quando uma IA comercial aprende com uma obra: o autor, um fundo coletivo ou ninguém?
- Você já fez trabalho de rotulagem ou avaliação de IA? Como era o pagamento e o contrato?
- Se o PL 2338 fosse votado amanhã, o que você colocaria nele?

## Fontes

- LAION, [LAION-5B: an open large-scale dataset](https://laion.ai/blog/laion-5b/), 31 mar 2022.
- LAION, [nota sobre a manutenção dos conjuntos](https://laion.ai/notes/laion-maintenance/), 19 dez 2023.
- LAION, [Releasing Re-LAION-5B](https://laion.ai/blog/relaion-5b/), 30 ago 2024.
- CompVis, [ficha do modelo Stable Diffusion v1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4), Hugging Face.
- Billy Perrigo, [OpenAI Used Kenyan Workers on Less Than $2 Per Hour to Make ChatGPT Less Toxic](https://time.com/6247678/openai-chatgpt-kenya-workers/), TIME, 18 jan 2023.
- Wikipedia, [Stability AI](https://en.wikipedia.org/wiki/Stability_AI) (processos da Getty e de Andersen e outros), consultada em 1º nov 2026.
- Wikipedia, [Artificial intelligence and copyright](https://en.wikipedia.org/wiki/Artificial_intelligence_and_copyright) (Thaler contra Perlmutter e o acordo da Anthropic), consultada em 1º nov 2026.
- U.S. Copyright Office, [Copyright and Artificial Intelligence](https://www.copyright.gov/ai/), relatórios de 2024 e 2025.
- Planalto, [Lei nº 9.610, de 19 de fevereiro de 1998](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm).
- Câmara dos Deputados, [ficha de tramitação do PL 2338/2023](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262), consultada em 1º nov 2026.
- Merovian, [PL 2.338/2023: o marco legal da IA ainda espera a Câmara](https://merovian.app/blog/pl-2338-marco-legal-da-inteligencia-artificial), 2026.
