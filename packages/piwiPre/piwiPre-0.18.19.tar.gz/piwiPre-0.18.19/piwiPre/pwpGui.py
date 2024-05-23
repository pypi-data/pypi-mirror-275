
import os
import tkinter
from tkinter import ttk
import tkinter.font

from piwiPre.pwpLogoSmall import pwpLogo_png


class PwpGui:
    tk = None
    label_font = None
    font_pixels = None
    GREEN = "#aaaEEEaaa"
    GREY = "#eeeEEEeee"
    GREY2 = "#cccCCCccc"
    LIGHT_GREY = "#e00e00e00"
    WHITE = "white"
    ORANGE = "#ff7700"
    LIGHT_BLUE = "#dddDDDeee"
    BUTTON_WIDTH = 10
    RADIO_WIDTH = 8
    VALUE_WIDTH = 60

    def __init__(self, name, language):
        self.root = None
        self.frm = None
        self.language = language
        self.widgets = []  # record all items to be able to change the language
        try:
            if PwpGui.tk is None:
                PwpGui.tk = tkinter.Tk()
                self.root = PwpGui.tk
            else:
                self.root = tkinter.Toplevel()
            self.root.title(name)

            self.frm = ttk.Frame(self.root, padding=10)
            self.frm.grid()
        except tkinter.TclError:
            print("Unable to start Tk")

        self.feedback = None  # displayer of messages
        if PwpGui.label_font is None:
            PwpGui.label_font = tkinter.font.Font(size=9, family="Helvetica", weight="bold")
            PwpGui.font_pixels = PwpGui.label_font.measure("n")

    def record_widget(self, widget):
        self.widgets.append(widget)

    def remove_widget(self, widget):
        if widget in self.widgets:
            self.widgets.remove(widget)
        else:
            raise OSError

    def set_language(self, language):
        self.language = language
        for widget in self.widgets:
            widget.set_language(language)

    @staticmethod
    def delete():
        PwpGui.tk = None
        PwpGui.label_font = None
        PwpGui.font_pixels = None

    def column_sizes(self, sizes):
        for i in range(0, len(sizes)):
            self.frm.columnconfigure(i, minsize=PwpGui.font_pixels * sizes[i])

    def mainloop(self):
        if self.root:
            self.root.mainloop()

    def exit(self):
        print("Exiting from program")
        self.root.destroy()
        if self.root == PwpGui.tk:
            PwpGui.delete()

    # @staticmethod
    # def relative_path(path: str,
    #                   cwd: str):
    #     """
    #     get the relative path vs cwd
    #     if not on the same drive, or not inside cwd, returns an absolute path
    #     :param path:
    #     :param cwd:
    #     :return: new path
    #     """
    #     abs_path = os.path.abspath(path)
    #     abs_cwd = os.path.abspath(cwd)
    #
    #     if os.path.splitdrive(abs_path)[0] == os.path.splitdrive(abs_cwd)[0]:
    #         # they are on same drive
    #         res = str(os.path.relpath(abs_path, abs_cwd))
    #         res = abs_path if res.startswith('..') else res
    #     else:
    #         # home and path are on a different drive, so realpath would fail
    #         res = abs_path
    #     res = res.replace('\\', '/')
    #
    #     return res

    # ---------------------------------------------------------------------------------------------
    # graphical elements

    def add_messager(self, row, title, fr_title, height):
        if not self.feedback:
            self.feedback = GuiMessager(root_gui=self, frm=self.frm, row=row,
                                        title=title, fr_title=fr_title, height=height)

    def gui_msg(self, line, tag=None):
        if not self.feedback:
            print(line)
        if tag is None:
            self.feedback.insert(tkinter.END, line + "\n")
        else:
            self.feedback.insert(tkinter.END, line + "\n", tag)
        self.feedback.yview(tkinter.END)

    def gui_warning(self, line):
        self.gui_msg("WARNING: " + line, "orange")

    def gui_error(self, line):
        self.gui_msg("ERROR  : " + line, "red")


