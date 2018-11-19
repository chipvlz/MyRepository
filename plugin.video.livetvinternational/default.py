#!/usr/bin/python
#coding=utf-8
import xbmc,xbmcaddon,xbmcplugin,xbmcgui,sys,urllib,urllib2,re,os,codecs,unicodedata,base64
import simplejson as json

addonID = 'plugin.video.livetvinternational'
addon = xbmcaddon.Addon(addonID)
pluginhandle = int(sys.argv[1])
home = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path') ).decode("utf-8")
logos = xbmc.translatePath(os.path.join(home,"logos\\"))
dataPath = xbmc.translatePath(os.path.join(home, 'resources'))
apk = xbmc . getCondVisibility ( 'system.platform.android' )
O00O0OOO00 = 'YzNCbFkybGhiRG92TDJodmJXVXZZV1JrYjI1ekwzQnNkV2RwYmk1MmFXUmxieTVrYjJOMWFIVmk='
O00O0OO000 = 'L3Jlc291cmNlcy9wbGF5bGlzdHMvc291cmNlZmlsZV9pbnRlcm5hdGlvbmFsLnhtbA=='



def TVChannel(url):
    xmlcontent = GetUrl(url)
    names = re.compile('<name>(.+?)</name>').findall(xmlcontent)
    if len(names) == 1:
        items = re.compile('<item>(.+?)</item>').findall(xmlcontent)
        for item in items:
            thumb=""
            title=""
            link=""
            if "/title" in item:
                title = re.compile('<title>(.+?)</title>').findall(item)[0]
            if "/link" in item:
                link = re.compile('<link>(.+?)</link>').findall(item)[0]            
            if "/thumbnail" in item:
                thumb = re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            if "redirecttopakindia" in link:                   
                link = re.compile('<link>(.+?)</link>').findall(item)[0] #required but not mean anything
            if "redirecttoshahidmbc" in link:                   
                link = re.compile('<link>(.+?)</link>').findall(item)[0] #required but not mean anything
            if ("redirecttoyoutube" in link) or ("redirecttodailymotion" in link):                   
                link = re.compile('<link>(.+?)</link>').findall(item)[0] #required but not mean anything
            if ("tosportsdevil" in link) or ("tovdubt" in link):                   
                link = re.compile('<link>(.+?)</link>').findall(item)[0]
            if ("redirecttomovieshd" in link) or ("toyeuphim" in link) or ("redirecttonetmovie" in link) or \
               ("redirectto1channel" in link) or ("redirecttokenh108" in link) or ("redirecttokenh88" in link) or \
               ("redirecttomoviebox" in link) or ("redirecttophimvang" in link) or ("redirecttoxomgiaitri" in link) or \
               ("redirecttoxixam" in link) or ("redirecttovkool" in link) or ("tomovienight" in link) or ("toyify" in link) or \
               ("tomovieshd2" in link) or ("tocartoons8" in link) or ("tokiddiecartoons" in link) or ("tonavix" in link) or \
               ("toxmovies8" in link) or ("togenesis" in link) or ("tophoenix" in link) or ("toanhtrang" in link) or \
               ("tophim14" in link) or ("tofootball" in link) or ("toxemphimso" in link) or ("toenter" in link) or \
               ("toitv" in link) or ("tofilmon1" in link) or ("tofilmon2" in link) or ("toirantv" in link) or ("tozeus" in link) or \
               ("tomoneysp" in link) or ("tophim60s" in link) or ("tophim3s" in link) or ("toukturk" in link) or ("tocablestv" in link) or \
               ("tonbafull" in link) or ("tokhmertv" in link) or ("tohotkhmer" in link) or ("tomoviekhmer" in link) or \
               ("tokhmera" in link) or ("tovideo4kh" in link) or ("tophumikh" in link) or ("tocartoonhd" in link) or ("toazdrama" in link) or \
               ("todrama24" in link) or ("todramago" in link) or ("tocartoongo" in link) or ("tosominaltv" in link) or \
               ("tomovieru" in link) or ("toanimego" in link) or ("toccloud" in link) or ("toadryanlist" in link) or ("tomuttsnuts" in link) or \
               ("tonbareplays" in link) or ("tomdgenvideos" in link) or ("tocastaway" in link) or ("toexodus" in link) or \
               ("tomdvodlocker" in link) or ("tomdhdmovie14" in link) or ("tomd123movies" in link) or ("tomdwatch32hd" in link) or ("toespn3" in link) or ("tozemtv" in link) or \
               ("toyoutubeft" in link)  or ("toprosport" in link) or ("toxshare" in link) or ("tophimmoi" in link) or ("tom4u" in link) or ("tomovievault" in link) or ("tomoviepool" in link) or \
               ("tomdafdah" in link) or ("tomdhdbox" in link) or ("tomdpubfilm" in link) or ("tomdscenepeeper" in link) or ("tomdluckytv" in link) or ("topac12" in link) or \
               ("tomic" in link) or ("tohappymovies" in link) or ("tosureshot" in link) or ("tomdyesmovies" in link) or ("toicefilms" in link) or \
               ("tozen" in link) or ("tometalliq" in link) or ("tobob1" in link) or ("tokodi4vnlauncher" in link) or ("tobennu" in link) or ("tobobunleashed" in link) or ("tofilmon3" in link) or \
               ("tohieuhientt" in link) or ("tophimhot" in link) or ("tomovies1" in link) or ("tofantastic" in link) or ("tocovenant" in link) or ("tomobdro" in link)  or ("toplanetmma" in link) or \
               ("tofirefox" in link) or ("tosilk" in link) or ("tostreamhub" in link) or ("tosport365" in link) or ("tosupremacysports" in link) or ("tomegakhmer" in link) or ("toicdrama" in link):
                link = re.compile('<link>(.+?)</link>').findall(item)[0]              
            add_Link(title, link, thumb)
        xbmc.executebuiltin('Container.SetViewMode(52)')        
    else:
        for name in names:
            addDir('' + name + '', url+"?n="+name, 'index', '')
        xbmc.executebuiltin('Container.SetViewMode(52)')

		

		
