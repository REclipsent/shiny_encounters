from tkinter import *
from tkinter import ttk
import encounter_io as ei


def increment_counter(*args) -> None:
    current_count: int = count.get()
    current_pokemon: str = pokemon.get().strip()

    if current_pokemon == "":
        return

    current_count += 1

    count.set(current_count)
    ei.save_counts(current_pokemon, current_count)


def reset_count(*args) -> None:
    count.set(0)


def load_pokemon(*args) -> None:
    requested_pokemon: str = pokemon.get().strip()
    old_count: int = ei.load_counts(requested_pokemon)
    count.set(old_count)


root = Tk()
root.title('Shiny Encounter Tracker')

pokemon = StringVar()
ttk.Entry(root, textvariable=pokemon).grid(row=0, column=0, padx=10, pady=10, sticky=W)
pokemon.trace('w', load_pokemon)

count = IntVar()
ttk.Label(root, textvariable=count).grid(row=1, column=0, padx=10, pady=10, sticky=W)

ttk.Button(root, text='Encounter', command=increment_counter).grid(row=2, column=0, padx=10, pady=10, sticky=W)
ttk.Button(root, text='Reset', command=reset_count).grid(row=2, column=1, padx=10, pady=10, sticky=W)
ttk.Button(root, text='Quit', command=root.quit).grid(row=2, column=2, padx=10, pady=10, sticky=W)


if __name__ == '__main__':
    root.mainloop()