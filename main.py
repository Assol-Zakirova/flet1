import flet as ft 


def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT
    text_hello = ft.Text(value='Hello world')
    greeting_history = []
    history_text = ft.Text('История приветствий:')
    def text_name(_):
        name = name_input.value.strip()

        if name:
            text_hello.color = None
            text_hello.value = f'Hello {name}'
            name_input.value = None

            greeting_history.append(name)
            a = greeting_history
            history_text.value = 'История приветствий:\n' + '\n'.join(greeting_history)

        else:
            text_hello.value = "Введите имя!"
            text_hello.color = ft.Colors.RED

    elevated_button = ft.ElevatedButton('send', on_click=text_name, icon=ft.Icons.SEARCH, color=ft.Colors.RED, icon_color=ft.Colors.BLACK)

    name_input = ft.TextField(label='Введите что-нибудь', on_submit=text_name, expand=True)

    def thememode(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK

    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)
    def clear_history(_):
        print(greeting_history)
        greeting_history.clear()
        print(greeting_history)
        history_text.value = 'История приветствий:'
    def sort_history(_):
        greeting_history.sort(key=lambda m: m[0])
        history_text.value = 'Отсортированная история приветствий:\n' + '\n'.join(greeting_history)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    sort_button = ft.IconButton(icon=ft.Icons.SORT, on_click=sort_history)
    main_object = ft.Row([name_input, elevated_button, thememode_button, clear_button, sort_button])
    page.add(text_hello, main_object, history_text)


ft.app(target=main)

