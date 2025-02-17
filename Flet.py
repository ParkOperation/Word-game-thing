import flet as ft
import random

def main(page: ft.Page):
    words = ["Lantern", "Glacier", "Thunder", "Puzzle", "Whistle", "Velvet", "Echo", "Marshmallow", "Orbit", "Breeze", "Cactus", "Doodle", "Summit", "Ripple", "Wilson"]
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
        input_field.focus()  
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

    def check_word(e):
        nonlocal current_index, mistakes
        if input_field.value.strip().lower() == words[current_index].lower():
            status_label.value = "Correctly Written! Very Nice!"
            status_label.color = "green"
        else:
            status_label.value = "Incorrectly Written! Cmon, you can do better."
            status_label.color = "red"
            mistakes += 1

        current_index += 1
        if current_index < total_words:
            word_label.value = words[current_index]
            progress_label.value = f"{current_index}/{total_words}"
        else:
            accuracy = ((total_words - mistakes) / total_words) * 100
            accuracy_label.value = f"Your Accuracy: {accuracy:.2f}%"
            progress_label.value = f"{total_words}/{total_words}"
            input_field.disabled = True  

        input_field.value = ""
        input_field.focus() 
        page.update()

    page.add(word_label, status_label, progress_label, accuracy_label, input_field, reset_button)
    input_field.focus()

ft.app(target=main)
