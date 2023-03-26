import os
from os.path import join
# 获取当前文件的路径
current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path+'/markdown/figures')
fig_dir = current_path+'/markdown/figures'
img_file = join(fig_dir, '2021041013351176.png')
print(img_file)