class GuiMessager:
    def __init__(self, root_gui: PwpGui, frm, row, title, fr_title, height=5, width=1400):  # width is in pixel !
        self.frm = frm
        self.width = width
        self.separator = GuiSeparator(root_gui, frm=frm, row=row, text=title, fr_text=fr_title)
        font = tkinter.font.Font(size=10, family="Courier")

        chars = int(self.width / font.measure("n")) - 1
        # -------------- Feedback
        row += 1

        self.scroller = GuiScrollable(root_gui, frm, row=row, column_sizes=[], name="messenger",
                                      width=self.width,
                                      height=height*font.measure("n")*2)
        # CAVEAT: height in pixels
        #         * 2 because character width != height.

        self.feedback = tkinter.Text(self.scroller.frm, background=PwpGui.LIGHT_GREY,
                                     padx=3, pady=3,
                                     font=font,
                                     #  height=height,
                                     width=chars,)
        self.feedback.pack()
        self.feedback.tag_config('orange', foreground=PwpGui.ORANGE)
        self.feedback.tag_config('red', foreground="red")
        self.feedback.tag_config('blue', foreground="blue")

    def insert(self, where, line, tag=None):
        self.feedback.insert(where, line, tag)

    def yview(self, d):
        self.feedback.yview(d)


# ====================================================================================
# GuiButton
# ====================================================================================


class GuiButton(tkinter.Button):
    def __init__(self, root_gui: PwpGui, frm, column, row, text, fr_text, command,
                 background="green",  sticky="W",
                 width=PwpGui.BUTTON_WIDTH):
        super().__init__(frm, text=fr_text if root_gui.language == 'fr' else text,
                         width=width, command=command,
                         background=background, foreground="white",
                         activebackground="white", activeforeground=background,
                         )
        self.grid(column=column, row=row, sticky=sticky)
        self.back_ground = background
        self.column = column
        self.text = text
        self.fr_text = fr_text
        self.root_gui = root_gui
        root_gui.record_widget(self)

    def set_language(self, lan):
        # print(f"Set language Button({self.fr_text}) {lan}")
        self["text"] = self.fr_text if lan == "fr" else self.text

    def disable(self):
        self.configure(background=PwpGui.GREY2)
        self["state"] = 'disabled'

    def enable(self):
        self.configure(background=self.back_ground)
        self["state"] = 'normal'

    def show(self, row):
        self.grid(column=self.column, row=row, sticky="W")

    def hide(self):
        self.grid_forget()


# ================================================================================
# GuiLabel
# ================================================================================


class GuiLabel(ttk.Label):
    def __init__(self, root_gui: PwpGui, frm, column, row, text, fr_text,
                 col_span=1, background=None, width=10, bold=None, relief=False):
        super().__init__(frm, text=fr_text if root_gui.language == "fr" else text,
                         background=background, anchor="w", padding=2,
                         width=width,
                         font=PwpGui.label_font if bold else None, border=0, borderwidth=0,
                         relief='sunken' if relief else 'flat',
                         foreground="grey" if relief else None,)

        self.grid(column=column, row=row, sticky="W", columnspan=col_span, padx=1, pady=1)
        self.back_ground = background
        self.column = column
        self.text = text
        self.fr_text = fr_text
        self.root_gui = root_gui
        self.col_span = col_span
        root_gui.record_widget(self)

    def set(self, text, fr_text):
        lan = self.root_gui.language
        self["text"] = fr_text if lan == "fr" else text

    def set_language(self, lan):
        # print(f"Set language Label({self.text}) {lan}")
        self["text"] = self.fr_text if lan == "fr" else self.text

    def show(self, row):
        self.grid(column=self.column, row=row, sticky="W", columnspan=self.col_span)

    def hide(self):
        self.grid_forget()

# ====================================================================================
# DirChooser
# ====================================================================================


class _DirChooserField:
    def __init__(self, root_gui: 'GuiDirChooser', frm, path, abspath, row, max_width1, max_width2, _choice):
        self.root_gui = root_gui
        self.frm = frm
        self.label = GuiLabel(root_gui, frm,
                              text=path, fr_text=path,
                              column=0, row=row, width=max_width1)
        self.abspath = GuiLabel(root_gui, frm,
                                text=abspath, fr_text=abspath,
                                column=1, row=row, width=max_width2, relief=True)

        self.choose = None
        self.enter = None

        # if choice:
        if True:
            self.choose = GuiButton(root_gui, frm, text="Choose", fr_text="Choisir",
                                    command=lambda: self.root_gui.select(path), sticky="N",
                                    background="green", column=3, row=row)

        # else:
        if True:
            self.enter = GuiButton(root_gui, frm, text="Enter", fr_text="Entrer",
                                   command=lambda: self.root_gui.enter(path), sticky="N",
                                   background="green", column=2, row=row)

    def delete(self):
        if self.enter:
            self.enter.destroy()
        if self.choose:
            self.choose.destroy()
        self.label.destroy()
        self.abspath.destroy()


