---
titulo: O feed tem gerente
linha_fina: O Instagram jura que não tem "um algoritmo". Tem vários, com uns 700 candidatos por rolagem e uma dúzia de apostas sobre o que você vai fazer. Fomos ler o que a própria empresa publica.
eixo: Tecnologia
data: 2026-11-01
ordem: 3
conferido: 2026-11-01
resumo: Como o Instagram decide quem vê o quê, contado pela própria Meta. E por que a pergunta mais interessante é quem escolhe o que o sistema tenta maximizar.
---

## Para quem tem pressa

- O Instagram diz que não tem um algoritmo único. Feed, Stories, Explorar e Reels têm cada um o seu sistema de ranqueamento.
- No feed, segundo a ficha técnica publicada pela Meta em junho de 2026, um modelo leve separa uns 700 posts candidatos e outro calcula uma nota de relevância para uns 500. A nota sai de previsões do tipo "qual a chance de você compartilhar isso por mensagem".
- Desde 2024 a empresa vem punindo repost e conta que só republica conteúdo alheio, e em 2026 estendeu a regra para fotos e carrosséis.
- Toda essa engenharia serve a um objetivo que alguém escolheu. As métricas mudam o que milhões de pessoas veem, e quem mexe nelas tem crachá.

## Começou com um problema de engenharia

Em 2021, o chefe do Instagram, Adam Mosseri, publicou um texto para explicar como o app funciona. A justificativa para ranquear o feed vem logo no começo: em 2016, as pessoas já perdiam 70% de todos os posts do feed, porque seguiam gente demais para ver tudo. A ordem cronológica tinha virado uma fila que ninguém alcançava.

A solução foi ordenar por previsão de interesse. E, como toda decisão de engenharia que vira produto, essa também mudou de dono no caminho: a ordem passou a servir ao que a empresa quer que você faça.

Mosseri repete uma frase que virou mantra da empresa: o Instagram não tem um algoritmo singular. Cada parte do app (Feed, Stories, Explorar, Reels, busca) tem o seu, ajustado ao jeito como as pessoas usam aquela tela.

## Como o feed escolhe, segundo a própria Meta

A Meta publica "fichas de sistema" explicando o ranqueamento. A do feed do Instagram foi atualizada em 29 de junho de 2026 e descreve uma linha de montagem com duas etapas:

1. Um modelo leve passa pelo inventário de posts das contas que você segue e seleciona uns 700 mais relevantes.
2. Modelos mais pesados calculam uma nota de relevância para uns 500 deles, e a ordem do seu feed sai dessa nota.

A nota é a soma de várias apostas sobre o seu comportamento. A ficha lista, entre as principais:

- a chance de você gostar do post;
- a chance de você mandar o post para alguém por mensagem direta;
- a chance de você pular o post;
- quanto tempo você deve passar olhando para ele.

Para fazer essas apostas, o sistema usa sinais como a sua atividade recente, informações sobre o post, informações sobre quem postou e o seu histórico de interação com essa pessoa. A própria ficha cita detalhes deliciosamente específicos, como quantas vezes você tocou no botão de compartilhar nos últimos 28 dias. Em 2023, Mosseri disse que os sinais são milhares e as previsões, cerca de uma dúzia.

Os posts sugeridos (de contas que você não segue) e os anúncios vêm de outros sistemas, com fichas próprias. No Explorar, a maior parte do conteúdo é de gente que você não segue, e a popularidade do post pesa bem mais.

## A guerra contra o repost

Em abril de 2024, o Instagram anunciou uma mudança de regra que mexeu com muita conta grande:

- conta que posta repetidamente conteúdo dos outros sem acrescentar nada (dez vezes ou mais em 30 dias) deixa de aparecer nas recomendações, e só quem já segue continua vendo;
- quando há cópia exata, o original substitui o repost nas recomendações, e quem criou recebe aviso;
- repost passa a levar um selo com link para a conta de quem criou;
- reels de contas menores passam a ser mostrados primeiro para um público pequeno, siga ele a conta ou não, e ganham alcance se forem bem.

Em fevereiro de 2025, a empresa disse que tudo isso já estava no ar para todo mundo. Em abril de 2026, estendeu a regra de originalidade para fotos e carrosséis e afirmou que, nos Estados Unidos, 75% das recomendações já vinham de posts originais. Repostar com borda, marca d'água ou legenda nova não conta como original.

