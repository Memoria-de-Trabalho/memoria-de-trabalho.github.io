---
titulo: Para onde vai a taxa da maquininha
linha_fina: Cada vez que alguém passa o cartão, uma fatia da venda some antes de chegar no caixa. Seguimos esse dinheiro até o banco do cliente, a bandeira e a empresa da maquininha.
eixo: Tecnologia
data: 2026-11-01
ordem: 4
conferido: 2026-11-01
resumo: Intercâmbio, bandeira, credenciadora e antecipação de recebíveis explicados sem economês. Com teto do Banco Central no débito e nenhum teto no crédito.
---

## Para quem tem pressa

- A taxa que o comerciante paga na maquininha (o MDR) é dividida entre o banco que emitiu o cartão, a bandeira e a empresa da maquininha.
- A fatia do banco emissor se chama tarifa de intercâmbio. Desde abril de 2023, o Banco Central limita essa tarifa a 0,5% no débito e 0,7% no pré-pago. No crédito, não tem teto.
- A taxa média do cartão de crédito no Brasil anda por volta de 2,2%. Na União Europeia, onde a lei põe teto, fica perto de 0,3%.
- A maquininha também ganha com a sua pressa: quem quer receber o crédito antes do prazo paga para antecipar, e isso é empréstimo com outro nome.
- O Pix entrou nessa briga cobrando zero de pessoa física e, desde junho de 2025, com o Pix Automático para cobrança recorrente.

## A venda de R$ 100 que chega magra

Um café vende R$ 100 no crédito. No extrato, aparece menos. O dinheiro que sumiu tem nome técnico: **taxa de desconto**, ou MDR, que é quanto a empresa da maquininha desconta da venda.

Essa empresa se chama **credenciadora** (ou adquirente, no jargão do mercado). Ela não fica com tudo. O MDR é repartido mais ou menos assim:

| Quem | Recebe | Por quê |
|---|---|---|
| Banco que emitiu o cartão do cliente | **tarifa de intercâmbio** | É quem dá o crédito e corre o risco de calote |
| Bandeira (Visa, Mastercard, Elo...) | tarifa da bandeira | É dona das regras e da rede por onde a transação passa |
| Credenciadora (a empresa da maquininha) | o que sobra | Aluga a máquina, processa a venda e paga o lojista |

O Banco Central define a tarifa de intercâmbio como a remuneração paga pela credenciadora ao emissor do cartão em cada transação. Em português de padaria: o banco do cliente ganha um pedágio toda vez que o cliente compra.

## O teto que só vale para metade da história

Em setembro de 2022, o Banco Central publicou a Resolução BCB nº 246. Desde 1º de abril de 2023, ela limita a tarifa de intercâmbio:

- a 0,5% de qualquer transação no **débito**;
- a 0,7% de qualquer transação no **pré-pago**.

E o crédito? A resolução não toca nele. É no crédito que mora a taxa mais gorda, e lá o intercâmbio continua sendo o que o mercado decide.

Para ter uma ideia do tamanho, um técnico do Banco Central comparou a taxa média do cartão de crédito no Brasil, cerca de 2,2%, com cerca de 0,3% na União Europeia, onde existe teto em lei. Ou seja, o café brasileiro paga umas sete vezes mais que o café de Lisboa para aceitar o mesmo cartão. O café de Lisboa, aliás, não está achando ruim.

## Quando cada maquininha só aceitava uma bandeira

Até 2010, o mercado era dividido de um jeito que hoje parece piada. A Cielo (que até 2009 se chamava Visanet) só aceitava Visa, e a Redecard só aceitava Mastercard. Comerciante que quisesse aceitar as duas bandeiras precisava de duas maquininhas no balcão, com dois aluguéis.

A exclusividade acabou em 1º de julho de 2010. Desde então, uma máquina aceita várias bandeiras, apareceu concorrência e as maquininhas coloridas tomaram as feiras. A briga ficou mais barulhenta, mas as duas gigantes seguiram grandes por muitos anos.

