#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64 , json , logging , requests , urlresolver
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.xomgiaitri'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 ii11i ( 'Search' , 'http://www.xomphimbo.com/xem/search/%s/1.html' , 'search' , 'http://www.viettv24.com/addonicons/Search.jpg' )
 ii11i ( 'Phim Lẻ' , 'http://www.xomphimbo.com/xem/the-loai/phim-dien-anh' , 'index' , 'http://www.viettv24.com/addonicons/Movies.jpg' )
 ii11i ( 'Phim Bộ' , 'http://www.xomphimbo.com/xem/the-loai/phim-bo' , 'index' , 'http://www.viettv24.com/addonicons/Series.jpg' )
 ii11i ( 'Phim Bộ theo Quốc Gia' , 'http://www.xomphimbo.com/' , 'videosbyregion' , 'http://www.viettv24.com/addonicons/Regions.jpg' )
 ii11i ( 'Phim Lẻ theo Thể Loại' , 'http://www.xomphimbo.com/' , 'videosbycategory' , 'http://www.viettv24.com/addonicons/Categories.jpg' )
 if 66 - 66: iIiI * iIiiiI1IiI1I1 * o0OoOoOO00
 I11i = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 I11i = xbmc . translatePath ( os . path . join ( I11i , "temp.jpg" ) )
 urllib . urlretrieve ( 'http://drive.google.com/uc?export=jpg&id=0B-ygKtjD8Sc-OUxwbVR5ZzZsbFJFT3A5aS04YlJkdDJtQ3BF' , I11i )
 O0O = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I11i )
 Oo = xbmcgui . WindowDialog ( )
 Oo . addControl ( O0O )
 #Oo . doModal ( )
 if 2 - 2: o0 * i1 * ii1IiI1i % OOooOOo / I11iIi1I / IiiIII111iI
def IiII ( ) :
 ii11i ( "Hồng Kong" , "http://www.xomphimbo.com/xem/category/1/phim-bo-hong-kong.html" , "index" , "" )
 ii11i ( "Hồng Kong (VNLT)" , "http://www.xomphimbo.com/xem/category/28/phim-bo-hong-kong-vnlt.html" , "index" , "" )
 ii11i ( "Hàn Quốc" , "http://www.xomphimbo.com/xem/category/4/phim-bo-han-quoc.html" , "index" , "" )
 ii11i ( "Hàn Quốc (vietsub)" , "http://www.xomphimbo.com/xem/category/29/phim-bo-han-quoc-vietsub.html" , "index" , "" )
 ii11i ( "Trung Quốc" , "http://www.xomphimbo.com/xem/category/2/phim-bo-trung-quoc.html" , "index" , "" )
 ii11i ( "Đài Loan" , "http://www.xomphimbo.com/xem/category/3/phim-bo-dai-loan.html" , "index" , "" )
 ii11i ( "Việt Nam" , "http://www.xomphimbo.com/xem/category/5/phim-bo-viet-nam.html" , "index" , "" )
 ii11i ( "Thái Lan" , "http://www.xomphimbo.com/xem/category/22/phim-bo-thai-lan.html" , "index" , "" )
 ii11i ( "Các Loại Khác" , "http://www.xomphimbo.com/xem/category/7/cac-loai-khac.html" , "index" , "" )
 if 28 - 28: Ii11111i * iiI1i1
def i1I1ii1II1iII ( ) :
 ii11i ( "Hành Động" , "http://www.xomphimbo.com/xem/category/8/hanh-dong.html" , "index" , "" )
 ii11i ( "Tình Cảm" , "http://www.xomphimbo.com/xem/category/9/tinh-cam.html" , "index" , "" )
 ii11i ( "Phim Hài" , "http://www.xomphimbo.com/xem/category/10/phim-hai.html" , "index" , "" )
 ii11i ( "Kinh Dị" , "http://www.xomphimbo.com/xem/category/11/kinh-di.html" , "index" , "" )
 ii11i ( "Kiếm Hiệp" , "http://www.xomphimbo.com/xem/category/12/kiem-hiep.html" , "index" , "" )
 ii11i ( "Việt Nam" , "http://www.xomphimbo.com/xem/category/15/viet-nam.html" , "index" , "" )
 ii11i ( "Hài Kịch" , "http://www.xomphimbo.com/xem/category/16/hai-kich.html" , "index" , "" )
 ii11i ( "Ca Nhạc" , "http://www.xomphimbo.com/xem/category/17/ca-nhac.html" , "index" , "" )
 ii11i ( "Cải Lương" , "http://www.xomphimbo.com/xem/category/18/cai-luong.html" , "index" , "" )
 ii11i ( "Phóng Sự" , "http://www.xomphimbo.com/xem/category/19/phong-su.html" , "index" , "" )
 ii11i ( "Các Loại Khác" , "http://www.xomphimbo.com/xem/category/20/cac-loai-khac.html" , "index" , "" )
 if 86 - 86: oO0o
