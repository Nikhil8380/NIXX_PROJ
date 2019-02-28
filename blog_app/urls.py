from django.urls import path,re_path
from django.conf.urls import url,include
from blog_app import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

#app_name='BLOG_APP'
urlpatterns=[
url(r'^$', views.post_list_view,name='home'),
    url(r'^register/$', views.signup_view, name='register'),
    path('add_post', views.add_post,name='add_post'),
    path('add_profile', views.add_profile),
    path('like', views.like_post,name='like_post'),
    path('update_post/<int:id>', views.update_post,name='update_post'),
    path('post_delete/<int:id>', views.post_delete,name='post_delete'),
    path('profile', views.profile_view),
    path('index', views.index),
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list_view,name='post_list_by_tag_name'),
    path('contact/', views.contact_view),
    path('about/', views.about_view),
    #re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view, name='detail_view'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail_view,name='detail_view'),
    url(r'^post_detail/(?P<pk>\d+)/$',views.post_detail_view2.as_view(),name='detail_view2'),
    path('<int:id>/share/', views.mail_send_view),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls',namespace='social')),
    #path('logout/',views.logout_view),
    path('change_password/',views.change_password),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)