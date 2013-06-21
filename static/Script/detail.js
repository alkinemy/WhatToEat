$(document).ready(function() {
	$("#modifyRestaurantButton").click(function() {
		window.location.href = modifyRestaurantUrl;
	});

	$("#returnRestaurantList").click(function() {
		window.location.href = '/restaurantList';
	});

	$("#modifyRestaurantFoodListButton").click(function() {
		window.location.href = modifyRestaurantFoodListUrl;
	});
});