class GuiDirChooser(PwpGui):
    """
    Class to choose a directory
    All paths are internally relative to CWD
    """
    running_chooser = None

    def __init__(self, root_gui, dir_name, name, called,
                 self_test=False, x=None, y=None, language="en"):
        """
        class PwpDirChooser(PwpGui):
        :param root_gui:  calling objet. must implement called(path)
        :param called: method from the father, called upon success
        :param dir_name:
        :param self_test:
        """
        super().__init__("Choisir un répertoire" if language == "fr" else "Directory chooser",
                         language=language)
        self.dir_name = dir_name
        self.father = root_gui
        self.called = called
        if x is not None and y is not None:
            self.root.geometry(f"+{int(x + 10)}+{y + 10}")
        self.columns = [35, 30, 15, 15, ]
        self.column_sizes(self.columns)
        self.do_dirs = tkinter.StringVar()
        self.folders = []
        self.scrollable = None

        row = 0
        # ----------------------- Logo and banner

        self.logo = pwpLogo_png.tk_photo()
        tkinter.Label(self.frm, image=self.logo).grid(column=0, row=row, sticky="W")

        title_font = tkinter.font.Font(size=14, family="Helvetica", weight="bold")
        title = f"Change '{name}'"

        lab = ttk.Label(self.frm, font=title_font, text=title)
        lab.grid(column=1, row=row, columnspan=8, sticky="W")

        # ----------------------- Abort
        row += 1
        GuiLabel(self, self.frm,
                 text=f"Previous {name}",
                 fr_text=f"Précédent {name}",
                 column=0, row=row, width="")

        val = os.path.abspath(self.dir_name)

        self.cur_dir = GuiLabel(self, self.frm,
                                text=val,
                                fr_text=val,
                                relief=True,
                                width=len(val),
                                column=1, row=row, col_span=2)

        self.abort = GuiButton(self, self.frm, column=3, row=row, sticky="N",
                               text="Cancel", fr_text="Annuler",
                               background='red',
                               command=self.exit)

        # ----------------------- sub directories
        row += 1
        self.sep1 = GuiSeparator(self, self.frm, row=row,
                                 text="Directories to choose",
                                 fr_text="Choisir un répertoire",
                                 width=800)

        # -----------------------

        row += 1
        GuiLabel(self, self.frm, column=0, row=row, text="Filename", fr_text="Fichier", bold=True)

        GuiLabel(self, self.frm, column=1, row=row,
                 text="path relative to CWD, or absolute if outside CWD",
                 fr_text="chemin relatif à CWD, ou absolu si en dehors de CWD",
                 bold=True,
                 width=PwpGui.VALUE_WIDTH, col_span=4, background=PwpGui.GREY)

        row += 1
        self.first_row = row
        self.build_list()
        if self_test:
            self.root.after(2 * 1000, lambda: self.enter('..'))
            self.root.after(3 * 1000, lambda: self.select('..'))
            self.root.after(4 * 1000, lambda: self.exit())
        self.frm.focus_set()
        if GuiDirChooser.running_chooser is not None:
            GuiDirChooser.running_chooser.exit()
        GuiDirChooser.running_chooser = self
        self.mainloop()

    def build_list(self):
        row = self.first_row
        for item in self.folders:
            item.delete()
        if self.scrollable:
            self.scrollable.suicide()

        father = os.path.dirname(os.path.abspath(self.dir_name))

        all_lines = [
            ("[HOME]", os.path.expanduser("~")),
            ('[CWD]', os.getcwd()),
            ("[.]  = this directory", os.path.abspath(self.dir_name)),
            ("[..] = father", os.path.abspath(father)),
            ]

        all_dirs = os.listdir(self.dir_name) if os.path.isdir(self.dir_name) else []
        all_lines += [(f, os.path.abspath(self.dir_name + '/' + f))
                      for f in all_dirs if os.path.isdir(self.dir_name + '/' + f)]

        max_width1 = 30
        max_width2 = PwpGui.VALUE_WIDTH

        for line in all_lines:
            max_width1 = max(max_width1, len(line[0]))
            max_width2 = max(max_width2, len(line[1]))

        # self.cur_dir['text'] = os.path.abspath(self.dir_name)
        # self.cur_dir['width'] = max_width2

        self.folders = []

        row += 1
        first = True

        self.scrollable = GuiScrollable(self.father, self.frm, row=row, name="multilevel",
                                        height=int(min(20, len(all_lines))*PwpGui.font_pixels*3.8),
                                        width=(max_width1 + max_width2+30)*PwpGui.font_pixels)
        self.scrollable.column_sizes(self.columns)
        cur_frame = self.scrollable.frm
        row = 0
        for line in all_lines:
            self.folders.append(_DirChooserField(self, cur_frame, path=line[0], abspath=line[1], row=row, _choice=first,
                                                 max_width1=max_width1, max_width2=max_width2, ))
            first = False
            row += 1

    def select(self, path: str):
        if path.startswith("[.]"):  # with current dirChooser, only . can be selected
            full_path = os.path.relpath(self.dir_name)
        elif path.startswith("[..]"):
            full_path = os.path.relpath(os.path.dirname(os.path.abspath(self.dir_name)))
        elif path.startswith("[HOME]"):
            full_path = os.path.relpath(os.path.expanduser("~"))
        elif path.startswith("[CWD]"):
            full_path = "."
        else:
            full_path = os.path.relpath(self.dir_name + '/' + path)

        if self.father and self.called:
            self.called(full_path)
        print(f"Chose directory '{full_path}'")
        self.exit()

    def enter(self, path):
        if path.startswith("[.]"):  # with current dirChooser, '.' can not be entered
            full_path = os.path.abspath(self.dir_name)
        elif path.startswith("[..]"):
            full_path = os.path.abspath(os.path.dirname(os.path.abspath(self.dir_name)))
        elif path.startswith("[HOME]"):
            full_path = os.path.relpath(os.path.expanduser("~"))
        elif path.startswith("[CWD]"):
            full_path = "."
        else:
            full_path = os.path.abspath(self.dir_name + '/' + path)

        print(f"Enter directory '{full_path}'")
        self.dir_name = full_path
        self.build_list()

    def exit(self):
        super().exit()
        GuiDirChooser.running_chooser = None

