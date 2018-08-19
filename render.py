#!/usr/bin/env python


def main():
	with open('templates/profile.yml','r') as f:
		data = f.read()
	with open('templates/template.html', 'r') as f:
		tmpl = f.read().decode('utf8')

		