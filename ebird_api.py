
from ebird.api import get_taxonomy, get_taxonomy_forms, get_taxonomy_versions
from tokens import get_creds
import json
import random

def get_bird_name():
	creds = get_creds()
	taxonomy = get_taxonomy(creds['api_key'])
	prev_name = ''
	bird_list = []

	for bird in taxonomy:
		name = ''
		try:
			name = bird['familyComName']
			try:
				name = name.split(' ')[-1]
			except:
				pass
			try:
				name = name.split('-')[-1]
			except:
				pass
			try:
				name = name.split(',')[-1]
			except:
				pass
			if name[-1] == 's':
				name = name[:-1]
			if prev_name != name:
				prev_name = name
				bird_list.append(name)
		except:
			pass

	n = random.randint(0,len(bird_list) -1)
	return bird_list[n]

