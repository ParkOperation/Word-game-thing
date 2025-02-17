import flet as ft
import random

def main(page: ft.Page):
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince"]
    total_words = len(words)

    def reset_game():
        nonlocal words, current_index, mistakes
        random.shuffle(words)
        current_index = 0
        mistakes = 0
        word_label.value = words[current_index]
        status_label.value = ""
        progress_label.value = f"0/{total_words}"
        accuracy_label.value = "Accuracy: 100%"
        input_field.value = ""
        input_field.disabled = False
        page.update()

    current_index = 0
    mistakes = 0
    random.shuffle(words)

    word_label = ft.Text(words[current_index], size=24, weight="bold")
    status_label = ft.Text("", size=20)
    progress_label = ft.Text(f"0/{total_words}")
    accuracy_label = ft.Text("Accuracy: 100%")
    input_field = ft.TextField(on_submit=lambda e: check_word(e))
    reset_button = ft.ElevatedButton(text="Reset", on_click=lambda e: reset_game())

  #braulio was here lmfao