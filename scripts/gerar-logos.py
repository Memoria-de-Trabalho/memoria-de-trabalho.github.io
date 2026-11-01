#!/usr/bin/env python3
"""Gera os SVGs de assets/logos/ com todo o texto convertido em curvas.

- memoria-de-trabalho.svg: logo principal (pente de RAM)
- alternativos/: carimbo, lambe-lambe e estêncil, para outros materiais

Os SVGs não dependem de fonte instalada nem de internet: cada linha é montada pelo HarfBuzz
(com o kerning da fonte) a partir dos arquivos em scripts/fontes/ e desenhada como <path>.
A caixa de tinta de cada linha é medida nas próprias curvas, então o enquadramento é exato
em qualquer programa (navegador, Finder, Figma, Illustrator, Inkscape).

Uso:
    python3 -m pip install -r scripts/requirements.txt
    python3 scripts/gerar-logos.py
"""
import math
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

RAIZ = Path(__file__).resolve().parent
SAIDA = RAIZ.parent / "assets" / "logos"

ARQUIVOS = {
    "anton": "Anton-Regular.ttf",
    "alfa": "AlfaSlabOne-Regular.ttf",
    "estencil": "BigShouldersStencilDisplay-Black.ttf",
    "elite": "SpecialElite-Regular.ttf",
}
_fontes = {}


def fonte(nome):
    if nome not in _fontes:
        caminho = RAIZ / "fontes" / ARQUIVOS[nome]
        dados = caminho.read_bytes()
        _fontes[nome] = (TTFont(caminho), hb.Font(hb.Face(dados)))
    return _fontes[nome]


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
    """Uma linha de texto em curvas, com corpo calculado para a tinta ter `largura`.

    `esp` é o espaçamento extra entre letras, em frações do corpo.
    """

    def __init__(self, nome_fonte, texto, largura=None, corpo=None, esp=0.0):
        tt, hb_font = fonte(nome_fonte)
        upem = tt["head"].unitsPerEm
        buf = hb.Buffer()
        buf.add_str(texto)
        buf.guess_segment_properties()
        hb.shape(hb_font, buf)

        glifos, nomes = tt.getGlyphSet(), tt.getGlyphOrder()
        caneta = SVGPathPen(glifos, ntos=lambda v: ("%.1f" % v).rstrip("0").rstrip("."))
        limites = BoundsPen(glifos)
        x = 0
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            glifo = glifos[nomes[info.codepoint]]
            deslocamento = (1, 0, 0, 1, x + pos.x_offset, pos.y_offset)
            glifo.draw(TransformPen(caneta, deslocamento))
            glifo.draw(TransformPen(limites, deslocamento))
            x += pos.x_advance + esp * upem
        xmin, ymin, xmax, ymax = limites.bounds

        self.corpo = corpo if corpo else largura * upem / (xmax - xmin)
        escala = self.corpo / upem
        self.escala, self.caminho = escala, caneta.getCommands()
        self.largura = (xmax - xmin) * escala
        self.recuo = xmin * escala
        self.alto = ymax * escala
        self.desce = max(-ymin, 0) * escala

    def svg(self, x_tinta, base, cor):
        return (
            f'<path transform="translate({x_tinta - self.recuo:.2f} {base:.2f}) scale({self.escala:.5f} {-self.escala:.5f})" '
            f'fill="{cor}" d="{self.caminho}"/>'
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
        f"  <defs>{filtro_tinta(furos)}{defs_extra}</defs>\n"
        f"  {corpo}\n</svg>\n"
    )
    destino = SAIDA / nome
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(svg, encoding="utf-8")


def carimbo():
    vermelho, util, respiro, vao, margem = "#C8102E", 720, 34, 22, 60
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
    # capa do podcast: o mesmo cartaz sobre fundo preto, para as falhas de tinta não virarem
    # transparência quando exportado em JPG/PNG 3000×3000
    fundo = f'<rect width="{lado:.2f}" height="{lado:.2f}" fill="{preto}"/>'
    documento("../capa/capa-podcast.svg", "capa do podcast", lado, lado, fundo + corpo, furos=0.3)


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
    util, respiro, lateral, margem = 840, 26, 34, 48
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


def favicon():
    """Ícone quadrado: a sigla MdT sobre os contatos do pente de RAM. Sem textura, que vira borrão em 16 px."""
    vermelho, papel, lado = "#C8102E", "#F2EBDD", 64
    sigla = Linha("anton", "MdT", 46)
    base = 27 + sigla.alto / 2
    contatos = "".join(
        f'<rect x="{x}" y="49" width="2.6" height="8" fill="{papel}"/>'
        for x in range(7, 57, 5) if x != 37  # o vão faz as vezes do chanfro do pente
    )
    corpo = (
        f'<rect width="{lado}" height="{lado}" rx="10" fill="{vermelho}"/>'
        + sigla.svg((lado - sigla.largura) / 2, base, papel)
        + contatos
    )
    documento("../favicon/favicon.svg", "ícone", lado, lado, corpo)


if __name__ == "__main__":
    for gerar in (pente_de_ram, carimbo, lambe_lambe, estencil, favicon):
        gerar()
    print("ok:", ", ".join(sorted(str(p.relative_to(SAIDA)) for p in SAIDA.rglob("*.svg") if not p.name.startswith("."))))
