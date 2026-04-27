import flet as ft

def main_layout(page: ft.Page):
    
    modulos = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        on_change=lambda _: print("a"),#A la espera de funcion de cambio de vista
        destinations=[
            """
            Vistas
            """
        ]
    )