def IIII ( url ) :
 Oo0oO0oo0oO00 = i111I ( url )
 II1Ii1iI1i = re . compile ( '<td align="center"><a href=".(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/></a>' ) . findall ( Oo0oO0oo0oO00 )
 for iiI1iIiI , OOo , Ii1IIii11 in II1Ii1iI1i :
  Ii1IIii11 = Ii1IIii11 . replace ( "xomgiaitri.com" , "mythugian.net" )
  Ii1IIii11 = Ii1IIii11 . replace ( "www." , "" )
  Ii1IIii11 = "/" . join ( Ii1IIii11 . split ( "/" ) [ : - 1 ] ) + "/" + urllib . quote ( Ii1IIii11 . split ( "/" ) [ - 1 ] )
  ii11i ( "[B]" + OOo + "[/B]" , "http://www.xomphimbo.com/xem" + iiI1iIiI , 'mirrors' , Ii1IIii11 )
 Oooo0000 = re . compile ( '<a class="pagelink" [^>]* href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( Oo0oO0oo0oO00 . replace ( "'" , '"' ) )
 for iiI1iIiI , i11 in Oooo0000 :
  ii11i ( i11 , iiI1iIiI . replace ( "./" , "http://www.xomphimbo.com/xem/" ) , 'index' , "" )
  if 41 - 41: O00o0o0000o0o . oOo0oooo00o * I1i1i1ii - IIIII
def I1 ( ) :
 try :
  O0OoOoo00o = xbmc . Keyboard ( '' , 'Enter search text' )
  O0OoOoo00o . doModal ( )
  if 31 - 31: i111IiI + o0OoOoOO00 . ii1IiI1i
  if ( O0OoOoo00o . isConfirmed ( ) ) :
   OOoO00o = urllib . quote_plus ( O0OoOoo00o . getText ( ) )
  IIII ( II111iiii % OOoO00o )
 except : pass
 if 48 - 48: ii1IiI1i . iIiI - OOooOOo % iiI1i1 / O00o0o0000o0o . O00o0o0000o0o
def i1Ii ( url ) :
 I111I11 = O0O00Ooo ( url )
 Oo0oO0oo0oO00 = i111I ( I111I11 )
 OOoooooO = re . compile ( '<span class="name"[^>]*>(.+?)</span>' ) . findall ( Oo0oO0oo0oO00 )
 if 14 - 14: oO0o % iiI
 if "VIP A : " in OOoooooO :
  OOoooooO . insert ( 0 , OOoooooO . pop ( OOoooooO . index ( "VIP A : " ) ) )
 if "VIP D : " in OOoooooO :
  OOoooooO . insert ( 0 , OOoooooO . pop ( OOoooooO . index ( "VIP D : " ) ) )
 if "VIP B : " in OOoooooO :
  OOoooooO . insert ( 0 , OOoooooO . pop ( OOoooooO . index ( "VIP B : " ) ) )
 for IiI1I1 in range ( len ( OOoooooO ) ) :
  OoO000 = [ "Flv :" , "OK :" ]
  if not any ( x in OOoooooO [ IiI1I1 ] for x in OoO000 ) :
   ii11i ( "[%d] - %s" % ( IiI1I1 + 1 , OOoooooO [ IiI1I1 ] ) , I111I11 . encode ( "utf-8" ) , 'episodes' , "" )
   if 42 - 42: Ii11111i - iIiiiI1IiI1I1 / i11iIiiIii + iiI1i1 + ii1IiI1i
def iIi ( url , name ) :
 Oo0oO0oo0oO00 = i111I ( url )
 if 40 - 40: Ii11111i . OOooOOo . i1 . iIiiiI1IiI1I1
 name = name . split ( "] - " ) [ 1 ]
 I11iii = re . compile ( '<div class="listserver"><span class="name"[^>]*>%s</span>(.+?)</div>' % name ) . findall ( Oo0oO0oo0oO00 )
 OO0O00 = re . compile ( '<a href="(.+?)"><font[^>]*><b>(.+?)</b></font></a>' ) . findall ( I11iii [ 0 ] )
 if ( "episode_bg_2" in I11iii [ 0 ] ) :
  ii1 = re . compile ( '<font class="episode_bg_2">(.+?)</font>' ) . findall ( I11iii [ 0 ] )
  o0oO0o00oo ( "Part - " + ii1 [ 0 ] . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf8" ) , url , 'loadvideo' , '' , name )
 for II1i1Ii11Ii11 , iII11i in OO0O00 :
  o0oO0o00oo ( "Part - " + iII11i . replace ( "&nbsp;" , "" ) . strip ( ) , "http://www.xomphimbo.com/xem/" + II1i1Ii11Ii11 , 'loadvideo' , '' , name )
  if 97 - 97: oO0o % oO0o + o0OoOoOO00 * oOo0oooo00o
def O0O00Ooo ( url ) :
 o0o00o0 = i111I ( url )
 return re . compile ( '<p class="w_now"><a href="(.+?)" title="Xem phim trực tuyến">' ) . findall ( o0o00o0 ) [ 0 ]
 if 25 - 25: i1 - I1i1i1ii . iIiI
def I11ii1 ( url , name ) :
 I11II1i = xbmcgui . ListItem ( name )
 Oo0oO0oo0oO00 = i111I ( url )
 if "proxy.link" in Oo0oO0oo0oO00 :
  IIIIIooooooO0oo = re . compile ( "'proxy.link', '(.+?)'" ) . findall ( Oo0oO0oo0oO00 )
  Oo0oO0oo0oO00 = i111I ( IIIIIooooooO0oo [ 0 ] )
 IIIIIooooooO0oo = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( Oo0oO0oo0oO00 )
 if ( len ( IIIIIooooooO0oo ) == 0 ) :
  IIiiiiiiIi1I1 = None
  I1IIIii = re . compile ( 'file\: "(.+?)"' ) . findall ( Oo0oO0oo0oO00 )
  if 'iframe src="http://play.mythugian.net/' in Oo0oO0oo0oO00 :
   IIIIIooooooO0oo = re . compile ( 'iframe src="(http://play.mythugian.net/.+?)"' ) . findall ( Oo0oO0oo0oO00 )
   Oo0oO0oo0oO00 = i111I ( IIIIIooooooO0oo [ 0 ] )
   IIIIIooooooO0oo = re . compile ( '(\[\{"label".+?\}\])' ) . findall ( Oo0oO0oo0oO00 )
   try :
    IIiiiiiiIi1I1 = json . loads ( IIIIIooooooO0oo [ 0 ] ) [ - 1 ] [ "file" ]
   except :
    IIiiiiiiIi1I1 = json . loads ( IIIIIooooooO0oo [ 0 ] ) [ - 1 ] [ "src" ]
  elif 'iframe src="http://img.mythugian.net/' in Oo0oO0oo0oO00 :
   try :
    IIIIIooooooO0oo = re . search ( 'iframe[^>]*src="(http://img.mythugian.net/.+?)"' , Oo0oO0oo0oO00 ) . group ( 1 )
    try :
     IIiiiiiiIi1I1 = re . search ( 'link=(.+?)$' , IIIIIooooooO0oo ) . group ( 1 ) . decode ( "base64" )
     IIiiiiiiIi1I1 = oOoOooOo0o0 ( IIiiiiiiIi1I1 )
    except :
     Oo0oO0oo0oO00 = i111I ( IIIIIooooooO0oo )
     try :
      OOOO = [ ]
      OOOO += [ re . search ( 'c3RhcnRcfHByaW1hcnlcfCguKz8pXHw=' . decode ( "base64" ) , Oo0oO0oo0oO00 ) . group ( 1 ) ]
      try :
       OOOO += [ re . search ( 'XHxnb29nbGVcfChcdyspXHxjb2xvclx8' . decode ( "base64" ) , Oo0oO0oo0oO00 ) . group ( 1 ) ]
      except : pass
      IIiiiiiiIi1I1 = oOoOooOo0o0 ( "aHR0cHM6Ly9kcml2ZS5nb29nbGUuY29tL2ZpbGUvZC8lcy92aWV3" . decode ( "base64" ) % ( "-" . join ( OOOO ) ) )
     except :
      try :
       OOOO = [ ]
       OOOO += [ re . search ( 'c3RhcnRcfChcdyspXHxzZXR1cA==' . decode ( "base64" ) , Oo0oO0oo0oO00 ) . group ( 1 ) ]
       OOOO += [ re . search ( 'XHxnb29nbGVcfChcdyspXHxjb2xvclx8' . decode ( "base64" ) , Oo0oO0oo0oO00 ) . group ( 1 ) ]
       OOOO += [ re . search ( 'cHJpbWFyeVx8KFx3KylcfHN0YXJ0cGFyYW0=' . decode ( "base64" ) , Oo0oO0oo0oO00 ) . group ( 1 ) ]
       IIiiiiiiIi1I1 = oOoOooOo0o0 ( "aHR0cHM6Ly9kcml2ZS5nb29nbGUuY29tL2ZpbGUvZC8lcy92aWV3" . decode ( "base64" ) % ( "-" . join ( OOOO ) ) )
      except :
       try :
        IIIIIooooooO0oo = re . search ( 'sources = (\[.+?\]);' , Oo0oO0oo0oO00 )
        IIiiiiiiIi1I1 = json . loads ( IIIIIooooooO0oo . group ( 1 ) ) [ - 1 ] [ "file" ]
       except :
        try :
         IIIIIooooooO0oo = re . search ( '"(https://drive.google.com/file/.+?)"' , Oo0oO0oo0oO00 ) . group ( 1 )
         IIiiiiiiIi1I1 = oOoOooOo0o0 ( IIIIIooooooO0oo . replace ( "preview" , "view" ) )
        except :
         IIiiiiiiIi1I1 = re . search ( '"(http\://.+?\.mediafire\.com/.+?)"' , Oo0oO0oo0oO00 ) . group ( 1 )
   except : pass
  elif I1IIIii is not None :
   if "http://" not in I1IIIii [ 0 ] :
    I1IIIii [ 0 ] = "http://www.xomphimbo.com/xem/" + I1IIIii [ 0 ]
   IIiiiiiiIi1I1 = I1IIIii [ 0 ]
  elif "app.box.com" in Oo0oO0oo0oO00 :
   OOO00 = re . compile ( 'https://app.box.com/embed_widget/s/(.+?)\?' ) . findall ( Oo0oO0oo0oO00 ) [ 0 ]
   iiiiiIIii = i111I ( "https://app.box.com/index.php?rm=preview_embed&sharedName=%s" % OOO00 )
   O000OO0 = json . loads ( iiiiiIIii ) [ "file" ] [ "versionId" ]
   IIiiiiiiIi1I1 = "https://app.box.com/representation/file_version_%s/video_480.mp4?shared_name=%s" % ( O000OO0 , OOO00 )
  elif "drive.google.com/file" in Oo0oO0oo0oO00 :
   IIiiiiiiIi1I1 = oOoOooOo0o0 ( IIIIIooooooO0oo . replace ( "preview" , "view" ) )
  elif "openload" in Oo0oO0oo0oO00 :
   try :
    IIiiiiiiIi1I1 = re . compile ( '"(https://openload.+?)"' ) . findall ( Oo0oO0oo0oO00 ) [ 0 ]
    IIiiiiiiIi1I1 = urlresolver . resolve ( IIiiiiiiIi1I1 )
   except :
    pass
  else :
   IIIIIooooooO0oo = re . compile ( "file: '.+?'" ) . findall ( Oo0oO0oo0oO00 )
   if "http://" not in IIIIIooooooO0oo [ 0 ] :
    IIiiiiiiIi1I1 = "http://www.xomphimbo.com/xem/" + IIIIIooooooO0oo [ 0 ]
   else :
    IIiiiiiiIi1I1 = IIIIIooooooO0oo [ 0 ]
  I11II1i . setPath ( IIiiiiiiIi1I1 )
 else :
  if "http://" not in IIIIIooooooO0oo [ 0 ] :
   IIIIIooooooO0oo [ 0 ] = "http://www.xomphimbo.com/xem/" + IIIIIooooooO0oo [ 0 ]
  I11II1i . setPath ( IIIIIooooooO0oo [ 0 ] )
 I11II1i . setProperty ( "IsPlayable" , "true" )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I11II1i )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I11II1i )
 if 43 - 43: IIIII - iiI % o0 . oO0o
