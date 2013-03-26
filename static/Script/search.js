$(document).ready(function() {
	//상세검색버튼 클릭시
	$('#AdvancedSearchStartButton').click(function() { 
		window.location.replace('advancedSearch');
	});

	$('#FoodSearcher').submit(function() {
		data = $('#FoodSearcher').serialize();

		$.ajax({
			type:'POST',
			url:'/search/',
			data: data,
			dataType: "json",
			success: function(data) {
				//data[0].state 이런식으로 접근해야함
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
				else if (state == 2) { $("#searchResult").append("<p>검색 도중 오류가 발생했습니다.<br />잠시 뒤에 다시 시도해주시기 바랍니다.</p>"); } else { resultDiv = $("#searchResult"); resultDiv.append("<p>")
							 .append("<h2>" + data[0].restaurant_name + "</h2>")
							 .append("<h3>" + data[0].restaurant_phonenumber + "</h3>")
							 .append("<h3>" + data[0].category_name + ", " + data[0].region_name + "</h3>")
							 .append("<h3>" + data[0].food_name + ", " + data[0].food_price + "원</h3>");
					$("#searchResult").append("</p>");
				}
			},
			error: function(xhr,err) {
				alert("readyState: "+xhr.readyState+"\nstatus: "+xhr.status);
				//alert("responseText: "+xhr.responseText);
			}
		});
		event.preventDefault();
	});

	$('#advancedRestaurantSearcher').submit(function() {
		alert("아직 안짬");
		data = $('#FindRestaurant').serialize();

		$.ajax({
			type:'POST',
			url:'/restaurantSearch/',
			data: data,
			dataType: "json",
			success: function(data) {
				alert("123");
			},
			error: function(xhr,err) {
				alert("readyState: "+xhr.readyState+"\nstatus: "+xhr.status);
				//alert("responseText: "+xhr.responseText);
			}
		});
		event.preventDefault();*/
	});
});
