# -*- coding: utf-8 -*-
#https://www.facebook.com/groups/vietkodi/

import re
import urlfetch
import os
from time import sleep
from addon import notify, alert, ADDON
import simplejson as json
import random
import xbmc
from config import VIETMEDIA_HOST
import urllib




USER_VIP_CODE = ADDON.getSetting('user_vip_code')

def fetch_data(url, headers=None, data=None):
  	if headers is None:

  		headers = { 
    				'User-agent'	: 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0',
                	'Referer'		: 'http://www.google.com',
                	'X-User-VIP'    :  USER_VIP_CODE
            }
  	try:

  		if data:
  			response = urlfetch.post(url, headers=headers, data=data)
  		else:
			response = urlfetch.get(url, headers=headers)

		return response

	except Exception as e:
  		print e
  		pass


def get(url):
	if '//fptplay.net' in url:
		return get_fptplay(url)
	if 'www.fshare.vn' in url:
		return get_fshare(url)
	if '//4share.vn' in url:
		return get_4share(url)
	if 'hdonline.vn' in url:
		return get_hdonline(url)
	if '//vtvgo.vn' in url:
		return get_vtvgo(url)
	if '//htvonline.com.vn' in url:
		return get_htvonline(url)
	if '//hplus.com.vn' in url:
		return get_htvplus(url)
	if '//xuongphim.tv' in url:
		return get_xuongphim(url)
	if '//phim3s.net' in url:
		return get_phim3s(url)
	if 'tvnet.gov.vn' in url:
		return getTvnet(url)
	if '//kenh1.mobifone.com.vn' in url:
		return get_mobifone(url)
	if '//thvl.vn' in url:
		return get_thvl(url)
	if 'link.tvmienphi.biz' in url:
		return get_tvmienphi(url)
	if 'serverthunghiem' in url:
		return get_serverthunghiem(url)
	if 'web.tv24.vn' in url:
		return get_servertv24(url)
	if 'acestream' in url:
		return getAcestream(url)
	if 'sop:' in url:
		return getSopcast(url)
	if 'vtv.vn' in url:
		return getVtv(url)	
	if 'dzone.vn' in url:
		return getDzone(url)
	if 'clip.vn' in url:
		return getClipvn(url)
	else:
		return url

def get_hdonline(url):
	attempt = 1
	MAX_ATTEMPTS = 5
	
	while attempt < MAX_ATTEMPTS:
		if attempt > 1: 
			sleep(2)
		url_play = ''
		notify (u'Lấy link lần thứ #%s'.encode("utf-8") % attempt)
		attempt += 1
		headers = { 
				'User-Agent' 	: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
				'Referer'		: 'http://hdonline.vn'
			}
		response = fetch_data(url, headers)
		if not response:
			return ''

		cookie = response.cookiestring

		match = re.search(r'eval\(function\((.*?)split\(\'\|\'\),0,\{\}\)\)', response.body)
		if match:
			eval_js = 'eval(function(' + match.group(1) + 'split(\'|\'),0,{}))'
			
			response = fetch_data('http://vietmediaf.net:4000/api/v1/decode/hdo', None, {'data': eval_js})

			json_data = json.loads(response.body)
			_x = random.random()
			url_play = ('http://hdonline.vn%s&format=json&_x=%s' % (json_data['playlist'][0]['file'], _x))
			
			#tim ep
			
			match = re.search(r'\-tap-(\d+)-[\d.]+?\.html$', url)
			if match:
				ep = match.group(1)
				url_play = url_play.replace('ep=1','ep='+ep)
			
			break
		else:
			match = re.search(r'\-tap-(\d+)-[\d.]+?\.html$', url)
			if not match:
				ep = 1
			else:
				ep = match.group(1)
			match = re.search(r'"file":"(.*?)","', response.body)
			if match:
				url_play = 'http://hdonline.vn' + match.group(1).replace('\/','/') + '&format=json'
				url_play = url_play.replace('ep=1','ep=' + str(ep))
				break
	if len(url_play) == 0:
		notify (u'Không lấy được link.')
		return ''

	headers = { 
				'User-Agent' 	: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
				'Referer'		: 'http://hdonline.vn',
				'Accept'		: 'json',
				'Cookie'		: cookie
			}
	
	
	response = fetch_data(url_play, headers)

	json_data = json.loads(response.body)
	video_url = json_data['file']
	if json_data.get('level') and len(json_data['level']) > 0:
		video_url = json_data['level'][len(json_data['level']) - 1]['file']

	subtitle_url = ''
	if json_data.get('subtitle') and len(json_data['subtitle']) > 0:
		for subtitle in json_data['subtitle']:
			subtitle_url = subtitle['file']
			if subtitle['code'] == 'vi':
				subtitle_url = subtitle['file']
				break
	
	if len(subtitle_url) > 0:		
		subtitle_url = ('http://data.hdonline.vn/api/vsub.php?url=%s' % subtitle_url)
		return video_url + "[]" + subtitle_url
	else:
		return video_url

	xbmc.log(video_url)
		
