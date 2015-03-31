from core.models import *
import requests, json
from django.core.management.base import BaseCommand, CommandError


def get_scrape():
	r = requests.get("https://www.kimonolabs.com/api/dkrbuxr4?apikey=2RDsgK4l1iZS8H71yc9GgF2gDFQvSZtm")
	r = r.json()
	for song in r['results']['collection1']:
		print song['title']
		s = Song(title =song['title'], tab = song['tab'], artist_name = song['artist'])
		s.save()

class Command(BaseCommand):
    help = ''

    # def add_arguments(self, parser):
    # 	parser.add_argument('poll_id', nargs='+', type=int)
    def handle(self, *args, **options):
    	# login_test()
    	# select_goal_test()
    	#getTotalTimeTest('bb@bb.com')
    	
    	get_scrape()











