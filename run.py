# use tkinter to bulid an gui, can select a variable: mode and get an imput url, then a start button to run the code
import tkinter as tk
import os

def start_button():
    import tkinter.messagebox as messagebox
    messagebox.showinfo(title='提示', message='正在下载中，请稍后')   
    
    url = url_entry.get()
    mode = mode_option.get()
    category_url = url
    article_url= url
    start_page=1
    page_num=100
    markdown_dir='markdown'
    figure_dir = 'markdown/figures'
    pdf_dir='pdf'
    combine_together = 0
    to_pdf = 0

    if mode == "下载整个库的文章":
        os.system(f"python -u ./main.py --category_url {category_url} --start_page {start_page} --page_num {page_num} --markdown_dir {markdown_dir} --pdf_dir {pdf_dir}")
    elif mode == "下载单篇文章":
        os.system(f"python -u ./main.py --article_url {article_url} --markdown_dir {markdown_dir} --pdf_dir {pdf_dir} ")

        
root = tk.Tk() 
root.title("CSDN2MD downloader")

#输入框 
url_label = tk.Label(root, text="请输入URL: ") 
url_label.pack(side=tk.LEFT) 
url_entry = tk.Entry(root, width=50) 
url_entry.pack(side=tk.LEFT)

#选择变量 
mode_label = tk.Label(root, text="请选择模式: ") 
mode_label.pack(side=tk.LEFT) 
mode_option = tk.StringVar() 
mode_option.set("下载单篇文章") 
mode_menu = tk.OptionMenu(root, mode_option, "下载单篇文章", "下载整个库的文章") 
mode_menu.pack(side=tk.LEFT)

#开始按钮 
start_button = tk.Button(root, text="开始下载", command=start_button) 
start_button.pack(side=tk.LEFT)


root.mainloop()