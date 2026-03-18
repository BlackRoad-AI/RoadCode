# BlackRoad-AI RoadCode

Canonical RoadCode workspace and automation hub for BlackRoad-AI.

## What Lives Here

- RoadCode landing page and deploy surface
- org-specific operator workflows
- automation entrypoints for GitHub, Gitea, Slack, and Cloudflare

## Deploy

This repo ships a static site from site/ to both GitHub Pages and Cloudflare Pages.

- GitHub Pages URL: https://blackroad-ai.github.io/RoadCode/
- Cloudflare Pages URL: https://blackroad-ai-roadcode.pages.dev
- Expected Cloudflare project name: blackroad-ai-roadcode

## Operator Notes

- Default branch: main
- GitHub Pages workflow: .github/workflows/github-pages.yml
- Workflow: .github/workflows/roadcode-pages.yml
- Site entrypoint: site/index.html
