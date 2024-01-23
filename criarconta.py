from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch()
    # Criar uma nova página no navegador
