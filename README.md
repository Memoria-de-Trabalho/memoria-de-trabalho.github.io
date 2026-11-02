# Memória de Trabalho

Podcast de e para profissionais de tecnologia de esquerda: trabalho, tecnologia, organização e soberania digital. Este repositório guarda o site (publicado pelo GitHub Pages em https://memoria-de-trabalho.github.io) e a identidade visual.

O site é estático (HTML + CSS, sem build e sem Jekyll).

- `index.html`: página principal
- `artes/`: página com logos, capa, ícone e papéis de parede para baixar (gerada por `scripts/gerar-artes.py`, arquivos em `assets/artes/`)
- `conteudo/artigos/`: fonte dos artigos em Markdown; `artigos/` é gerado por `scripts/gerar-artigos.py`
- `docs/ESTILO.md`: guia de estilo de escrita (vale para todo texto publicado)
- `AGENTS.md` e `.claude/`: instruções, skills e agente revisor para quem desenvolve ou escreve com agentes
- `assets/logos/memoria-de-trabalho.svg`: logo principal (pente de RAM)
- `assets/logos/alternativos/`: carimbo, lambe-lambe e estêncil, para outros materiais
- `assets/capa/`: capa do podcast (SVG gerado pelo script; PNG e JPG 3000×3000 exportados com o Inkscape, `--export-png-color-mode=RGB_8` para sair sem transparência)
- `scripts/gerar-logos.py`: gera todos os SVGs com o texto em curvas (sem depender de fonte instalada). Precisa de `pip install -r scripts/requirements.txt`
- `scripts/fontes/`: Anton, Alfa Slab One, Big Shoulders Stencil Display e Special Elite (Google Fonts, licença SIL OFL)
- `TAREFAS.md`: próximos passos do projeto
- `REGISTRO.md`: decisões e histórico

Para ver localmente: `python3 -m http.server` na raiz e abrir http://localhost:8000.
