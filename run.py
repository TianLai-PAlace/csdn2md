# use tkinter to bulid an gui, can select a variable: mode and get an imput url, then a start button to run the code
import tkinter as tk
import os

def start_button():
   
    url = url_entry.get()
    if '?' in url:
        url = url.split('?')[0]
    
    current_path = os.path.dirname(os.path.abspath(__file__))
    mode = mode_option.get()
    category_url = url
    article_url= url
    start_page=1
    page_num=100
    markdown_dir=current_path+'/markdown'
    figure_dir = current_path+'/markdown/figures'
    pdf_dir='pdf'
    combine_together = 0
    to_pdf = 0
    abspath=os.path.abspath('.')

    if mode == "csdn-下载整个库的文章":
        os.system(f"python -u {abspath}/main.py --category_url {category_url} --start_page {start_page} --page_num {page_num} --markdown_dir {markdown_dir} --pdf_dir {pdf_dir}")
    elif mode == "csdn-下载单篇文章":
        os.system(f"python -u {abspath}/main.py --article_url {article_url} --markdown_dir {markdown_dir} --pdf_dir {pdf_dir} ")
    elif mode == "zhihu-专栏":
        os.system(f"python -u {abspath}/zhihu/zhihu_zhuanlan.py -l {article_url}")
    elif mode == "zhihu-问答":
        os.system(f"python -u {abspath}/zhihu/zhihu_answer.py -l {article_url}")
    elif mode == "zhihu-收藏夹":
        os.system(f"python -u {abspath}/zhihu/zhihu_collection.py -l {article_url}")


        
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
mode_option.set("csdn-下载单篇文章") 
mode_menu = tk.OptionMenu(root, mode_option, "csdn-下载单篇文章", "csdn-下载整个库的文章","zhihu-专栏","zhihu-问答","zhihu-收藏夹") 
mode_menu.pack(side=tk.LEFT)

#开始按钮 
start_button = tk.Button(root, text="开始下载", command=start_button) 
start_button.pack(side=tk.LEFT)


root.mainloop()