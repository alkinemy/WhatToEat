$(document).ready(function() {
	//상세검색버튼 클릭시
	$('#AdvancedSearchStartButton').click(function() { 
		window.location.replace('advancedSearch');
	});

	function showSearchResult(data) {
		state = data[0].state;
		$("#searchResult").empty();
		if (state == 0) {
			$("#searchResult").append("<p>")
							  .append("<h2>굶으세요</h2>")
							  .append("<h3>운이 참 없네요...<br />꽝입니다.<br />당신은 밥을 먹을 수 없습니다.<br />다이어트 하세요!</h3><br /></p>");
		}
		else if (state == 1) {
			$("#searchResult").append("<p>검색 결과가 없습니다!<br />다시 검색해주세요!</p>");
		}
		else if (state == 2) { 
			$("#searchResult").append("<p>검색 도중 오류가 발생했습니다.<br />잠시 뒤에 다시 시도하시거나 관리자에게 문의 부탁드립니다.</p>"); 
		} 
		else { 
			resultDiv = $("#searchResult"); 
			resultDiv.append("<p>")
					 .append("<h2>" + data[0].restaurant_name + "</h2>")
					 .append("<h3>" + data[0].restaurant_phonenumber + "</h3>")
					 .append("<h3>" + data[0].category_name + ", " + data[0].region_name + "</h3>")
					 .append("<h3>" + data[0].food_name + ", " + data[0].food_price + "원</h3>")
					 .append("</p>");
		}
	}

	$('#FoodSearcher').submit(function() {
		data = $('#FoodSearcher').serialize();

		$.ajax({
			type:'POST',
			url:'/search/',
			data: data,
			dataType: "json",
			success: function(data) {
				showSearchResult(data);
			},
			error: function(xhr,err) {
				alert("readyState: "+xhr.readyState+"\nstatus: "+xhr.status);
				//alert("responseText: "+xhr.responseText);
			}
		});
		event.preventDefault();
	});

	function getRestaurantList()
	{
		data = $('#advancedFoodSearcher').serialize();
	
		$.ajax({
			type:'POST',
			url:'advancedRestaurantSearch/',
			data: data,
			dataType: "json",
			success: function(data) {
				state = data[0].state
				$("#restaurantSearchResult").empty();
				restaurants = data[1]
				for (var i = 0; i != restaurants.length; i++) {
					restaurant = restaurants[i];
					id = "checkboxRestaurant" + restaurant.id;
					string = '<input id="' + id + '" type="checkbox" name="restaurant" value="' 
							+ restaurant.id + '" /><label for="' + id + '">' 
							+ restaurant.Name + '</label>';
					$("#restaurantSearchResult").append(string);
				}
			},
			error: function(xhr,err) {
				alert("readyState: "+xhr.readyState+"\nstatus: "+xhr.status);
			}
		});
	}
	
	$('#advancedFoodSearcher').submit(function() {
		data = $('#advancedFoodSearcher').serialize();

		$.ajax({
			type:'POST',
			url:'advancedFoodSearch/',
			data: data,
			dataType: "json",
			success: function(data) {
				showSearchResult(data);
			},
			error: function(xhr,err) {
				alert("readyState: "+xhr.readyState+"\nstatus: "+xhr.status);
			}
		});
		event.preventDefault();
	});

	$('input[name=category]').click(function(t) {
		getRestaurantList();
	});

	$('input[name=region]').click(function(t) {
		getRestaurantList();
	});

	$('#selectCategoryAll').click(function() {
		$('#cancelCategoryAll').prop('checked', false);
		$('input[name=category]').prop('checked', true);
		getRestaurantList();
	});

	$('#cancelCategoryAll').click(function() {
		$('#selectCategoryAll').prop('checked', false);
		$('input[name=category]').prop('checked', false);
		getRestaurantList();
	});

	$('#selectRegionAll').click(function() {
		$('#cancelRegionAll').prop('checked', false);
		$('input[name=region]').prop('checked', true);
		getRestaurantList();
	});

	$('#cancelRegionAll').click(function() {
		$('#selectRegionAll').prop('checked', false);
		$('input[name=region]').prop('checked', false);
		getRestaurantList();
	});
	
	$('#selectRestaurantAll').click(function() {
		$('#cancelRestaurantAll').prop('checked', false);
		$('input[name=restaurant]').prop('checked', true);
	});

	$('#cancelRestaurantAll').click(function() {
		$('#selectRestaurantAll').prop('checked', false);
		$('input[name=restaurant]').prop('checked', false);
	});
});
