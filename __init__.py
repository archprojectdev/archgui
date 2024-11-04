"""
__init__.py
"""

import FreeSimpleGUI as fsg

import os
import io
import json
import shutil
import importlib

from sys import platform

from .Windows import Windows
from .Model import Model
from .Workarea import Workarea

workarea = Workarea(platform, fsg)
windows = Windows(platform, fsg, workarea)

models_event = {}
specters = {}


if os.path.isdir("archgui_events"):

    for file in os.listdir("archgui_events"):
        file_split = os.path.splitext(file)

        if file_split[1] == ".py":
            my_module = importlib.import_module("archgui_events." + file_split[0])
            models_event[file_split[0]] = my_module.Events()
else:

    print("Le dossier 'archgui_events' est introuvable.")
    exit(0)


if os.path.isdir("archgui_windows"):

    for file in os.listdir("archgui_windows"):
        file_split = os.path.splitext(file)

        if file_split[1] == ".json":
            specters[file_split[0]] = json.load(io.open("archgui_windows/" + file))
else:

    print("Le dossier 'archgui_events' est introuvable.")
    exit(0)


config = json.load(io.open("archgui/config/default.json"))

windows.load_config(config)
models_window = {}

for model in models_event:
    models_window[model] = Model(windows, model, specters[model])

windows.load_models(models_window, models_event)


def define_modules(modules):
    """
    :param modules:
    :return:
    """
    global windows

    if windows.define_modules(modules):
        return True
    else:
        return False


def define_main(uniqid: str):
    """
    :param uniqid:
    :return:
    """
    global windows

    if windows.define_main(uniqid=uniqid):
        return True
    else:
        return False


def open(model: str, monitor=None, id=None, title=None, uniqid=None, location=None, size=None):
    """
    :param model:
    :param monitor:
    :param id:
    :param title:
    :param uniqid:
    :param location:
    :param size:
    :return:
    """
    global windows

    uniqid = windows.open(
        model=model,
        monitor=monitor,
        id=id,
        title=title,
        uniqid=uniqid,
        location=location,
        size=size)

    if uniqid:
        return uniqid
    else:
        return False


def bind(uniqid: str, binds: list):
    """
    :param uniqid:
    :param binds:
    :return:
    """
    global windows

    if windows.bind(
            uniqid=uniqid,
            binds=binds):
        return True
    else:
        return False


def update(uniqid: str, items: list):
    """
    :param uniqid:
    :param items:
    :return:
    """
    global windows

    if windows.update(
            uniqid=uniqid,
            items=items):
        return True
    else:
        return False


def close(uniqid: str):
    """
    :param uniqid:
    :return:
    """
    global windows

    if windows.close(uniqid=uniqid):
        return True
    else:
        return False


def graph_draw_image(uniqid: str, graph: str, location: list, image=None):
    """
    :param uniqid:
    :param graph:
    :param location:
    :param image:
    :return:
    """
    global windows

    result = windows.graph_draw_image(
        uniqid=uniqid,
        graph=graph,
        location=location,
        image=image)
    return result


def graph_bring_figure_to_front(uniqid: str, graph: str, figure: int):
    """
    :param uniqid:
    :param graph:
    :param figure:
    :return:
    """
    global windows

    if windows.graph_bring_figure_to_front(
            uniqid=uniqid,
            graph=graph,
            figure=figure):
        return True
    else:
        return False


def graph_send_figure_to_back(uniqid: str, graph: str, figure: int):
    """
    :param uniqid:
    :param graph:
    :param figure:
    :return:
    """
    global windows

    if windows.graph_send_figure_to_back(
            uniqid=uniqid,
            graph=graph,
            figure=figure):
        return True
    else:
        return False


def run():
    """
    run()
    """
    global windows

    windows.events_run()
