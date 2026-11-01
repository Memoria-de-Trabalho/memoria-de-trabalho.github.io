#!/usr/bin/env python3
"""Gera os SVGs de assets/logos/ com o texto enquadrado pelas métricas reais das fontes.

- memoria-de-trabalho.svg: logo principal (pente de RAM)
- alternativos/: carimbo, lambe-lambe e estêncil, para outros materiais

Nada é esticado: cada linha recebe o corpo de fonte que faz a tinta ocupar exatamente a
largura útil, e as caixas são desenhadas em volta do texto com o mesmo respiro dos dois lados.

Métricas medidas no navegador com canvas.measureText a 1000px, em milésimos do corpo:
(início da tinta, fim da tinta, altura acima da linha de base, descida abaixo dela).
Se mudar algum texto, meça de novo.

Uso: python3 scripts/gerar-logos.py
"""
import math
from pathlib import Path

SAIDA = Path(__file__).resolve().parent.parent / "assets" / "logos"

FONTES = {
    "anton": ("Anton, Impact, sans-serif", 400),
    "alfa": ("'Alfa Slab One', serif", 400),
    "estencil": ("'Big Shoulders Stencil Display', sans-serif", 900),
    "elite": ("'Special Elite', 'Courier New', monospace", 400),
}

METRICAS = {
    "anton": {
        "MEMÓRIA": (38, 3564, 1101, 8),
        "DE TRABALHO": (38, 4812, 867, 8),
        "TRABALHO": (10, 3673, 867, 8),
        "MEMÓRIA DE TRABALHO": (38, 8625, 1101, 8),
    },
    "alfa": {
        "DE": (20, 1499, 778, 0),
        "PODCAST": (20, 5302, 792, 14),
    },
    "estencil": {
        "MEMÓRIA DE TRABALHO": (40, 8657, 979, 10),
    },
    "elite": {
        "PODCAST · TECNOLOGIA & CLASSE TRABALHADORA": (30, 23128, 717, 30),
        "tecnologia · trabalho · luta": (1, 14045, 693, 224),
        "PODCAST DE TRABALHADORES DA TECNOLOGIA": (30, 21489, 717, 30),
        "PODCAST · TECNOLOGIA & CLASSE": (30, 15618, 717, 30),
    },
}

FONTES_CSS = (
    '<style>@import url("https://fonts.googleapis.com/css2?family=Alfa+Slab+One&amp;family=Anton'
    '&amp;family=Big+Shoulders+Stencil+Display:wght@900&amp;family=Special+Elite&amp;display=block");</style>'
)


def filtro_tinta(furos):
    """Borda irregular + falhas de tinta. `furos` controla quanto do traço some (0 a 1)."""
    corte = 8.6 + (0.5 - furos) * 16
    inclinacao = -12 - (0.5 - furos) * 8
    return (
        '<filter id="tinta" x="-4%" y="-4%" width="108%" height="108%">'
        '<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" seed="7" result="onda"/>'
        '<feDisplacementMap in="SourceGraphic" in2="onda" scale="4" xChannelSelector="R" yChannelSelector="G" result="borda"/>'
        '<feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="2" seed="4" result="grao"/>'
        f'<feColorMatrix in="grao" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  {inclinacao:.1f} 0 0 0 {corte:.1f}" result="mascara"/>'
        '<feComposite in="borda" in2="mascara" operator="in"/>'
        "</filter>"
    )


class Linha:
    """Uma linha de texto com corpo calculado para a tinta ter `largura` (com espaçamento `esp` em frações do corpo)."""

    def __init__(self, fonte, texto, largura=None, corpo=None, esp=0.0):
        self.fonte, self.texto, self.esp = fonte, texto, esp
        ini, fim, alto, desce = METRICAS[fonte][texto]
        unidade = (fim - ini) / 1000 + esp * (len(texto) - 1)
        self.corpo = corpo if corpo else largura / unidade
        self.largura = unidade * self.corpo
        self.recuo = ini * self.corpo / 1000
        self.alto = alto * self.corpo / 1000
        self.desce = max(desce, 0) * self.corpo / 1000

    def svg(self, x_tinta, base, cor):
        familia, peso = FONTES[self.fonte]
        texto = self.texto.replace("&", "&amp;")
        espaco = f' letter-spacing="{self.esp * self.corpo:.2f}"' if self.esp else ""
        return (
            f'<text x="{x_tinta - self.recuo:.2f}" y="{base:.2f}" font-family="{familia}" font-weight="{peso}" '
            f'font-size="{self.corpo:.2f}"{espaco} fill="{cor}">{texto}</text>'
        )


