import logging
import getopt
import sys
import json
import re
from pyquery import PyQuery as pq
import zhihu_config, get, write,html2md #removed ", json2md",,added "html2md"
import os
abspath=os.path.abspath('.')
	
def Parse(config):

	doc = pq(config.html)
	config.body = doc('main .QuestionPage .RichContent .RichContent-inner .RichText').html()

	metas = doc('main > .QuestionPage > meta').items()
	for meta in metas:
		if meta.attr('itemprop') == 'name':
			config.title = meta.attr('content')
	if config.title == '':
		logging.warning('fail to get title!!!')

	metas = doc('.AnswerCard > .QuestionAnswer-content > .ContentItem > .ContentItem-meta > .AuthorInfo > meta').items()
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

	f = open(abspath+'/zhihu/cookie.json', 'r')
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

	print(config.title)


if __name__ == '__main__':
    main(sys.argv[1:])
    print("完成！！")