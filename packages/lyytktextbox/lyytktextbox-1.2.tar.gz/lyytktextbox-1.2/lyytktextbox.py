from tkinter import Tk, Text, Menu, messagebox, simpledialog
from datetime import datetime
import base64
import pandas as pd
import subprocess
import threading
import time
import json
import pandas as pd
import urllib
from urllib.parse import quote
from io import BytesIO, StringIO
from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from pynput.mouse import Controller
from datetime import datetime
from win10toast import ToastNotifier
from functools import partial

import lyytext
from lyylog import log
from lyyapp import 提取url
from lyyapp import set_volume as vol
from lyyapp import format_ocr_text as format_text
from sqlalchemy import create_engine, text
import mysql.connector
import lyycfg
import lyynircmd
import lyyre
LAST_MSG = ""
MSG_HISTORY = []

toaster = ToastNotifier()
id_last_msg = 0
LAST_MSG = ""
teacher_value_dict = {}
# 额外信息 = info_cfg.subscribe_teachers

# 额外信息 = "or name in ('dingjilijie','sunan','jinrongxiaoyaonv','yaogucike','jinrongxiaoyaonu','jiucaigongshehongbaoshu','shuchuceshi','qingdaoxiaoerge','xiatian','taiyangdeweixiao','qingyiyouzi','wuhuishushu','tianshidiaoyan','qingdao','qingyiyouzi','taiyangdeweixiao','veget','xingchen','xinshengdailongkonglong','dila') "
message_sent = None
# asyncio.create_task(send_msg_ws(msg))

def send_notification(title, message):
    toaster.show_toast(title, message, duration=10)

def get_mouse_position():
    mouse = Controller()
    return mouse.position


