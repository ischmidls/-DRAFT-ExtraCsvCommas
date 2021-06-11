"""
graphicCsv.py

This file creates a graphic user interface (GUI)
for the change_csv program

https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-pattern-1a-one-shot-window-the-simplest-pattern

"""

import changeCsv as cc
import PySimpleGUI as sg
import os.path


def query_window(window, layout):
    """
    pop up window to name output file
    """
    new_layout = [[sg.Text('Enter output name: ')],
              [sg.InputText(key='-IN-')],
              [sg.Submit(), sg.Cancel()]]

    window[layout].update(new_layout)

    event, values = window.read()
    window.close()

    return values['-IN-']



def event_folder(values, window):
    """
    return txt file names from selected folder
    """
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
    """
    create an event loop
    """
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-FOLDER-":
            event_folder(values, window)
        if event == "-FILE LIST-":
            os.chdir(values["-FOLDER-"])
            o_file = query_window()
            cc.Spaces(values["-FILE LIST-"][0]).space_comma(o_file)


def main():
    layout = [
        [
            sg.Text("Pick a file path: "),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Text("Pick a file to separate: "),
            sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"),
        ]

    ]

    # Create the window
    window = sg.Window(title="Comma Separated Values", layout=layout, margins=(300, 150))

    event_loop(window)

    window.close()


if __name__ == '__main__':
    main()
