import logging
import getopt
import sys
import json
import re
from pyquery import PyQuery as pq
import zhihu_config, get, html2md, write
import os
abspath=os.path.abspath('.')

def Parse(config):

	doc = pq(config.html)
	config.body = doc('main .Post-Main .Post-RichTextContainer .RichText').html()

	config.title = doc('main .Post-Main h1').text()
	if config.title == '':
		logging.warning('failing to get title')

	metas = doc('main .Post-Main .Post-Author > .AuthorInfo').items()
	for	meta in metas:
		if meta.attr('itemprop') == 'name':
			config.author = meta.attr('content')
		if meta.attr('itemprop') == 'url':
			config.author_link = meta.attr('content')
	if config.author == '':
		logging.warning('fail to get author!!!')

	return config

def main(argv):

	config = zhihu_config.Config()

	f = open(abspath+f'/zhihu/cookie.json', 'r')
	content = f.read()
	cjson = json.loads(content)
	f.close()

	config.headers['accept'] = cjson['cookie']['accept']
	config.headers['user-agent'] = cjson['cookie']['user-agent']
	config.headers['cookie'] = cjson['cookie']['cookie']

	opts, args = getopt.getopt(argv, '-h-l:-s:', [help])
	for opt_name, opt_val in opts:
		if opt_name in ('-h', '--help'):
			print('-l [url] -s [savefile]')
			sys.exit()
		if opt_name == '-l':
			config.url = opt_val
		if opt_name == '-s':
			config.filepath = opt_val

	if config.url == '':
		print("Please input url!")
		sys.exit()

	config = get.GetHtml(config)
	config = Parse(config)
	config.content = html2md.Html2md(config.body)
	write.Printf(config)

	print(config.title + '--' + config.author)

if __name__ == '__main__':
    main(sys.argv[1:])
    print("完成！！")