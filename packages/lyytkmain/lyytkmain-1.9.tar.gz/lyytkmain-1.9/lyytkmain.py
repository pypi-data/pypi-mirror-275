# -*- coding: utf-8 -*-
# black: no-wrap
import os,sys,time
from datetime import datetime
import tkinter as tk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import tkinter.font as tkFont

import threading
import queue
import win32gui,win32api,win32con
import json
import pandas as pd
from PIL import Image, ImageTk, ImageFilter
import base64
import io
import lyyinit
from lyylog import log
import lyypymysql
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
            self.process_data(json.dumps(self.json_msg))
        # 调用默认的窗口过程函数来处理其他消息
        return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)
    
    
class  lyytkGUI:
    def __init__(self, data_queue=None,ico_path="",config={}) -> None:
        self.data_queue=data_queue        
        self.all_config_dict = config
        self.gui_config_dict = self.all_config_dict.get("gui_config")
        self.INFO_config_dict = self.all_config_dict.get("info_config").get("INFO")
        self.enable_speak = self.all_config_dict.gui_config.modules.enable_speak
        self.root = ttkb.Window()
        self.style = ttkb.Style()
        self.root.title(self.all_config_dict.get("gui_config").get("SYSTEM").get("title"))
        self.root.protocol("WM_DELETE_WINDOW", self.root.withdraw)  # 把点击x关闭窗口变成不要关闭并最小化到托盘
        self.红色雅黑 = tkFont.Font(family="Microsoft YaHei", size=11, weight="bold")
        self.窗口win启动 = False
        self.root.geometry(lyyinit.get_geometry_dynamic(fulltext=self.all_config_dict.get("gui_config").get("SYSTEM").get("geometry")))
        if not ico_path:
            self.root.iconbitmap( "icon\\main.ico")            
        self.root.resizable(True, True) 
        self.root.wm_attributes("-topmost", 1)
        self.ins_function=None
        self.ins_text_box=None
        self.ins_img=None
        self.ins_ico=None
        self.init_var()
        self.after_check_win32messages_loop()
        self.after_update_gui_from_display_cmd()
        self.ins_lyysql = lyypymysql.mysql_class(password="Yc124164")
        
    # Tkinter GUI更新函数
    def after_update_gui_from_display_cmd(self):
        
        """
        接收 (fastapi服务器放入data_queue队列中、需要查询涨停原因的) 的股票代码，弹出涨停原因窗口显示。
        """
        try:
            data = self.data_queue.get_nowait()  #data_dict = {'code': '000001', 'cmd': 'reason'}
            #data_dict = {"time":msg_time,"chinesename":chinesename,"message":msg_content,"cmd":"showmsg","msgtype":msg_type,"widget":widget}

            if isinstance(data,list):
                for data_dict in data:  
                    self.display_all_msg(data_dict)
                    
            else:
                self.display_all_msg(data)
                
                
        except queue.Empty:
            #print("~", end="")
            pass
        # except Exception as e:
        #     print("error in update_gui_from_data_queue", e)
        finally:
        # 每隔100毫秒检查一次队列
            self.root.after(200, self.after_update_gui_from_display_cmd)
    def set_status_bar(self, text,key=":"):
        with self.status_bar_var_lock:
            self.status_bar_dict[key]= text.ljust(20) if key ==":" else text
            self.status_bar_var.set(json.dumps(self.status_bar_dict,ensure_ascii=False).replace("{","").replace("}","").replace('"','').replace(",","  ").replace("\n",""))
        self.root.update_idletasks()
    def on_closing(self):
        self.root.iconify()

    def decode_base64_image(self,image_base64_str):
        print("# 解码Base64编码的图片数据")
        image_data = base64.b64decode(image_base64_str)
        print("img_data=",type(image_data))
        image = Image.frombytes('RGB', (1, 1), image_data)  # 修改这里的图像尺寸和模式

        return image

    def display_img(self,widget,img_key):
        print("I",end="")
        try:
            mytkimg = self.images_dict.get(img_key)
            self.image_list_to_keep.append(mytkimg)
            widget.image_create(tk.END, image=mytkimg)
            widget.insert(tk.END, "\n")
        except Exception as e:
            print(f"display_img_error={e}")
        widget.update_idletasks()


    def insert_and_highlight(self, textbox, text, color_tag):
        """在文本框中插入文本，并高亮关键字"""
        # 获取关键字条件字典中的关键字
        keywords = self.INFO_config_dict.get("keyword_condition", [])
        if isinstance(keywords, str):
            keywords = json.loads(keywords)
        
        # 初始化起始位置
        start_index = 0
        
        # 遍历文本，查找关键字并插入
        while start_index < len(text):
            # 查找下一个关键字的位置
            nearest_keyword = None
            nearest_pos = len(text)
            
            for keyword in keywords:
                pos = text.find(keyword, start_index)
                if pos != -1 and pos < nearest_pos:
                    nearest_keyword = keyword
                    nearest_pos = pos
            
            # 如果找到了关键字之前的普通文本，插入它
            if nearest_pos > start_index:
                textbox.insert("end", text[start_index:nearest_pos], color_tag)
            
            # 如果找到了关键字，插入并高亮显示
            if nearest_keyword:
                end_pos = nearest_pos + len(nearest_keyword)
                tag_name = f"highlight_{nearest_keyword}"
                textbox.tag_config(tag_name, foreground="red", font=("微软雅黑", 12, "bold"), background="yellow")
                textbox.insert("end", text[nearest_pos:end_pos], tag_name)
                start_index = end_pos
            else:
                # 处理剩余的文本，且确保只插入一次
                # if start_index < len(text):
                #     textbox.insert("end", text[start_index:], color_tag)
                break


    def display_all_msg(self,dt,debug=False):
        if debug: print("enter displayallmsg")
        msgtype, msg_time, chinesename,message,color_tag,img_key,widget_s= dt.get("msgtype"),dt.get("msg_time"),dt.get("chinesename"),dt.get("message"),dt.get("color"),dt.get("img_key"),dt.get("widget")
        if int(widget_s)==1:
            target_text_box = self.textbox_kernel
        elif int(widget_s)==2:
            target_text_box = self.textbox_other  
        elif int(widget_s)==3:
            target_text_box = self.textbox_keyword    
        else:
            print("==lyytkmain, display_all_msg, else 未知widget序号======widget_s=",widget_s)
            
        if msgtype =="text":
            if debug: print("just display text=====================")
            blank = "\n" if self.last_teacher==chinesename else "\n\n"
            
            # target_text_box.insert("end", f"[{msg_time}] [{chinesename}] {message} {blank}", color_tag)
            # target_text_box.tag_config(color, foreground=color)
            self.insert_and_highlight(target_text_box, f"[{msg_time}] [{chinesename}] {message} {blank}", color_tag)
            
            with self.last_teacher_lock:
                self.last_teacher=chinesename
            if widget_s=="1" or widget_s==1:
                if debug: print("收到widget_s为1的消息，需要放到to_speak_queue中去。")
                self.to_speak_queue.put(chinesename + " " + message)

        elif msgtype =="img":
            target_text_box.insert("end", f"{msg_time} {chinesename} ------图片消息------ ", color_tag)
            self.display_img(target_text_box,img_key)
        if not self.ins_function.is_mouse_inside():
            target_text_box.see(tk.END)




    def after_check_win32messages_loop(self):
        # 处理消息
        win32gui.PumpWaitingMessages()
        # 继续定时检查是否有新的消息
        self.root.after(200, self.after_check_win32messages_loop)


        
    def after_check_queue(self,q):
        try:
            # 从队列中获取结果，非阻塞
            result = q.get_nowait()
            # 更新GUI组件，显示结果
            #label.config(text=result)
        except queue.Empty:
            # 如果队列为空，什么都不做
            pass
        finally:
            # 每隔100毫秒再次检查队列
            self.root.after(100, self.after_check_queue, q)
            
    def init_var(self):
        self.teachers_queue = queue.Queue()
        self.last_id_queue = queue.Queue()
        self.to_speak_queue = queue.Queue()
        self.reason_queue = queue.Queue()
        self.stop_event = threading.Event()       
        self.update_text_lock = threading.Lock()
        self.teacher_lock = threading.Lock()
        self.last_code_kingtrader_lock = threading.Lock()
        self.last_teacher = ""
        self.last_teacher_lock = threading.Lock()
        self.image_list = []
        self.image_list_lock = threading.Lock()
        self.image_list_to_keep = []
        self.image_list_to_keep_lock = threading.Lock()
        self.images_dict = {}
        self.undo_stack = []
        self.redo_stack = []
        # self.load_last_10msgs()
        # 设置对话框的外观
        self.style.configure("Chat.TFrame", background="#F0F0F0")
        self.style.configure("Chat.TLabel", background="#F0F0F0", font=("Arial", 12))
        self.style.configure("Chat.TEntry", background="white", font=("Arial", 12))
        self.PILphtoimge = None
        self.image = None
        self.last_file = None
        self.n = 0
        self.last_id = 0
        self.img_list = []
        self.last_code_kingtrader = ""
        self.win_sub_dict ={}#记录当前窗口的子窗口
        self.reason_dict = {}
        self.stk_code_name_dict = {}
        self.teacher_value_dict = {}
        self.status_bar_var = tk.StringVar()
        self.status_bar_var_lock = threading.Lock()
        self.status_bar_dict = {}
        self.update_tkinter_widget_lock = threading.Lock()
        self.last_msg_time_dict = {"novip":"1970-01-01 00:00:00","vip":"1970-01-01 00:00:00","subscribe":"1970-01-01 00:00:00"}
        self.mysql_task_lock = threading.Lock()
        self.mysql_task = []
        



if __name__ == "__main__":
    pass