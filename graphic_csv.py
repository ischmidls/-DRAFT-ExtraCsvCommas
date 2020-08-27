"""
graphic_csv.py

This file creates a graphic user interface (GUI)
for the change_csv program

https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-pattern-1a-one-shot-window-the-simplest-pattern

"""

import change_csv as cc
import PySimpleGUI as sg
import os.path


def query_up():
    layout = [[sg.Text('Enter output name: ')],
              [sg.InputText(key='-IN-')],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Window Title', layout)

    event, values = window.read()
    window.close()

    return values['-IN-']


def event_folder(values, window):
    folder =values["-FOLDER-"]
    try:
        # Get list of files in folder
        file_list = os.listdir(folder)
    except:
        file_list = []

    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith(".txt")
    ]
    window["-FILE LIST-"].update(fnames)


def event_loop(window):
    # Create an event loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-FOLDER-":
            event_folder(values, window)
        if event == "-FILE LIST-":
            os.chdir(values["-FOLDER-"])
            o_file = query_up()
            cc.Spaces(values["-FILE LIST-"][0]).space_comma(o_file)


def main():
    layout = [
        [
            sg.Text("Files"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"),
        ]

    ]

    # Create the window
    window = sg.Window(title="Point of View", layout=layout, margins=(300, 150))

    event_loop(window)

    window.close()


if __name__ == '__main__':
    main()
