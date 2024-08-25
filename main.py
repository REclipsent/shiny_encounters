from tkinter import *
from tkinter import ttk
import encounter_io as ei


def increment_counter(*args) -> None:
    current_count: int = count.get()
    current_pokemon: str = pokemon.get().strip()

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
root.title('Shiny Encounter')

pokemon = StringVar()
ttk.Entry(root, textvariable=pokemon).pack()
pokemon.trace('w', load_pokemon)

count = IntVar()
ttk.Label(root, textvariable=count).pack()

ttk.Button(root, text='Encounter', command=increment_counter).pack()
ttk.Button(root, text='Reset', command=reset_count).pack()
ttk.Button(root, text='Quit', command=root.quit).pack()


if __name__ == '__main__':
    root.mainloop()