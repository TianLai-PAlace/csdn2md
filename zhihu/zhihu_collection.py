import zhihu_config, get, html2md, write
import json
import getopt
import sys
import re

def UrlTransform(config):
	A = '/(\d+)\??'
	config.collection_id = re.search(A, config.url).group(1)
	pre = 'https://www.zhihu.com/api/v4/favlists/'
	suffix = '/items?include=data%5B%2A%5D.created%2Ccontent.comment_count%2Csuggest_edit%2Cis_normal%2Cthumbnail_extra_info%2Cthumbnail%2Cdescription%2Ccontent%2Cvoteup_count%2Ccreated%2Cupdated%2Cupvoted_followees%2Cvoting%2Creview_info%2Cis_labeled%2Clabel_info%2Crelationship.is_authorized%2Cvoting%2Cis_author%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset='
	config.url = pre + str(config.collection_id) + suffix

def GetAllCollectins(config):
	totals = json.loads(config.html)['paging']['totals']
	preurl = config.url
	page = 0
	while(page < totals):
		config.url = preurl + str(page)
		print('get url: ' + config.url)
		config = get.GetHtml(config)
		config.filepath = f'../markdown/collection' + str(config.collection_id) + '-' + str(page // 20) + '.md'
		#write.Text(config.html, 'collect8.json')
		contents = json.loads(config.html)['data']
		for item in contents:
			print(item)
			if 'question' in item['content']:
				config.url = ''
				config.question_id = item['content']['question']['id']
				config.answer_id = item['content']['id']
				config.title = item['content']['question']['title']
				config.author = item['content']['author']['name']
				config.author_link = item['content']['author']['url'].replace('/api/v4', '')
				config.content = html2md.Html2md(item['content']['content'])
			else:
				config.url = item['content']['url']
				config.title = item['content']['title']
				config.author = item['content']['author']['name']
				config.author_link = item['content']['author']['url'].replace('/api/v4', '')
				config.content = html2md.Html2md(item['content']['content'])
			write.Printf(config)
			print(config.url + ' 完成！！！')
		page += 20
		print('col' + str(page // 20) + '完成！！！')

def main(argv):

	config = zhihu_config.Config()

	f = open('cookie.json', 'r')
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


	UrlTransform(config)
	#print(config.url)
	config = get.GetHtml(config)
	GetAllCollectins(config)


	# write.Text(config.html, 'collect2.json')

if __name__ == '__main__':
    main(sys.argv[1:])
    print("完成！！")