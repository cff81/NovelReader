import tkinter as tk


def setting_page(settings):
    root = tk.Tk()
    root.title("设置")
    width = 500
    height = 450
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size_geo)
    root["background"] = "#B9B9B9"
    root.resizable(False, False)

    Font = (str(settings.font), 15, 'bold')

    frame = tk.Frame(root, background="#B9B9B9")
    frame.grid(row=0, column=0)

    setting1 = tk.Label(frame, text="Per Page", bg="#C9C9C9", fg="black", font=Font)
    setting1.grid(row=0, column=0, padx=40, pady=10)
    setting2 = tk.Label(frame, text="Automatic Flip", bg="#C9C9C9", fg="black", font=Font)
    setting2.grid(row=1, column=0, padx=40, pady=10)
    setting3 = tk.Label(frame, text="Column", bg="#C9C9C9", fg="black", font=Font)
    setting3.grid(row=2, column=0, padx=40, pady=10)
    setting4 = tk.Label(frame, text="Color", bg="#C9C9C9", fg="black", font=Font)
    setting4.grid(row=3, column=0, padx=40, pady=10)
    setting5 = tk.Label(frame, text="Font Size", bg="#C9C9C9", fg="black", font=Font)
    setting5.grid(row=4, column=0, padx=40, pady=10)
    setting6 = tk.Label(frame, text="Hotkey", bg="#C9C9C9", fg="black", font=Font)
    setting6.grid(row=5, column=0, padx=40, pady=10)
    setting7 = tk.Label(frame, text="Font", bg="#C9C9C9", fg="black", font=Font)
    setting7.grid(row=6, column=0, padx=40, pady=10)

    set1 = tk.Spinbox(frame, from_=20, to=80, increment=2, font=Font, justify='center')
    set1.grid(row=0, column=1)
    set1.delete(0, tk.END)
    set1.insert(0, str(settings.perPage))
    set2 = tk.Spinbox(frame, from_=2, to=10, increment=1, font=Font, justify='center')
    set2.grid(row=1, column=1)
    set2.delete(0, tk.END)
    set2.insert(0, str(settings.automaticFlip))
    set3 = tk.Spinbox(frame, from_=1, to=3, increment=1, font=Font, justify='center')
    set3.grid(row=2, column=1)
    set3.delete(0, tk.END)
    set3.insert(0, str(settings.column))
    set4 = tk.Entry(frame, font=Font, justify='center')
    set4.grid(row=3, column=1)
    set4.delete(0, tk.END)
    set4.insert(0, str(settings.color))
    set5 = tk.Spinbox(frame, from_=10, to=24, increment=2, font=Font, justify='center')
    set5.grid(row=4, column=1)
    set5.delete(0, tk.END)
    set5.insert(0, str(settings.fontSize))

    frame6 = tk.Frame(frame)
    frame6.grid(row=5, column=1)
    hotkey_list = ["ctrl", "alt"]
    var6 = tk.StringVar(frame6)
    if settings.hotkey in hotkey_list:
        index = hotkey_list.index(settings.hotkey)
        var6.set(hotkey_list[index])
    else:
        raise ValueError("设置热键出错")
    set6 = tk.OptionMenu(frame6, var6, *hotkey_list)
    set6.pack()

    frame7 = tk.Frame(frame)
    frame7.grid(row=6, column=1)
    font_list = ["楷体", "黑体", "宋体", "微软雅黑"]
    var7 = tk.StringVar(frame7)
    if settings.font in font_list:
        index = font_list.index(settings.font)
        var7.set(font_list[index])
    else:
        raise ValueError("设置字体出错")
    set7 = tk.OptionMenu(frame7, var7, *font_list)
    set7.pack()

    frame2 = tk.Frame(root, background="#B9B9B9")
    frame2.grid(row=1, column=0, pady=30)

    button1 = tk.Button(frame2, text='取消', width=8, height=2, command=root.destroy)
    button1.grid(row=0, column=0, padx=24)

    def reset():
        from settings import Settings
        set1.delete(0, tk.END)
        set1.insert(0, str(Settings.perPage))
        set2.delete(0, tk.END)
        set2.insert(0, str(Settings.automaticFlip))
        set3.delete(0, tk.END)
        set3.insert(0, str(Settings.column))
        set4.delete(0, tk.END)
        set4.insert(0, str(Settings.color))
        set5.delete(0, tk.END)
        set5.insert(0, str(Settings.fontSize))

    button2 = tk.Button(frame2, text='重置', width=8, height=2, command=reset)
    button2.grid(row=0, column=1, padx=24)

    def save():
        settings.perPage = int(set1.get())
        settings.automaticFlip = int(set2.get())
        settings.column = int(set3.get())
        settings.color = set4.get()
        settings.fontSize = int(set5.get())
        settings.hotkey = var6.get()
        settings.font = var7.get()
        settings.save()
        settings.read()
        root.destroy()

    button3 = tk.Button(frame2, text='保存', width=8, height=2, command=save)
    button3.grid(row=0, column=2, padx=24)
    root.mainloop()
