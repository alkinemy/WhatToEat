$(document).ready(function() {
	$('#whatToDoButton').click(function() {
		$.ajax({
			type: 'POST',
			url: '/whatToDo/',
			data: '',
			dataType: 'json',
			success: function(data) {
			},
			error: function(xhr,err) { 
                alert("readyState: "+xhr.readyState+"\nstatus: "+xhr.status); 
            } 
		});
	});	

	$('#addToDoButton').click(function() {
	});

});
