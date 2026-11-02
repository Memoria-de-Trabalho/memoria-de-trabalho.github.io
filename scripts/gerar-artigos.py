#!/usr/bin/env python3
"""Gera a seção de artigos do site a partir dos Markdown em conteudo/artigos/.

Também carimba a versão do CSS (`style.css?v=<hash>`) nas páginas que gera e no index.html.

Para cada `conteudo/artigos/<slug>.md` escreve `artigos/<slug>/index.html`, refaz o índice
`artigos/index.html` e a lista de artigos da página inicial (entre os marcadores
`<!-- artigos:inicio -->` e `<!-- artigos:fim -->` do index.html).

Antes de gerar, roda o revisor de estilo (scripts/revisar-estilo.py): se houver erro, nada é
gravado. Use --forcar só para pré-visualizar um rascunho.

Cabeçalho de cada artigo (entre linhas `---`):
    titulo, linha_fina, eixo, data, conferido, resumo   (obrigatórios)
    ordem     número para desempatar artigos do mesmo dia (menor aparece primeiro)
    rascunho  true para não publicar

Uso:
    python3 -m pip install -r scripts/requirements.txt
    python3 scripts/gerar-artigos.py [--forcar]
"""
import hashlib
import html
import importlib.util
import math
import re
import sys
from datetime import date
from pathlib import Path

import markdown

RAIZ = Path(__file__).resolve().parent.parent
FONTE = RAIZ / "conteudo" / "artigos"
SAIDA = RAIZ / "artigos"
INICIO = RAIZ / "index.html"
SITE = "https://memoria-de-trabalho.github.io"
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto",
         "setembro", "outubro", "novembro", "dezembro"]
OBRIGATORIOS = ("titulo", "linha_fina", "eixo", "data", "conferido", "resumo")
PAGINAS_FIXAS = (RAIZ / "index.html",)  # artes/index.html é feita pelo gerar-artes.py


def versao_css():
    """Hash curto do CSS: muda o link quando o estilo muda, e o cache do GitHub Pages não serve CSS velho."""
    return hashlib.sha1((RAIZ / "assets" / "style.css").read_bytes()).hexdigest()[:8]


def data_extenso(iso):
    d = date.fromisoformat(iso)
    dia = "1º" if d.day == 1 else str(d.day)
    return f"{dia} de {MESES[d.month - 1]} de {d.year}"


def ler(caminho):
    texto = caminho.read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", texto, flags=re.S)
    if not m:
        sys.exit(f"{caminho.name}: falta o cabeçalho entre linhas ---")
    meta = {}
    for linha in m.group(1).splitlines():
        if ":" in linha:
            chave, valor = linha.split(":", 1)
            meta[chave.strip()] = valor.strip().strip('"')
    faltando = [c for c in OBRIGATORIOS if not meta.get(c)]
    if faltando:
        sys.exit(f"{caminho.name}: faltam no cabeçalho: {', '.join(faltando)}")
    corpo = m.group(2)
    palavras = len(re.findall(r"\w+", re.sub(r"(?s)^## Fontes.*", "", corpo, flags=re.M)))
    meta.update(slug=caminho.stem, corpo=corpo, leitura=max(1, math.ceil(palavras / 200)))
    return meta


def html_do_corpo(corpo):
    h = markdown.markdown(corpo, extensions=["tables", "sane_lists"], output_format="html")
    # links para fora abrem em outra aba
    h = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', h)
    return h.replace("<table>", '<div class="tabela"><table>').replace("</table>", "</table></div>")


def cabeca(titulo, descricao, prefixo, url):
    e = html.escape
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(titulo)}</title>
  <meta name="description" content="{e(descricao)}">
  <meta property="og:title" content="{e(titulo)}">
  <meta property="og:description" content="{e(descricao)}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/capa/capa-podcast-3000.jpg">
  <link rel="icon" href="{prefixo}favicon.ico" sizes="32x32">
  <link rel="icon" href="{prefixo}assets/favicon/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="{prefixo}assets/favicon/apple-touch-icon.png">
  <link rel="stylesheet" href="{prefixo}assets/style.css?v={versao_css()}">
</head>
<body>
  <nav class="topo wrap">
    <a href="{prefixo}">Memória de Trabalho</a>
    <a href="{prefixo}artigos/">Artigos</a>
    <a href="{prefixo}artes/">Artes</a>
  </nav>
"""


RODAPE = """    <footer>
      Memória de Trabalho · feito por trabalhadores · achou um erro? Escreva para a gente e a gente corrige.
    </footer>
  </main>