class info_class:
    def __init__(self, main_module) -> None:
        self.main_module = main_module
        self.config_INFO = self.main_module.all_config_dict.get("info_config").get("INFO")
        self.msg_limit = int(self.config_INFO.get("msg_limit"))
        self.vip_msg_limit = int(self.config_INFO.get("vip_msg_limit"))

        print("msg limt = ",self.msg_limit)
        self.last_msgid=0
        self.db_config = lyycfg.DotDict(self.main_module.all_config_dict.get("gui_config").get("data_source"))
        self.kernel_teachers_color_dict = json.loads(self.config_INFO.get("kernel_teachers_color"))
        print("self.kernel_teachers_color_dict=",self.kernel_teachers_color_dict)     
        print("self.db_config=",self.db_config)
        self.last_time_lock = threading.Lock()

        fun_query_stock_info_vip_teachers = partial(self.query_stock_info, teacher_type="vip")
        fun_query_stock_info_all_teachers = partial(self.query_stock_info, teacher_type="novip")
        self.main_module.mysql_task.append(fun_query_stock_info_vip_teachers)
        self.main_module.mysql_task.append(fun_query_stock_info_all_teachers)


    def build_and_query_sql(self,teacher_type="vip",debug=False):
        debug = True
        if debug: print("in info_clasee,enter build_and_query_sql")
        vip_name_list = list(self.kernel_teachers_color_dict.keys()) 
        conditions = []
        if debug: print("inbuild_andquery,",self.main_module.last_msg_time_dict)
        pre_query   = "SELECT time, chinesename, message FROM stock_info where "
        if teacher_type == "vip":
            keyword_list = list(json.loads(self.main_module.all_config_dict.info_config.INFO.keyword_condition))
            vip_name_placeholders = ", ".join(["'{}'".format(name) for name in vip_name_list])
            sqlquery = self.main_module.ins_lyysql.build_query("message",keyword_list,    ["chinesename IN ({})".format(vip_name_placeholders)], keywords_logic_operator="OR", logic_operator="OR", time_limit= self.main_module.last_msg_time_dict[teacher_type], order_by_column="time", sort_order="desc", limit=int(self.vip_msg_limit), debug=False)
            #    def build_query(self, keywords_column_name:str, keywords: list, conditions: list, keywords_logic_operator: str = "OR", logic_operator: str = 'AND',order_by_column:str="", sort_order:str="desc", limit:int=100, debug=False) -> str:
            if debug: print("endquery=",pre_query+sqlquery)
            self.main_module.ins_lyysql.cursor.execute(pre_query + sqlquery)
            if debug: print("查询语句:", pre_query +sqlquery,"查询成功结束！")
        else:
            if len(vip_name_list) > 0:
                conditions.append("chinesename NOT IN ({})".format(", ".join(["%s"] * len(vip_name_list))))
                # 从配置中读取black_list字典
                black_list = self.config_INFO["black_list"]
                black_list = black_list if isinstance(black_list, dict) else json.loads(black_list)
                # 获取black_list中的所有键，并将其转换为正则表达式字符串
                # 使用列表推导式和join方法                
                regexp_str = '|'.join(black_list.keys())
                # 构建MySQL的NOT REGEXP语句
                conditions.append(f"chinesename NOT REGEXP '{regexp_str}'")

            query = "SELECT time, chinesename, message FROM stock_info WHERE ({}) AND time > %s order by time desc limit 500".format(" AND ".join(conditions))
            # 输出查询语句
            formatted_query = query % tuple(vip_name_list + [self.main_module.last_msg_time_dict[teacher_type]])
            #print("查询语句:", formatted_query)
            self.main_module.ins_lyysql.cursor.execute(query, vip_name_list + [self.main_module.last_msg_time_dict[teacher_type]])

    
    def query_stock_info_all_loop(self,main_module=None, teacher_type="vip",debug=False):
        print("in infoclass, start query_stock_info_all")
        while self.main_module.stop_event.is_set() == False:
            try:
                self.main_module.ins_lyysql.get_connector(before_notice="准备连接MySQL...",after_notice="MySQL连接成功")
                #print("qeuall,afster",len(self.main_module.mysql_task))
                for fun in self.main_module.mysql_task:
                    fun()
                time.sleep(1)
                #self.query_stock_info(teacher_type="novip")
            except mysql.connector.Error as e:
                print("in lyytktextbox.py,query_stock_info_all, errmsg="+str(e))

                time.sleep(10)
        self.cursor.close()
        self.main_module.cnx.close()
        
    def query_stock_info(self,main_module=None,teacher_type="vip"):
        # 连接到MySQL数据库
        time.sleep(1)
        try:
            self.main_module.set_status_bar("正在查询MySQL数据...")
            start_time = datetime.now()
            self.build_and_query_sql(teacher_type=teacher_type)            
            self.main_module.set_status_bar(f"查询结束{teacher_type}")
            self.main_module.set_status_bar(round((datetime.now()-start_time).total_seconds(),2), "查询耗时")
        except Exception as e:
            print(f"in_uquery_info, sqlerror{e}")
                
            # 获取查询结果并显示在文本框中
        self.process_mysql_data(teacher_type=teacher_type)
            
                #self.insert_data(result)
                # 使用wx.CallAfter()将更新UI的操作传递给主线程执行
                # 更新最新查询时间
            # 关闭数据库连接


            
    def process_mysql_data(self, teacher_type,debug=False):
            
        try:
            tmp_time = None
            all_data = []
            self.main_module.set_status_bar("处理数据中...")
            result = list(self.main_module.ins_lyysql.cursor.fetchall())
            if debug: print("in,processmysql_data,lenof_result=",len(result))
            i=0
            for row in reversed(result):
                if debug: print(f"处理第{i}条信息",row)
                i+=1
                tmp_time = row[0]
                item = self.convert_format_data(row,teacher_type)
                all_data.append(item)
                self.main_module.data_queue.put([item])
            self.main_module.set_status_bar("数据处理完毕")
            if len(all_data)>0:
                with self.last_time_lock:
                    self.main_module.last_msg_time_dict[teacher_type] = str(tmp_time)
                self.main_module.set_status_bar(str(tmp_time).replace(datetime.now().strftime("%Y-%m-%d"),""),"消息最后时间")
        except Exception as e:
            print(f"inqueryinfo，process_mysql_data,err={e}")

    def convert_format_data(self,row, teacher_type,widget=None,msg_color = "black",debug=False):
        """
        格式化MySQL查询结果。data = [{"time":,"chinesename":}]
        最终转化为：
        widget:widget, insert: target:image.open
        """
        if debug: print("enter======convert_format_data== eovcvert format data")
        today_date = datetime.now().strftime("%Y-%m-%d")
        msg_time = str(row[0]).replace(today_date+" ","")
        chinesename = row[1]
        message = row[2]
        msg_type, msg_content = lyyre.identify_content( message)
        if widget is None:        
            if  chinesename in self.kernel_teachers_color_dict.keys():
                widget=1
                msg_color = self.kernel_teachers_color_dict.get(chinesename)
            else:  
                widget=3 if teacher_type == "vip" else 2
        #msg_content =  self.get_img_data_from_url(msg_content) if msg_type == "img" else msg_content
        data_dict = {"msg_time":msg_time,"chinesename":chinesename,"message":msg_content,"cmd":"showmsg","msgtype":msg_type,"widget":widget,"color":msg_color}

        if msg_type == "img":
            img_key = datetime.now(). microsecond
            data_dict["img_key"] = img_key
            img = self.get_img_data_from_url(msg_content)
            if img:
                self.main_module.images_dict[img_key] = ImageTk.PhotoImage(img)
        return data_dict


    def get_message_loop(self):
        print("enter msgloop")
        try:
            while True:
                    # f1999info.getinfo_sqlite(lyywin)
                    self.query_stock_info()
                    #lyywin.gui_function.set_statusbar3(datetime.now().strftime("%H:%M:%S"))
        except Exception as e:
            print("in keep_get_info", e)
            time.sleep(20)
            self.get_message_loop()
        finally:
            pass
        
    def lyyspeak(self, debug=False):
        x = 0
        while self.main_module.stop_event.is_set() == False:
            print("@",end="")
            try:
                now = datetime.now()
                timeint = now.hour * 100 + now.minute
                if timeint < 825 and timeint > 2100:
                    if debug:
                        print("too early, be quiet, current_time < 08:25 or timeint > 2100, return")
                    time.sleep(60)  # 等待一段时间再次检查
                    continue

                # 从队列中获取要说的文本
                if not self.main_module.to_speak_queue.empty():
                    if debug: print("speak_queuenot empty")
                    if self.main_module.to_speak_queue.qsize() > 1:
                        print("queue里面好多数据啊，省略一些")
                        for _ in range(self.main_module.to_speak_queue.qsize() - 1):
                            self.main_module.to_speak_queue.get()
                    to_speak_text = self.main_module.to_speak_queue.get()
                    if debug:print("播放列表中内容。当前列表=", to_speak_text)
                    
                    # 格式化文本并分割标题和消息
                    to_speak_text = lyytext.format_to_speak_text(to_speak_text)
                    # 发送一个通知
                    # send_notification(title, message)
                    
                    to_speak_text = to_speak_text[: max(80, len(to_speak_text))].replace(":", "")
                    if self.main_module.all_config_dict.get("gui_config").get("modules").get("enable_speak") and x>20:                        
                        print("to_speak_test<",to_speak_text,">")
                        lyynircmd.speak_text(to_speak_text)

                time.sleep(1)
                x+=1
            except Exception as e:
                log("lyyspeak,error,msg-=" + str(e))
                time.sleep(10)  # 发生异常时等待一段时间再次尝试
        else:
            print("lyyspeaker module is disbled, check configuration file")



    def process_teachers_messages(self, info_dict, debug=False):
        if "markdown" in info_dict.keys():
            # msg_json_text= {"msgtype": "markdown", "markdown": {"title": "\u676, "text": "\u6427"}, "at": {"atMobiles": [], "isAtAll": false}, "time": "2023-38", "name": "wodequn", "chinesename": "\u6211\u7684\u7fa4"}
            print("这是fpsq来的01框架的钉钉消息")
            msg_text = info_dict["markdown"]["text"]
        else:
            # print("不是markdown消息")
            msg_text = info_dict["message"]
        global LAST_MSG
        if msg_text == LAST_MSG:
            # print("---------重复----------------------")
            return
        else:
            # print("last msg=<" + LAST_MSG + ">", "MSG=" + "<" + msg_text + ">")
            LAST_MSG = msg_text

        for word in self.main_module.all_config_dict.get("info_cfg.ini",{"error":"no info_cfg.ini"}).get("block_keywords","no block_keywords").split("|"):
            if word in msg_text:
                print("block word=<" + word + ">")
                return

        msg_text = lyytext.add_stockname_for_stkcode(msg_text)
        # print("info_dict['message']=<" + info_dict['message']+">,  msg_text=<"+ msg_text+">")
        teacher_name = info_dict["chinesename"]
        if teacher_name == "输入测试":
            print("shuruceshi")
            if "lyycmd" in msg_text:
                print("lyycmd in msg_text")
                lyycmd = msg_text.replace("lyycmd", "").strip()
                print("try to exec  lyycmd:<" + lyycmd, ">")
                exec(lyycmd)
            else:
                print("只是输入测试,不做额外处理。normaltext=<", msg_text + ">")
        
        msgtime = info_dict["time"].replace(str(datetime.now())[:10], "").strip()

        if "http" in msg_text:
            url = 提取url(msg_text, debug=debug)
            text_else = msg_text.replace(url, "").replace("![screenshot]()", "")
            if len(text_else) > 12:
                # print("len(text_except_url) > 12 text_except_url=", text_else[:60])
                self.display_msg( msgtime, teacher_name, text_else, debug=debug)
            self.process_url( url, msgtime, teacher_name, msg_text, debug=debug)
        else:
            self.display_msg( msgtime, teacher_name, msg_text, debug=debug)


    def process_url(self, url, msgtime, teacher_name, msg_text, debug=False):        
        widget = self.main_module.textbox_kernel if teacher_name in self.kernel_teachers_color_dict.keys() else self.main_module.textbox_kernel
        
        if "pdf" in url:
            self.main_module.last_file = url
            if debug:
                print("下载链接为文件")
            widget.insert("end", url, "blue")
            widget.tag_config("link", foreground="blue", underline=True)
            widget.tag_bind("link", "<Button-1>", self.main_module.ins_function.open_link)
        elif "pic" in url or ".jpg" in url or ".png" in url or ".jpeg" in url or ".bmp" in url:
            if debug:
                print("下载链接为图片,url=", url, "pic in url=", "pic" in url, ".jpg" in url, ".png" in url, ".jpeg" in url, ".bmp" in url)
            self.show_image(widget, url, msgtime, teacher_name)
        else:
            self.display_msg( msgtime, teacher_name, url, tag="link", debug=debug)
            widget.tag_config("link", foreground="blue", underline=True)
            widget.tag_bind("link", "<Button-1>", self.main_module.ins_function.open_link)
            # 为 "link" 标签设置样式
            widget.tag_configure("link", foreground="blue", underline=True)

            # 为 "link" 标签添加一个鼠标移入事件
            widget.tag_bind("link", "<Enter>", self.main_module.ins_function.on_enter_link)

            # 为 "link" 标签添加一个鼠标移出事件
            widget.tag_bind("link", "<Leave>", self.main_module.ins_function.on_leave_link)

            # 为 "link" 标签添加一个点击事件
            widget.tag_bind("link", "<Button-1>", self.main_module.ins_function.open_link)

    def process_simple_text(self, text, debug=False):
        print("这是普通消息，直接显示，内容为：" + text)
        import time

        if "http" in text:
            url = 提取url(text, debug=debug)
            # process_teachers_messages(text[:text.index(url)])
        if "pdf" in text:
            url = text
            self.main_module.last_file = url
            if debug:
                print("下载链接为文件")
            self.main_module.textbox_kernel过滤并显示(url, location=tk.END, color="blue")
            self.main_module.textbox_kernel.tag_config("link", foreground="blue", underline=True)
            self.main_module.textbox_kernel.tag_bind("link", "<Button-1>", self.main_module.open_link)
        elif "pic" in text or ".jpg" in text or ".png" in text or ".jpeg" in text or ".bmp" in text:
            # print("下载链接为图片,url为", url)
            # self.main_module.textbox_kernel过滤并显示()
            self.show_image(self, url)
            return
        else:
            if debug:
                print("Normal text message")
            self.main_module.textbox_kernel.tag_config("link", foreground="blue", underline=True)
            self.main_module.textbox_kernel.tag_bind("link", "<Button-1>", self.main_module.open_link)

            # TO_SPEAK_LIST.append(text)


    def process_recieved_msg(self,msg_json_text, process_args=None, debug=False):
        global TO_SPEAK_LIST
        debug=True
        """    
        print("收到消息，进入process_recieved_msg, text=<", text,">")
        如果是带有指令的文本
        sql消息：{"id":817277,"time":1698415772000,"chinesename":"vip\u9876\u7ea7\u7406\u89e3","message":"https:\/\/gchat.qpic.cn\/gchatpic_new\/724710691\/724710691-2731142198-8D75211539538FC69895370B6F2004A2\/0"},{"id":817282,"time":1698415829000,"chinesename":"vip\u9876\u7ea7\u7406\u89e3","message":"\u51a0\u9f99\u4e5f\u56de\u5c01\u4e86
    \uff0c\u4e0b\u5468\u4e00\u5c31\u770b\u9f99\u5dde\u4e86"}
        """
        # if debug: print("收到消息，进入process_recieved_msg, text=", msg_json_text)
        # print("enter process_recieved_msg, msg_json_text=", msg_json_text)
        try:
            msg_json = json.loads(msg_json_text) if isinstance (msg_json_text,str) else msg_json_text
            if debug:
                print("msg_json=", msg_json)
            if "msgtype" in msg_json.keys():
                msgtype = msg_json["msgtype"]
        except Exception as e:
            print("in process_recieved_msg json.loads error", e)
            try:
                self.process_simple_text( msg_json_text)
            except Exception as e:
                print("in process_recieved_msg process_simple_text error", e)
            finally:
                pass
            return
        # print(msgtype, "fdsafdsaf")

        if msgtype == "ztreason":
            try:
                if debug:
                    print("这是涨停原因消息", msg_json)
                self.main_module.gui_reason_module.show_msgwin(msg_json)
            except Exception as e:
                print("in f1999msg process_reciedved _msg , eason_module.show_msgwin(msg_json)", e)
            finally:
                pass

        elif msgtype in ["winmsg", "showsql", "showmsg", "showsys", "mengxia", "showwss"]:
            # print("enter showmsg, msg_json_text=", msg_json_text)
            # print("stringio=",StringIO(msg_json_text))
            try:
                import traceback
                self.process_teachers_messages(msg_json)

            except Exception as e:
                traceback.print_exc()
                print("process_teachers_messages error=", e)
        elif msgtype == "execcmd":
            cmd = msg_json["cmd"]
            if cmd == "clear":
                self.main_module.textbox_kernel.delete(1.0, tk.END)


    def ocr_it(self, base64img):
        print("------------------------------------ocr----------------------------------------")
        import requests
        import json

        url = "http://127.0.0.1:10024/api/ocr"
        data = {"base64": base64img, "ocr": {"language": "models/config_chinese.txt", "cls": False, "limit_side_len": 960, "tbpu": {"merge": "MergeLine"}}, "rapid": {"language": "简体中文", "angle": False, "maxSideLen": 1024, "tbpu": {"merge": "MergeLine"}}}

        response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))

        if response.status_code == 200:
            result = response.json()
            data = result.get("data")
            for i in data:
                print(i["text"])
                self.main_module.textbox_kernel.insert(tk.END, i["text"] + "\n")
        else:
            print("识别失败")
            
    def get_img_data_from_url(self,url,debug=True):
        url = url.replace(" ","")
        try:
            # 对 URL 进行编码
            # url = quote(url, safe='/:')
            with urllib.request.urlopen(url) as response:
                try:
                    image_data = BytesIO(response.read())
                    image = Image.open(image_data)
                except Exception as e:
                    print(f"BytesIO下载图片出错，  url={url},应该是图片网址有问题。error=", e)
                    return
                # 获取原始图片大小
                width, height = image.size
                if width > 500:
                    rate = width / 500
                    new_width ,new_height =    int(width / rate),int(height / rate)                                      
                    image.thumbnail((new_width, new_height), None)  # 使用thumbnail方法进行缩放
                return image 
            
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f"404 Not Found，一般是网址问题， url={url},忽略此条信息即可。url=" + url)
            else:
                # 处理其他HTTP错误
                print("HTTP Error:", e.code)
        except Exception as e:
            print(f"in get_img_data_from_url, url={url}, Error displaying image:", str(e))


    def show_image(self, widget, tkimage,url, msgtime, teacher_name, debug=False):
        if debug:
            print("enter show image, imgurl=", url)
        self.display_msg( msgtime, teacher_name, msg_text="--------", debug=debug)

        self.main_module.PIL_photoimage = ImageTk.PhotoImage(tkimage)
        
        with self.main_module.image_list_to_keep_lock:
            self.main_module.image_list_to_keep.append(self.main_module.PIL_photoimage)  # 保存图片引用以避免图片消失

        if debug:
            print("finish resize,new size=", tkimage.size)

        # 添加到图片列表
        widget.image_create(tk.END, image=self.main_module.PIL_photoimage)
        # 在图像后面添加一个换行符，以便继续显示文本
        widget.insert(tk.END, "\n")
        widget.update_idletasks()  # 刷新文本框




