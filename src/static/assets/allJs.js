

 

 
 
    function openNav() {
        document.getElementById("mySidenav").style.width = "250px";
        //document.getElementById("main").style.marginLeft = "250px";
    }

    function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
        //document.getElementById("main").style.marginLeft = "0";
    }

 


    $(function () {
    $("#contactForm").validate({
		
    rules: {
    name: {
		required: true,
		minlength:3,
		maxlength:50
		},
	email: {
		required: true
		},
	Contact: {
		required: true,
		number:true,
		minlength:9,
		maxlength:10
		},
	Message: {
		required: true,
		minlength:10,
		maxlength:200
		}
    
	 
    },
	
     messages: {
            },
            submitHandler: function (form) {
            return false;
			
            }
    });
    });
	




 		$(function () {
                // $('#datetimepicker3').datetimepicker({
                //     format: 'LT'
                // });
            });
	
function convertTo24Hour(time) {
    var hours = parseInt(time.substr(0, 2));
    if(time.indexOf('am') != -1 && hours == 12) {
        time = time.replace('12', '0');
    }
    if(time.indexOf('pm') != -1 && hours < 12) {
        time = time.replace(hours, (hours + 12));
    }
    time = time.replace(/(am|pm)/,'');
    return time
}

$(function () {
$('#estimater').validate({
    rules: {
    pickup: {
    	required: true
    	},
    dropoff: {
    	required: true
    	},
    //vehicle_type: {
    //	required: false
    //	},
    date: {
    	required: true
    	},
    time: {
    	required: true
    	}
    },
    messages: {
            },

    submitHandler: function(form) {
		console.log('onchange time')
		var start_time = convertTo24Hour($("#time").val().toLowerCase());		
        var pickup = $('#origin-input').val();
        var dropoff = $('#destination-input').val();
        var vehicle_type = $("input[name='vehicle_type_name']:checked").val();     
        var date = $('#date').val();
		var time = start_time       
        console.log(typeof(start_time))
        var start_time =$.trim(start_time);
        var date = new Date(date);
        var database_date = (date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate() );
        var database_datetime = database_date+' '+start_time+':00.000000'
        console.log('database_datetime')
        console.log(database_datetime)
        console.log(vehicle_type)

	    if(vehicle_type==null){
            console.log('if')
		    $('#modalVehicleType').modal('show');         
            return false;
		}
        else{
            $('#modalVehicleType').modal('hide');         
        }
		var country = $('#country').val();
		var state = $('#state').val();
		var city = $('#city').val();
        //var vehicle_type = $("input[name='vehicle_type']:checked").val();

        console.log('line 130')

        $(".estimate_btn").html("<span style='color:#ccc !important;'><i class='fa fa-spinner fa-spin'></i> Fetching fare data...</span>");
		$.ajax({
			type : "POST",
			crossDomain: true,
			data : {
                pickup : pickup,
                form_name : 'estimatorForm',
                dropoff : dropoff,
                country : country,
                state : state,
                city : city,
                vehicle_type : vehicle_type,
                date : date,
                time : time,
                database_datetime:database_datetime
			},
			success : function(data) {
                console.log('success')
                console.log(data)
            estimatedCost = "Thanks";
            $(".estimatedCost").html(" ");
            $(".estimate_btn").html("ESTIMATE")

            if(data == "1"){            
                $(".estimatedCost").append("<label>Pick-up and Drop-off address can not be same.</label>");
                }
            else if (data == "0"){              
                $(".estimatedCost").append("<label>Currently service not available in your region.</label>");


            }
            else{
                $(".estimatedCost").append("<label>Estimated Fare: $"+data+"</label>");
            }

            },
			error: function (data) {
			    console.log(data);
                console.log('fail')
			}
		});
		return false;
    }

});
   
    $("input[name='vehicle_type_name']").change(function(){  
        $('.VehicleDropDown li.active').removeClass('active');
        $(this).parent('li').addClass('active');

    });



});





 






	