# ================================================================================
# GuiStringEditor
# ================================================================================


class GuiStringEditor(PwpGui):
    """
    Class to edit a string
    """
    running_editor = None

    def __init__(self, root_gui: PwpGui, father, name, initial, x=None, y=None):
        """
        class PwpStringEditor(PwpGui):
        :param father:  calling objet. must implement select_dir(path)
        :param initial: initial value
        """
        super().__init__("String Editor", language=root_gui.language)
        self.initial = initial
        self.father = father
        self.root_gui = root_gui

        # we do NOT record a String editor to its root GUI,
        # because string editors are dynamically built with the right language
        # and are destroyed after usage
        # root_gui.record_item(self)

        self.variable = tkinter.StringVar()
        self.variable.set(initial)

        if x is not None and y is not None:
            self.root.geometry(f"+{int(x + 10)}+{y + 10}")

        self.column_sizes([15, 55, 18, 18])

        # ----------------------- Logo and banner
        row = 0

        self.logo = pwpLogo_png.tk_photo()
        tkinter.Label(self.frm, image=self.logo).grid(column=0, row=row, sticky="W")

        # ----------------------- Title
        row += 1
        GuiLabel(self, self.frm, column=0, row=row, text="Change", fr_text="Changer",  bold=True)
        GuiLabel(self, self.frm, column=1, row=row, text=name, fr_text=name, bold=True)

        row += 1
        GuiLabel(self, self.frm, column=0, row=row, bold=True, width=15,
                 text="Current value", fr_text="Valeur courante")
        GuiLabel(self, self.frm, column=1, row=row, text=initial, fr_text=initial)

        # ----------------------- Abort
        row += 1

        entry = tkinter.Entry(self.frm, background=PwpGui.GREEN, width=65,
                              textvariable=self.variable, state=tkinter.NORMAL)
        entry.grid(column=0, row=row, sticky="W", columnspan=2)

        GuiButton(self, self.frm, column=2, row=row, text="Ok", fr_text="Ok", command=self.choose)
        GuiButton(self, self.frm, column=3, row=row, text="Cancel", fr_text="Annuler", command=self.exit,
                  background="red")

        self.frm.focus_set()
        if GuiStringEditor.running_editor is not None:
            GuiStringEditor.running_editor.exit()
        GuiStringEditor.running_editor = self
        self.mainloop()

    # def set_language(self, language):
    #     super().set_language(language)

    def choose(self):
        ret_val = self.variable.get()
        if self.father:
            self.father.set_value_and_refresh(ret_val, "GUI", "modify")
        print(f"Chose '{ret_val}'")
        self.exit()


