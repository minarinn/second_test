import flet as ft

def main(page: ft.Page):
    page.title = "Список покупок"
    page.vertical_alignment = "start"

    list_of_items = ft.Column()
    input = ft.TextField(hint_text="Введите товар", expand=True)

    def add(e):
        if input.value.strip() == "":
            return
        
        new_row = ft.Row()
        chek = ft.Checkbox(label=input.value)
        button_del = ft.IconButton(icon=ft.Icons.DELETE)

        def del_fn(ev):
            list_of_items.controls.remove(new_row)
            page.update()

        button_del.on_click = del_fn

        new_row.controls.append(chek)
        new_row.controls.append(button_del)

        list_of_items.controls.append(new_row)

        input.value = ""
        page.update()

    knopka_dobav = ft.ElevatedButton("Добавить", on_click=add)

    page.add(
        ft.Text("Список покупок", size=24, weight="bold"),
        ft.Row([input, knopka_dobav]),
        list_of_items
    )

ft.app(target=main)
