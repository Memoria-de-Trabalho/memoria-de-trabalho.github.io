#!/usr/bin/env python3
"""Exporta as artes do Memória de Trabalho para download e gera a página artes/index.html.

Parte dos SVGs feitos por scripts/gerar-logos.py e cria, em assets/artes/:
- logos/<arte>-<largura>.png   cada arte em várias larguras, com fundo transparente
- icone/mdt-<lado>.png          o ícone quadrado em vários tamanhos
- papeis/<tema>-<L>x<A>.jpg     papéis de parede para celular e computador
- miniaturas/<tema>-<tipo>.jpg  prévias leves para a página

Precisa do Inkscape na linha de comando (para rasterizar com o filtro de tinta) e do Pillow
(para converter em JPG). Rode depois do gerar-logos.py:

    python3 scripts/gerar-artes.py
"""
import html
import importlib.util
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "assets" / "artes"
PAGINA = RAIZ / "artes" / "index.html"
PAPEL, PRETO, VERMELHO = "#F2EBDD", "#141414", "#C8102E"

ARTES = [  # (slug, nome, arquivo de origem, descrição curta)
    ("pente-de-ram", "Pente de RAM", "assets/logos/memoria-de-trabalho.svg",
     "O logo principal. A caixa é um módulo de memória, com chanfro e contatos."),
    ("lambe-lambe", "Lambe-lambe", "assets/logos/alternativos/lambe-lambe.svg",
     "Cartaz de poste em amarelo. Quadrado, serve de capa e de post."),
    ("carimbo", "Carimbo", "assets/logos/alternativos/carimbo.svg",
     "Tinta vermelha e borda dupla, levemente torto, como todo carimbo honesto."),
    ("estencil", "Estêncil", "assets/logos/alternativos/estencil.svg",
     "Letra vazada sobre faixa vermelha. Feito para banner, camiseta e faixa de ato."),
]
LARGURAS = [512, 1024, 2048, 4096]
ICONE = ("assets/favicon/favicon.svg", [256, 512, 1024, 2048])

CELULAR = [(1080, 1920), (1080, 2400), (1179, 2556), (1290, 2796), (1440, 3200)]
COMPUTADOR = [(1366, 768), (1920, 1080), (2560, 1440), (2560, 1600), (3440, 1440), (3840, 2160)]
TEMAS = [  # (slug, nome, arte, fundo, fração da largura no celular, fração da altura no computador, troca de cor)
    ("pente-claro", "Pente de RAM, claro", "pente-de-ram", PAPEL, 0.86, 0.30, None),
    # vermelho sobre preto quase some: no tema escuro a tinta vira cor de papel
    ("pente-escuro", "Pente de RAM, escuro", "pente-de-ram", PRETO, 0.86, 0.30, (VERMELHO, PAPEL)),
    ("lambe-lambe", "Lambe-lambe", "lambe-lambe", VERMELHO, 0.86, 0.62, None),
    ("carimbo", "Carimbo", "carimbo", PAPEL, 0.86, 0.52, None),
    ("estencil", "Estêncil", "estencil", PRETO, 0.90, 0.26, None),
]