def oOoOooOo0o0 ( url , hq = True ) :
 o00 = "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)"
 OooOooo = {
 'User-Agent' : o00 ,
 'Accept-Encoding' : 'gzip, deflate, sdch' ,
 }
 iiiiiIIii = requests . get ( url , headers = OooOooo )
 O000oo0O = iiiiiIIii . text
 try :
  IIIIIooooooO0oo = re . compile ( '(\["fmt_stream_map".+?\])' ) . findall ( O000oo0O ) [ 0 ]
  OOOOi11i1 = [ "38" , "37" , "46" , "22" , "45" , "18" , "43" ]
  if not hq : OOOOi11i1 . reverse ( )
  IIIii1II1II = json . loads ( IIIIIooooooO0oo ) [ 1 ] . split ( "," )
  for i1I1iI in OOOOi11i1 :
   for oo0OooOOo0 in IIIii1II1II :
    if oo0OooOOo0 . startswith ( i1I1iI + "|" ) :
     url = oo0OooOOo0 . split ( "|" ) [ 1 ]
     o0O = "|User-Agent=%s&Cookie=%s" % ( urllib . quote_plus ( o00 ) , urllib . quote_plus ( iiiiiIIii . headers [ 'set-cookie' ] ) )
     return url + o0O
 except :
  try :
   return re . search ( "fmt_stream_map\=18\|(.+?)(\||$)" , O000oo0O ) . group ( 1 )
  except : pass
  if 72 - 72: oOo0oooo00o / iIiiiI1IiI1I1 * i1 - IIIII
