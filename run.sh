#!/bin/bash
#############################
# CopyRight ~~~~~~
# Author: axzml
# Date: 2020-03-07
#############################

read -p "1:下载专栏全部文章 2:下载单独文章:  " download_category

if (($download_category == 1)); then
    echo "you have selectd 专栏全部文章下载"
    read -p "输入url:  " category_url
elif (($download_category == 2)); then
    echo "you have selectd 单独文章下载"
    read -p "输入url:  " article_url
else
    echo "请输入 1 或 2"
    read -p "按任意键结束" xer
    exit 0
fi

read -p "是否继续？(1/0)  " continue_flag
if (($continue_flag == 1));then
    set +x
    #download_category=true  ## 如果为 true, 就需要指定 catetory 的 url; 否则需要指定文章的 url
    #category_url='https://blog.csdn.net/hy592070616/category_11522440.html'
    #article_url='https://blog.csdn.net/qq_55058006/article/details/115570993'
    category_url = ${category_url}
    article_url= ${article_url}
    start_page=1
    page_num=100
    markdown_dir='markdown'
    figure_dir = 'markdown/figures'
    pdf_dir='pdf'

    if (($download_category == 1)); then
        python -u main.py \
            --category_url ${category_url} \
            --start_page ${start_page} \
            --page_num ${page_num} \
            --markdown_dir ${markdown_dir} \
            --pdf_dir ${pdf_dir} \
            --combine_together \
            --to_pdf \
            #--with_title \
            #--rm_cache \ ## dangerous option, remove all caches
    elif (($download_category == 2)); then
        python -u main.py \
            --article_url ${article_url} \
            --markdown_dir ${markdown_dir} \
            --pdf_dir ${pdf_dir} \
            --to_pdf \
            #--with_title \
            #--rm_cache \ ## dangerous option, remove all caches
            #--combine_together \
    else
        echo "请输入 1 或 0"
        read -p "按任意键结束" xer
        exit 0
    fi
fi
echo "下载目录为 .\ ${markdown_dir}"
read -p "按任意键结束" xer
#explorer ${markdown_dir}
