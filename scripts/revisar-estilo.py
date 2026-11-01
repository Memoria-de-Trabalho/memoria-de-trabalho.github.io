#!/usr/bin/env python3
"""Confere os artigos contra o guia de estilo (docs/ESTILO.md).

Erros (o build dos artigos para): travessão, hífen como travessão, a fórmula "não é X, é Y",
clichês proibidos, exclamação, artigo sem fontes ou sem data de conferência.
Avisos (não param o build): listas e enumerações de exatamente três itens em excesso.

Uma linha marcada com <!-- estilo: ok --> é ignorada.

Uso: python3 scripts/revisar-estilo.py [arquivo.md ...]   (sem argumentos: todos os artigos)
"""
import re
import sys
from pathlib import Path

ARTIGOS = Path(__file__).resolve().parent.parent / "conteudo" / "artigos"

TRAVESSAO = re.compile(r"[—–]")
HIFEN_SOLTO = re.compile(r"[\wÀ-ú,] - [\wÀ-ú]")
FORMULA = [
    re.compile(r"\bnão (?:é|era|foi|está) (?:sobre|só|apenas)\b[^.!?\n]{0,90}?[,;:]\s*(?:é|era|foi|mas)\b", re.I),
    re.compile(r"\bnão se trata de\b", re.I),
    re.compile(r"\bmais do que [^.!?\n]{1,60}, (?:é|era|foi)\b", re.I),
    re.compile(r"\bnão (?:é|era) [^.!?\n]{1,60}[,;] (?:é|era|e sim)\b", re.I),
    re.compile(r"\bnão (?:é|era) [^.!?\n]{1,60}\. (?:(?:Ela|Ele|Isso) )?(?:é|era)\b", re.I),  # a mesma fórmula em duas frases
]
CLICHES = [
    "vale ressaltar", "vale destacar", "é importante destacar", "é importante ressaltar", "no fim do dia",
    "em suma", "em última análise", "mergulhar", "mergulho", "navegar por", "desvendar",
    # "jornada" só no sentido figurado; jornada de trabalho, normal ou máxima é termo trabalhista
    "sua jornada", "nossa jornada", "nessa jornada", "essa jornada", "jornada do cliente", "jornada de transformação",
    "potencializar", "alavancar", "robusto", "divisor de águas", "neste artigo",
]
# "A, B e C" que não seja o fim de uma lista maior ("W, A, B e C" não conta)
TRIO_FRASE = re.compile(r"(?<!, )\b[\wÀ-ú]+(?: [\wÀ-ú]+){0,2}, [\wÀ-ú]+(?: [\wÀ-ú]+){0,2} e [\wÀ-ú]+\b")
LIMITE_TRIOS = 4


def linhas_de_texto(texto):
    """Linhas de prosa: sem front matter, sem a seção de fontes, sem URLs e sem linhas liberadas."""
    corpo = re.sub(r"\A---\n.*?\n---\n", lambda m: "\n" * m.group(0).count("\n"), texto, flags=re.S)
    em_fontes = False
    for n, linha in enumerate(corpo.splitlines(), 1):
        if re.match(r"^##\s+Fontes", linha):
            em_fontes = True
        elif re.match(r"^##\s", linha):
            em_fontes = False
        if em_fontes or "<!-- estilo: ok -->" in linha:
            continue
        yield n, re.sub(r"\]\([^)]*\)|https?://\S+", "]", linha)


def revisar(caminho):
    texto = caminho.read_text(encoding="utf-8")
    erros, avisos = [], []
    meta = re.match(r"\A---\n(.*?)\n---\n", texto, flags=re.S)
    if not meta or not re.search(r"^conferido:\s*\d{4}-\d{2}-\d{2}", meta.group(1), re.M):
        erros.append((1, "falta `conferido: AAAA-MM-DD` no cabeçalho"))
    if not re.search(r"^##\s+Fontes\s*\n(?:.*\n)*?.*\]\(https?://", texto, re.M):
        erros.append((0, "falta a seção `## Fontes` com pelo menos um link"))
    if not re.search(r"^##\s+E eu com isso\?", texto, re.M):
        erros.append((0, "falta a seção `## E eu com isso?`"))

    trios = 0
    for n, linha in linhas_de_texto(texto):
        if TRAVESSAO.search(linha):
            erros.append((n, "travessão ou meia-risca"))
        if HIFEN_SOLTO.search(linha):
            erros.append((n, "hífen solto usado como travessão"))
        for padrao in FORMULA:
            if padrao.search(linha):
                erros.append((n, "fórmula de correção dramática (\"não é X, é Y\")"))
                break
        baixa = linha.lower()
        for cliche in CLICHES:
            if cliche in baixa:
                erros.append((n, f"clichê proibido: \"{cliche}\""))
        if "!" in linha.replace("<!--", ""):
            erros.append((n, "exclamação"))
        trios += len(TRIO_FRASE.findall(linha))

    # listas de tópicos com exatamente três itens
    for bloco in re.split(r"\n\s*\n", texto):
        itens = [l for l in bloco.splitlines() if re.match(r"^\s*(?:[-*]|\d+\.)\s", l)]
        if itens and len(itens) == 3 and len(itens) == len(bloco.strip().splitlines()):
            avisos.append("lista com exatamente três itens (varie a quantidade)")
    if trios > LIMITE_TRIOS:
        avisos.append(f"{trios} enumerações do tipo \"A, B e C\" (limite sugerido: {LIMITE_TRIOS})")
    return erros, avisos


def main(argumentos):
    # o disco externo cria arquivos ._* (metadados do macOS) ao lado de cada arquivo
    arquivos = [Path(a) for a in argumentos] or sorted(p for p in ARTIGOS.glob("*.md") if not p.name.startswith("."))
    total = 0
    for arquivo in arquivos:
        erros, avisos = revisar(arquivo)
        total += len(erros)
        situacao = "ok" if not erros else f"{len(erros)} erro(s)"
        print(f"{arquivo.name}: {situacao}" + (f", {len(avisos)} aviso(s)" if avisos else ""))
        for n, msg in erros:
            print(f"  erro  linha {n}: {msg}" if n else f"  erro  {msg}")
        for msg in avisos:
            print(f"  aviso {msg}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
