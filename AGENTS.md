# Memória de Trabalho: instruções para agentes

Site e identidade visual do Memória de Trabalho, podcast de e para profissionais de tecnologia de esquerda. O site é publicado pelo GitHub Pages em https://memoria-de-trabalho.github.io a partir da branch `main` do repositório `Memoria-de-Trabalho/memoria-de-trabalho.github.io`. Este repositório serve tanto para desenvolver o site quanto para escrever os artigos.

## Regras

- **Idioma:** textos do site, artigos, commits e documentação em português do Brasil.
- **Commits em nome da organização:** autor e committer são sempre `Memória de Trabalho <noreply@memoria-de-trabalho.github.io>` (já configurado no `git config` local do repositório). Nada de nome pessoal e nada de linha de coautoria (`Co-Authored-By`), nem de gente nem de IA.
- **Contato público:** conteúdo e tecnicalidades com Lucas Rafaldini, pelo e-mail thothandson@icloud.com (Thoth & Son, empresa dele). Está no expediente da página inicial, no rodapé das páginas geradas e no README.
- **Estilo de escrita:** todo texto publicado segue o [guia de estilo](docs/ESTILO.md). Leia antes de escrever qualquer coisa que vá para o site. O resumo: direto, franco, carismático, sem pose e com humor e ironia que miram para cima. Sem travessão, sem a fórmula "não é X, é Y", sem enumerar tudo em três.
- **Fatos com fonte:** todo número e toda afirmação contestável têm link na seção "Fontes" do artigo e data de conferência no cabeçalho. O que não deu para confirmar não entra, ou entra com a ressalva escrita.
- **Site estático puro:** HTML e CSS, sem framework, sem npm e sem Jekyll (por isso o `.nojekyll`). As páginas de artigo são geradas por script Python, e o resultado é commitado.
- **Não edite à mão o que é gerado:** `artigos/`, `artes/`, `assets/artes/`, o bloco entre `<!-- artigos:inicio -->` e `<!-- artigos:fim -->` do `index.html`, o `?v=` do CSS nas páginas e os SVGs de `assets/logos/`, `assets/capa/` e `assets/favicon/`. Edite a fonte e rode o script.
- **Identidade visual:** vermelho `#C8102E`, preto `#141414`, papel `#F2EBDD`, amarelo `#FFE600`; títulos em Anton, detalhes em Special Elite, texto em Inter (tokens em `assets/style.css`). Logos e ícones têm o texto em curvas: nunca volte a usar `<text>` com fonte importada em SVG, porque fora do navegador o texto vaza da caixa.
- **Acessibilidade e celular:** a página tem que funcionar em 375 px sem rolagem lateral, com contraste bom e `alt`/`aria-label` nas imagens.

## Publicar com cuidado

O repositório é público, mas a pasta do projeto tem coisas que **não** podem ir para o GitHub:

- `manuais/`, `notas/` e `PAUTAS.md` estão no `.gitignore` e ficam só no disco. Nunca force a entrada deles (`git add -f`).
- Pode haver **commits locais ainda não publicados** com planos privados (por exemplo, tarefas e registro). Antes de qualquer `git push`, rode `git log --oneline origin/main..main` e confira o que vai junto. Se houver commit que não deve sair, publique só o necessário a partir de uma branch criada de `origin/main` (o passo a passo está na skill `publicar-site`).
- Cada `git push` na `main` publica o site em cerca de um minuto.

## Estrutura

| Caminho | O que é |
|---|---|
| `index.html` | Página inicial: sobre, pautas, artigos (bloco gerado), episódios, onde ouvir, expediente |
| `artes/index.html` | Artes para baixar: logos em várias larguras, capa, ícone e papéis de parede (gerada, não editar) |
| `conteudo/artigos/<slug>.md` | **Fonte dos artigos**, em Markdown com cabeçalho (`titulo`, `linha_fina`, `eixo`, `data`, `ordem`, `conferido`, `resumo`, `rascunho`) |
| `artigos/` | Páginas geradas dos artigos e o índice (não editar) |
| `docs/ESTILO.md` | Guia de estilo de escrita |
| `assets/style.css` | Todo o CSS do site |
| `assets/logos/`, `assets/capa/`, `assets/favicon/`, `favicon.ico` | Marca gerada por script |
| `scripts/gerar-artigos.py` | Gera as páginas de artigos, o índice, o bloco da página inicial e a versão do CSS |
| `scripts/revisar-estilo.py` | Confere os artigos contra o guia de estilo; o gerador roda ele antes e para se houver erro |
| `scripts/gerar-logos.py` | Gera logos, capa e favicon com o texto em curvas (fontes em `scripts/fontes/`) |
| `scripts/gerar-artes.py` | Exporta as artes em PNG e os papéis de parede em JPG para `assets/artes/` e gera a página `artes/` (precisa do Inkscape) |
| `TAREFAS.md`, `REGISTRO.md` | Próximos passos e decisões; o vault do Obsidian do Lucas lê esses arquivos |

## Ambiente

```bash
python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/gerar-artigos.py     # artigos
.venv/bin/python scripts/gerar-logos.py       # marca (SVGs)
.venv/bin/python scripts/gerar-artes.py       # downloads e papéis de parede (depois do gerar-logos)
python3 scripts/revisar-estilo.py             # só a revisão de estilo
python3 -m http.server 8000                   # ver em http://localhost:8000
```

A pasta fica num disco externo do macOS, que cria arquivos ocultos `._*` ao lado de cada arquivo. Eles estão no `.gitignore`, e os scripts pulam esses arquivos. Se o servidor local não conseguir ler o disco, copie o site para uma pasta temporária e sirva de lá.

## Verificar antes de publicar

1. `scripts/revisar-estilo.py` sem erros. Avisos de "três itens" pedem uma segunda olhada no texto.
2. `scripts/gerar-artigos.py` rodado depois da última mudança em artigo ou no CSS.
3. Página conferida no navegador no desktop e em 375 px, com o console sem erros.
4. `git status` sem nada de `manuais/`, `notas/` ou `PAUTAS.md`, e `git log origin/main..main` conferido.

## Skills e agentes

- `.claude/skills/novo-artigo`: escrever um artigo do zero (pesquisa, rascunho, revisão, geração).
- `.claude/skills/publicar-site`: conferir, commitar e publicar sem levar junto o que é privado.
- `.claude/agents/revisor-de-texto.md`: revisa um artigo contra o guia de estilo e confere as fontes.

## Contexto

- O nome vem do duplo sentido: memória de trabalho é a *working memory* do computador e a memória de quem trabalha. Os quatro eixos de pauta são Trabalho, Tecnologia, Organização e Soberania.
