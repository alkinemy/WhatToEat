# -*- coding: utf-8 -*-
import json
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.template import loader
from django.db.models import Q
#from django.utils import simplejson
#from django.core.serializers.json import DjangoJSONEncoder
from recommend_food.models import Categories, Regions, Restaurants, Foods


#그냥 메인 화면 보여줌
def index(request):
	return render(request, 'Main/index.html')

#메인화면에서 검색하는걸 기준으로 작성
@csrf_protect
def search(request):
	if random.random() <= 0.01:
		result = \
		[
			{
				"state":"0"
			}
		]

		return HttpResponse(json.dumps(result), content_type='application/json')

	#배달주문할 때는 지역이 중요하지 않기 때문에 지역은 일단 빼기로 함
	try:
		checked_categories = request.POST.getlist('category')
		priceLowerBound = request.POST.get('priceLowerBound')
		priceUpperBound = request.POST.get('priceUpperBound')

		while checked_categories:
			category_pk = random.choice(checked_categories)
			restaurant_list = Restaurants.objects.filter(Category=category_pk)

			while restaurant_list:
				restaurant = random.choice(restaurant_list)
				food_list = Foods.objects.filter(Q(Restaurant=restaurant.pk), Q(Price__gt=int(priceLowerBound)), Q(Price__lt=int(priceUpperBound)))

				if not food_list:
					restaurant_list = restaurant_list.exclude(pk=restaurant.pk)
					continue

				food = random.choice(food_list)
				break;
			else:
				checked_categories.remove(category_pk)
				continue

			category = Categories.objects.get(pk=category_pk)
			region = restaurant.Region

			#가능하면 같은 칸에 넣지 말고 다른 칸에 넣자
			result = \
			[
				{
					"state":"3", 
					"category_name":category.Name, 
					"region_name":region.Name, 
					"restaurant_name":restaurant.Name, 
					"restaurant_phonenumber":restaurant.PhoneNumber,
					"food_name":food.Name, 
					"food_price":food.Price
				}
			]
	
			return HttpResponse(json.dumps(result), content_type='application/json')

		else:
			result = \
			[
				{
					"state":"1"
				}
			]

			return HttpResponse(json.dumps(result), content_type='application/json')
				
	except Exception,e:
		result = \
		[
			{
				"state":"2"
			}
		]

		print(e)
		return HttpResponse(json.dumps(result), content_type='application/json')

def loadAdvancedSearch(request):
	return render(request, 'Main/advancedSearch.html')

#조건에 맞는 음식점을 전부 출력함
@csrf_protect
def advancedRestaurantSearch(request):
	checked_categories = request.POST.getlist('category')
	checked_regions = request.POST.getlist('region')

	try:
		restaurant = []
		if checked_categories and checked_regions:
			restaurant = Restaurants.objects.filter(Q(Category_id__in=checked_categories), Q(Region_id__in=checked_regions)).values()
		elif checked_categories:
			restaurant = Restaurants.objects.filter(Category_id__in=checked_categories).values()
		elif checked_regions:
			restaurant = Restaurants.objects.filter(Region_id__in=checked_regions).values()

		result = \
		[
			{
				"state":"3"
			}
		]
		result.append(list(restaurant))
		#너무 쓸데없는 데이터가 많이 감 나중에 고쳐보기
	
		return HttpResponse(json.dumps(result), content_type='application/json')

	except Exception,e:
		result = \
		[
			{
				"state":"2"
			}
		]

		print(e)
		return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_protect
def advancedFoodSearch(request):
	result = \
	[
		{
			"state":"0"
		}
	]
	return HttpResponse(json.dumps(result), content_type='application/json')
	

def loadRegisterRestaurant(request):
	return render(request, 'Main/registerRestaurant.html')


@csrf_protect
def registerRestaurant(request):
	try:
		restaurant_name = request.POST.get('restaurant_name')
		restaurant_phone = request.POST.get('restaurant_phone')
		restaurant_detail = request.POST.get('restaurant_detail')
		checked_category = request.POST.get('category')
		checked_region = request.POST.get('region')

		foods_name = request.POST.getlist('food_name')
		foods_price = request.POST.getlist('food_price')
		foods_detail = request.POST.getlist('food_detail')

		category_object = Categories.objects.get(pk=int(checked_category))
		region_object = Regions.objects.get(pk=int(checked_region))

		#db에 등록하기 전에 validation 작업이 필요할 듯

		new_restaurant = Restaurants(Name=restaurant_name, Category=category_object, PhoneNumber=restaurant_phone, Region=region_object, Detail=restaurant_detail)
		new_restaurant.save()

		for i in range(len(foods_name)):
			new_food = Foods(Name=foods_name[i], Price=int(foods_price[i]), Restaurant=new_restaurant)
			new_food.save()
			

		result = \
		[
			{
				"state":"0"
			}
		]

		return HttpResponse(json.dumps(result), content_type='application/json')


	except Exception,e:
		result = \
		[
			{
				"state":"1"
			}
		]

		print(e)
		return HttpResponse(json.dumps(result), content_type='application/json')
		

def restaurantList(request):
	return render(request, 'Main/restaurantList.html')



@csrf_protect
def loadRestaurantList(request):
	try:
		checked_category = request.POST.get('category')
		print(checked_category)
		restaurants = Restaurants.objects.filter(Category_id=int(checked_category)).values('Name')
		print(restaurants)

		result = \
		[
			{
				"state":"0",
			}
		]

		result.extend(restaurants)

		print(result)

		return HttpResponse(json.dumps(result), content_type='application/json')
	except Exception,e:
		result = \
		[
			{
				"state":"1"
			}
		]

		return HttpResponse(json.dumps(result), content_type='application/json')