def Channel():
    content = iI11IIiiIII(iI11IIiiiII)
    match=re.compile("<title>([^<]*)<\/title>\s*<link>([^<]+)<\/link>\s*<thumbnail>(.+?)</thumbnail>").findall(content)	
    for title,url,thumbnail in match:
		addDir(title,url,'tvchannel',thumbnail)	
    xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)


def iI11IIiiIII(file):
    try:
        f = open(file, 'r')
        content = f.read()
        f.close()
        return content  
    except:
        pass

def resolveUrl(url):
	if 'xemphimso' in url:
		content = Get_Url(url)	
		url = urllib.unquote_plus(re.compile("file=(.+?)&").findall(content)[0])
	elif 'vtvplay' in url:
		content = Get_Url(url)
		url = content.replace("\"", "")
		url = url[:-5]
	elif 'vtvplus' in url:
		content = Get_Url(url)
		url = re.compile('var responseText = "(.+?)";').findall(content)[0]		
	elif 'htvonline' in url:
		content = Get_Url(url)	
		url = re.compile('data\-source=\"([^\"]*)\"').findall(content)[0]
	elif 'hplus' in url:
		content = Get_Url(url)	
		url = re.compile('iosUrl = "(.+?)";').findall(content)[0]		
	else:
		url = url
	item=xbmcgui.ListItem(path=url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)	  
	return		
	


def Get_M3U(url,iconimage):
  m3ucontent = Get_Url(url)
  match = re.compile('#EXTINF:-?\d,(.+?)\n(.+)').findall(m3ucontent)
  for name,url in match:
	  add_Link(name.replace('TVSHOW - ','').replace('MUSIC - ',''),url,iconimage)
	  
