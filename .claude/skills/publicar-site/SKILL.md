---
name: publicar-site
description: Conferir, commitar e publicar mudanças do site do Memória de Trabalho no GitHub Pages sem levar junto arquivos ou commits privados. Use sempre antes de qualquer git push neste repositório.
---

# Publicar o site

1. **Gere o que é gerado:** `.venv/bin/python scripts/gerar-artigos.py` (e `scripts/gerar-logos.py` se mexeu na marca). O gerador de artigos para se o revisor de estilo achar erro.
2. **Confira no navegador** a página mudada, no desktop e em 375 px, com o console sem erros.
3. **Confira o que vai sair:**
   ```bash
   git status --short                     # nada de manuais/, notas/ ou PAUTAS.md
   git log --oneline origin/main..main    # commits locais que ainda não foram publicados
   ```
4. **Se não houver commit local pendente** (ou se todos puderem ser publicados): faça um commit pequeno com mensagem em português dizendo o que mudou e rode `git push`.
5. **Se houver commit local que não deve ir para o GitHub**, publique só a mudança nova a partir de `origin/main` e depois recoloque os commits locais por cima:
   ```bash
   git fetch
   git checkout -b publicar origin/main        # as mudanças ainda não commitadas vêm junto
   git add <só os arquivos desta mudança>
   git commit -m "…"
   git push origin publicar:main
   git checkout main
   git rebase publicar                          # os commits locais voltam por cima
   git branch -d publicar
   ```
   Se o rebase reclamar de "local changes" que não existem, é o disco externo confundindo as datas dos arquivos: `git rebase --abort` e rode de novo com `git -c core.trustctime=false -c core.checkStat=minimal rebase publicar`.
6. **Confira no ar:** espere o build terminar (`gh api repos/Memoria-de-Trabalho/memoria-de-trabalho.github.io/pages/builds/latest --jq .status` deve dizer `built` com o commit novo) e abra a página publicada.
