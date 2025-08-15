# NOME DO ARQUIVO: app.py (versão com ft.Colors corrigido)

import flet as ft
from datetime import datetime
import random

# ===================================================================
# IMPORTANTE: Insira o "Cloud Name" da sua conta do Cloudinary aqui
# ===================================================================
CLOUDINARY_CLOUD_NAME = "dqinmfcnb"
# ===================================================================

# Fontes
FONT_TITLE = "Philosopher"
FONT_SUBTITLE = "Philosopher"
FONT_BUTTON = "Roboto"


def main(page: ft.Page):
    page.title = "Liturgia Diária"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#eceff1"
    page.padding = 20

    # Carrega as fontes para a página (buscando de um repositório público do Google Fonts)
    page.fonts = {
        "Philosopher": "https://github.com/google/fonts/raw/main/ofl/philosopher/Philosopher-Regular.ttf",
        "Roboto": "https://github.com/google/fonts/raw/main/apache/roboto/Roboto-Regular.ttf"
    }

    # --- Lógica para Montar a URL da Imagem ---
    today = datetime.now()
    formatted_date = today.strftime('%Y_%m_%d')
    image_url = f"https://res.cloudinary.com/{CLOUDINARY_CLOUD_NAME}/image/upload/salmos/salmo_{formatted_date}.png"

    # --- Elementos Visuais ---
    title = ft.Text("Liturgia Diária", size=36, weight=ft.FontWeight.BOLD, font_family=FONT_TITLE)
    subtitle = ft.Text("Prova de Amor", size=20, italic=True, font_family=FONT_SUBTITLE)
    psalm_image = ft.Image(
        src=image_url,
        width=300,
        height=375,
        fit=ft.ImageFit.CONTAIN,
        border_radius=ft.border_radius.all(8)
    )

    # --- Efeito de Hover para os Botões ---
    def on_hover(e):
        # CORREÇÃO AQUI: ft.Colors (com 'C' maiúsculo)
        e.control.bgcolor = ft.Colors.BLACK12 if e.data == "true" else "transparent"
        e.control.update()

    # --- Funções dos Botões ---
    def share_whatsapp(e):
        page.launch_url(f"https://api.whatsapp.com/send?text=Veja o Salmo do Dia: {image_url}")

    def open_image(e):
        page.launch_url(image_url)

    def copy_link(e):
        page.set_clipboard(image_url)
        page.snack_bar = ft.SnackBar(ft.Text("Link copiado!"), open=True)
        page.update()

    # --- Botões com Estilo de Fonte Corrigido ---
    button_style = ft.ButtonStyle(
        color="black",
        bgcolor="transparent",
        shape=ft.RoundedRectangleBorder(radius=8),
        text_style=ft.TextStyle(font_family=FONT_BUTTON, size=14)
    )

    share_buttons = ft.Row(
        controls=[
            ft.ElevatedButton("WhatsApp", icon="share", on_click=share_whatsapp, style=button_style, on_hover=on_hover),
            ft.ElevatedButton("Abrir", icon="open_in_new", on_click=open_image, style=button_style, on_hover=on_hover),
            ft.ElevatedButton("Copiar Link", icon="copy", on_click=copy_link, style=button_style, on_hover=on_hover),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        spacing=10
    )

    # --- Container principal com moldura ---
    main_container = ft.Container(
        content=ft.Column(
            [
                title,
                subtitle,
                psalm_image,
                share_buttons
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        width=380,
        bgcolor="#ffffff",
        border=ft.border.all(1, "#e0e0e0"),
        border_radius=ft.border_radius.all(15),
        padding=ft.padding.symmetric(vertical=25, horizontal=20),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            # CORREÇÃO AQUI: ft.Colors (com 'C' maiúsculo) e ft.colors.BLACK
            color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
            offset=ft.Offset(0, 5),
        )
    )

    page.add(main_container)


if __name__ == "__main__":
    # Removi o timer de fundo para simplificar o código
    ft.app(target=main)