def artigos():
    """Reaproveita o cabeçalho, o rodapé e a versão do CSS do gerador de artigos."""
    spec = importlib.util.spec_from_file_location("gerar_artigos", RAIZ / "scripts" / "gerar-artigos.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def inkscape(svg, png, largura, altura=None, fundo=None):
    cmd = ["inkscape", str(svg), "--export-type=png", f"--export-filename={png}", f"--export-width={largura}"]
    if altura:
        cmd.append(f"--export-height={altura}")
    if fundo:
        cmd += [f"--export-background={fundo}", "--export-background-opacity=1", "--export-png-color-mode=RGB_8"]
    subprocess.run(cmd, check=True, capture_output=True)


def em_jpg(png, jpg, largura=None):
    imagem = Image.open(png).convert("RGB")
    if largura:
        imagem = imagem.resize((largura, round(imagem.height * largura / imagem.width)), Image.LANCZOS)
    imagem.save(jpg, "JPEG", quality=90, optimize=True, progressive=True, subsampling=0)


def miolo(svg_texto):
    """viewBox e conteúdo de um SVG, para encaixá-lo dentro de outro."""
    caixa = re.search(r'viewBox="([^"]+)"', svg_texto).group(1)
    corpo = re.search(r"<svg[^>]*>(.*)</svg>", svg_texto, flags=re.S).group(1)
    return caixa, corpo


def papel_de_parede(arte_svg, fundo, largura, altura, fracao_celular, fracao_pc):
    caixa, corpo = miolo(arte_svg)
    _, _, lw, la = map(float, caixa.split())
    if altura > largura:  # celular: a arte ocupa uma fração da largura, um pouco abaixo do meio (o relógio fica no topo)
        w = largura * fracao_celular
        h = w * la / lw
        x, y = (largura - w) / 2, altura * 0.56 - h / 2
    else:  # computador: a arte ocupa uma fração da altura, no centro
        h = altura * fracao_pc
        w = h * lw / la
        if w > largura * 0.8:
            w = largura * 0.8
            h = w * la / lw
        x, y = (largura - w) / 2, (altura - h) / 2
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{largura}" height="{altura}" viewBox="0 0 {largura} {altura}">'
            f'<rect width="100%" height="100%" fill="{fundo}"/>'
            f'<svg x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" viewBox="{caixa}">{corpo}</svg></svg>')


def gerar_arquivos(tmp):
    # ignore_errors: no disco externo os ._* do macOS somem junto com o arquivo e o rmtree tropeça neles
    shutil.rmtree(SAIDA, ignore_errors=True)
    for pasta in ("logos", "icone", "papeis", "miniaturas"):
        (SAIDA / pasta).mkdir(parents=True, exist_ok=True)

    for slug, _, origem, _ in ARTES:
        for largura in LARGURAS:
            inkscape(RAIZ / origem, SAIDA / "logos" / f"{slug}-{largura}.png", largura)
    origem, lados = ICONE
    for lado in lados:
        inkscape(RAIZ / origem, SAIDA / "icone" / f"mdt-{lado}.png", lado, lado)

    textos = {slug: (RAIZ / origem).read_text(encoding="utf-8") for slug, _, origem, _ in ARTES}
    for tema, _, arte, fundo, fc, fp, cor in TEMAS:
        texto = textos[arte].replace(*cor) if cor else textos[arte]
        for largura, altura in CELULAR + COMPUTADOR:
            svg = tmp / f"{tema}-{largura}x{altura}.svg"
            svg.write_text(papel_de_parede(texto, fundo, largura, altura, fc, fp), encoding="utf-8")
            png = tmp / f"{tema}-{largura}x{altura}.png"
            inkscape(svg, png, largura, altura, fundo)
            em_jpg(png, SAIDA / "papeis" / f"{tema}-{largura}x{altura}.jpg")
        em_jpg(tmp / f"{tema}-1080x2400.png", SAIDA / "miniaturas" / f"{tema}-celular.jpg", 240)
        em_jpg(tmp / f"{tema}-1920x1080.png", SAIDA / "miniaturas" / f"{tema}-pc.jpg", 480)


def links(itens):
    return " · ".join(f'<a href="{href}" download>{html.escape(rotulo)}</a>' for rotulo, href in itens)


