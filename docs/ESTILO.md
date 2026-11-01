# Guia de estilo · Memória de Trabalho

Vale para tudo o que o Memória de Trabalho publica: artigos, textos do site, descrições de episódio e posts. Quem escreve aqui (gente ou agente) lê isto antes.

## A voz

Escrevemos como uma colega de trabalho esperta conversando no café: **direta, franca, carismática e sem pose**. Dá para rir no meio do texto. A ironia e o sarcasmo são bem-vindos quando miram para cima: patrão, big tech, governo, lobby, a cultura de startup. Nunca miram no leitor, em colegas de trabalho ou em quem sabe menos.

- **Fale com "você".** O leitor trabalha com tecnologia, então jargão de TI pode ficar sem explicação. Conceito político e econômico (hegemonia, intercâmbio, Seção 301) sempre vem explicado na primeira vez que aparece.
- **Frase curta.** Uma ideia por frase. Se precisou de ponto e vírgula, provavelmente são duas frases.
- **Concreto antes de abstrato.** Comece pelo caso (a invoice que demora três dias para cair, o reels que some do feed) e só depois explique o mecanismo.
- **Sem pose acadêmica e sem tom de coach.** Nada de "neste artigo iremos abordar". Também nada de "transforme sua carreira".
- **Humor com fato embaixo.** A piada só funciona se a informação estiver certa. Primeiro o fato, depois a graça.

## Proibido

Estes tiques fazem o texto soar como máquina ou como palestra motivacional. O `scripts/revisar-estilo.py` acusa a maioria deles.

1. **Travessão e meia-risca** (`—` e `–`) como pausa ou aposto. Troque por vírgula, ponto, dois-pontos ou parênteses. Em intervalos, escreva "de 2010 a 2026".
2. **Hífen solto como travessão** (`palavra - palavra`).
3. **A fórmula da correção dramática:** "não é sobre X, é sobre Y", "não se trata de X, mas de Y", "mais do que X, é Y", "X? Não. É Y". Diga direto o que é.
4. **Tudo em três.** Listas de exatamente três itens, três adjetivos em fila, três exemplos sempre. Às vezes são dois, às vezes cinco. Varie de propósito.
5. **Clichês de texto gerado:** "vale ressaltar", "é importante destacar", "no fim do dia", "em suma", "mergulhar fundo", "navegar por", "jornada", "desvendar", "cenário" como muleta, "potencializar", "alavancar", "robusto", "um verdadeiro divisor de águas".
6. **Pergunta retórica em série** no começo de parágrafo. Uma de vez em quando, tudo bem.
7. **Exclamação** para dar empolgação. Se a frase precisa de exclamação, reescreva a frase.

Se uma linha precisar quebrar uma regra por um bom motivo (uma citação literal, por exemplo), marque o fim dela com `<!-- estilo: ok -->`.

## Fatos

- **Todo número e toda afirmação contestável têm fonte com link** na seção "Fontes".
- **A data em que as fontes foram conferidas** vai no campo `conferido` do artigo e aparece no topo da página.
- **Quando há disputa, os dois lados aparecem.** Ironia não substitui argumento do outro lado.
- **Nada de acusação sem documento.** "Fez lobby" só com registro público do lobby. Processo em andamento é acusação, não condenação, e o texto diz isso.
- **Citação literal curta**, entre aspas e com a fonte. Fonte em inglês pode ser traduzida, e aí não vai entre aspas.
- **Se não conseguiu confirmar, não publique o fato.** Ou escreva com a ressalva clara ("segundo a reportagem X, que não conseguimos confirmar na fonte original").

## Estrutura de um artigo

1. **Título** curto, com gancho. Pode ser pergunta, provocação ou piada.
2. **Linha fina:** uma ou duas frases dizendo do que se trata e por que importa.
3. **Para quem tem pressa:** o resumo em tópicos, quantos forem necessários (de preferência não três).
4. **Corpo** em seções com intertítulos que contam a história. Tabela quando houver dado comparável.
5. **E eu com isso?**: o que o assunto tem a ver com quem trabalha com tecnologia. Obrigatório.
6. **Para conversar:** perguntas para levar ao trabalho, ao grupo ou ao episódio. Opcional.
7. **Fontes:** lista com link, veículo e data.

## Exemplos

| Evite | Prefira |
|---|---|
| Não é sobre tecnologia, é sobre poder. | Toda tecnologia tem dono, e o dono decide as regras. |
| O Pix é rápido, gratuito e democrático. | O Pix cai na hora e não cobra nada de pessoa física. |
| Vale ressaltar que o SWIFT não move dinheiro. | O SWIFT não move um centavo. Ele move mensagens. |
| Neste artigo, vamos mergulhar no universo das maquininhas. | A maquininha cobra uma taxa. Vamos seguir esse dinheiro. |
| Isso muda tudo — e ninguém percebeu. | Isso muda bastante coisa, e quase ninguém percebeu. |
