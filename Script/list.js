$(document).ready(function() {
	function showRestaurantList(data) {
		$("#showList").empty();
		state = data[0].state;
		$("#showList").append("<p>");
		for (var i = 1; i < data.length; i++) {
			//편집페이지나 메뉴 보여주는 페이지로 리다이렉팅
			var restaurantDetailUrl = url.replace(0, data[i].pk);
			string = '<a href="' + restaurantDetailUrl + '">' + data[i].Name + '</a><br />';
			$("#showList").append(string);
		};
		$("#showList").append("</p>");
	}

	$('.radioCategory').click(function() {
		//$('#loadRestaurantListForm').submit();
		data = $('#loadRestaurantListForm').serialize();
		$(this).attr('checked', 'checked');

		$.ajax({
			type:'POST',
			url:'loadRestaurantList/',
			data: data,
			dataType: 'json',
			success: function(data) {
				showRestaurantList(data)
			},
			error: function(xhr,err) {
				alert("readyState: "+xhr.readyState+"\nstatus: "+xhr.status);
			}
		});
		//event.preventDefault();
	});


	/*$('#loadRestaurantListForm').submit(function() {
		data = $('#loadRestaurantListForm').serialize();

		$.ajax({
			type:'POST',
			url:'/loadRestaurantList/',
			data: data,
			dataType: "json",
			success: function(data) {
				state = data[0].state;
				alert('성공');
				if (state == 0) {
					restaurants = data[0].restaurants;
					alert(restaurants);
				}
				else {
					alert("error");
				}
			},
			error: function(xhr,err) {
				alert("readyState: "+xhr.readyState+"\nstatus: "+xhr.status);
			}
		});
		event.preventDefault();
	});*/
});
