import flet as ft
from datetime import datetime, timezone, timedelta

def main(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.LIGHT
    text_hello = ft.Text(value = 'Hello world!')
    def text_name(_):
        name = name_input.value.strip()
        if name:
            text_hello.color = None
            tz = timezone(timedelta(hours=6))
            now = datetime.now(tz)
            text_hello.value = f'{now.strftime("%Y-%m-%d %H:%M:%S")} - Hello {name}'
        else:
            text_hello.value = 'Enter the name!'
            text_hello.color = ft.Colors.RED
    def change_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
    elevated_button  = ft.ElevatedButton('send', on_click=text_name)
    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=change_theme) 
    name_input = ft.TextField(label = 'Enter something')
    page.add(text_hello, name_input, elevated_button, thememode_button)
ft.app(target = main)