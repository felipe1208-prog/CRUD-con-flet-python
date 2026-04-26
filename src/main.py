import flet as ft

def main(page: ft.Page):
    page.title = "CRUD Programadores"
    page.window.width = 1000
    page.window.height = 600
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()

if __name__ == "__main__":
    ft.run(main)