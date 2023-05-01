
def Text(entry, f):
	print(entry, file=open(f, "a", encoding="utf-8"))

def Printf(config):

	if not config.filepath:
		config.filepath = "./markdown/"+config.title + '--' + config.author + '的回答.md'
	if not config.url:
		config.url = 'https://www.zhihu.com/question/' + str(config.question_id) + '/answer/' + str(config.answer_id)

	Text('## Question: [' + config.title + '](' + config.url + ')', config.filepath)
	Text('### Author: [' + config.author + '](' + config.author_link + ')', config.filepath)
	Text(config.content, config.filepath)