def estrela(cx, cy, raio, cor):
    pontos = []
    for i in range(10):
        r = raio if i % 2 == 0 else raio * 0.4
        ang = math.radians(-90 + 36 * i)
        pontos.append(f"{cx + r * math.cos(ang):.2f},{cy + r * math.sin(ang):.2f}")
    return f'<polygon points="{" ".join(pontos)}" fill="{cor}"/>'


def documento(nome, rotulo, largura, altura, corpo, furos=0.5, defs_extra=""):
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {largura:.0f} {altura:.0f}" role="img" '
        f'aria-label="Memória de Trabalho — {rotulo}">\n'
        f"  <defs>{FONTES_CSS}{filtro_tinta(furos)}{defs_extra}</defs>\n"
        f"  {corpo}\n</svg>\n"
    )
    destino = SAIDA / nome
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(svg, encoding="utf-8")


def carimbo():
    vermelho, util, respiro, vao, margem = "#C8102E", 720, 34, 22, 44
    l1 = Linha("anton", "MEMÓRIA", util)
    l2 = Linha("anton", "DE TRABALHO", util)
    tag = Linha("elite", "PODCAST · TECNOLOGIA & CLASSE TRABALHADORA", util, esp=0.06)

    x0 = margem + vao + respiro
    y0 = margem + vao + respiro
    base1 = y0 + l1.alto
    base2 = base1 + 26 + l2.alto
    filete = base2 + 24
    base3 = filete + 4 + 20 + tag.alto
    fundo = base3 + tag.desce

    caixa_x, caixa_y = x0 - respiro, y0 - respiro
    caixa_l, caixa_a = util + 2 * respiro, fundo - y0 + 2 * respiro
    largura, altura = caixa_l + 2 * (vao + margem), caixa_a + 2 * (vao + margem)
    corpo = (
        f'<g transform="rotate(-3 {largura / 2:.0f} {altura / 2:.0f})" filter="url(#tinta)">'
        f'<rect x="{caixa_x - vao:.2f}" y="{caixa_y - vao:.2f}" width="{caixa_l + 2 * vao:.2f}" height="{caixa_a + 2 * vao:.2f}" rx="6" fill="none" stroke="{vermelho}" stroke-width="12"/>'
        f'<rect x="{caixa_x:.2f}" y="{caixa_y:.2f}" width="{caixa_l:.2f}" height="{caixa_a:.2f}" fill="none" stroke="{vermelho}" stroke-width="3"/>'
        + l1.svg(x0, base1, vermelho)
        + l2.svg(x0, base2, vermelho)
        + f'<rect x="{x0:.2f}" y="{filete:.2f}" width="{util}" height="4" fill="{vermelho}"/>'
        + tag.svg(x0, base3, vermelho)
        + "</g>"
    )
    documento("alternativos/carimbo.svg", "carimbo", largura, altura, corpo)


def lambe_lambe():
    preto, amarelo, vermelho = "#111", "#FFE600", "#E5142A"
    util, respiro, borda = 600, 58, 28
    cab = Linha("alfa", "PODCAST", corpo=36)
    l1 = Linha("anton", "MEMÓRIA", util)
    de = Linha("alfa", "DE", corpo=60)
    faixa = de.alto + 2 * 22
    l2 = Linha("anton", "TRABALHO", util)
    tag = Linha("elite", "tecnologia · trabalho · luta", util, esp=0.04)
    vaos = [30, 24, 24, 30]
    altura_util = cab.alto + l1.alto + l1.desce + faixa + l2.alto + tag.alto + tag.desce + sum(vaos)

    lado_util = max(util, altura_util)
    interno = lado_util + 2 * respiro
    lado = interno + 2 * borda
    x0 = borda + respiro + (lado_util - util) / 2
    y = borda + respiro + (lado_util - altura_util) / 2

    partes = [f'<rect x="{borda / 2}" y="{borda / 2}" width="{lado - borda:.2f}" height="{lado - borda:.2f}" fill="{amarelo}" stroke="{preto}" stroke-width="{borda}"/>']
    base = y + cab.alto
    xc = x0 + (util - cab.largura) / 2
    meio = base - cab.alto / 2
    partes.append(cab.svg(xc, base, preto))
    for a, b in ((x0, xc - 20), (xc + cab.largura + 20, x0 + util)):
        partes.append(f'<rect x="{a:.2f}" y="{meio - 2:.2f}" width="{b - a:.2f}" height="4" fill="{preto}"/>')
    base += vaos[0] + l1.alto
    partes.append(l1.svg(x0, base, preto))
    topo_faixa = base + l1.desce + vaos[1]
    partes.append(f'<rect x="{x0:.2f}" y="{topo_faixa:.2f}" width="{util}" height="{faixa:.2f}" fill="{preto}"/>')
    xd = x0 + (util - de.largura) / 2
    partes.append(de.svg(xd, topo_faixa + 22 + de.alto, amarelo))
    meio_faixa = topo_faixa + faixa / 2 + 2
    partes.append(estrela(xd - 44, meio_faixa, 20, amarelo))
    partes.append(estrela(xd + de.largura + 44, meio_faixa, 20, amarelo))
    base = topo_faixa + faixa + vaos[2] + l2.alto
    partes.append(l2.svg(x0, base, vermelho))
    base += vaos[3] + tag.alto
    partes.append(tag.svg(x0, base, preto))

    corpo = f'<g filter="url(#tinta)">{"".join(partes)}</g>'
    documento("alternativos/lambe-lambe.svg", "lambe-lambe", lado, lado, corpo, furos=0.3)