class gui_textbox_class:
    def __init__(self, main_module):
        self.main_module = main_module
        self.root = self.main_module.root
        self.notebox = self.main_module.textbox_rule
        self.msgbox = self.main_module.textbox_kernel
        self.search_word = None
        self.last_index = '1.0'
        self.initialize_styles()
        self.create_context_menu()
        self.bind_events()
        self.add_right_menu()

    def initialize_styles(self):
        styles = {"saddlebrown": "saddlebrown", "darkorange": "darkorange", "blue": "blue", "purple": "purple", "green": "green", "red": "red", "yellow": "yellow", "浅灰色": "#8E236B", "olive": "olive", "steelblue": "steelblue", "orangered": "orangered", "maroon": "maroon", "chocolate": "chocolate", "navajowhite": "navajowhite", "gray_bg": "gray"}
        for tag, style in styles.items():
            self.msgbox.tag_configure(tag, foreground=style)

        self.msgbox.tag_configure("bold", font=("黑体", 12))

    def add_right_menu(self):
        # 创建右键菜单
        self.menu = Menu(self.root, tearoff=0)
        self.menu.add_command(label="剪切", command=lambda: self.root.event_generate("<Control-x>"))
        self.menu.add_command(label="复制", command=lambda: self.root.event_generate("<Control-c>"))
        self.menu.add_command(label="粘贴", command=lambda: self.root.event_generate("<Control-v>"))
        self.menu.add_separator()
        self.menu.add_command(label="清空", command=lambda: self.textbox_kernel.delete("1.0", "end"))
        self.menu.add_separator()
        self.menu.add_command(label="全选", command=lambda: self.root.event_generate("<Control-a>"))
        self.notebox.bind_class("Text", "<Button-3>", self.show_context_menu)
        self.notebox.bind_class("Text", "<Double-Button>", self.toggle_fullscreen)
        self.notebox.bind_class("Text", "<Double-Button-1>", self.toggle_fullscreen)

    def create_context_menu(self):
        self.menu = Menu(self.root, tearoff=0)
        menu_commands = [("剪切", lambda: self.root.event_generate("<Control-x>")), ("复制", lambda: self.root.event_generate("<Control-c>")), ("粘贴", lambda: self.root.event_generate("<Control-v>")), ("清空", lambda: self.msgbox.delete("1.0", "end")), ("全选", lambda: self.root.event_generate("<Control-a>"))]
        for label, command in menu_commands:
            self.menu.add_command(label=label, command=command)
        self.menu.add_separator()

    def bind_events(self):
        self.notebox.bind_class("Text", "<Button-3>", self.show_context_menu)
        self.notebox.bind_class("Text", "<Double-Button>", self.toggle_fullscreen)
        self.notebox.bind_class("Text", "<Double-Button-1>", self.toggle_fullscreen)

    def show_context_menu(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def toggle_fullscreen(self, event):
        current_font = self.msgbox.cget("font")
        font_family, original_font_size = current_font.split()
        font_size = int(original_font_size)

        if event.widget.winfo_toplevel().attributes("-fullscreen"):
            font_size -= 6
            event.widget.winfo_toplevel().attributes("-fullscreen", False)
        else:
            font_size += 6
            event.widget.winfo_toplevel().attributes("-fullscreen", True)
        new_font = (font_family, font_size)
        self.msgbox.config(font=new_font)
        self.notebox.config(font=new_font)

    def find(self, event=None):
        textbox =event.widget
        text = textbox.get("1.0", "end-1c")
        # 获取用户想要查找的关键字
        # 这里假设用户已经通过某种方式输入了要查找的关键字
        # 例如，通过一个输入框获取
        self.search_word = simpledialog.askstring("Find", "Enter the text to find:")
        # 检查搜索词是否为空
        if not self.search_word:
            return
        # 在文本中查找搜索词
        index =textbox.search(self.search_word, "1.0", tk.END)
        if index:
            # 如果找到了搜索词，可以选择将其高亮显示
            # 这里使用标签方法将搜索词标记为高亮
            textbox.tag_add("highlight", index, f"{index}+{len(self.search_word)}c")
            textbox.tag_config("highlight", background="yellow")
            textbox.see(index)
        else:
            # 如果没有找到搜索词，可以给用户一个提示
            print("没有找到搜索词:",self.search_word)




    def find_next(self, event=None):
        print("enter find_next")
        if not self.search_word:
            print("没有搜索内容，返回。")
            return  # 如果没有搜索内容，直接返回

        # 从上一次找到的索引之后开始搜索
        self.msgbox = event.widget
        start_index = self.msgbox.search(self.search_word, self.last_index + "+1c", "end")
        if start_index:
            end_index = f"{start_index}+{len(self.search_word)}c"
            self.msgbox.tag_remove("search", "1.0", "end")  # 移除上一次的高亮
            self.msgbox.tag_add("search", start_index, end_index)
            self.msgbox.tag_config("search", background="red", foreground="black")
            self.msgbox.see(start_index)
            self.last_index = end_index  # 更新最后找到的索引
        else:
            messagebox.showinfo("Find", "No more occurrences found.")
            self.last_index = '1.0'  # 重置搜索起点


    def process_and_display_text(self, row):
        rpltxt = str(datetime.now())[5:10] + " "
        msg_time = row[1].replace(rpltxt, "") + " "
        msg_teacher = row[2].replace("vip", "").replace("理解", "").replace("游资", "").replace("投研", "") + ":"
        if row[2] != self.last_teacher:
            prefix = "\n" + msg_time + msg_teacher
        else:
            prefix = msg_time
        full_msg = prefix + row[3] + "\n"
        self.display_text(full_msg, msg_teacher)
        self.last_teacher = row[2]

    def display_text(self, tmptext, msg_teacher):
        dict_color = {"顶级": "blue", "公子复盘": "green", "妖股刺客": "purple", "梅森投研": "orange"}
        for key, value in dict_color.items():
            if key in msg_teacher:
                self.msgbox.tag_configure(value, foreground=value)
                break
        self.msgbox.insert("end", tmptext, value)
        self.msgbox.see("end")

    def filter_and_display_text(self, text, location="end", color="black"):
        self.msgbox.insert(location, text, color)



if __name__ == "__main__":

    root = Tk()
    notebox = Text(root)
    msgbox = Text(root)
    gui_textbox = gui_textbox_class(root, notebox, msgbox)
    root.mainloop()
