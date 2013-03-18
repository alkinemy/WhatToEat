$(document).ready(function() {
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
					$("#searchResult").append(
						"<p>운이 참 없네요...<br />꽝입니다.<br />당신은 밥을 먹을 수 없습니다.<br />"
					);
					$("#searchResult").append(
						"다이어트 하세요.<br /></p>"
					);
				}
				else if (state == 1) {
					$("#searchResult").append("<p>검색 결과가 없습니다!<br />다시 검색해주세요!</p>");
				}
				else {
					resultDiv = $("#searchResult");
					resultDiv.append("<p>")
							 .append("<h2>" + data[0].restaurant_name + "</h2><br />")
							 .append("<h3>" + data[0].category_name + ", " + data[0].region_name + "</h3><br />")
							 .append("<h3>" + data[0].food_name + ", " + data[0].food_price + "</h3>");
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
});
