#!/usr/bin/env python
import jinja2
import yaml
import re
import math

def remove_tag(text):
	return re.sub(text, '<.*>', '')

def main():
	with open('templates/profile.yml','r') as f:
		profile_data = f.read()
	with open('templates/template.html', 'r') as f:
		template_data = f.read().decode('utf8')
	
	env = jinja2.Environment()
	env.filters['remove_tag'] = remove_tag

	template = env.from_string(template_data)
	args = yaml.load(profile_data)

	with open('./index.html', 'w') as f:
		content = template.render(data=args,ceil=math.ceil,len=len)
		f.write(content.encode('utf8'))

if __name__ == '__main__':
	main()