$('#enquiry_form').validate({
rules: {
    name: {
		required: true,
		minlength:3,
		maxlength:50,
		},
	email: {
		required: true,
		},
	subject: {
		required: true,		
		minlength:5,
		maxlength:255,
		},
	enquiry: {
		required: true,
		minlength:10,
		maxlength:255,
		},
    
	 
    },
    submitHandler: function(form) {
        //Prepare csrf token
		//var csrftoken = getCookie('csrftoken');
		//Collect data from fields
		var name = $('#name').val();
		var email = $('#email').val();
		var subject = $('#subject').val();
		var enquiry = $('#enquiry').val();

        $("#contact_form_button").html("<span style='color:#ccc !important;'><i class='fa fa-spinner fa-spin'></i> Submitting...</span>");

		$.ajax({
			type : "POST",
			crossDomain: true,
			data : {
			name : name,
			email : email,
			subject : subject,
			enquiry : enquiry
			},
			success : function(data) {
			enquiry_form = document.getElementById('enquiry_form');
            enquiry_form.style.display = 'none';
            $('input[type="text"],input[type="email"], textarea').val('');

            data_success = "Thank you for contacting Lymousine! "+'<br>'+"Our team will be in touch with you shortly.";
            $("#div_messages").html(" ");
            $("#div_messages").append("<div id='images' class='text-center'><img src='static/image/logo.png'></div><div id= 'success-alert' class='alert alert-custm alert-dismissable'>" + data_success + "</div>");
            $("#contact_form_button").html("Submit");
			//setTimeout(function () {
			//     $("#success-alert").alert('close');
			//}, 2000);
			// setTimeout(function(){
			//  $('#ContactModal').modal('hide')
			//}, 2000);

			},

			// handle a non-successful response
			//error : function(xhr,errmsg,err) {
			//console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
			//
			//}


			error: function (data) {
			console.log(data);
            $("#contact_form_button").html("Submit");
			//data_fail = 'Please fill all the fields';
			//$("#div_messages").html("");
			//$("#div_messages").append("<div id= 'danger-alert' class='alert alert-danger alert-dismissable'>" + data_fail + "</div>");
			}
		});

		return false;
    }
});


$('.close').on('click',function(){	
    enquiry_form = document.getElementById('enquiry_form');
    enquiry_form.style.display = 'block';
    $("#div_messages").html(" ");

})

$('#cont').on('click',function(){
	enquiry_form = document.getElementById('enquiry_form');
    enquiry_form.style.display = 'block';
    $("#div_messages").html(" ");
})
