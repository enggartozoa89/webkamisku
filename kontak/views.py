from django.shortcuts import render

def index (request):
 context ={
  'judul'          : 'kontak Kamisku', 
  'isi'            : 'Selamat Datang di Web Kamisku',
  'title'          : 'Kontak Kamisku', 
  'banner'         : 'kontak/images/kontak.png',
  'css_global'     : 'css/css_global.css',
  'css_apps'       : [
   'blog/css/css_apps.css',
   'kontak/css/css_apps.css',
   ],
  'nav'            : [
   (''             , 'home =>'),
   ('blog/'        , 'blog =>'),
   ('kontak/'      , 'kontak =>'),
  ]
 }
 return render(request, 'kontak/index.html', context) 