def estencil():
    vermelho, papel = "#D7261E", "#F2EBDD"
    util, respiro, vao, margem = 860, 30, 16, 20
    l1 = Linha("estencil", "MEMÓRIA DE TRABALHO", util)
    tag = Linha("elite", "PODCAST DE TRABALHADORES DA TECNOLOGIA", util, esp=0.15)

    x0 = margem + vao + respiro
    y0 = margem + vao + respiro
    base1 = y0 + l1.alto
    base2 = base1 + l1.desce + 24 + tag.alto
    fundo = base2 + tag.desce
    caixa_l = util + 2 * (respiro + vao)
    caixa_a = fundo - y0 + 2 * (respiro + vao)
    corpo = (
        '<g filter="url(#tinta)">'
        f'<rect x="{margem}" y="{margem}" width="{caixa_l:.2f}" height="{caixa_a:.2f}" fill="{vermelho}"/>'
        f'<rect x="{margem + vao}" y="{margem + vao}" width="{caixa_l - 2 * vao:.2f}" height="{caixa_a - 2 * vao:.2f}" fill="none" stroke="{papel}" stroke-width="3"/>'
        + l1.svg(x0, base1, papel)
        + tag.svg(x0, base2, papel)
        + "</g>"
    )
    documento("alternativos/estencil.svg", "estêncil", caixa_l + 2 * margem, caixa_a + 2 * margem, corpo)


def pente_de_ram():
    vermelho = "#C8102E"
    util, respiro, lateral, margem = 840, 26, 34, 28
    l1 = Linha("anton", "MEMÓRIA DE TRABALHO", util)
    tag = Linha("elite", "PODCAST · TECNOLOGIA & CLASSE", util, esp=0.3)

    etiqueta_l = util + 2 * respiro
    etiqueta_a = l1.alto + 20 + tag.alto + tag.desce + 2 * respiro
    esq, topo = margem, margem
    dir_ = esq + etiqueta_l + 2 * lateral
    et_x, et_y = esq + lateral, topo + 26
    contato_y = et_y + etiqueta_a + 22
    fundo = contato_y + 26 + 8
    clipe = topo + (fundo - topo) * 0.62
    chave = esq + (dir_ - esq) * 0.6

    placa = (
        f"M{esq},{topo} H{dir_} V{clipe - 14:.2f} a14,14 0 0 0 0,28 V{fundo:.2f} "
        f"H{chave + 12:.2f} V{fundo - 18:.2f} H{chave - 12:.2f} V{fundo:.2f} H{esq} "
        f"V{clipe + 14:.2f} a14,14 0 0 0 0,-28 Z"
    )
    contatos = "".join(
        f'<rect x="{x:.2f}" y="{contato_y:.2f}" width="9" height="26" fill="{vermelho}"/>'
        for x in [esq + 22 + 16 * i for i in range(int((dir_ - esq - 44) / 16) + 1)]
        if not chave - 24 < x + 4.5 < chave + 24
    )
    x0, y0 = et_x + respiro, et_y + respiro
    base1 = y0 + l1.alto
    base2 = base1 + 20 + tag.alto
    largura, altura = dir_ + margem, fundo + margem
    corpo = (
        f'<g transform="rotate(-2 {largura / 2:.0f} {altura / 2:.0f})" filter="url(#tinta)">'
        f'<path d="{placa}" fill="none" stroke="{vermelho}" stroke-width="8" stroke-linejoin="round"/>'
        f'<rect x="{et_x}" y="{et_y}" width="{etiqueta_l}" height="{etiqueta_a:.2f}" fill="none" stroke="{vermelho}" stroke-width="3"/>'
        + l1.svg(x0, base1, vermelho)
        + tag.svg(x0, base2, vermelho)
        + contatos
        + "</g>"
    )
    documento("memoria-de-trabalho.svg", "pente de RAM", largura, altura, corpo)


if __name__ == "__main__":
    for gerar in (pente_de_ram, carimbo, lambe_lambe, estencil):
        gerar()
    print("ok:", ", ".join(sorted(str(p.relative_to(SAIDA)) for p in SAIDA.rglob("*.svg") if not p.name.startswith("."))))
