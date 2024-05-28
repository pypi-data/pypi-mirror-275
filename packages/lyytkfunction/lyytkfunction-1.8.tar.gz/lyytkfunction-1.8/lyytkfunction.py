import sys,os
import tkinter as tk
import pystray
import threading
from PIL import Image, ImageTk, ImageFilter
import lyyinit
import keyboard
import webbrowser
import subprocess
import win32api,win32con,win32gui
import json
from datetime import datetime
import lyynircmd

def adjust_volume_based_on_time(night_vol=0.06, daytime_vol=0.4):
    # 获取当前的时间
    now = datetime.now()
    # 判断时间是否早于8点30或者晚于9点
    if now.hour < 8 or (now.hour == 8 and now.minute < 30) or now.hour > 21:
        lyynircmd.set_volume_to(night_vol)
    else:
        lyynircmd.set_volume_to(daytime_vol)

class Win32MessageHandler:
    def __init__(self, main_module):
        self.UWM_STOCK = win32api.RegisterWindowMessage("Stock")
        self.main_module = main_module
        self.hwnd = None
        self.json_msg = {"msgtype": "winmsg", "time": str(datetime.now())[:19], "chinesename": "win32广播", "message": ""}
        # "msgtype": "showsys", "time": str(datetime.now())[:19], "chinesename": "监管监控", "message": result_string}

    def create_window(self):
        # 注册窗口类
        self.register_window_class("MyWndClass")

        # 创建窗口
        self.hwnd = win32gui.CreateWindowEx(0, "MyWndClass", "接收方窗口", win32con.WS_OVERLAPPEDWINDOW, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, 0, 0, win32api.GetModuleHandle(None), None)  # 扩展窗口样式  # 窗口类名  # 窗口标题  # 窗口样式  # 窗口位置  # 窗口大小  # 父窗口句柄  # 菜单句柄  # 实例句柄  # 创建参数

        # 隐藏窗口
        win32gui.ShowWindow(self.hwnd, win32con.SW_HIDE)

    def register_window_class(self, class_name):
        # 注册窗口类
        wc = win32gui.WNDCLASS()
        wc.lpfnWndProc = self.wnd_proc
        wc.lpszClassName = class_name
        win32gui.RegisterClass(wc)

    def wnd_proc(self, hwnd, msg, wparam, lparam):
        if msg == self.UWM_STOCK:
            # 处理接收到的消息
            target_code = wparam
            print("接收到消息：", target_code)
            # 在这里进行您的处理逻辑
            self.json_msg["message"] = str(target_code)
            self.main_module.ins_function.process_recieved_msg(json.dumps(self.json_msg), self.main_module)
        # 调用默认的窗口过程函数来处理其他消息
        return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)


class gui_ico_class:
    def __init__(self, main_module, icon_path) -> None:
        self.main_module = main_module
        self.icon_path = icon_path
        self.icon = None
        self.init_tray_icon()

    def init_tray_icon(self):
        # 创建托盘图标菜单
        menu = (
            pystray.MenuItem("显示", self.show_window, default=True),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("关于", self.about),
            pystray.MenuItem("退出程序", action=self.exit_program)
        )
        # 打开图标图像
        image = Image.open(self.icon_path)
        # 创建托盘图标实例
        self.icon = pystray.Icon("name", image, "应无所住而生其心", menu)

    def start_tray_icon(self,lyywin=None):
        # 在主线程中启动托盘图标
        if self.icon:
            self.icon.run()

    def about(self):
        tk.messagebox.showinfo("关于", "逆袭起点 超出你的期待")

    def exit_program(self):
        # 退出程序的逻辑
        self.icon.stop()
        self.main_module.root.quit()
        

    def show_window(self):
        # 显示主窗口的逻辑
        self.main_module.root.deiconify()


