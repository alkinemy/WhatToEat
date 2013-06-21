from django.conf.urls import patterns, url

from recommend_food import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^search/$', views.search, name='search'),

	url(r'^advancedSearch/$', views.loadAdvancedSearch, name='advancedSearch'),
	url(r'^advancedSearch/advancedRestaurantSearch/$', views.advancedRestaurantSearch, name='advancedRestaurantSearch'),
	url(r'^advancedSearch/advancedFoodSearch/$', views.advancedFoodSearch, name='advancedFoodSearch'),

	url(r'^registerRestaurant/$', views.loadRegisterRestaurant, name='registerRestaurant'),
	url(r'^registerRestaurant/registerNewRestaurant/$', views.registerNewRestaurant, name='registerNewRestaurant'),

	url(r'modifyRestaurantDetail/(\d+)/$', views.loadModifyRestaurant, name='modifyRestaurant'),
	url(r'modifyRestaurantDetail/modifyOldRestaurant/(\d+)/$', views.modifyOldRestaurant, name='modifyOldRestaurant'),

	url(r'modifyRestaurantFoodList/(\d+)/$', views.loadModifyRestaurantFoodList, name='modifyRestaurantFoodList'),
	url(r'modifyRestaurantFoodList/modifyFoodDetail/(\d+)/$', views.modifyFoodDetail, name='modifyFoodDetail'),
	url(r'modifyRestaurantFoodList/addNewFood/(\d+)$', views.addNewFood, name='addNewFood'),
	
	url(r'^restaurantList/$', views.restaurantList, name='restaurantList'),
	url(r'^restaurantList/loadRestaurantList/$', views.loadRestaurantList, name='loadRestaurantList'),
	url(r'^restaurantList/restaurantDetail/(\d+)/$', views.restaurantDetail, name='restaurantDetail'),
)