# ================================================================================
# GuiInfo
# ================================================================================


class GuiInfo(PwpGui):
    def __init__(self):
        super().__init__("info", language="en")
        self.logo = pwpLogo_png.tk_photo()
        tkinter.Label(self.frm, image=self.logo).grid(column=0, row=0, sticky="W")

        self.title = ttk.Label(self.frm, text="info",  padding=4, width=100, font=self.label_font)
        self.title.grid(column=0, row=1, sticky="N")

        self.label = ttk.Label(self.frm, text="info", anchor="w", padding=4, width=100)
        self.label.grid(column=0, row=2, sticky="W")

        self.hide()

    def show(self, title, info, x, y):
        self.title['text'] = title
        self.label['text'] = info
        self.root.deiconify()
        self.root.lift()

        self.root.geometry(f"+{int(x + 10)}+{y + 10}")

    def hide(self):
        self.root.withdraw()


class GuiLevelSeparator:
    def __init__(self, root_gui, frm, row, label, fr_label):
        self.frm = frm
        self.frame = tkinter.Frame(frm, width=1300, height=4, background="#aaaCCCaaa", )
        self.frame.grid(column=0, row=row, columnspan=9, sticky="W")
        self.label = GuiLabel(root_gui, frm, column=1, row=row, bold=True, col_span=3, width="",
                              text=label, fr_text=fr_label)
        self.root_gui = root_gui
        self.root_gui.record_widget(self)

    def set_language(self, _lang):
        pass

    def suicide(self):
        self.root_gui.remove_widget(self)
        self.root_gui.remove_widget(self.label)


class GuiSeparator:
    def __init__(self, root_gui, frm, row, text, fr_text, width=1300):
        self.frm = frm
        self.frame = tkinter.Frame(self.frm, width=width, height=10, background=PwpGui.LIGHT_BLUE)
        self.frame.grid(column=0, row=row, columnspan=9, sticky="W")  # noqa
        self.label = GuiLabel(root_gui, frm, column=0, row=row, background=PwpGui.LIGHT_BLUE,
                              text=text, fr_text=fr_text, bold=True, col_span=5, width="")

    def set(self, text, fr_text):
        self.label.set(text, fr_text)


class GuiLevelButton(GuiButton):
    def __init__(self, root_gui, frm, row, command, label, fr_label, value: str,
                 column=0,
                 text_on='[-]', text_off='[+]', width=3):

        super().__init__(root_gui, frm, column=column, row=row, text=text_on, fr_text=text_on,
                         command=lambda: command(self.value),
                         background="green", width=width)
        self.frame = tkinter.Frame(frm, width=900, height=10, background="#aaaCCCaaa",)
        self.frame.grid(column=0, row=row, columnspan=8, sticky="W")
        self.frame.lower(self)
        self.label = GuiLabel(root_gui, frm, column=1, row=row, text=label, fr_text=fr_label,
                              bold=True, col_span=3, width="")
        self.value = value
        self.command = command
        self.text_on = text_on
        self.text_off = text_off
        self.column = column

    def refresh(self, level: str):
        if level == self.value:
            self["text"] = self.text_on
        else:
            self["text"] = self.text_off

    def show(self, row):
        self.grid(column=self.column, row=row, sticky="W")
        self.frame.grid(column=0, row=row, columnspan=8, sticky="W")
        self.frame.lower(self)
        self.label.show(row)

    def hide(self):
        self.grid_forget()
        self.label.hide()


