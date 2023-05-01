import re

def replace_label(m):
	if m.group(1) == '/p' or m.group(1) == 'br/':
		return '\n'
	elif re.match('img', m.group(1)):
		link = re.search(' src="https://(.*?)"', m.group(1))
		if link:
			return ''.join(('![]','(https://',link.group(1),')\n'))
	else:
		return ''

def delete_label(content):
	if content:
		body = content
		pat = re.compile('<(.*?)>')
		all_match = re.findall(pat, body)
		body = re.sub(pat, replace_label, body)
		return body
	else:
		return ""

def Html2md(content):
	return delete_label(content)
