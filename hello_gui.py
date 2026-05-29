import tkinter as tk
from tkinter import messagebox, scrolledtext

class EnhancedGUI:
    def __init__(self, root):
        # 设置主窗口
        self.root = root
        self.root.title("增强版GUI程序")
        self.root.geometry("500x400")  # 设置窗口大小
        self.root.resizable(True, True)  # 允许调整窗口大小
        self.root.config(bg="#f0f0f0")  # 设置背景颜色
        
        # 创建主框架
        self.main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建标题标签
        self.title_label = tk.Label(
            self.main_frame,
            text="欢迎使用增强版GUI程序",
            font=("SimHei", 16, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        self.title_label.pack(pady=(0, 20))
        
        # 创建输入区域框架
        self.input_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.input_frame.pack(fill=tk.X, pady=(0, 10))
        
        # 创建输入标签
        self.input_label = tk.Label(
            self.input_frame,
            text="请输入内容：",
            font=("SimHei", 10),
            bg="#f0f0f0",
            anchor="w"
        )
        self.input_label.pack(fill=tk.X, pady=(0, 5))
        
        # 创建输入框
        self.entry = tk.Entry(
            self.input_frame,
            width=50,
            font=("SimHei", 10),
            bd=2,
            relief=tk.SUNKEN
        )
        self.entry.pack(fill=tk.X, ipady=5)
        self.entry.bind("<Return>", lambda event: self.submit_action())  # 绑定回车键
        
        # 创建按钮框架
        self.button_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.button_frame.pack(fill=tk.X, pady=(10, 15))
        
        # 创建提交按钮
        self.submit_button = tk.Button(
            self.button_frame,
            text="提交",
            command=self.submit_action,
            font=("SimHei", 10),
            bg="#4CAF50",
            fg="white",
            relief=tk.RAISED,
            padx=10
        )
        self.submit_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # 创建清空按钮
        self.clear_button = tk.Button(
            self.button_frame,
            text="清空",
            command=self.clear_action,
            font=("SimHei", 10),
            bg="#f44336",
            fg="white",
            relief=tk.RAISED,
            padx=10
        )
        self.clear_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # 创建复制按钮
        self.copy_button = tk.Button(
            self.button_frame,
            text="复制结果",
            command=self.copy_action,
            font=("SimHei", 10),
            bg="#2196F3",
            fg="white",
            relief=tk.RAISED,
            padx=10
        )
        self.copy_button.pack(side=tk.LEFT)
        
        # 创建结果区域
        self.result_label = tk.Label(
            self.main_frame,
            text="结果显示：",
            font=("SimHei", 10),
            bg="#f0f0f0",
            anchor="w"
        )
        self.result_label.pack(fill=tk.X, pady=(15, 5))
        
        # 创建滚动文本框显示结果
        self.result_text = scrolledtext.ScrolledText(
            self.main_frame,
            width=60,
            height=10,
            font=("SimHei", 10),
            bd=2,
            relief=tk.SUNKEN,
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.result_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # 创建状态标签
        self.status_var = tk.StringVar()
        self.status_var.set("就绪")
        self.status_label = tk.Label(
            root,
            textvariable=self.status_var,
            font=("SimHei", 9),
            bg="#e0e0e0",
            fg="#666666",
            anchor="w"
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
    
    def submit_action(self):
        try:
            user_input = self.entry.get().strip()
            if user_input:
                # 启用文本框，插入内容，然后禁用
                self.result_text.config(state=tk.NORMAL)
                self.result_text.delete(1.0, tk.END)  # 清空现有内容
                self.result_text.insert(tk.END, f"您输入的内容是：{user_input}\n\n")
                
                # 添加一些处理信息
                self.result_text.insert(tk.END, f"字符数：{len(user_input)}\n")
                self.result_text.insert(tk.END, f"单词数（以空格分隔）：{len(user_input.split())}\n")
                
                # 检查是否包含数字
                has_digits = any(char.isdigit() for char in user_input)
                self.result_text.insert(tk.END, f"包含数字：{'是' if has_digits else '否'}\n")
                
                # 检查是否包含字母
                has_letters = any(char.isalpha() for char in user_input)
                self.result_text.insert(tk.END, f"包含字母：{'是' if has_letters else '否'}\n")
                
                self.result_text.config(state=tk.DISABLED)
                self.status_var.set("提交成功")
                self.root.config(bg="#e8f5e8")  # 成功时改变背景色
            else:
                messagebox.showwarning("警告", "请输入内容！")
                self.status_var.set("未输入内容")
                self.root.config(bg="#ffebee")  # 警告时改变背景色
        except Exception as e:
            messagebox.showerror("错误", f"发生错误：{str(e)}")
            self.status_var.set(f"发生错误")
            self.root.config(bg="#ffebee")
    
    def clear_action(self):
        self.entry.delete(0, tk.END)
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.DISABLED)
        self.status_var.set("已清空")
        self.root.config(bg="#f0f0f0")  # 恢复默认背景色
        self.entry.focus_set()  # 焦点回到输入框
    
    def copy_action(self):
        try:
            result = self.result_text.get(1.0, tk.END).strip()
            if result:
                # 使用tkinter内置的剪贴板功能
                self.root.clipboard_clear()  # 清空剪贴板
                self.root.clipboard_append(result)  # 将文本添加到剪贴板
                self.status_var.set("结果已复制到剪贴板")
                messagebox.showinfo("成功", "结果已复制到剪贴板")
            else:
                messagebox.showwarning("警告", "没有可复制的内容")
                self.status_var.set("没有可复制的内容")
        except Exception as e:
            messagebox.showerror("错误", f"复制失败：{str(e)}")
            self.status_var.set("复制失败")

if __name__ == "__main__":
    # 创建主窗口
    root = tk.Tk()
    
    # 确保中文正常显示
    try:
        # 这里设置字体，确保中文显示正常
        pass
    except:
        pass
    
    # 创建并运行应用
    app = EnhancedGUI(root)
    root.mainloop()