def Oo0O0O0ooO0O ( url ) :
 IIIIii = ""
 O0o0 = urllib2 . Request ( url )
 O0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 O0o0 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 OO00Oo = urllib2 . urlopen ( O0o0 )
 url = OO00Oo . geturl ( )
 try :
  IIIIii = re . compile ( '"https://drive.google.com/file/d/(.+?)/.+?"' ) . findall ( url ) [ 0 ]
 except :
  pass
 OO00Oo . close ( )
 return IIIIii
 if 51 - 51: I1i1i1ii * I11iIi1I + oO0o + ii1IiI1i
def i111I ( url ) :
 O0o0 = urllib2 . Request ( url )
 O0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 O0o0 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 OO00Oo = urllib2 . urlopen ( O0o0 )
 Oo0oO0oo0oO00 = OO00Oo . read ( )
 OO00Oo . close ( )
 Oo0oO0oo0oO00 = '' . join ( Oo0oO0oo0oO00 . splitlines ( ) ) . replace ( '\'' , '"' )
 Oo0oO0oo0oO00 = Oo0oO0oo0oO00 . replace ( '\n' , '' )
 Oo0oO0oo0oO00 = Oo0oO0oo0oO00 . replace ( '\t' , '' )
 Oo0oO0oo0oO00 = re . sub ( '  +' , ' ' , Oo0oO0oo0oO00 )
 Oo0oO0oo0oO00 = Oo0oO0oo0oO00 . replace ( '> <' , '><' )
 return Oo0oO0oo0oO00
 if 66 - 66: OOooOOo