class GuiFrame(ttk.Frame):
    def __init__(self, frm, row, column=0, width=100, height=100, columnspan=9, column_sizes=None):     # noqa
        super().__init__(frm, width=width, height=height)
        super().grid(column=column, row=row, columnspan=columnspan, sticky="W")
        self.row = row
        column_sizes = column_sizes or []
        for i in range(0, len(column_sizes)):
            self.columnconfigure(i, minsize=PwpGui.font_pixels * column_sizes[i])


class GuiScrollable(ttk.Frame):
    canvases = []

    def __init__(self, root_gui: PwpGui, frm, row, height=400, width=1400, column_sizes=None, name=""):
        super().__init__(frm)
        super().grid(column=0, row=row, columnspan=9, sticky="W")
        self.root_gui = root_gui
        self.name = name
        self.levels = []
        self.all_lines = {}  # all_lines[name] = item
        self.variable = tkinter.StringVar()
        self.variable.set(str(0))
        self.row = row

        self.canvas = tkinter.Canvas(self, width=width, height=height)
        GuiScrollable.canvases.append(self.canvas)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.frm = ttk.Frame(self.canvas)
        self.frm.grid(column=0, row=row, columnspan=9, sticky="W")

        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)
        self.canvas.bind_all("<Button-4>", self.on_mouse_wheel)
        self.canvas.bind_all("<Button-5>", self.on_mouse_wheel)
        self.column_sizes(column_sizes if column_sizes else [])

        self.canvas.create_window((0, 0), window=self.frm, anchor="nw")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def suicide(self):
        pass
        for level in self.levels:
            level.suicide()
            del level
        for name in self.all_lines:
            self.all_lines[name].suicide()
        del self.all_lines
        if self.canvas in GuiScrollable.canvases:
            GuiScrollable.canvases.remove(self.canvas)
        self.destroy()

    def column_sizes(self, sizes):
        for i in range(0, len(sizes)):
            self.frm.columnconfigure(i, minsize=PwpGui.font_pixels * sizes[i])

    @staticmethod
    def on_mouse_wheel(event):
        # O ---> x
        # |
        # v
        # Y
        if GuiScrollable.canvases is not None:
            for canvas in reversed(GuiScrollable.canvases):
                root_x = canvas.winfo_rootx()
                root_y = canvas.winfo_rooty()
                height = canvas.winfo_height()
                width = canvas.winfo_width()
                if (root_x <= event.x_root <= root_x + width) and (root_y <= event.y_root <= root_y + height):
                    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
                    return
        # else, out of my window, do nothing

    def add_level(self, row, label, fr_label):
        level = GuiLevelSeparator(self.root_gui, self.frm, row=row, label=label, fr_label=fr_label)
        self.levels.append(level)

    def add_item(self, item, name):
        if name is not None:
            self.all_lines[name] = item


# class GuiMultiLevels(tkinter.Frame):
#     def __init__(self, root, frm, row, column_sizes):
#         super().__init__(frm)
#         self.root = root
#         self.frm = self
#         self.levels = []
#         self.lines = {}                 # lines[cur_level][name] = item
#         self.all_lines = {}             # all_lines[name] = item
#         self.variable = tkinter.StringVar()
#         self.variable.set(str(0))
#         self.row = row
#         super().grid(column=0, row=row, columnspan=9, sticky="W")   # noqa
#         self.column_sizes(column_sizes)
#
#     def suicide(self):
#         for level in self.levels:
#             self.root.remove_widget(level)
#             del level
#         self.destroy()
#
#     def column_sizes(self, sizes):
#         for i in range(0, len(sizes)):
#             self.frm.columnconfigure(i, minsize=PwpGui.font_pixels * sizes[i])
#
#     def add_level(self, row, label, fr_label):
#         cur_level = str(len(self.levels))
#         new_level = GuiLevelButton(self.root, self.frm, row=row, command=self.refresh,
#                                    label=label, fr_label=fr_label,
#                                    value=cur_level)
#         self.levels.append(new_level)
#         self.lines[cur_level] = {}
#
#     def add_item(self, item, name):
#         cur_level = str(len(self.levels)-1)
#         if len(self.levels) > 0:
#             self.lines[cur_level][name] = item
#             self.all_lines[name] = item
#
#     def refresh(self, level_number: str = "0"):
#         row = self.row
#         for i in range(0, len(self.levels)):
#             cur_level = str(i)
#             self.levels[i].refresh(level_number)
#             self.levels[i].show(row=row)
#             row += 1
#             for _k, item in self.lines[cur_level].current_constraints():
#                 if cur_level == level_number:
#                     item.show(row=row)
#                     row += 1
#                 else:
#                     item.hide()
#

