from django.shortcuts import render

def index (request):
 context ={
  'judul'          : 'Blog Kamisku', 
  'isi'            : 'Selamat Datang di Web Kamisku',
  'title'          : 'Blog Kamisku', 
  'banner'         : 'blog/images/blog.png',
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
 return render(request, 'blog/index.html', context) 