E, desde dezembro de 2025, existe o "Seu algoritmo": o app mostra um resumo dos assuntos que acha que você curte e deixa você ajustar. Começou nos Reels, chegou ao Explorar em abril de 2026 e, desde junho de 2026, vale para o app inteiro. É a primeira vez que a empresa deixa você ver uma parte do perfil que ela montou de você.

## O que a empresa nega

Mosseri escreveu que o Instagram não esconde conteúdo para forçar ninguém a comprar anúncio. Acreditar ou não fica com você. O que dá para dizer é que a empresa nunca precisou esconder nada para ganhar dinheiro com atenção: basta ordenar.

Em 2021, uma ex-funcionária vazou para o Wall Street Journal documentos internos que ficaram conhecidos como Facebook Files. Entre eles estavam pesquisas que a própria empresa fazia desde 2018 sobre os efeitos do Instagram em usuários jovens. A empresa sabia mais sobre o próprio produto do que contava em público, o que não é exatamente uma surpresa, mas foi bom ver em documento.

## A pergunta que a ficha técnica não responde

A ficha explica como o sistema prevê. Ela não explica por que essas previsões e não outras. A escolha de somar "chance de compartilhar" com "tempo olhando" e "chance de pular", com pesos que ninguém de fora conhece, é uma decisão de negócio que chega ao time de engenharia como OKR.

Quem já trabalhou com recomendação conhece o roteiro. Alguém define a métrica norte, alguém faz o teste A/B, alguém comemora o ganho de 0,3% em retenção. Ninguém na sala precisa ser mau para o resultado ser ruim. Basta todo mundo otimizar a coisa errada com muita competência.

## E eu com isso?

Se você trabalha com produto, dados ou machine learning, você é o gerente do feed de alguém. A métrica que o seu time persegue decide o que milhões de pessoas veem antes de dormir. Vale perguntar nas reuniões quem escolheu aquele objetivo e o que acontece com quem fica de fora da otimização (o criador pequeno, o assunto chato e importante, a notícia que não engaja).

Se você só usa o app, vale saber que dá para fugir da fila. Os feeds de "seguindo" em ordem cronológica existem, e redes do Fediverso, como o Mastodon, mostram as postagens em ordem de chegada, sem ninguém apostando no seu comportamento.

E se você publica qualquer coisa (inclusive um podcast de esquerda sobre trabalho, para dar um exemplo aleatório), a regra de originalidade é uma rara boa notícia: o algoritmo agora pune quem copia. Pelo menos até a próxima mudança de regra, que ninguém vai consultar você antes de fazer.

## Para conversar

- Qual métrica o seu time otimiza hoje? O que ela deixa de fora?
- Você usaria um feed sem ranqueamento, em ordem de chegada? Por quanto tempo?
- O que deveria ser público sobre um sistema de recomendação usado por milhões de pessoas?
- Se o seu feed fosse montado por um sindicato de criadores, o que ele premiaria?

## Fontes

- Adam Mosseri, [Shedding More Light on How Instagram Works](https://about.instagram.com/blog/announcements/shedding-more-light-on-how-instagram-works), Instagram, 8 jun 2021.
- Adam Mosseri, [Instagram Ranking Explained](https://about.instagram.com/blog/announcements/instagram-ranking-explained), Instagram, 31 mai 2023.
- Meta, [Our approach to explaining ranking](https://transparency.meta.com/features/explaining-ranking/), atualizado em 31 dez 2023.
- Meta, [ficha de sistema do feed do Instagram](https://transparency.meta.com/features/explaining-ranking/ig-feed/), atualizada em 29 jun 2026.
- Instagram para criadores, [Ajudando criadores de conteúdo a encontrar novos públicos](https://creators.instagram.com/blog/recommendations-and-originality), 30 abr 2024.
- Instagram para criadores, [Ajudando criadores de conteúdo de todos os tamanhos a crescerem](https://creators.instagram.com/blog/helping-creators-of-all-sizes-break-through), fev 2025.
- Instagram para criadores, [conteúdo original ganha prioridade](https://creators.instagram.com/blog/rewarding-original-creators-on-instagram/), 30 abr 2026.
- Instagram, [Your Algorithm](https://about.instagram.com/blog/announcements/reels-algorithm-control), atualizações de 10 dez 2025, 15 abr 2026 e 10 jun 2026.
- Wikipedia, [2021 Facebook leak](https://en.wikipedia.org/wiki/2021_Facebook_leak), consultada em 1º nov 2026.