def Index(url,iconimage):
    byname = url.split("?n=")[1]
    url = url.split("?")[0]
    xmlcontent = GetUrl(url)
    channels = re.compile('<channel>(.+?)</channel>').findall(xmlcontent)
    for channel in channels:
        if byname in channel:
            items = re.compile('<item>(.+?)</item>').findall(channel)
            for item in items:
                thumb=""
                title=""
                link=""
                if "/title" in item:
                    title = re.compile('<title>(.+?)</title>').findall(item)[0]
                if "/link" in item:
                    link = re.compile('<link>(.+?)</link>').findall(item)[0]
                if "/thumbnail" in item:
                    thumb = re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                if "youtube" in link:                   
                    addDir(title, link, 'episodes', thumb)
                #old version if ("youtube" in link) or ("redirecttomovieshd" in link) or ("redirecttonetmovie" in link) or \
                   #("redirectto1channel" in link) or ("redirecttokenh108" in link) or ("redirecttokenh88" in link) or \
                   #("redirecttomoviebox" in link) or ("redirecttophimvang" in link) or ("redirecttoxomgiaitri" in link) or \
                   #("redirecttoxixam" in link) or ("redirecttovkool" in link):                   
                    #addDir(title, link, 'episodes', thumb)
                else:                   
                    addLink('' + title + '', link, 'play', thumb)
    skin_used = xbmc.getSkinDir()
    if skin_used == 'skin.xeebo':
        xbmc.executebuiltin('Container.SetViewMode(50)')
		
def IndexGroup(url):
    xmlcontent = GetUrl(url)
    names = re.compile('<name>(.+?)</name>').findall(xmlcontent)
    if len(names) == 1:
        items = re.compile('<item>(.+?)</item>').findall(xmlcontent)
        for item in items:
            thumb=""
            title=""
            link=""
            if "/title" in item:
                title = re.compile('<title>(.+?)</title>').findall(item)[0]
            if "/link" in item:
                link = re.compile('<link>(.+?)</link>').findall(item)[0]
            if "/thumbnail" in item:
                thumb = re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            add_Link(title, link, thumb)
        skin_used = xbmc.getSkinDir()
        if skin_used == 'skin.xeebo':
            xbmc.executebuiltin('Container.SetViewMode(52)')
        else:
            xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)			
    else:
        for name in names:
            addDir('' + name + '', url+"?n="+name, 'index', '')

def Index_Group(url):
	xmlcontent = GetUrl(url)
	names = re.compile('<name>(.+?)</name>\s*<thumbnail>(.+?)</thumbnail>').findall(xmlcontent)
	if len(names) == 1:
		items = re.compile('<item>(.+?)</item>').findall(xmlcontent)
		for item in items:
			thumb=""
			title=""
			link=""
			if "/title" in item:
				title = re.compile('<title>(.+?)</title>').findall(item)[0]
			if "/link" in item:
				link = re.compile('<link>(.+?)</link>').findall(item)[0]
			if "/thumbnail" in item:
				thumb = re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
			addLink(title, link, 'play', thumb)
		skin_used = xbmc.getSkinDir()
		if skin_used == 'skin.xeebo':
				xbmc.executebuiltin('Container.SetViewMode(50)')
	else:
		for name,thumb in names:
			addDir(name, url+"?n="+name, 'index', thumb)

def menulist(homepath):
  try:
    mainmenu=open(homepath, 'r')  
    link=mainmenu.read()
    mainmenu.close()
    match=re.compile("<title>([^<]*)<\/title>\s*<link>([^<]+)<\/link>\s*<thumbnail>(.+?)</thumbnail>").findall(link)
    return match
  except:
    pass

	
def PlayVideo(url,title):
    
        title = urllib.unquote_plus(title)
        playlist = xbmc.PlayList(1)
        playlist.clear()
        listitem = xbmcgui.ListItem(title)
        listitem.setInfo('video', {'Title': title})
        xbmcPlayer = xbmc.Player()
        playlist.add(url, listitem)
        xbmcPlayer.play(playlist)

def Get_Url(url):
    try:
		req=urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)')
		response=urllib2.urlopen(req)
		link=response.read()
		response.close()  
		return link
    except:
		pass
    
def GetUrl(url):
    link = ""
    if os.path.exists(url)==True:
        link = open(url).read()
    else:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
    link = ''.join(link.splitlines()).replace('\'','"')
    link = link.replace('\n','')
    link = link.replace('\t','')
    link = re.sub('  +',' ',link)
    link = link.replace('> <','><')
    return link
	
