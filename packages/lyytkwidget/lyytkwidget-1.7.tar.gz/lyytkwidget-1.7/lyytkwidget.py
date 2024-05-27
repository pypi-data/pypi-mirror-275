import os, sys
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter.scrolledtext import ScrolledText

import lyyapp
import lyyprocess

import subprocess
import json
import configparser

cf = configparser.ConfigParser()
cf.read("gui_config", encoding="utf-8")

config_file = r"D:\\UserData\\resource\\gui\\subscribe_teacher.json"


class root_widget_class:
    def __init__(self, main_module) -> None:
        """小部件，先建notebook，再建分组，再建文本框等控件"""
        self.main_module = main_module
        self.var_enable_speak = tk.BooleanVar()
        self.available_themes = self.main_module.root.style.theme_names()  # 获取可用主题列表
        self.font_name = self.main_module.all_config_dict.get("info_config").get("INFO").get("font_name")
        self.font_size = self.main_module.all_config_dict.get("info_config").get("INFO").get("font_size")
        
        # 菜单中开启朗读相关值获取
        self.var_enable_speak.set(self.main_module.enable_speak)
        self.main_module.teacher_value_dict= self.main_module.all_config_dict.get("subscribe_teacher")
        #print("teacher_value_dict=", self.main_module.teacher_value_dict)# {'大师兄擒妖': True, 'f1024': True, '这股有毒': True, '青岛': True, '平凡之路': True, '小锦鲤': True}

        self.textbot_list = []
        # 首先添加notebook，以便后续的控件添加到notebook中
        self.add_notebook()
        self.add_controls_to_frame1()
        self.create_teacher_checkboxes()


    def update_teacher_value_dict_and_textbox(self, teacher, var):
        """
        更新教师订阅状态
        """
        with self.main_module.teacher_lock:
            self.main_module.teacher_value_dict[teacher] = var.get()
        self.write_teacher_value_dict()
        self.main_module.last_id_queue.put(0)
        print("更新教师订阅状态", teacher, var.get())

    def write_teacher_value_dict(self):
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(self.main_module.teacher_value_dict, f, ensure_ascii=False, indent=2)

    def create_teacher_checkboxes(self,teachers=None):
        self.main_module.teacher_vars = []
        # teachers = f1999cfg.info_cfg.subscribe_teachers.split(",")
        teachers = self.main_module.teacher_value_dict.keys() if teachers==None else teachers
        # 创建滚动条
        scrollbar = ttk.Scrollbar(self.group_frame_teacher)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 创建 Canvas
        self.canvas = tk.Canvas(self.group_frame_teacher, yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 设置滚动条与 Canvas 的关联
        scrollbar.config(command=self.canvas.yview)

        # 创建 Frame 作为 Canvas 的子控件
        frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=frame, anchor=tk.NW)

        # 创建一个包含3个控件的Frame
        row_frame = None
        for i, teacher in enumerate(teachers):
            if i % 5 == 0:
                row_frame = ttk.Frame(frame)
                row_frame.pack(side=tk.TOP, fill=tk.X)

            var = tk.BooleanVar(value=self.main_module.teacher_value_dict.get(teacher, False))
            teacher = teacher.strip("'")
            # cb = tk.Checkbutton(row_frame, text=teacher, variable=var)
            cb = tk.Checkbutton(row_frame, text=teacher, variable=var, command=lambda teacher=teacher, var=var: self.update_teacher_value_dict_and_textbox(teacher, var))
            cb.pack(side=tk.LEFT, padx=1, pady=1)
            self.main_module.teacher_vars.append(var)
            # 创建右键菜单
        self.popup_menu = tk.Menu(self.group_frame_teacher, tearoff=0)
        self.popup_menu.add_command(label="全部选中", command=self.select_all)
        self.popup_menu.add_command(label="全部取消选择", command=self.deselect_all)
        self.popup_menu.add_command(label="反选", command=self.toggle_selection)

        # 配置 Canvas 的滚动区域
        frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

        # 绑定鼠标滚轮滚动事件到 Canvas 上
        self.canvas.bind("<Enter>", self.bind_mousewheel)
        self.canvas.bind("<Leave>", self.unbind_mousewheel)
        self.group_frame_teacher.bind("<Button-3>", self.show_popup_menu)
        self.bind_to_children(self.group_frame_teacher, "<Button-3>", self.show_popup_menu)

    def add_notebook(self):
        print("add_notebook")
        self.main_module.notebook = ttk.Notebook(self.main_module.root)
        # notebook的第一个选项卡
        self.main_module.frame0_kernel = ttk.Frame(self.main_module.notebook)
        self.main_module.notebook.add(self.main_module.frame0_kernel, text="核心主线")
        self.group_kernel_teachers = ttk.LabelFrame(self.main_module.frame0_kernel, text="核心老师")
        self.group_kernel_teachers.place(relx=0, rely=0, relheight=0.16, relwidth=1)
        self.group_kernel_msg = ttk.LabelFrame(self.main_module.frame0_kernel, text="核心信息")
        self.group_kernel_msg.place(relx=0, rely=0.18, relheight=0.8, relwidth=1)
        self.main_module.textbox_kernel = ScrolledText(self.group_kernel_msg, undo=True, font=(self.font_name, self.font_size), max=-1)
        self.main_module.textbox_kernel.place(x=0, y=0, relwidth=0.98, relheight=0.89)
        
        #print("textbox_kernel loaded",self.main_module.textbox_kernel)
        # 使用分组框架，将控件分组
        self.main_module.frame1_信息订阅 = ttk.Frame(self.main_module.notebook)
        self.main_module.notebook.add(self.main_module.frame1_信息订阅, text="信息订阅")
        self.group_frame_teacher = ttk.LabelFrame(self.main_module.frame1_信息订阅, text="大V选择")
        # self.main_module.notebook.add(self.group_frame_teacher, text="教师分组")
        self.group_frame_teacher.place(relx=0, rely=0, relheight=0.16, relwidth=1)
        self.group_frame_message = ttk.LabelFrame(self.main_module.frame1_信息订阅, text="信息订阅")
        # self.main_module.notebook.add(self.another_frame, text="另一个分组")
        self.group_frame_message.place(relx=0, rely=0.18, relheight=0.8, relwidth=1)
        # 消息框加入到分组框中



        self.main_module.textbox_other = ScrolledText(self.group_frame_message, undo=True, font=(self.font_name, self.font_size), max=-1)
        self.main_module.textbox_other.place(x=0, y=0, relwidth=0.98, relheight=0.89)
        # 创建一个 Scrollbar 小部件，并设置其控制 Text 小部件的滚动
        scrollbar_main_text = ttk.Scrollbar(self.group_frame_message, orient="vertical", command=self.main_module.textbox_other.yview)
        scrollbar_main_text.place(**self.main_module.ins_function.scroll_location_from_textbox(self.main_module.textbox_other))
        # 配置 Text 小部件的 yscrollcommand 为 Scrollbar 的 set 方法
        self.main_module.textbox_other.config(yscrollcommand=scrollbar_main_text.set)
        # notebook的第二个选项卡
        self.main_module.frame2_keyword = ttk.Frame(self.main_module.notebook)
        self.main_module.notebook.add(self.main_module.frame2_keyword, text="关键词消息")
        
        
        self.main_module.textbox_keyword  = tk.Text(self.main_module.frame2_keyword, undo=True)
        self.main_module.textbox_keyword.config(font=self.main_module.红色雅黑, fg="red")
        self.main_module.textbox_keyword.place(relx=0, rely=0.02, relwidth=0.98, relheight=0.9)

        scrollbar2 = ttk.Scrollbar(self.main_module.frame2_keyword, orient="vertical", command=self.main_module.textbox_keyword.yview)
        # 计算滚动条的放置位置和大小
        # 获取文本框的布局信息 使用更新后的布局信息放置滚动条
        scrollbar2.place(**self.main_module.ins_function.scroll_location_from_textbox(self.main_module.textbox_keyword))
        # 配置文本框使用滚动条
        self.main_module.textbox_keyword.config(yscrollcommand=scrollbar2.set)
        scrollbar2.config(command=self.main_module.textbox_keyword.yview)



        # 第三个选项卡
        self.main_module.frame3_rule = ttk.Frame(self.main_module.notebook)
        self.main_module.notebook.add(self.main_module.frame3_rule, text="操盘规则")

        
        self.main_module.textbox_rule  = tk.Text(self.main_module.frame3_rule, undo=True)
        self.main_module.textbox_rule.config(font=self.main_module.红色雅黑, fg="red")
        self.main_module.textbox_rule.place(relx=0, rely=0.1, relwidth=0.98, relheight=0.8)
        bt = tk.Button(self.main_module.frame3_rule, text="保存提醒", command=self.main_module.ins_widget_fun.save_notice)
        bt.place(relx=0.42, rely=0.04, relwidth=0.15, height=24)



        scrollbar_textbox_rule = ttk.Scrollbar(self.main_module.frame3_rule, orient="vertical", command=self.main_module.textbox_rule.yview)
        # 计算滚动条的放置位置和大小
        # 获取文本框的布局信息 使用更新后的布局信息放置滚动条
        scrollbar_textbox_rule.place(**self.main_module.ins_function.scroll_location_from_textbox(self.main_module.textbox_rule))
        # 配置文本框使用滚动条
        self.main_module.textbox_rule.config(yscrollcommand=scrollbar_textbox_rule.set)
        scrollbar_textbox_rule.config(command=self.main_module.textbox_rule.yview) 
        
        

        # 第四个选项卡
        self.main_module.frame4 = ttk.Frame(self.main_module.notebook)
        # self.frame4.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.main_module.notebook.add(self.main_module.frame4, text="信息查询")

        self.textbox_search = ScrolledText(self.main_module.frame4, undo=True)
        self.textbox_search.place(relx=0, rely=0.32, relwidth=1, relheight=0.1)

        self.textbox_search_input = tk.Text(self.main_module.frame4, undo=True)
        self.textbox_search_input.place(relx=0, rely=0.8, relwidth=0.7, relheight=0.1)

        self.main_module.notebook.pack(fill=tk.BOTH, expand=True)

    def 关键字订阅(self):
        if not hasattr(self,"win_subscribe"):
            import lyywinsubscribe
            self.main_module.win_subscribe = lyywinsubscribe.gui_subscribe_class(self.main_module)
        self.main_module.win_subscribe.win_sub()

    def change_theme(self):
        """更改应用程序的主题"""
        self.main_module.style.theme_use(self.selected_theme.get())
        self.main_module.all_config_dict.get("SYSTEM")["theme_name"] = self.selected_theme.get()
        self.main_module.save_config("gui_config")


    def enable_speak(self, event=None):
        enable_speak = bool(self.var_enable_speak.get())  # 将值转换为布尔值
        self.main_module.enable_speak = not self.main_module.enable_speak
        self.var_enable_speak.set(self.main_module.enable_speak)
        print("点击菜单，切换状态后，", self.var_enable_speak.get(),self.main_module.enable_speak)

    def add_controls_to_frame1(self):

        main_menu = tk.Menu(self.main_module.root)
        # 1.1 文件菜单：在顶级菜单实例下创建子菜单实例
        menusb_file = tk.Menu(main_menu, tearoff=False)

        # 1.2 创建文件菜单下的子菜单
        menusb_file.add_command(label="新建")
        menusb_file.add_command(label="打开")
        menusb_file.add_separator()
        #menusb_file.add_command(label="重启", command=lyytkfunction.restartMyself)
        menusb_file.add_command(label="重启程序", command=self.main_module.ins_function.restartMyself)
        menusb_file.add_command(label="退出", command=self.main_module.ins_function.exit_program)

        # 1.3 为顶级菜单实例添加菜单，并级联相应的子菜单实例
        main_menu.add_cascade(label="文件(F)", menu=menusb_file, underline=3)

        # 2.1  工具菜单：在顶级菜单实例下创建子菜单实例
        menusb_tools = tk.Menu(main_menu, tearoff=False)
        # 2.2  创建工具菜单下的子菜单
        menusb_tools.add_command(label="检测通达信服务器", command=self.main_module.ins_function.help_help, accelerator="Ctrl+Alt+T")
        menusb_tools.add_command(label="更新统计排序得分", command=self.main_module.ins_function.help_help, accelerator="F1")
        menusb_tools.add_command(label="测试语音播放", command=lambda: self.main_module.to_speak_queue.put("This is a testing voice"), accelerator="F1")
        print("====================before create menu, self.var_enable_speak=", self.var_enable_speak, self.var_enable_speak.get())
        menusb_tools.add_checkbutton(label="开启语音播放", command=self.enable_speak, variable=self.var_enable_speak, onvalue=True, offvalue=False)
        menusb_tools.add_command(label="关闭显示器", command=lyyapp.关闭显示器, accelerator="Ctrl+Alt+F2")
        main_menu.add_cascade(label="工具(T)", menu=menusb_tools, underline=3)

        # 3.1 视图菜单：在顶级菜单实例下创建子菜单实例
        menusb_view = tk.Menu(main_menu, tearoff=False)
        menusb_view.add_command(label="窗口置顶", command=self.main_module.ins_function.bring_window_to_top, accelerator="F1")
        menusb_view.add_command(label="重启_get_stock_info获取", command=lambda: lyyprocess.restart_program(r"D:\Soft\_lyysoft\get_stock_info","get_stock_info.exe"))
        menusb_view.add_command(label="重启@MyService获取", command=lambda: self.main_module.ins_function.restart_service("@MyService"))
        menusb_view.add_command(label="订阅老师", command=lambda: lyyprocess.open_file_in_new_thread(r"D:\UserData\resource\gui\info_config"), accelerator="F1")

        # 创建一个子菜单来列出所有主题
        themes_menu = tk.Menu(menusb_view, tearoff=False)
        # 创建一个变量来跟踪当前选中的主题
        self.selected_theme = tk.StringVar(value=self.main_module.all_config_dict.get("gui_config").get("SYSTEM").get("theme_name"))
        self.main_module.style.theme_use(self.selected_theme.get())

        # 为每个主题创建一个Radiobutton菜单项
        for theme in self.main_module.style.theme_names():
            themes_menu.add_radiobutton(label=theme, variable=self.selected_theme, value=theme, command=self.change_theme)
        # 将子菜单添加到你的菜单项中
        menusb_view.add_cascade(label="主题选择", menu=themes_menu)

        # 3.2  创建视图菜单下的子菜单
        main_menu.add_cascade(label="视图(V)", menu=menusb_view, underline=3)

        # 4.1 系统设置菜单：在顶级菜单实例下创建子菜单实例
        menusb_system = tk.Menu(main_menu, tearoff=False)
        # 4.2  创建工具菜单下的子菜单
        ifAutoRestart = tk.BooleanVar()
        menusb_system.add_command(label="参数设置", command=lambda: self.main_module.instance_para_setting.打开参数设置窗口(), accelerator="F1")

        menusb_system.add_command(label="配置文件编辑器", command=lambda: subprocess.Popen("cfg_manager.exe") if os.path.isfile("cfg_manager.exe") else print("Error: cfg_manager.exe not found"))
        menusb_system.add_command(label="模块设置", command=self.main_module.ins_function.help_help, accelerator="F1")
        menusb_system.add_command(label="编辑计划任务", command=self.main_module.ins_function.modify_schedule, accelerator="Ctrl+Alt+S")
        menusb_system.add_command(label="关键字订阅", command=self.关键字订阅, accelerator="F1")
        menusb_system.add_command(label="全局调试开关", command=lambda: globals().update({"GLOBAL_DEBUG": not globals().get("GLOBAL_DEBUG", False)}), accelerator="F1")
        menusb_system.add_command(label="颜色名称", command=lambda: os.startfile("color_name.png"), accelerator="F1")
        menusb_system.add_command(label="颜色代码", command=lambda: os.startfile("color_name_code.jpg"), accelerator="F1")
        # 4.3 为顶级菜单实例添加菜单，并级联相应的子菜单实例
        main_menu.add_cascade(label="系统设置(S)", menu=menusb_system, underline=5)

        # 5.1 系统设置菜单：在顶级菜单实例下创建子菜单实例

        # 读取配置文件
        cf_menu = configparser.ConfigParser()
        cf_menu.read("menu.ini", encoding="utf-8")

        # 创建子菜单
        menusb_help = tk.Menu(main_menu, tearoff=False)
        # 添加子菜单项
        for section in cf_menu.sections():
            program_name = cf_menu.get(section, "name")
            cmd = cf_menu.get(section, "command")
            menusb_help.add_command(label=program_name, command=lambda cmd=cmd: os.startfile(cmd))

        # 5.2  创建系统设置菜单下的子菜单
        main_menu.add_cascade(label="三方模块(H)", menu=menusb_help, underline=3)
        menusb_help.add_command(label="帮助说明", command=self.main_module.ins_function.help_help, accelerator="F1")

        menusb_help.add_command(label="关于", command=self.main_module.ins_function.help_help)
        menusb_help.add_separator()
        menusb_help.add_command(label="万一开户", command=self.main_module.ins_function.help_help, accelerator="F1")

        # 显示菜单
        self.main_module.root.config(menu=main_menu)  # =root['menu']=main_menu
        fontStyle = tkFont.Font(family=self.main_module.all_config_dict.get("info_config").get("INFO").get("font_name"), size=20)
        path =  "icon\\block.ico"
        # root["background"] = "#C9C9C9"
        lb = tk.Label(self.main_module.root, text="重要提醒")

        # def show_text_box(self):

        bt = tk.Button(self.main_module.frame1_信息订阅, text="放大看图", command=self.main_module.ins_img.open_last_img)
        bt.place(relx=0.8, rely=0.18, relwidth=0.15, height=24)

        text2Stringvar = tk.StringVar()

        statusbar_dynamic_history = tk.Label(self.main_module.root, text="", textvariable=self.main_module.status_bar_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusbar_dynamic_history.place(x=0, rely=0.91, relwidth=1, relheight=0.05)

        #statusbar_dynamic_history.bind("<Double-1>", self.main_module.ins_function.show_more_text)
        self.main_module.root.bind("<Control-n>", self.main_module.ins_function.help_help)  # 此快捷键成功
        self.main_module.root.bind("<Control-N>", self.main_module.ins_function.help_help)
        self.main_module.root.bind("<Control-j>", self.main_module.ins_function.modify_schedule)
        self.main_module.root.bind("<Control-J>", self.main_module.ins_function.modify_schedule)
        # self.root.bind("<Control-h>", 打开日志文件)
        # self.root.bind("<Control-H>", 打开日志文件)
        self.main_module.root.bind("<Escape>", lambda event: self.main_module.root.attributes("-fullscreen", False))  # Press Esc to exit full screen
        self.main_module.root.bind("<Control-z>", self.main_module.ins_function.undo)
        self.main_module.root.bind("<Control-Z>", self.main_module.ins_function.undo)
        self.main_module.root.bind_all("<Control-Shift-a>", self.main_module.ins_function.help_help)

        for widget in [self.main_module.textbox_kernel,self.main_module.textbox_other,self.main_module.textbox_keyword]:            

            widget.bind("<Control-f>", lambda event: self.main_module.ins_text_box.find(event))  # 绑定 Ctrl+F 到查找功能
            widget.bind("<Control-Shift-f>", lambda event: self.clear(event))  # 绑定 Ctrl+Shift+F 到清除查找结果的功能
            widget.bind("<F3>", lambda event: self.main_module.ins_text_box.find_next(event))  # 绑定 F3 到查找下一处
            
        
    def bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def show_popup_menu(self, event):
        """显示右键菜单"""
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup_menu.grab_release()

    def select_all(self):
        """选中所有复选框"""
        for var in self.main_module.teacher_vars:
            var.set(True)
        # 可能需要更新UI或其他逻辑
        self.write_teacher_value_dict()  # 保存到配置文件


    def deselect_all(self):
        """取消选中所有复选框"""
        for var in self.main_module.teacher_vars:
            var.set(False)
        # 可能需要更新UI或其他逻辑
        self.write_teacher_value_dict()  # 保存到配置文件

    def toggle_selection(self):
        """反选所有复选框"""
        for var in self.main_module.teacher_vars:
            var.set(not var.get())
        # 可能需要更新UI或其他逻辑
        self.write_teacher_value_dict()  # 保存到配置文件

    def bind_to_children(self, parent, event, handler):
        """递归绑定事件到所有子组件"""
        parent.bind(event, handler)
        for child in parent.winfo_children():
            self.bind_to_children(child, event, handler)


class TextEditor:
    def __init__(self, master):
        self.master = master
        self.color = "black"  # 默认字体颜色
        self.size = 12  # 默认字体大小

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Hello, world!", font=(None, self.size))
        self.label.pack()

        # 添加字体颜色选择器
        self.color_button = tk.Button(self.master, text="更改颜色", command=self.change_color)
        self.color_button.pack()

    def change_color(self):
        # 获取新的字体颜色
        new_color = input("请输入新的字体颜色: ")
        self.color = new_color
        # 更新标签的字体颜色
        self.label["foreground"] = self.color

    def set_font_size(self, new_size):
        # 设置新的字体大小
        self.size = new_size
        # 更新标签的字体大小
        self.label["font"] = (None, self.size)

    def __str__(self):
        return f"字体颜色: {self.color}, 字体大小: {self.size}"