class GuiExpandable(ttk.Label):
    info_window = None
    width = 15

    def __init__(self, frm, column, row, name, text):
        super().__init__(frm, text="ESSAI",
                         background="green",
                         foreground="white",
                         anchor="w", padding=2, width=GuiExpandable.width)
        self.name = name
        self.actual_text = None
        self.mini = None
        self.set(text)
        self.grid(column=column, row=row, sticky="W")
        self.bind("<Button-1>", self.show_info)
        self.bind("<ButtonRelease-1>", self.hide_info)
        self.column = column

        if GuiExpandable.info_window is None:
            GuiExpandable.info_window = GuiInfo()

    def show(self, row):
        self.grid(column=self.column, row=row, sticky="W")

    def hide(self):
        self.grid_forget()

    def show_info(self, event):
        GuiExpandable.info_window.show(self.name, self.actual_text, event.x_root, event.y_root)

    @staticmethod
    def hide_info(_event):
        GuiExpandable.info_window.hide()

    def set(self, text):
        self.actual_text = text
        self.mini = text[-GuiExpandable.width:]
        self['text'] = self.mini

    def get(self):
        return self.actual_text


class GuiValue:
    def __init__(self, root_gui: PwpGui, frm, row: int,
                 dico: dict, fr_dico: dict,
                 column: int = 0, columnspan=1,     # noqa
                 width: int = PwpGui.VALUE_WIDTH):

        self.root_gui = root_gui
        root_gui.record_widget(self)
        self.internal = tkinter.StringVar()
        self.dico = dico
        self.fr_dico = fr_dico
        self.value = None
        self.internal.set("???")
        self.entry = tkinter.Entry(frm, width=width,
                                   textvariable=self.internal, state=tkinter.DISABLED,
                                   )
        self.entry.grid(column=column, row=row, sticky="W", columnspan=columnspan)

    def get(self):
        return self.value

    def set(self, val):
        self.value = val
        translated = "???"
        if val in self.dico:
            translated = self.dico[val] if self.root_gui.language == "en" else self.fr_dico[val]
        self.internal.set(translated)

    def set_language(self, lang):
        val = self.value
        translated = "???"
        if val in self.dico:
            translated = self.dico[val] if lang == "en" else self.fr_dico[val]
        self.internal.set(translated)


class GuiRadios:
    def __init__(self, root_gui: PwpGui, frm, name: str or None, fr_name: str or None,
                 row: int, dico: dict, fr_dico: dict,
                 variable, command, column: int = 0, width: int = 10):
        # dico and fr_dico are dict[value] = displayed text

        if name is not None:
            self.label = GuiLabel(root_gui=root_gui, frm=frm, text=name, fr_text=fr_name,
                                  column=column, row=row, bold=True, width=width,)
            column += 1

        self.dico = dico
        self.fr_dico = fr_dico
        self.radios = {}

        root_gui.record_widget(self)
        for val, text in fr_dico.items():
            rad = ttk.Radiobutton(frm, value=val, text=text if root_gui.language == "fr" else dico[val],
                                  command=command,
                                  # width=PwpGui.RADIO_WIDTH,
                                  variable=variable)
            rad.grid(column=column, row=row, sticky="W")
            self.radios[val] = rad
            column += 1

    def get_xy(self):
        for val in self.radios:
            return self.radios[val].winfo_rootx(), self.radios[val].winfo_rooty()

    def set_language(self, lang):
        for val in self.radios:
            rad = self.radios[val]
            rad['text'] = self.fr_dico[val] if lang == "fr" else self.dico[val]

    def disable(self):
        for val in self.radios:
            self.radios[val]["state"] = 'disabled'

    def enable(self):
        for val in self.radios:
            self.radios[val]["state"] = 'normal'
