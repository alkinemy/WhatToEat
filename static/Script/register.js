$(document).ready(function() {
	$("#addFoodButton").click(function() {
		//$("#restaurantTable").append('<tr><td>이름</td><td><input type="textbox" name="food_name" /></td><td>가격</td><td><input type="textbox" name="food_price" /></td></tr>');
		$("#foodTextbox tr:last").after('<tr><td>이름</td><td><input type="textbox" name="food_name" /></td><td>가격</td><td><input type="textbox" name="food_price" /></td></tr>');
	});


	$('#registerRestaurantForm').submit(function() {
		data = $('#registerRestaurantForm').serialize();

		$.ajax({
			type:'POST',
			url:'/registerRestaurant/',
			data: data,
			dataType: "json",
			success: function(data) {
				state = data[0].state;
				if (state == 0) {
					alert("음식점 등록 성공!");
					$('#registerRestaurantForm')[0].reset();

				}
				else {
					alert("음식점 등록 실패");
				}
			},
			error: function(xhr,err) {
				alert("readyState: "+xhr.readyState+"\nstatus: "+xhr.status);
				//alert("responseText: "+xhr.responseText);
			}
		});
		event.preventDefault();
	});
});