def add_Link(name,url,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=stream"+"&iconimage="+urllib.quote_plus(iconimage)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setProperty('IsPlayable', 'true')
    if 'redirecttopakindia' in url:
        u = 'plugin://plugin.video.pakindia'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttoshahidmbc' in url:
        u = 'plugin://plugin.video.shahidmbcnet'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttoyoutube' in url:
        u = 'plugin://plugin.video.youtube'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttodailymotion' in url:
        u = 'plugin://plugin.video.dailymotion_com'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tosportsdevil' in url:
        u = 'plugin://plugin.video.SportsDevil'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tovdubt' in url:
        u = 'plugin://plugin.video.vdubt'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttomovieshd' in url:
        u = 'plugin://plugin.video.giaitritv'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toxmovies8' in url:
        u = 'plugin://plugin.video.xmovies8'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'togenesis' in url:
        u = 'plugin://plugin.video.genesis'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomovieshd2' in url:
        u = 'plugin://plugin.video.movieshd'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok        
    if 'toyify' in url:
        u = 'plugin://plugin.video.yifymovies.hd'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomovienight' in url:
        u = 'plugin://plugin.video.movienight'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tophoenix' in url:
        u = 'plugin://plugin.video.phstreams'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tocartoons8' in url:
        u = 'plugin://plugin.video.cartoons8'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tokiddiecartoons' in url:
        u = 'plugin://plugin.video.kiddiecartoons'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tonavix' in url:
        u = 'plugin://plugin.video.navi-x'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttonetmovie' in url:
        u = 'plugin://plugin.video.netmovie'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttonetmovie' in url:
        u = 'plugin://plugin.video.netmovie'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirectto1channel' in url:
        u = 'plugin://plugin.video.1channel'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttokenh108' in url:
        u = 'plugin://plugin.video.kenh108.com'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttokenh88' in url:
        u = 'plugin://plugin.video.kenh88'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttomoviebox' in url:
        u = 'plugin://plugin.video.moviebox'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttophimvang' in url:
        u = 'plugin://plugin.video.phimvang.org'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttoxomgiaitri' in url:
        u = 'plugin://plugin.video.xomgiaitri'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttoxixam' in url:
        u = 'plugin://plugin.video.phim.xixam.com'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttoxomgiaitri' in url:
        u = 'plugin://plugin.video.xomgiaitri'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttovkool' in url:
        u = 'plugin://plugin.video.vkool'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toyeuphim' in url:
        u = 'plugin://plugin.video.yeuphim1'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toanhtrang' in url:
        u = 'plugin://plugin.video.anhtrang.org'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tophim14' in url:
        u = 'plugin://plugin.video.phim14.net'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tofootball' in url:
        u = 'plugin://plugin.video.footballreplays'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toxemphimso' in url:
        u = 'plugin://plugin.video.xemphimso'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toenter' in url:
        u = 'plugin://plugin.video.allinone'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toitv' in url:
        u = 'plugin://plugin.video.itvplus'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tofilmon1' in url:
        u = 'plugin://plugin.video.F.T.V'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tofilmon2' in url:
        u = 'plugin://plugin.video.filmontv'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toirantv' in url:
        u = 'plugin://plugin.video.IRAN'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tozeus' in url:
        u = 'plugin://plugin.video.zeus'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomoneysp' in url:
        u = 'plugin://plugin.video.MoneySports'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tophim60s' in url:
        u = 'plugin://plugin.video.phim60s'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tophim3s' in url:
        u = 'plugin://plugin.video.phim3s'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toukturk' in url:
        u = 'plugin://plugin.video.ukturk'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tocablestv' in url:
        u = 'plugin://plugin.program.super.favourites'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tonbafull' in url:
        u = 'plugin://plugin.video.nbafullgames'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tokhmertv' in url:
        u = 'plugin://plugin.video.KhmerTv'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tohotkhmer' in url:
        u = 'plugin://plugin.video.hotkhmer'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomoviekhmer' in url:
        u = 'plugin://plugin.video.MovieKhmer'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tokhmera' in url:
        u = 'plugin://plugin.video.KhmerAvenue'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tovideo4kh' in url:
        u = 'plugin://plugin.video.video4Khmer'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tophumikh' in url:
        u = 'plugin://plugin.video.PhumiKhmer'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tocartoonhd' in url:
        u = 'plugin://plugin.video.cartoonhd'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toazdrama' in url:
        u = 'plugin://plugin.video.azdrama'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'todrama24' in url:
        u = 'plugin://plugin.video.drama24h'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'todramago' in url:
        u = 'plugin://plugin.video.dramago'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tocartoongo' in url:
        u = 'plugin://plugin.video.cartoongo'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tosominaltv' in url:
        u = 'plugin://plugin.video.sominaltv'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomovieru' in url:
        u = 'plugin://plugin.video.movierulz'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toanimego' in url:
        u = 'plugin://plugin.video.animego'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toccloud' in url:
        u = 'plugin://plugin.video.ccloudtv'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toadryanlist' in url:
        u = 'plugin://plugin.video.adryanlist'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomuttsnuts' in url:
        u = 'plugin://plugin.video.mutttsnutz'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tonbareplays' in url:
        u = 'plugin://plugin.video.nbareplays'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomdgenvideos' in url:
        u = 'plugin://plugin.video.mdgenvideos'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tocastaway' in url:
        u = 'plugin://plugin.video.castaway'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toexodus' in url:
        u = 'plugin://plugin.video.exodus'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomdvodlocker' in url:
        u = 'plugin://plugin.video.mdvodlocker'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomdhdmovie14' in url:
        u = 'plugin://plugin.video.mdhdmovie14'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomd123movies' in url:
        u = 'plugin://plugin.video.md123movies'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomdwatch32hd' in url:
        u = 'plugin://plugin.video.mdwatch32hd'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toespn3' in url:
        u = 'plugin://plugin.video.espn_3'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tozemtv' in url:
        u = 'plugin://plugin.video.ZemTV-shani'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toyoutubeft' in url and apk:
        u = xbmc . executebuiltin ( 'StartAndroidActivity ( org.chromium.youtube_apk )' )  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok
    if 'toprosport' in url:
        u = 'plugin://plugin.video.prosport'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toxshare' in url:
        u = 'plugin://plugin.video.xshare'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tophimmoi' in url:
        u = 'plugin://plugin.video.hkn.phimmoi'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tom4u' in url:
        u = 'plugin://plugin.video.mdm4u'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomovievault' in url:
        u = 'plugin://plugin.video.mdmovievault'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomoviepool' in url:
        u = 'plugin://plugin.video.mdmoviepool'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomdafdah' in url:
        u = 'plugin://plugin.video.mdafdah'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomdhdbox' in url:
        u = 'plugin://plugin.video.mdhdbox'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomdpubfilm' in url:
        u = 'plugin://plugin.video.mdpubfilm'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomdscenepeeper' in url:
        u = 'plugin://plugin.video.mdscenepeeper'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomdluckytv' in url:
        u = 'plugin://plugin.video.mdluckytv'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'topac12' in url:
        u = 'plugin://plugin.video.Pac-12'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomic' in url:
        u = 'plugin://plugin.video.mic'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tohappymovies' in url:
        u = 'plugin://plugin.video.happymovies'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tosureshot' in url:
        u = 'plugin://plugin.video.sureshot'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomdyesmovies' in url:
        u = 'plugin://plugin.video.mdyesmovies'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toicefilms' in url:
        u = 'plugin://plugin.video.icefilms'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tozen' in url:
        u = 'plugin://plugin.video.zen'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tometalliq' in url:
        u = 'plugin://plugin.video.metalliq'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tobob1' in url:
        u = 'plugin://plugin.video.bob'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tokodi4vnlauncher' in url:
        u = 'plugin://plugin.video.kodi4vn.launcher'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tobennu' in url:
        u = 'plugin://plugin.video.bennu'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tobobunleashed' in url:
        u = 'plugin://plugin.video.bob.unleashed'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tofilmon3' in url:
        u = 'plugin://plugin.video.filmon.simple'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tohieuhientt' in url:
        u = 'plugin://plugin.video.HieuHien.vn'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tophimhot' in url:
        u = 'plugin://plugin.video.accessasiatv'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomovies1' in url:
        u = 'plugin://plugin.video.movies1'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tofantastic' in url:
        u = 'plugin://plugin.video.fantastic'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tocovenant' in url:
        u = 'plugin://plugin.video.covenant'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomobdro' in url and apk:
        u = xbmc . executebuiltin ( 'StartAndroidActivity ( com.mobdro.android )' )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok
    if 'toplanetmma' in url:
        u = 'plugin://plugin.video.ufc-finest'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tofirefox' in url and apk:
        u = xbmc . executebuiltin ( 'StartAndroidActivity ( org.mozilla.tv.firefox )' )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok
    if 'tosilk' in url and apk:
        u = xbmc . executebuiltin ( 'StartAndroidActivity ( com.amazon.cloud9 )' )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok
    if 'tostreamhub' in url:
        u = 'plugin://plugin.video.streamhub'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tosport365' in url:
        u = 'plugin://plugin.video.sport365.live'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tosupremacysports' in url:
        u = 'plugin://plugin.video.Supremacy.Sports'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomegakhmer' in url:
        u = 'plugin://plugin.video.Mega_Khmer_Addon'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toicdrama' in url:
        u = 'plugin://plugin.video.icdrama'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)   

