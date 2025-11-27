from django.shortcuts import render

def index (request):
 context ={
  'judul'          : 'Web Kamisku', 
  'isi'            : 'Selamat Datang di Web Kamisku',
  'title'          : 'Web Kamisku', 
  'banner'         : 'images/beranda.png',
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
 return render(request, 'index.html', context) 
