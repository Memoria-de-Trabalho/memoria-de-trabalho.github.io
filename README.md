# Memória de Trabalho

Podcast de e para profissionais de tecnologia de esquerda: trabalho, tecnologia, organização e soberania digital. Este repositório guarda o site (publicado pelo GitHub Pages em https://memoria-de-trabalho.github.io) e a identidade visual.

O site é estático (HTML + CSS, sem build e sem Jekyll).

- `index.html`: página principal
- `marca.html`: logo principal e alternativos, com sugestões de uso
- `assets/logos/memoria-de-trabalho.svg`: logo principal (pente de RAM)
- `assets/logos/alternativos/`: carimbo, lambe-lambe e estêncil, para outros materiais
- `scripts/gerar-logos.py`: gera todos os SVGs com o texto enquadrado pelas métricas reais das fontes
- `TAREFAS.md`: próximos passos do projeto
- `REGISTRO.md`: decisões e histórico

Para ver localmente: `python3 -m http.server` na raiz e abrir http://localhost:8000.
