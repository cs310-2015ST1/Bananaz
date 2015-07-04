
/**
 * Created by Haoran
 */
	$(document).ready(function() {

		// JQuery code to be added in here.

        $('#display_users').click(function(){

	         $.get('/update_users/', function(data){
	                   $('#all_users').html(data);

	               });
	    });



	});