</body>
</html>
"""


def cartao(a, prefixo):
    e = html.escape
    return (f'        <li class="cartao-artigo">\n'
            f'          <p class="kicker">{e(a["eixo"])} · {a["leitura"]} min</p>\n'
            f'          <h3><a href="{prefixo}{a["slug"]}/">{e(a["titulo"])}</a></h3>\n'
            f'          <p>{e(a["resumo"])}</p>\n'
            f'        </li>\n')


def pagina_artigo(a):
    e = html.escape
    meta = (f'Publicado em {data_extenso(a["data"])} · fontes conferidas em '
            f'{data_extenso(a["conferido"])} · {a["leitura"]} min de leitura')
    return (cabeca(f'{a["titulo"]} · Memória de Trabalho', a["linha_fina"], "../../",
                   f'{SITE}/artigos/{a["slug"]}/')
            + '  <main class="wrap">\n    <article class="artigo">\n'
            + f'      <p class="kicker">{e(a["eixo"])}</p>\n'
            + f'      <h1>{e(a["titulo"])}</h1>\n'
            + f'      <p class="linha-fina">{e(a["linha_fina"])}</p>\n'
            + f'      <p class="meta">{meta}</p>\n'
            + html_do_corpo(a["corpo"])
            + '\n      <p class="voltar"><a href="../">← todos os artigos</a></p>\n    </article>\n'
            + RODAPE)


def pagina_indice(artigos):
    return (cabeca("Artigos · Memória de Trabalho",
                   "Textos curtos, com fonte e sem pose sobre trabalho, tecnologia, organização e soberania.",
                   "../", f"{SITE}/artigos/")
            + '  <main class="wrap">\n    <header class="page-head">\n'
            + '      <p class="kicker">Artigos</p>\n      <h1>Para ler e discutir</h1>\n'
            + '      <p>Textos curtos, com fonte e sem pose sobre trabalho, tecnologia, organização e soberania. '
            + 'Cada um pode virar pauta de episódio, e as sugestões são bem-vindas.</p>\n    </header>\n'
            + '    <section>\n      <ul class="lista-artigos">\n'
            + "".join(cartao(a, "") for a in artigos)
            + '      </ul>\n    </section>\n' + RODAPE)


def atualizar_inicio(artigos):
    s = INICIO.read_text(encoding="utf-8")
    bloco = ('<!-- artigos:inicio -->\n      <ul class="lista-artigos">\n'
             + "".join(cartao(a, "artigos/") for a in artigos)
             + '      </ul>\n      <!-- artigos:fim -->')
    novo, n = re.subn(r"<!-- artigos:inicio -->.*?<!-- artigos:fim -->", bloco, s, flags=re.S)
    if n != 1:
        sys.exit("index.html: não achei os marcadores <!-- artigos:inicio --> e <!-- artigos:fim -->")
    INICIO.write_text(novo, encoding="utf-8")


def revisor():
    spec = importlib.util.spec_from_file_location("revisar_estilo", RAIZ / "scripts" / "revisar-estilo.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def main(argumentos):
    fontes = sorted(p for p in FONTE.glob("*.md") if not p.name.startswith("."))  # pula os ._* do macOS
    artigos = [a for a in map(ler, fontes) if a.get("rascunho", "").lower() != "true"]
    if "--forcar" not in argumentos and revisor().main([str(FONTE / f'{a["slug"]}.md') for a in artigos]):
        sys.exit("\nO revisor de estilo achou erros; nada foi gerado. Corrija ou use --forcar para pré-visualizar.")
    artigos.sort(key=lambda a: (-date.fromisoformat(a["data"]).toordinal(), int(a.get("ordem", 99)), a["titulo"]))
    for a in artigos:
        destino = SAIDA / a["slug"] / "index.html"
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(pagina_artigo(a), encoding="utf-8")
    (SAIDA / "index.html").write_text(pagina_indice(artigos), encoding="utf-8")
    atualizar_inicio(artigos)
    for pagina in PAGINAS_FIXAS:
        texto = pagina.read_text(encoding="utf-8")
        pagina.write_text(re.sub(r'href="assets/style\.css(?:\?v=\w+)?"', f'href="assets/style.css?v={versao_css()}"', texto),
                          encoding="utf-8")
    print(f"ok: {len(artigos)} artigo(s) em artigos/ e na página inicial")


if __name__ == "__main__":
    main(sys.argv[1:])
