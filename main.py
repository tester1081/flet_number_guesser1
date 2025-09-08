import flet as ft
import random
import asyncio
from flet import *

def main(page: ft.Page):
    page.title = 'Guess a number'

    lowest_number = ft.TextField(hint_text='Enter a lower number')
    highest_number = ft.TextField(hint_text='Enter a higher number')
    results = ft.Text(value="Results Would Show Up HERE...", color=Colors.BLACK)

    async def change_function(e):
        if not lowest_number.value or not highest_number.value:
            results.value = "Error: Both fields must not be empty"
            results.color = Colors.RED
            page.update()
            await asyncio.sleep(3)
            results.value = "Results Would Show Up HERE..."
            results.color = Colors.BLACK
            page.update()
            return

        min_num = int(lowest_number.value)
        high_num = int(highest_number.value)

        if min_num > high_num:
            results.value = "Error: enter a minimum number in the first field"
            results.color = Colors.RED
            page.update()
            await asyncio.sleep(3)
            results.value = "Results Would Show Up HERE..."
            results.color = Colors.BLACK
            page.update()
            return

        generate = random.randint(min_num, high_num)
        results.value = f"Generated Number is {generate}"
        page.update()

    click = ft.ElevatedButton(text='Generate random', on_click=change_function)
    page.add(lowest_number, highest_number, results, click)

# this makes it run as a web app
ft.app(target=main, view=ft.WEB_BROWSER)