def o0oO0o00oo ( name , url , mode , iconimage , mirrorname ) :
 oO000Oo000 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 i111IiI1I = True
 O0 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 O0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 O0 . setProperty ( "IsPlayable" , "true" )
 i111IiI1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO000Oo000 , listitem = O0 )
 return i111IiI1I
 if 30 - 30: I11iIi1I . O00o0o0000o0o - iIiI
def ii11i ( name , url , mode , iconimage ) :
 oO000Oo000 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i111IiI1I = True
 O0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i111IiI1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO000Oo000 , listitem = O0 , isFolder = True )
 return i111IiI1I
 if 8 - 8: iIiiiI1IiI1I1 - ii1I * o0OoOoOO00 + i11iIiiIii / IIIII % iiI1i1
def iIIIi1 ( k , e ) :
 iiII1i1 = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for IiI1I1 in range ( len ( e ) ) :
  o00oOO0o = k [ IiI1I1 % len ( k ) ]
  OOO00O = chr ( ( 256 + ord ( e [ IiI1I1 ] ) - ord ( o00oOO0o ) ) % 256 )
  iiII1i1 . append ( OOO00O )
 return "" . join ( iiII1i1 )
 if 84 - 84: Ii11111i * ii1IiI1i / oO0o - iiI
def IiI1 ( parameters ) :
 Oo0O00Oo0o0 = { }
 if 87 - 87: i111IiI * i1 % i11iIiiIii % OOooOOo - iiI1i1
 if parameters :
  O0ooo0O0oo0 = parameters [ 1 : ] . split ( "&" )
  for oo0oOo in O0ooo0O0oo0 :
   o000O0o = oo0oOo . split ( '=' )
   if ( len ( o000O0o ) ) == 2 :
    Oo0O00Oo0o0 [ o000O0o [ 0 ] ] = o000O0o [ 1 ]
 return Oo0O00Oo0o0
 if 42 - 42: OOooOOo
II = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 45 - 45: iiI * I11iIi1I % i1 * iIiI + oOo0oooo00o . OOooOOo
if os . path . exists ( II ) == False :
 os . mkdir ( II )
Oo0ooOo0o = os . path . join ( II , 'visitor' )
if 22 - 22: ii1I / i11iIiiIii * ii1I * o0OoOoOO00 . iiI1i1 / i11iIiiIii
if os . path . exists ( Oo0ooOo0o ) == False :
 from random import randint
 Iiii = open ( Oo0ooOo0o , "w" )
 Iiii . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 Iiii . close ( )
 if 75 - 75: OOooOOo % I11iIi1I % I11iIi1I . IIIII
def III1iII1I1ii ( utm_url ) :
 oOOo0 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  O0o0 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : oOOo0 }
 )
  OO00Oo = urllib2 . urlopen ( O0o0 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return OO00Oo
 if 54 - 54: iiI - I1i1i1ii % iiI1i1
def OOoO ( group , name ) :
 try :
  try :
   from hashlib import md5
  except :
   from md5 import md5
  from random import randint
  import time
  from urllib import unquote , quote
  from os import environ
  from hashlib import sha1
  iII = "1.0"
  ii1ii11IIIiiI = open ( Oo0ooOo0o ) . read ( )
  O00OOOoOoo0O = "XomGiaiTri"
  O000OOo00oo = "UA-52209804-2"
  oo0OOo = "www.viettv24.com"
  ooOOO00Ooo = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   IiIIIi1iIi = ooOOO00Ooo + "?" + "utmwv=" + iII + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( O00OOOoOoo0O ) + "&utmac=" + O000OOo00oo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , ii1ii11IIIiiI , "1" , "1" , "2" ] )
   if 68 - 68: i11iIiiIii % IiiIII111iI + i11iIiiIii
   if 31 - 31: o0OoOoOO00 . o0
   if 1 - 1: i1 / I11iIi1I % oOo0oooo00o * I1i1i1ii . i11iIiiIii
   if 2 - 2: IiiIII111iI * oO0o - ii1I + o0 . Ii11111i % oOo0oooo00o
   if 92 - 92: oOo0oooo00o
  else :
   if group == "None" :
    IiIIIi1iIi = ooOOO00Ooo + "?" + "utmwv=" + iII + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( O00OOOoOoo0O + "/" + name ) + "&utmac=" + O000OOo00oo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , ii1ii11IIIiiI , "1" , "1" , "2" ] )
    if 25 - 25: i1 - o0 / iIiI / I11iIi1I
    if 12 - 12: o0 * oOo0oooo00o % iIiiiI1IiI1I1 % ii1I
    if 20 - 20: iiI1i1 % O00o0o0000o0o / O00o0o0000o0o + O00o0o0000o0o
    if 45 - 45: Ii11111i - I1i1i1ii - iIiI - ii1IiI1i . o0OoOoOO00 / iiI
    if 51 - 51: iiI + oOo0oooo00o
   else :
    IiIIIi1iIi = ooOOO00Ooo + "?" + "utmwv=" + iII + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( O00OOOoOoo0O + "/" + group + "/" + name ) + "&utmac=" + O000OOo00oo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , ii1ii11IIIiiI , "1" , "1" , "2" ] )
    if 8 - 8: Ii11111i * OOooOOo - O00o0o0000o0o - ii1IiI1i * iiI1i1 % o0
    if 48 - 48: iiI
    if 11 - 11: oO0o + iIiI - ii1IiI1i / I11iIi1I + i1 . o0OoOoOO00
    if 41 - 41: O00o0o0000o0o - iiI - iiI
    if 68 - 68: iiI1i1 % IIIII
    if 88 - 88: ii1I - i111IiI + iiI1i1
  print "============================ POSTING ANALYTICS ============================"
  III1iII1I1ii ( IiIIIi1iIi )
  if 40 - 40: o0 * O00o0o0000o0o + iiI1i1 % oOo0oooo00o
  if not group == "None" :
   OOOOOoo0 = ooOOO00Ooo + "?" + "utmwv=" + iII + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( oo0OOo ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + O00OOOoOoo0O + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( O00OOOoOoo0O ) + "&utmac=" + O000OOo00oo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , ii1ii11IIIiiI , "1" , "2" ] )
   if 49 - 49: iiI . oOo0oooo00o
   if 11 - 11: I1i1i1ii * o0 . ii1I % iIiI + oOo0oooo00o
   if 78 - 78: ii1IiI1i . iiI1i1 + ii1IiI1i / oO0o / ii1IiI1i
   if 54 - 54: OOooOOo % oOo0oooo00o
   if 37 - 37: OOooOOo * i1 / i111IiI - oOo0oooo00o % o0OoOoOO00 . Ii11111i
   if 88 - 88: oOo0oooo00o . o0OoOoOO00 * o0OoOoOO00 % IIIII
   if 15 - 15: iIiiiI1IiI1I1 * o0 + i11iIiiIii
   if 6 - 6: i111IiI / i11iIiiIii + oOo0oooo00o * Ii11111i
   try :
    print "============================ POSTING TRACK EVENT ============================"
    III1iII1I1ii ( OOOOOoo0 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 80 - 80: o0OoOoOO00
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 83 - 83: oO0o . i11iIiiIii + o0OoOoOO00 . I11iIi1I * oO0o
oooO0 = IiI1 ( sys . argv [ 2 ] )
iIiIiiIIiIIi = oooO0 . get ( 'mode' )
II111iiii = oooO0 . get ( 'url' )
oO0OOOO0 = oooO0 . get ( 'name' )
if type ( II111iiii ) == type ( str ( ) ) :
 II111iiii = urllib . unquote_plus ( II111iiii )
if type ( oO0OOOO0 ) == type ( str ( ) ) :
 oO0OOOO0 = urllib . unquote_plus ( oO0OOOO0 )
 if 26 - 26: O00o0o0000o0o
I11iiI1i1 = str ( sys . argv [ 1 ] )
if iIiIiiIIiIIi == 'index' :
 OOoO ( "Browse" , oO0OOOO0 )
 IIII ( II111iiii )
elif iIiIiiIIiIIi == 'search' :
 OOoO ( "None" , "Search" )
 I1 ( )
elif iIiIiiIIiIIi == 'videosbyregion' :
 OOoO ( "Browse" , oO0OOOO0 )
 IiII ( )
elif iIiIiiIIiIIi == 'videosbycategory' :
 OOoO ( "Browse" , oO0OOOO0 )
 i1I1ii1II1iII ( )
elif iIiIiiIIiIIi == 'mirrors' :
 OOoO ( "Browse" , oO0OOOO0 )
 i1Ii ( II111iiii )
elif iIiIiiIIiIIi == 'episodes' :
 OOoO ( "Browse" , oO0OOOO0 )
 iIi ( II111iiii , oO0OOOO0 )
elif iIiIiiIIiIIi == 'loadvideo' :
 OOoO ( "Play" , oO0OOOO0 + "/" + II111iiii )
 I1i1Iiiii = xbmcgui . DialogProgress ( )
 I1i1Iiiii . create ( 'xomgiaitri.com' , 'Loading video. Please wait...' )
 I11ii1 ( II111iiii , oO0OOOO0 )
 I1i1Iiiii . close ( )
 del I1i1Iiiii
else :
 OOoO ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( I11iiI1i1 ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