def addLink(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
    return ok
	
def addDir(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    '''old version
    if 'redirecttomovieshd' in url:
        u = 'plugin://plugin.video.giaitritv'
    if 'redirecttonetmovie' in url:
        u = 'plugin://plugin.video.netmovie'
    if 'redirectto1channel' in url:
        u = 'plugin://plugin.video.1channel'
    if 'redirecttokenh108' in url:
        u = 'plugin://plugin.video.kenh108.com'
    if 'redirecttokenh88' in url:
        u = 'plugin://plugin.video.kenh88'
    if 'redirecttomoviebox' in url:
        u = 'plugin://plugin.video.moviebox'
    if 'redirecttophimvang' in url:
        u = 'plugin://plugin.video.phimvang.org'
    if 'redirecttoxomgiaitri' in url:
        u = 'plugin://plugin.video.xomgiaitri'
    if 'redirecttoxixam' in url:
        u = 'plugin://plugin.video.phim.xixam.com'
    if 'redirecttoxomgiaitri' in url:
        u = 'plugin://plugin.video.xomgiaitri'
    if 'redirecttovkool' in url:
        u = 'plugin://plugin.video.vkool'
    '''
    if ('www.youtube.com/user/' in url) or ('www.youtube.com/channel/' in url):
        u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
        ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
        return ok   
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok	
	
def parameters_string_to_dict(parameters):
    ''' Convert parameters encoded in a URL to a dict. '''
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

OO0O0OO000 = base64.b64decode(O00O0OOO00)
iI11IIii11 = base64.b64decode(OO0O0OO000)
iI11IIiii1 = base64.b64decode(O00O0OO000)
iI11IIiiiII = xbmc.translatePath(os.path.join(iI11IIii11 + iI11IIiii1))
DecryptData = base64.b64decode	
homeurl = 'c3BlY2lhbDovL2hvbWUvYWRkb25zL3BsdWdpbi52aWRlby5naWFpdHJpdHYvc291cmNlZmlsZV9pbnRlcm5hdGlvbmFsLnhtbA=='
params=parameters_string_to_dict(sys.argv[2])
mode=params.get('mode')
url=params.get('url')
name=params.get('name')
iconimage=None

try:
  iconimage=urllib.unquote_plus(params["iconimage"])
except:
  pass

if type(url)==type(str()):
    url=urllib.unquote_plus(url)
sysarg=str(sys.argv[1])

if mode == 'tvchannel':TVChannel(url)
elif mode == 'index':Index(url,iconimage)
elif mode == 'indexgroup':IndexGroup(url)	
elif mode == 'index_group':Index_Group(url)	

	
elif mode=='stream':
    dialogWait = xbmcgui.DialogProgress()
    dialogWait.create('Brought to you by Live-TV', 'Loading video. Please wait...')
    resolveUrl(url)
    dialogWait.close()
    del dialogWait	
elif mode=='play':
    dialogWait = xbmcgui.DialogProgress()
    dialogWait.create('Brought to you by Live-TV', 'Loading video. Please wait...')
    PlayVideo(url,name)
    dialogWait.close()
    del dialogWait
else:Channel()
xbmcplugin.endOfDirectory(int(sysarg))