class funs_class:
    def __init__(self, main_module) -> None:
        self.main_module = main_module
        self.check_and_restore_window()
    
    def process_recieved_msg(self,data=None):
        print("enter lyytkfunction.py funs_class, process_recieved_msg")
       
    def scroll_location_from_textbox(self,text_widget):
        """计算用来放置滚动条的位置信息"""
        text_place_info = text_widget.place_info()
        scrollbar_place_info = {"relx": float(text_place_info["relx"]) + float(text_place_info["relwidth"]) - 0.02, "rely": float(text_place_info["rely"]), "relwidth": 0.02, "relheight": text_place_info["relheight"]}  # 滚动条放置在文本框的右侧  # 假设滚动条宽度为父容器宽度的10%
        # 使用更新后的布局信息放置滚动条
        return(scrollbar_place_info)
    
    
    def is_mouse_inside(self,debug=False):
        # 获取鼠标的当前位置
        mouse_x = self.main_module.root.winfo_pointerx()
        mouse_y = self.main_module.root.winfo_pointery()

        # 获取窗体的位置和尺寸
        window_x = self.main_module.root.winfo_x()
        window_y = self.main_module.root.winfo_y()
        window_width = self.main_module.root.winfo_width()
        window_height = self.main_module.root.winfo_height()

        # 判断鼠标是否位于窗体范围内
        if (window_x <= mouse_x <= window_x + window_width) and (window_y <= mouse_y <= window_y + window_height):
            if debug: print("鼠标在窗体内",end="")
            return True
        else:
            if debug: print("鼠标不在窗体内",end="")
            return False

    
    def on_close(self,win):
        print("in gui fun, in on_close","win=",win)
        print("in on_close","self.main_module.win_sub_dict=",self.main_module.win_sub_dict)
        if win in self.main_module.win_sub_dict.values():
            key_to_delete = None
            for key, value in self.main_module.win_sub_dict.items():
                if value == win:
                    key_to_delete = key
                    break
            if key_to_delete is not None:
                del self.main_module.win_sub_dict[key_to_delete]
        win.destroy()
        
    def on_minimize(self,win):
        print("in gui fun, on_minimize","win=",win)
        print("in on_minimize","self.main_module.win_sub_dict=",self.main_module.win_sub_dict)
        if win in self.main_module.win_sub_dict.values():
            key_to_delete = None
            for key, value in self.main_module.win_sub_dict.items():
                if value == win:
                    key_to_delete = key
                    break
            if key_to_delete is not None:
                del self.main_module.win_sub_dict[key_to_delete]
        win.iconify()
        
    def on_restore(self,win):
        print("in gui fun, on_restore","win=",win)
        win.deiconify()
        self.main_module.win_sub_dict[len(self.main_module.win_sub_dict)] = win
        
        
    def sort_windows_by_x_coordinate(self,windows):
        sorted_windows = sorted(windows, key=lambda w: w.winfo_x())
        return sorted_windows

    def layout_windows(self,windows):
        print("in gui fun, layout_windows, windows:", windows,len(windows))
        for i, window in enumerate(windows):
            if i == 0:
                root_x = self.main_module.root.winfo_rootx()
                root_y = self.main_module.root.winfo_rooty()
                window.geometry(f"+{root_x - window.winfo_width()}+{root_y}")  # 吸附在主窗口右侧
            else:
                prev_window = windows[i-1]
                x = prev_window.winfo_x() + prev_window.winfo_width()   # 吸附在前一个窗体的右侧
                y = prev_window.winfo_y()
                window.geometry(f"+{x}+{y}")
                
    def children_win_follow_root(self, event):
        print("enter children_win_follow_root")
        #遍历win_sub_dict，获取value的值，这是Toplevel窗体，获取这些窗体位置，获取其X坐标的位置，把这几个窗体按照X坐标的位置进行排序，
        # 然后按照X坐标最小的放置在main_module.root的左边，其它的依次排列在main_module.root的右边这样就实现了子Toplevel窗体的旁边吸附，依此类推
        if len(self.main_module.win_sub_dict) == 0:
            return
        # 获取主窗口的中心点
        windows_list = list(self.main_module.win_sub_dict.values())
        # 按 X 坐标位置排序
        sorted_windows = self.sort_windows_by_x_coordinate(windows_list)
        # 布局窗体
        self.layout_windows(sorted_windows)


            
        # 跟随主窗口移动
        #self.main_module.root.geometry("+{0}+{1}".format(event.x_root, event.y_root))
    
    def check_and_restore_window(self):
        # 检查和恢复窗口的状态
        if lyyinit.is_busy_time() and (self.main_module.root.state() == "iconic" or not self.main_module.root.winfo_viewable()):
            self.main_module.root.deiconify()
        self.main_module.root.after(300000, self.check_and_restore_window)  # 继续调度函数

    # 使用该函数来获取所有文本框和文本控件
    def get_text_widgets(self, parent):
        text_widgets = []
        for widget in parent.winfo_children():
            if isinstance(widget, tk.Text) or isinstance(widget, tk.Entry):
                text_widgets.append(widget)
            else:
                text_widgets.extend(self.main_module.get_text_widgets(widget))
        return text_widgets

    def bring_window_to_top(self, event):
        window = event.widget.winfo_toplevel()
        window.attributes("-topmost", True)
        window.focus_force()

    def lyy恢复(self):
        self.main_module.root.deiconify()



    def paste(self):
        self.main_module.event_generate("<<Paste>>")

    def copy(self):
        self.main_module.event_generate("<<Copy>>")

    def cut(self):
        self.main_module.event_generate("<<Cut>>")

    def delete(self):
        self.main_module.event_generate("<Delete>")

    def select_all(self):
        self.main_module.tag_add("sel", "1.0", "end")

    def rightKey(self, event, editor):
        self.main_module.menubar.delete(0, "end")
        self.main_module.menubar.add_command(label="剪切", command=lambda: self.main_module.cut(editor))
        self.main_module.menubar.add_command(label="复制", command=lambda: self.main_module.copy(editor))
        self.main_module.menubar.add_command(label="粘贴", command=lambda: self.main_module.paste(editor))
        self.main_module.menubar.post(event.x_root, event.y_root)

    def notepad_view(self, event):
        answer = tk.messagebox.askokcancel(title="确定或取消", message="确定吗")
        if answer:
            self.main_module.win.state("zoomed")

        # ScrolledText.bind("<Control-z>", self.main_module.undo)
        # ScrolledText.bind("<Control-Z>", self.main_module.undo)
        # ScrolledText.bind("<Control-y>", self.main_module.redo)
        # ScrolledText.bind("<Control-Y>", self.main_module.redo)


    def restartMyself(self):
        pyt = sys.executable
        os.execl(pyt, pyt, *sys.argv)
        #icon.stop()
        
        
    def exit_program(self):
        # self.main_module.save_to_last_msg()
        global global_keep_running_flag
        global_keep_running_flag = False
        
        self.main_module.stop_event.set()
        self.main_module.root.quit()
        self.main_module.ins_ico.icon.stop()
        self.main_module.root.destroy()
        sys.exit()

    def download(self):
        thread = threading.Thread(target=self.download_sub)
        thread.daemon = True
        thread.start()

    def undo(self, event):
        event.edit_undo("<<Undo>>")

    def redo(self, event):
        event.edit_redo("<<Redo>>")

    def save_current_state(self):
        self.undo_stack.append(self.text_widget.get("1.0", "end-1c"))

    def undo(self, event):
        if self.undo_stack:
            current_state = self.text_box_kernel.get("1.0", "end-1c")
            self.redo_stack.append(current_state)
            prev_state = self.undo_stack.pop()
            self.main_module.text_box_kernel.delete("1.0", END)
            self.main_module.text_box_kernel.insert("1.0", prev_state)

    def redo(self, event):
        if self.redo_stack:
            current_state = self.text_box_kernel.get("1.0", "end-1c")
            self.undo_stack.append(current_state)
            next_state = self.redo_stack.pop()
            self.main_module.text_box_kernel.delete("1.0", END)
            self.main_module.text_box_kernel.insert("1.0", next_state)

    def set_statusbar_dynamic_history(self, text):
        self.main_module.状态栏文本变量1.set(text)

    def set_statusbar2(self, text):
        self.main_module.状态栏文本变量2.set(text)

    def set_statusbar3(self, text):
        self.main_module.状态栏文本变量3.set(text)

    def on_enter_link(self, event):
        # 改变链接的样式为蓝色斜体
        self.main_module.text_box_kernel.tag_configure("link", foreground="blue", underline=True, font=("Arial", 13, "italic"))

    def on_leave_link(self, event):
        # 改变链接的样式为蓝色正常
        self.main_module.text_box_kernel.tag_configure("link", foreground="blue", underline=True, font=("Arial", 13, "normal"))

    def open_link(self, event):
        print("open_link调用，将用默认浏览器打开链接")
        # 获取点击的位置
        index = self.main_module.text_box_kernel.index("@%d,%d" % (event.x, event.y))

        # 获取链接的开始和结束位置
        start, end = self.main_module.text_box_kernel.tag_prevrange("link", index)

        # 获取链接的文本
        url = self.main_module.text_box_kernel.get(start, end)
        # 使用默认浏览器打开链接
        webbrowser.open(url)

    def clear(self):
        self.main_module.text_box_kernel.tag_remove("search", "1.0", tk.END)


    def help_help(self, event=None):

        print("help_help")
        messagebox.showinfo("hello", "world")
        pass

    def modify_schedule(self, event=None):
        self.main_module.状态栏文本变量1.set("编辑计划任务")
        # res=os.system("c:\\windows\\system32\\notepad.exe jd_config.ini")
        res = subprocess.Popen("c:\\windows\\system32\\notepad.exe " +  "jd_config.ini")

if __name__ == "__main__":    
    show_msg_once()
    #show_toast()