## A maquininha também é banco

No débito, o dinheiro cai rápido. No crédito, o lojista costuma esperar semanas pelo dinheiro de uma venda que já fez. Quem precisa pagar o fornecedor antes disso pode pedir para **antecipar os recebíveis**: recebe hoje, com um desconto.

Esse desconto é juro. Antecipar recebível é pegar emprestado usando como garantia o dinheiro que você já ganhou. Muita oferta de "taxa zero" no crédito se paga na antecipação, onde fica o lucro de verdade. A maquininha é, talvez, a única startup que lucra diretamente com a pressa do cliente.

## O Pix bagunçou a festa

O Pix é gratuito para pessoa física, e o Banco Central limita quanto os bancos podem cobrar das empresas. O dinheiro cai na hora, sem intercâmbio e sem antecipação. Para quem vende em feira ou tem um pequeno comércio, isso mudou o caixa do mês.

Em 16 de junho de 2025, entrou no ar o **Pix Automático**, que funciona como um débito automático para contas recorrentes (academia, escola, conta de luz) e é gratuito para quem paga. É o Pix entrando no território do cartão de crédito recorrente e do boleto.

Não por acaso, foi o Pix que apareceu na queixa comercial dos Estados Unidos contra o Brasil em 2026. Contamos essa história em [Quem tem medo do Pix?](../quem-tem-medo-do-pix/).

## E eu com isso?

Se você trabalha em fintech, e-commerce ou qualquer produto com checkout, é você quem escreve o código do split de pagamento, escolhe a forma de pagamento que aparece primeiro na tela e implementa o botão "receber agora". Essas escolhas de interface viram taxa no bolso de alguém. Pix no topo da lista e cartão de crédito no topo da lista são decisões com dono, mesmo quando chegam ao time como "melhoria de conversão".

E se você é PJ e um dia vender curso, mentoria ou freela pela internet, vale fazer a conta de quanto do seu faturamento vai para intercâmbio, bandeira e credenciadora. Spoiler: é mais do que parece, e cresce com a sua pressa.

## Para conversar

- No produto em que você trabalha, qual forma de pagamento aparece primeiro? Quem decidiu, e com base em qual métrica?
- Faz sentido o Banco Central limitar o intercâmbio do débito e deixar o crédito livre?
- Se você tivesse um pequeno negócio, aceitaria só Pix? O que perderia?
- Quem deveria ficar com o pedágio de cada compra: o banco, a bandeira, a maquininha ou ninguém?

## Fontes

- Banco Central do Brasil, [Resolução BCB nº 246, de 26 de setembro de 2022](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=246), que limita a tarifa de intercâmbio no débito e no pré-pago, em vigor desde 1º abr 2023.
- Jeff Alvares, [The Political Economy of Brazil's Pix Payment System](https://www.promarket.org/2025/12/03/the-political-economy-of-brazils-pix-payment-system/), ProMarket, 3 dez 2025 (taxa média do crédito no Brasil e na União Europeia).
- Cooperativismo de Crédito, [mercado de cartões vive "nova era" de competição](https://cooperativismodecredito.coop.br/2010/06/mercado-de-cartoes-vive-nova-era-de-competicao), jun 2010.
- Exame, ["Tem mercado para todo mundo", diz presidente da Cielo](https://exame.com/negocios/tem-mercado-para-todo-mundo-diz-presidente-da-cielo), 2010.
- Capital Aberto, [Porteira aberta](https://capitalaberto.com.br/empresas/2010/02/porteira-aberta), fev 2010.
- Folha de Pernambuco, [Pix Automático será lançado em 16 de junho de 2025](https://www.folhape.com.br/economia/pix-automatico/350177/); Canaltech, [BC confirma lançamento do Pix Automático em junho de 2025](https://canaltech.com.br/mercado/bc-confirma-lancamento-do-pix-automatico-em-junho-de-2025-296277/).
