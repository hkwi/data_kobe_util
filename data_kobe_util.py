# coding: UTF-8
#
# For data.city.kobe.lg.jp release
#
from __future__ import print_function
import json
import re
import os.path
import xml.etree.ElementTree as ET
import lxml.html
import requests
import functools
try:
	from urllib import urlopen
except:
	from urllib.request import urlopen

def dataset():
	dataset = []
	atom_url = "https://data.city.kobe.lg.jp/data/feeds/dataset.atom"
	NS = dict(f="http://www.w3.org/2005/Atom")
	while atom_url:
		doc = ET.parse(urlopen(atom_url))
		for e in doc.findall(".//f:entry", NS):
			data = urlopen(e.find('f:link[@rel="enclosure"]', NS).get("href")).read()
			ds = json.loads(data.decode("UTF-8"))
			dataset.append(ds)
		
		nx = doc.find('.//f:link[@rel="next"]', NS)
		if nx is None:
			break
		else:
			atom_url = nx.get("href")
	return dataset

def hint():
	fn = "hint.json"
	if "__file__" in locals():
		fn = os.path.join(os.path.dirname(__file__), fn)
	with open(fn) as f:
		return json.load(f)

def published_urls():
	found = []
	warns = []
	for p in hint():
		if p.get("a") in ("Direct", "Html"):
			try:
				requests.head(p["url"])
				found.append(p["url"])
			except:
				warns.append(dict(message="resource access error %s" % p["url"]))
		elif p.get("a") == "Crawl":
			try:
				d = lxml.html.parse(p["index"])
			except:
				warns.append(dict(message="index page not access error %s" % p["index"]))
				continue
			
			r = d.getroot()
			r.make_links_absolute()
			for l in r.xpath("//a/@href"):
				if re.match(p["re"], l):
					found.append(l)
	return found, warns

def diff():
	ds = dataset()
	indexed = functools.reduce(lambda x,y:x+y,
		[[r["url"] for r in d["resources"]] for d in ds])
	published, warns = published_urls()
	for url in set(indexed) - set(published):
		# unpublished
		hit = False
		for d in ds:
			for r in d["resources"]:
				if url == r["url"]:
					warns.append(dict(message="not on HP %s" % url,
						dataset=d))
					hit = True
		if not hit:
			warns.append("something went wrong %s" % url)
	for url in set(published) - set(indexed):
		# unindexed
		warns.append(dict(message="new resource %s" % url))
	
	return warns
