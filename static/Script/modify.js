$(document).ready(function() {
	window.onbeforeunload = confirmExit;

	function confirmExit()
	{
		return "아직 음식점을 등록하지 않았습니다.";
	}

	$('#modifyRestaurantForm').submit(function() {
		data = $('#modifyRestaurantForm').serialize();

		$.ajax({
			type:'POST',
			url:modifyOldRestaurantUrl,
			data: data,
			dataType: "json",
			success: function(data) {
				state = data[0].state;
				if (state == 0) {
					alert("음식점 수정 성공!");
					window.location.replace(restaurantDetailUrl);
				}
				else {
					alert("음식점 수정 실패");
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