def gerar_pagina(art):
    e = html.escape
    p = "../assets/artes/"
    partes = []
    for slug, nome, origem, descricao in ARTES:
        pngs = [(f"PNG {w} px", f"{p}logos/{slug}-{w}.png") for w in LARGURAS]
        partes.append(
            f'        <li class="arte">\n          <div class="arte-previa"><img src="../{origem}" alt="{e(nome)}" loading="lazy"></div>\n'
            f'          <h3>{e(nome)}</h3>\n          <p>{e(descricao)}</p>\n'
            f'          <p class="baixar">{links([("SVG", "../" + origem)] + pngs)}</p>\n        </li>\n')
    logos = "".join(partes)

    icone_origem, lados = ICONE
    icone = links([("SVG", "../" + icone_origem)] + [(f"PNG {l} px", f"{p}icone/mdt-{l}.png") for l in lados]
                  + [("ICO", "../favicon.ico")])
    capa = links([("SVG", "../assets/capa/capa-podcast.svg"), ("PNG 3000 px", "../assets/capa/capa-podcast-3000.png"),
                  ("JPG 3000 px", "../assets/capa/capa-podcast-3000.jpg")])

    papeis = []
    for tema, nome, *_ in TEMAS:
        cel = links([(f"{l}×{a}", f"{p}papeis/{tema}-{l}x{a}.jpg") for l, a in CELULAR])
        pc = links([(f"{l}×{a}", f"{p}papeis/{tema}-{l}x{a}.jpg") for l, a in COMPUTADOR])
        papeis.append(
            f'        <li class="papel">\n          <div class="papel-previas">\n'
            f'            <img class="previa-celular" src="{p}miniaturas/{tema}-celular.jpg" alt="{e(nome)} no celular" loading="lazy">\n'
            f'            <img class="previa-pc" src="{p}miniaturas/{tema}-pc.jpg" alt="{e(nome)} no computador" loading="lazy">\n'
            f'          </div>\n          <h3>{e(nome)}</h3>\n'
            f'          <p class="baixar"><b>Celular</b> {cel}</p>\n          <p class="baixar"><b>Computador</b> {pc}</p>\n        </li>\n')

    return (art.cabeca("Artes · Memória de Trabalho",
                       "Logos, capa, ícone e papéis de parede do Memória de Trabalho para baixar em várias resoluções.",
                       "../", f"{art.SITE}/artes/")
            + '  <main class="wrap">\n    <header class="page-head">\n'
            + '      <p class="kicker">Artes</p>\n      <h1>Pode baixar</h1>\n'
            + '      <p>Logos, capa, ícone e papéis de parede, em todas as resoluções que a gente lembrou de exportar. '
            + 'Use à vontade em adesivo, camiseta, cartaz, slide de reunião e fundo de tela. '
            + 'O SVG aguenta qualquer tamanho; o PNG tem fundo transparente.</p>\n    </header>\n'
            + '    <section>\n      <h2>Logos</h2>\n      <ul class="lista-artes">\n' + logos + '      </ul>\n    </section>\n'
            + '    <section>\n      <h2>Papéis de parede</h2>\n'
            + '      <p>Escolha a resolução da sua tela. Se não souber, a maior serve e o aparelho ajusta.</p>\n'
            + '      <ul class="lista-papeis">\n' + "".join(papeis) + '      </ul>\n    </section>\n'
            + '    <section>\n      <h2>Capa e ícone</h2>\n      <ul class="lista-artes">\n'
            + '        <li class="arte">\n          <div class="arte-previa"><img src="../assets/capa/capa-podcast.svg" alt="Capa do podcast" loading="lazy"></div>\n'
            + f'          <h3>Capa do podcast</h3>\n          <p>Quadrada, no tamanho que as plataformas de podcast pedem.</p>\n          <p class="baixar">{capa}</p>\n        </li>\n'
            + '        <li class="arte">\n          <div class="arte-previa"><img src="../assets/favicon/favicon.svg" alt="Ícone MdT" loading="lazy"></div>\n'
            + f'          <h3>Ícone MdT</h3>\n          <p>Para foto de perfil, aba do navegador e atalho na tela inicial.</p>\n          <p class="baixar">{icone}</p>\n        </li>\n'
            + '      </ul>\n    </section>\n' + art.RODAPE)


def main():
    art = artigos()
    with tempfile.TemporaryDirectory() as tmp:
        gerar_arquivos(Path(tmp))
    PAGINA.parent.mkdir(exist_ok=True)
    PAGINA.write_text(gerar_pagina(art), encoding="utf-8")
    total = sum(f.stat().st_size for f in SAIDA.rglob("*") if f.is_file() and not f.name.startswith("."))
    print(f"ok: {sum(1 for f in SAIDA.rglob('*.*') if not f.name.startswith('.'))} arquivos em assets/artes "
          f"({total / 1024 / 1024:.1f} MB) e a página artes/index.html")


if __name__ == "__main__":
    main()