def getClipvn(url):
	response = urlfetch.fetch(url)
	regex = r'file\":\"(http.*?m3u8)'
	matches = re.search(regex, response.body)
	video_url = matches.group(1)
	video_url = video_url.replace('\/\/', '//')
	video_url = video_url.replace('\/', '/')
	return(video_url)
	
def getDzone(url):
	
	#Tim ID cua film
	regex = r"http.*?/(\d+)"
	matches = re.search(regex, url)
	idurl = matches.group(1)
	print (idurl)
	response = urlfetch.get(url)
	cookie=response.cookiestring;

	headers = { 
					'Host'				: 'service.tivi.dzone.vn',
					'User-Agent'		: 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
					'Cookie'			: cookie,
					'Referer'			: url,
					'Origin'			: 'http://dzone.vn'
				}
	asset_optn = {'type': 'media'}
	data = {'asset_optns': asset_optn, 'id': idurl}
	data = json.dumps(data)

	response = urlfetch.post('http://service.tivi.dzone.vn/api/v1/assets/'+idurl, data = data, headers =headers)
	json_data = json.loads(response.body)
	info = json_data['asset_result']['result']
	info = info['mediaFiles'][0]['url']
	return info

def getVtv(url)	:
	channelname1 = re.search(r"tuyen\/(.*?).htm", url).group(1)
	response = urlfetch.get(url)
	cookie=response.cookiestring;
	channelid1 = re.search(re.compile(r"disableLiveTv.init\((\d+),"), response.body).group(1)

	urlcheck = 'http://vtvapi.vcmedia.vn/handlers/checkdisablelivetv.ashx?channelId='+channelid1+'&channelName=' + channelname1
	headers = {'Host': 'vtvapi.vcmedia.vn',  'Origin': 'http://vtv.vn', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Referer': url}
	data = {'channelId': channelid1, 'channelName': channelname1}

	response = urlfetch.get(urlcheck, headers=headers)
	linkplay = re.search(r'src=\"(.*?)"', json.loads(response.body)['Content']).group(1)
	headers = {'Host': 'play.sohatv.vn', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Referer': url}
	response = urlfetch.get(linkplay, headers=headers)
	video_url = re.search(r"src=\"(.*?m3u8)", response.body).group(1)
	result = 'http://'+re.search(r"live=(.*)", urllib.unquote_plus(video_url)).group(1)
	return result
	
def getTvnet(url):
	response = urlfetch.get(url)
	cookie=response.cookiestring;
	regex = r"data-file=\"(.*?)\""
	match = re.search(regex, response.body)
	playerurl = match.group(1)
	playerurl = playerurl.replace('amp;', '')
	response = urlfetch.get(playerurl)
	json_data = json.loads(response.body)
	video_url = json_data[0]['url']	
	return video_url
	xbmc.log(video_url)
		
def getAcestream(url):
	if 'plugin:' in url:
		ace_link = url
	else:
		ace_link = 'plugin://program.plexus/?mode=1&url='+url+'&name=Video'
	return ace_link

def getSopcast(url):
	if 'plugin:' in url:
		sopcast_link = url
	else:
		sopcast_link = 'plugin://program.plexus/?mode=2&url='+url+'&name=Video'
	return sopcast_link
		
def get_fptplay(url):
	
	user = ADDON.getSetting('fptplay_user')
	password = ADDON.getSetting('fptplay_pass')
	country_code = ADDON.getSetting('country_code')
	matches = re.search(r"(.+)\s", country_code)
	country_code = matches.group(1)
	
	url_login = 'https://fptplay.net/user/login'

	r = urlfetch.get('https://fptplay.net')
	cookie = r.cookiestring;
	params = {'country_code': country_code, 'phone': user, 'password': password, 'submit': ''}
	headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','Referer':'https://fptplay.net/', 'cookie': cookie}
	
	r = urlfetch.post(url_login, headers=headers, data=params)
	
	headers = { 
				'Referer'			: url,
				'X-KEY'				: '123456',
	   			'X-Requested-With'	: 'XMLHttpRequest',
				'cookie'			: r.cookiestring
            }
	
	#Kiểm tra live tivi 
	match = re.search(r'\/livetv\/(.*)$', url)
	if match:
		channel_id = match.group(1)
		data = {
	  		'id' 	   : channel_id,
	  		'type'     : 'newchannel',
	  		'quality'  : 3,
	  		'mobile'   : 'web'
	    }
		r = urlfetch.post('https://fptplay.net/show/getlinklivetv', headers=headers, data=data)
		
		return json.loads(r.content)['stream']+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0&Referer=https://fptplay.net/livetv/'
			
	match = re.search(r'\-([\w]+)\.html', url)
	if not match:
		return

	movie_id = match.group(1)
	match = re.search(r'#tap-([\d]+)$', url)
	
	if match:
		episode_id = match.group(1)
	else:
		episode_id = 1

	data = {
  		'id' 	   : movie_id,
  		'type'     : 'newchannel',
  		'quality'  : 3,
  		'episode'  : episode_id,
  		'mobile'   : 'web',
    }

	r = urlfetch.post('https://fptplay.net/show/getlink', headers=headers, data=data)
	
	
	json_data = json.loads(r.content)
	return json_data['stream']+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0&Referer=https://fptplay.net/livetv/'
		
	

def get_vtvgo(url):
	response = urlfetch.get(url)
	cookie=response.cookiestring;
	match = re.search(re.compile(r"(xem-video)"), url)

	if not match:
		
		epgid = re.search(re.compile(ur'vtv\d-(.*?)\.'), url).group(1)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Cookie': cookie, 'Referer': url, 'X-Requested-With'  : 'XMLHttpRequest'}  
		data = {'epg_id': epgid, 'type':'1'}
		response = urlfetch.get('http://vtvgo.vn//get-program-channel?epg_id=' +epgid +'&type=1', headers=headers, data=data)
		json_data = json.loads(response.body)
		video_url = json_data['data']
		
	else:
		video_url = re.search(re.compile(r"addPlayer\('(.*?)'"), response.body).group(1)
	return video_url

def get_htvonline(url):
	response = fetch_data(url)
	cookie=response.cookiestring;
	if not response:
		return ''
	match = re.search(re.compile(r'data-source=\"(.*?)\"'), response.body)
	if not match:
		return ''
	video_url = match.group(1)
	xbmc.log(video_url)
	return video_url	

def get_servertv24(url):
	response = urlfetch.get('http://web.tv24.vn/')
	cookie=response.cookiestring;
	channelid = re.search(re.compile(r"\/(\d+)\/"), url).group(1)
	headers = {'Host': 'web.tv24.vn', 'Accept-Encoding': 'gzip, deflate, compress, identity, *', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Cookie': cookie, 'Referer': 'http://web.tv24.vn/dang-nhap'}
	data = {'mobile': '0907280386', 'password': '123456'}
	urlfetch.post('http://web.tv24.vn/client/login/process', headers=headers, data=data)
	data = {'channel_id': channelid}
	response = urlfetch.post('http://web.tv24.vn/client/channel/link', headers=headers, data=data)
	json_data = json.loads(response.body)
	video_url = json_data['data']['PLAY_URL']
	return video_url
	
	
def get_thvl(url):
	cookie = urlfetch.get('http://thvl.vn/').cookiestring;
	headers = {'Host': 'thvl.vn', 'Accept-Encoding': 'gzip, deflate, compress, identity, *', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Cookie': cookie, 'Referer': 'http://thvl.vn/jwplayer/?l=rtmp&i=http://thvl.vn/wp-content/uploads/2014/12/THVL1Online.jpg&w=640&h=360&a=0', 'X-Requested-With'	: 'XMLHttpRequest'}
	data = {'l': 'rtmp', 'i': 'http://thvl.vn/wp-content/uploads/2014/12/THVL1Online.jpg', 'w': '640', 'h': '360', 'a': '1'}
	response = urlfetch.get(url, data=data, headers=headers)
	return re.search(r'file:\s"(.*?)"', response.body).group(1)

def get_tvmienphi(url):
	cookie = urlfetch.get('http://www.tvmienphi.biz').cookiestring;
	headers = {'Host': 'link.tvmienphi.biz', 'Accept-Encoding': 'gzip, deflate, compress, identity, *', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Cookie': cookie, 'Referer': 'http://mi.tvmienphi.biz/'}
	return re.search(r'channel_stream\s=\s\"(.*?)\"', urlfetch.get(url, headers=headers).body).group(1)

def get_serverthunghiem(url):
	return re.search(r'data-file="(.*?)"', urlfetch.get(re.search(r'=(.*)', url).group(1)).body).group(1)
	
def get_xuongphim(url):
	response = urlfetch.get(url)
	#cookie=response.cookiestring;
	match = re.search(re.compile(ur'file:\s"(.*?)"'), response.body)
	video_url = match.group(1)
	match = re.search(re.compile(r'file:\s\"(\/sub.*?)\"'), response.body)
	if match:
		phude = '|http://xuongphim.tv/'+match.group(1)
	else:
		phude = ''
	return video_url+phude	

def get_phim3s(url):
	match = re.search(re.compile(r'\/(xem-phim\/)'), url)
	if match:
		url = url
	else:
		url = url +'xem-phim/'
	

	response = urlfetch.get(url)
	cookie = response.cookiestring;

	if 'phim-bo' in url:
			match = re.search(re.compile(r'\/(\d+)'), response.body)
			espisodeid = match.group(1)
	else:
			match = re.search(re.compile(r'data-id="(.*?)"'), response.body)
			espisodeid = match.group(1)
	print (espisodeid)
	match = re.search(re.compile(r'data-film-id="(.*?)"'), response.body)
	filmid = match.group(1)
	#print (filmid)
	import time
	ti = (int(time.time()*1000))
	data = {'espisode_id': espisodeid, '_': ti,}
	headers = { 
					'User-Agent'		: 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
					'Cookie'			: cookie,
					'Referer'			: url,
					'X-Requested-With'	: 'XMLHttpRequest'
								   }
	film_url = 'http://phim3s.net/ajax/episode/embed/?episode_id=' +espisodeid
	response = urlfetch.get(film_url, data=data, headers=headers)
	json_data = json.loads(response.body)
	google_url = json_data['video_url_hash']
	encode_url = 'http://sub2.phim3s.net/v3/?link=' +google_url+'&json=1&s=44'
	data = {'link': google_url, 'json': '1', 's': '44'}
	response = urlfetch.get(encode_url, data=data, headers=headers)
	json_data = json.loads(response.body)
	video_url = json_data[0]['file']
	return video_url
	


	
def get_mobifone(url):
	video_url = re.search(r'file:\s\"(.*?)\"', fetch_data(url).body).group(1)
	return video_url

def get_htvplus(url):
	response = urlfetch.get(url)
	if not response:
		return ''
	match = re.search(re.compile(r'iosUrl\s=\s\"(.*?)\"'), response.body)
	linklive = match.group(1)
	xbmc.log(linklive)
	cookie=response.cookiestring;
	headers = { 
				'User-Agent'		: 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
				'Cookie'			: cookie,
				'Referer'			: url,
    			'X-Requested-With'	: 'XMLHttpRequest'
				
            }
	data={'url':linklive,'type':'1'}
	response = urlfetch.post('http://hplus.com.vn/content/getlinkvideo/',data=data, headers=headers)
	if not response:
		return ''
	video_url = response.content
	#referer = urlfetch.get('http://hplus.com.vn/themes/front/player/jwplayer.flash.swf')
	
	return video_url+'|User-Agent%3DMozilla%2F5.0+%28Windows+NT+10.0%3B+WOW64%3B+rv%3A49.0%29+Gecko%2F20100101+Firefox%2F49.0%26Referer%3Dhttp%3A%2F%2Fhplus.com.vn%2Fthemes%2Ffront%2Fplayer%2Fjwplayer.flash.swf'	
		

	
		
def get_hash(m):
	md5 = m or 9
	s = ''
	code = 'LinksVIP.Net2014eCrVtByNgMfSvDhFjGiHoJpKlLiEuRyTtYtUbInOj9u4y81r5o26q4a0v'
	for x in range(0, md5):
		s = s + code[random.randint(0,len(code)-1)] 
    
	return s
def get_linkvips(fshare_url,username, password):
	host_url = 'http://linksvip.net'
	login_url = 'http://linksvip.net/login/'
	logout_url = 'http://linksvip.net/login/logout.php'
	getlink_url = 'http://linksvip.net/GetLinkFs'
	
	response = fetch_data(host_url)
	if not response:
		return
	
	cookie = response.cookiestring

	headers = { 
				'User-Agent' 	: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
				'Cookie'		: cookie,
				'Referer'		: host_url,
				'Content-Type'	: 'application/x-www-form-urlencoded; charset=UTF-8',
				'Accept'		: 'application/json, text/javascript, */*; q=0.01',
				'X-Requested-With'	: 'XMLHttpRequest'
            }
	
	data = {
			"u"				: username,
			"p"				: password,
			"auto_login"	: 'checked'
		}

	response = fetch_data(login_url, headers, data)

	video_url = ''
	if response.status == 200:
		json_data = json.loads(response.body)
		if int(json_data['status']) == 1:
			cookie = cookie + ';' + response.cookiestring
			headers['Cookie'] = cookie
			data = {
				"link"			: fshare_url,
				"pass"			: 'undefined',
				"hash"			: get_hash(32),
				"captcha"		: ''

			}
			headers['Accept-Encoding'] = 'gzip, deflate'
			headers['Accept-Language'] = 'en-US,en;q=0.8,vi;q=0.6'
			
			response = fetch_data(getlink_url, headers, data)

			json_data = json.loads(response.body)

			link_vip = json_data['linkvip']
			
			response = fetch_data(link_vip, headers)

			match = re.search(r'id="linkvip"\stype="text"\svalue="(.*?)"', response.body)
			if not match:
				return ''
			video_url = match.group(1)
			video_url = video_url.replace("[LinksVIP.Net]", "")
			xbmc.log(video_url)
			#logout
			response = fetch_data(logout_url, headers)
			
	return video_url

def get_4share(url):
	
	username = ADDON.getSetting('4share_username')
	password = ADDON.getSetting('4share_password')

	direct_url = ''
	url_account = VIETMEDIA_HOST + '?action=fshare_account_linkvips'
	response = fetch_data(url_account)
	json_data = json.loads(response.body)
	username = json_data['username']
	password = json_data['password']

	if len(username) > 0  and len(password) > 0:
		direct_url = get_linkvips(url, username,password)
		if len(direct_url) > 0:
			notify(u'Lấy link 4share VIP thành công.'.encode("utf-8"))
			return direct_url
	if len(direct_url) == 0:
		alert(u'Không lấy được link 4share.'.encode("utf-8"))
	return direct_url

def get_fshare(url):
	login_url = 'https://www.fshare.vn/login'
	logout_url = 'https://www.fshare.vn/logout'
	download_url = 'https://www.fshare.vn/download/get'

	username = ADDON.getSetting('fshare_username')
	password = ADDON.getSetting('fshare_password')
	
	match = re.search(r"(https://)", url)
	if not match:
		url = 'https://'+url
	else:
		url = url
	
	
	direct_url = ''
	if len(username) == 0  or len(password) == 0:
		try:
			url_account = VIETMEDIA_HOST + '?action=fshare_account_linkvips'
			response = fetch_data(url_account)
			json_data = json.loads(response.body)
			username = json_data['username']
			password = json_data['password']

			if len(username) > 0  and len(password) > 0:
				direct_url = get_linkvips(url, username,password)
				if len(direct_url) > 0:
					notify(u'Lấy link fshare VIP thành công.'.encode("utf-8"))
					return direct_url
		except:
			pass

	if len(username) == 0  or len(password) == 0:
		alert(u'Bạn chưa có TK VIP Fshare hoặc chưa có VMF CODE hoặc CODE hết hạn. Mời Cafe tác giả đi bạn. Soạn tin: VMF gửi 8698 hoặc Paypal to vietkodi@gmail.com. Sau khi nhập đợi 10 phút hệ thống update lại.'.encode("utf-8"))
		return

	response = fetch_data(login_url)
	if not response:
		return

	csrf_pattern = '\svalue="(.+?)".*name="fs_csrf"'

	csrf=re.search(csrf_pattern, response.body)
	fs_csrf = csrf.group(1)

	headers = { 
				'User-Agent' 	: 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0',
				'Cookie'		: response.cookiestring
            }
	
	data = {
			"LoginForm[email]"		: username,
			"LoginForm[password]"	: password,
			"fs_csrf"				: fs_csrf
		}

	response = fetch_data(login_url, headers, data)
	headers['Cookie'] = response.cookiestring
	headers['Referer'] = url
	
	attempt = 1
	MAX_ATTEMPTS = 8
	file_id = os.path.basename(url)
	if response and response.status == 302:
		notify (u'Đăng nhập fshare thành công'.encode("utf-8"))
		while attempt < MAX_ATTEMPTS:
			if attempt > 1: sleep(2)
			notify (u'Lấy link lần thứ #%s'.encode("utf-8") % attempt)
			attempt += 1

			response = fetch_data(url, headers, data)

			if response.status == 200:
				csrf=re.search(csrf_pattern, response.body)
				fs_csrf = csrf.group(1)
				data = {
						'fs_csrf'					: fs_csrf,
						'ajax'						: 'download-form',
						'DownloadForm[linkcode]'	: file_id
					}
				
				response=fetch_data(download_url, headers, data);
				
				json_data = json.loads(response.body)
				
				if json_data.get('url'):
					direct_url = json_data['url']
					break
				elif json_data.get('msg'):
					notify(json_data['msg'].encode("utf-8"))
			elif response.status == 302:
				direct_url = response.headers['location']
				break
			else:
				notify (u'Lỗi khi lấy link, mã lỗi #%s. Đang thử lại...'.encode("utf-8") % response.status) 

		response = fetch_data(logout_url, headers)
		if response.status == 302:
			notify (u'Đăng xuất fshare thành công'.encode("utf-8"))
	else:
		notify (u'Đăng nhập không thành công, kiểm tra lại tài khoản'.encode("utf-8"))
	if len(direct_url) > 0:
		notify (u'Đã lấy được link'.encode("utf-8"))
	else:
		notify (u'Không được link, bạn vui lòng kiểm tra lại tài khoản'.encode("utf-8"))

	return direct_url
