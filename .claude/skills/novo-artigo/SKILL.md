---
name: novo-artigo
description: Escrever um artigo novo para a seção de artigos do site do Memória de Trabalho, da pesquisa à página gerada. Use quando pedirem um artigo, texto, post ou versão de um texto para o site.
---

# Novo artigo

1. **Leia o guia de estilo** em `docs/ESTILO.md`. Ele manda mais do que qualquer instinto de escrita.
2. **Pesquise antes de escrever.** Junte fontes primárias (lei no Planalto, norma do Banco Central, documento oficial da empresa, decisão judicial) e, quando não houver, reportagem de veículo identificado. Anote URL, veículo e data de cada uma. Site do Banco Central e de outros órgãos costuma precisar de navegador para renderizar.
3. **Crie `conteudo/artigos/<slug>.md`** (slug em minúsculas, sem acento, com hífens) com o cabeçalho:

   ```
   ---
   titulo: …
   linha_fina: …
   eixo: Trabalho | Tecnologia | Organização | Soberania
   data: AAAA-MM-DD
   ordem: 1
   conferido: AAAA-MM-DD
   resumo: uma frase para o cartão da lista
   rascunho: true
   ---
   ```

   Enquanto `rascunho: true`, o artigo não é publicado.
4. **Siga a estrutura do guia:** "Para quem tem pressa", corpo com intertítulos, "E eu com isso?" (obrigatório), "Para conversar" (opcional) e "Fontes".
5. **Revise:** `python3 scripts/revisar-estilo.py conteudo/artigos/<slug>.md`. Corrija todos os erros. Para cada aviso de "três itens", reescreva ou justifique. Leia o texto inteiro mais uma vez procurando a fórmula "não é X, é Y" quebrada em duas frases e afirmações sem fonte.
6. **Peça a revisão do agente** `revisor-de-texto` quando o artigo for longo ou tiver muitos números.
7. **Tire o `rascunho: true`**, rode `.venv/bin/python scripts/gerar-artigos.py` e confira a página em `http://localhost:8000/artigos/<slug>/`, no desktop e em 375 px.
8. **Publique** com a skill `publicar-site`.
