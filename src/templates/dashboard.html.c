rides</h2>
                            <div class="line"></div>
                        </div><!-- end .page-sub-title -->
                        </div>


                        <div class="groupTwo"> 
                      <div class="clearfix"></div>

                        <div class="page-content bookRides">

                            <div class="rides-list">
                            {% if bookedRidesData is not None %}
                            {% for bookedRide in bookedRidesData.all %}
                               <article class="ride-box clearfix article_{{bookedRide.ride_id}}">

                                <div class="row">
                                    <div class="rideDAtetime col-sm-7">
                                      <i class="fa fa-calendar"></i>
                                      <span class="ridedatetimespan"> {{ bookedRide.ride_datetime }}</span>
                                    </div>
                                    <div class="rideNumber col-sm-5 text-right">
                                      {% if bookedRide.ride_id is not None %} <span class="rideNumberSpan1">Ride Number :</span> <span class="rideNumberSpan2">LYMO{{ bookedRide.ride_id }}</span>{% endif %}
                                    </div>
                                </div>

                                    <div class="ride-content inlines">
                                        <a href="#">
                                          <span class="fromAddress">{{ bookedRide.pickup_address }} </span>
                                          <span class="toAddress"> {{ bookedRide.drop_address }}</span>
                                        </a>
                                    </div>

                                    <ul class="ride-meta">
                                      <li>
                                        <span class="rideBy">ride by</span>
                                        <a href="#">{{ bookedRide.passenger_email }}</a>
                                      </li>
                                      <li>
					{{ bookedRide.status }}
                                      </li>
                                        <li class="ride-date">
                                            <a href="#" class="tooltip-link" data-original-title="Date" data-toggle="tooltip">
                                            </a>
                                        </li><!-- end .ride-date -->
                                        {% if bookedRide.ride_id is not None and  bookedRide.status != 'Ride Cancelled' %} 
                                       <li class="buttonStyle redbuttons cancelRideFormLI">
                                          <form method="POST" action="{% url 'ride:cancelRide' %}" class="cancelRideForm" style="padding: 0;position: relative;margin: 0;min-height: 0;top: 0">
                                          {% csrf_token %}
                                          <input type="hidden" name="ride_id" value="{{ bookedRide.ride_id }}">
                                          <input type="hidden" name="reason_to_cancel_ride" class="reason_to_cancel_ride" value="">
                                          <input type="hidden" name="cancellation_charges" class="cancellation_charges" value="">
                                          <input type="hidden" name="ride_status" value="9">
                                          <button type="button" class="btn btn-sm btn-warning CancelRideBTN" onclick="cancelRide('article_{{bookedRide.ride_id}}', {{bookedRide.ride_id}})" style="padding: 4px 5px 3px 5px;font-size: 10px;">
                                               <i class="fa fa-ban" aria-hidden="true"></i>
                                                Cancel Ride
                                            </button> 
                                          </form>
                                        </li>
                                        {% endif %}
                                      <!-- <li class="buttonStyle">
                                            <a href="#">
                                                <i class="fa fa-file-pdf-o"></i>
                                                Invoice
                                            </a>
                                        </li>
                    
                                        <li class="buttonStyle">
                                            <a href="#">
                                                <i class="fa fa-life-ring" aria-hidden="true"></i>
                                                Support
                                            </a>
					</li>  -->

                                    </ul><!-- end .ride-meta -->
                                    <div class="clearfix">&nbsp;</div>
                                    <h4 class="cancelRideRefundAmount" style="display: none;padding-top: 10px;border-top: 1px solid #b4acac;margin-top: 10px;text-align: center;"></h4>
                                    <div class="CancelRideReasonDIV" style="color:#000;padding: 20px 0px;text-align: center;display: none;">
                                      <label>Reason to cancel Ride</label>
                                      <select class="reason_to_cancel_ride_dropdown" name="cancelRideReason"></select>
                                      <!-- <textarea name="cancelRideReason" placeholder="Reason to Cancel Ride" class="cancelRideReason" style="width: 100%"></textarea> -->
                                      <div class="clearfix">&nbsp;</div>
                                      <button type="button" class="btn btn-danger confirmCancelRideBTN" onclick="confirmCancelRide('article_{{bookedRide.ride_id}}')">Confirm Cancellation of Ride</button>
                                      <button type="button" class="btn btn-success closeCancelRideBTN" onclick="closeCancelRide('article_{{bookedRide.ride_id}}')">close</button>
                                    </div>

                                </article><!-- end .ride-box -->
                            
                            {% endfor %}
                            {% endif %}

                                <div class="clearfix"></div>




                            </div><!-- end .events-list -->

                        </div><!-- end .page-content -->
                        </div>

                    </div>


<div class="col-md-5 col-sm-12 col-xs-12">

{% if companyStatus == False %}
  <form action="#" method="POST" class="col-md-4 pull-right" style="padding-top:200px;text-align: center">
   <h3 style="font-size: 24px;color: #fff;"> Company is Not Verified by Lymoserver<h3>
   <br />
   <h4 style="font-size: 20px;color: #fff;">Please Wait for sometime or contact <a href="lymousine.com" target="_blank">Lymousine</a></h4>
  </form>
 {% else %}

<form action="{% url 'ride:bookaridereque' %}" method="POST" class="col-md-4 pull-right" id="bookaRideform">
{% csrf_token %}
<div class="spaceOnly"><br><br><br><br><br><br><br><br><br><br></div>

         <div class="row form-with-labels text-center form_first_content">
         <h2 class="text-center rideBookTitle">Book Ride</h2>
          <div class="clearfix">&nbsp;</div> 
         <h2 class="text-center rideBookTitle" style="font-size: 20px">Enter Email or Mobile Number of your Contact</h2>          
          <div class="clearfix">&nbsp;</div>

          <div class="col-md-8 col-md-offset-2">
            <div class="form-group">
              <input type="text" name="email" value="" placeholder="email address" class="ajaxField required" aria-required="true" id="user_email" onclick="emailInit()"><span class="fa fa-person"></span>
            </div>
          </div>
          <div class="clearfix"></div>
          <h3 style="font-weight: bold;font-size: 13px;font-family: 'Fira Sans Condensed', sans-serif;">OR</h3>
          <div class="clearfix">&nbsp</div>
          
          <div class="col-md-8 col-md-offset-2">
            <div class="form-group">
              <input type="text" name="mobile" value="" placeholder="Mobile"  id="mobile" class="ajaxField required" aria-required="true"><span class="fa fa-phone"></span>
            </div>
          </div>

          <input type="button" value="Next" class="btn btn-lg btn-black btn-white aligncenter form_first_content_btn"  style="background: #1F1F1F;color: #fff;font-size: 16px;border-radius: 30px; margin: 0 auto;clear: both; display: block" onclick="check_user_lymousine()">

          
          <div class="checking_user_details_waiting">
            <button type="button" class="btn btn-lg btn-black btn-white aligncenter"style="background: #1F1F1F;color: #fff;font-size: 16px;border-radius: 30px; margin: 0 auto;clear: both; display: block">
              <img src="{% static 'assets/images/loading.gif' %}" class="pull-left" style="height: 19px">
             <div class="text-left" style="padding: 2px 20px;font-size: 15px;text-transform: none">Checking User Details...</div> 
             </button>
          </div>

           
           <h2 class="text-center rideBookTitle userFoundText" style="font-size: 16px;margin-top:10px"> <i class="fa fa-check"></i> User XYZ exist in the system. <br>Click <span style="font-size: 18px;cursor: pointer;" onclick="form_first_content_btn_submit()">here</span> to book a ride for the user XYZ</h2> 

           <h2 class="text-center rideBookTitle usernotFoundText" style="font-size: 16px;margin-top:10px"> <i class="fa fa-times"></i> User is not registered with Lymousine. <br>Please ask your Staff to register with Lymousine Portal.</h2> 
          <div class="clearfix"></div>
           
            

        </div>

        <div class="form_second_content">  
        <input type="hidden" value="" name="passengerid" id="passengerid">      
        <div class="menu-types">
          <a href="#" data-value="1" class="type-1 active">StandarD</a>
          <a href="#" data-value="3" class="type-3">LUXURY</a>
          <a href="#" data-value="2" class="type-2">SUV</a>
          <a href="#" data-value="4" class="type-4">VAN</a>
          <a href="#" data-value="5" class="type-5">Lymousine</a>
	  <a href="#" data-value="6" class="type-6">PET</a>

          <input type="hidden" name="type-value" id="type_value" class="type-value ajaxField" value="1">
        </div>
        <div class="row form-with-labels">
          <input type="hidden" name="from_country" id="from_country" value="">
          <input type="hidden" name="from_state" id="from_state" value="">
          <input type="hidden" name="from_city" id="from_city" value="">
          <input type="hidden" name="from_lat" id="from_lat" value="">
          <input type="hidden" name="from_lon" id="from_lon" value="">

          <input type="hidden" name="to_country" id="to_country" value="">
          <input type="hidden" name="to_state" id="to_state" value="">
          <input type="hidden" name="to_city" id="to_city" value="">
          <input type="hidden" name="to_lat" id="to_lat" value="">
          <input type="hidden" name="to_lon" id="to_lon" value="">
          <input type="hidden" name="country_id" id="country_id" value="">
          <input type="hidden" name="state_id" id="state_id" value="">
          <input type="hidden" name="city_id" id="city_id" value="">
          <input type="hidden" name="distance" id="distance" value="">
          <input type="hidden" name="cost" id="cost" value="">
          <input type="hidden" name="duration" id="duration" value="">




          <div class="col-md-6">
            <div class="form-group">
              <input type="text" id="origin-input" name="from" value="" placeholder="From Address..." class="ajaxField required" aria-required="true"><span class="fa fa-map-marker"></span>
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <input type="text" id="destination-input" name="to" value="" placeholder="To..." class="ajaxField"><span class="fa fa-map-marker"></span>
            </div>
          </div>
        </div>
        <div id="map"></div>
        <div class="row form-with-labels"> 

          <div class="col-md-6">
            <div class="form-group">
              <!--<input type="text" name="Ridedate" value="" placeholder="Date" class="ajaxField" id="datepicker"><span class="fa fa-calendar"></span>-->
             <div class="input-append date form_datetime">
               <input size="16" type="text" name="Ridedate" value="" readonly value="" placeholder="Date" class="ajaxField">
              <span class="add-on"><i class="icon-th"></i></span>
            </div>
            </div>
          </div>

           <div class="col-md-6">
            <div class="form-group">
      <select id="passengers-select" name="passengers" placeholder="No. of passengers" class="ajaxField">
	<option  value="1">1</option>
	<option  value="1">2</option>
	<option  value="1">3</option>
	<option  value="1">4</option>
      </select>
</div>
  </div>

  <div class="col-md-6">
    <div class="form-group">
      <input type="text" id="Remarks-input" name="Remarks" value="" placeholder="Remarks" class="ajaxField">
    </div>
  </div>
  
  <!-- <div class="col-md-6">
    <div class="form-group">
      <input type="text" name="Ridetime" value="" placeholder="Time" class="ajaxField" id="timepicker"><span class="fa fa-calendar"></span>
    </div>
  </div> -->
  <div class="clearfix">&nbsp;</div>
  <p class="text-center">for: <span class="finalFormUserCheck">XYZ</span></p>
  <div class="clearfix"></div>
  <div class="clearfix">&nbsp;</div>


</div>

<div style="clear: both; display: block; text-align: center">
 <button type="button" onclick="estimateRide()"  value="Book Ride" class="btn btn-lg btn-black btn-white aligncenter" style="background: #1F1F1F;color: #fff;font-size: 16px;border-radius: 30px; margin: 0 auto; " id="estimateRidebtn">Estimate Ride</button>
 </div>
<input type="hidden" id="type" name="type" value="2" class="ajaxField">




<button type="button" value="Book Ride" class="btn btn-lg btn-black btn-white aligncenter" style="background: #E63053;color: #fff;font-size: 16px;border-radius: 30px; margin: 0 auto; " id="estimateRidebtn">Submit</button>


<div class="clearfix"></div>
<div id="rideEstimatedCost">          
  <h3 h2 class="text-center rideEstimatedCostTitle" style="font-size: 20px"></h3>
</div>

<div id="rideBookedfail">          
  <h3 class="text-center rideBookTitle" style="font-size: 20px;margin-top: 30px">There is some problem booking the ride, Please check the Address Again or try again later.</h3>
</div>

</div>



 <div class="form_third_content"> 
   <h3>Select Payment Methods</h3>
  {% if paymentsDetailsData is not None %}
      {% for paymentsDetails in paymentsDetailsData.all %}
      <div class="col-md-12">
	<label style="cursor: pointer">
	  <input type="radio" name="paymentsDetails" value="{{ paymentsDetails.cardNumber }}"  onclick="changePayment('{{ paymentsDetails.cardNumber }}', '{{ paymentsDetails.nameOnCard }}', '{{ paymentsDetails.expirationDateMM }}', '{{ paymentsDetails.expirationDateYY }}', '{{ paymentsDetails.zipCode }}')" />
	  {{ paymentsDetails.nameOnCard }} / {{ paymentsDetails.cardNumber }}
	</label>
	</div>
	<div class="clearfix">&nbsp;</div>
      {% endfor %}
    {% endif %}

     <div id="payment-form">




<div class="panel-body">

<input type="hidden" name="estimatedCost" id="estimatedCost" value="">
<input type="hidden" name="zip_code" id="zip_code" value="">
	    <div class="form-group">
		<label for="cardNumber">
		    CARD HOLDER NAME</label>
		<div class="input-group">
		    <input type="text" data-braintree-name="cardholder_name" class="form-control" id="cardHolderName" placeholder="Card Holder Name"
			required autofocus />
		    <span class="input-group-addon"><span class="glyphicon glyphicon-user"></span></span>
		</div>
	    </div>
	    <div class="form-group">
		<label for="cardNumber">
		    CARD NUMBER</label>
		<div class="input-group">
		    <input type="text" data-braintree-name="number" class="form-control" id="cardNumber" placeholder="Valid Card Number"
			required autofocus />
		    <span class="input-group-addon"><span class="glyphicon glyphicon-lock"></span></span>
		</div>
	    </div>
	    <div class="row">
		<div class="col-xs-7 col-md-7">
		    <div class="form-group">
			<label for="expityMonth"> Expiry MM/YY</label>
			<div class="clearfix"></div>
			<div class="col-xs-6 col-lg-6 pl-ziro">
			    <input type="text" data-braintree-name="expiration_month" class="form-control" id="expityMonth" placeholder="MM" required />
			</div>
			<div class="col-xs-6 col-lg-6 pl-ziro">
			    <input type="text" data-braintree-name="expiration_year" class="form-control" id="expityYear" placeholder="YY" required /></div>
		    </div>
		</div>
		<div class="col-xs-5 col-md-5 pull-right">
		    <div class="form-group">
			<label for="cvCode">
			    CV CODE</label>
			<input type="password" class="form-control" id="cvCode" placeholder="CVV" required />
		    </div>
		</div>
	    </div>
	</div>

    </div>

  </div>                


<div id="rideBookedSuccess">
  <h2 class="text-center rideBookTitle" style="font-size: 25px;margin-bottom: 35px"><i class="fa fa-check"></i> Ride Booked Successfully</h2>
  <h3 h2 class="text-center rideBookTitle" style="font-size: 20px"> click <span onclick="form_reset()">here</span> to book another Ride</h3>
</div>




<div style="clear: both; display: block; text-align: center"> <button type="button"  class="btn btn-lg btn-black btn-white aligncenter" style="background: #1F1F1F;color: #fff;font-size: 16px;border-radius: 30px; margin: 0 auto;clear: both;" onclick="proceedToPayment()" id="paymentBtn">Proceed to Payment</button>

<div style="clear: both; display: block; text-align: center"> <button type="button"  class="btn btn-lg btn-black btn-white aligncenter" style="background: #1F1F1F;color: #fff;font-size: 16px;border-radius: 30px; margin: 0 auto;clear: both;"  id="bookrideBtn"  onclick="getToken()">Book Ride</button>
</div>
<!--<p class="text-center" onclick="form_reset()" id="cancelRide">Cancel Ride</p>-->

<p class="text-center"onClick="window.location.reload()" id="cancelRide">Cancel Ride</p>
</form>
{% endif %}

</div>



{% endblock container %}

{% block scripts %}
<script src="https://js.braintreegateway.com/js/braintree-2.32.1.min.js"></script>

<scipt src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/locale/af.js"></scipt>

 <script type="text/javascript">

  //var lymoServerURL = "http://127.0.0.1:5003/"
  var lymoServerURL = "{{ lymoSrvURL }}";
  var lymoServerURL_estimate = "{{ lymoRideEstimateURL }}";

  var vehicleTypeResponse = "";

  $(function () {
    $("#bookaRideform").validate({
        
    rules: {
    from: {
        required: true,
        },
    to: {
        required: true,
        },
    Ridedate:{
        required: true,
        },
    passengers: {
        required: true,
        },   
      },
      // submitHandler: function (form) {
      //     $("#bookrideBtn").html("Booking Ride...");
      //     return true;
      // } 
    });
    });

  function changePayment(cardNumber , nameOnCard , expirationDateMM , expirationDateYY, zip_code ){
      $("#cardHolderName").val(nameOnCard);
      $("#cardNumber").val(cardNumber);
      $("#expityMonth").val(expirationDateMM);
      $("#expityYear").val(expirationDateYY);
      $("#zip_code").val(zip_code);
      //getToken(nameOnCard, zip_code)
  }

function getToken(){
$("#bookrideBtn").html("<i class='fa fa-spinner fa-spin'></i> Booking Ride. Please wait...");
var cardHolderName = $("#cardHolderName").val();
var zip_code = $("#zip_code").val();

url = lymoServerURL+"lymousine/api/v2/thirdpartybttokengenration/"
data = {
"company": {{ companyDetailsData.lymo_profile_id }},
"lymo_user_id": {{ companyDetailsData.lymo_profile_id }},
"card_holder_name":cardHolderName,
"zip_code": zip_code,
"website" :"www.thirdparty.com"

}
$.ajax({
    url: url,
    type: "post",
    data: JSON.stringify(data),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',    
    success: function(response) {
      if (response['success']==true){


	var RideData = $("#bookaRideform").serialize();
	 $.ajax({
		url: "https://business.lymousine.com:1234/rides/bookaride",
		type: "post",
		data: RideData,                         
		success: function(Rideresponse) {
		  if(Rideresponse['data']['id']){

		    rideId = Rideresponse['data']['id'];
		     var client_token = response['bt_client_token'];
	console.log("setting up brain tree", client_token);
	//braintree.setup(clientToken,  'custom', {id: 'bookaRideform'});
	 //braintree.setup(clientToken, "dropin", { container: "payment-form" });

                 var client = new braintree.api.Client({clientToken: client_token});

                 var cardNumber = $("#cardNumber").val();
                 var exprityData = $("#expityMonth").val() + "/"+ $("#expityYear").val();

                  client.tokenizeCard({
                    number: cardNumber,
                    expirationDate: exprityData
                  }, function (err, nonce) {
                    // Send nonce to your server
                    transaction_amount = $("#estimatedCost").val();
                     paymentData = {
                        "ride_id":  rideId,
                        "transaction_amount": transaction_amount,
                        "nonce_from_the_client": nonce,
                        "customer_id": response['customer_id'],
                        }
                      $.ajax({
                        url: lymoServerURL+"lymousine/api/v2/thirdpartybtnonpayment/",
                        type: "post",
                        data: JSON.stringify(paymentData),
                        contentType: 'application/json; charset=utf-8',
                        dataType: 'json',    
                      success: function(response) {
                        $("#bookaRideform").submit();
                      }
                      });


                  });

                          }
                        }

                      });

              }                
            }
                
        });
}
  
   
   function form_first_content_btn_submit(){
    $(".form_first_content").hide();
    $(".form_second_content").show();
    $(".form_third_content").hide();
   }

   function form_reset(){
    $("#bookaRideform").trigger('reset');
    $(".form_first_content").show();
    $(".form_second_content").hide();
    $(".form_third_content").hide(); 
    $(".form_first_content_btn").show();
      $(".checking_user_details_waiting").hide();
      $(".userFoundText").hide();
      $("#rideBookedSuccess").hide();
      $("#rideBookedfail").hide();
       $("#bookrideBtn").html("Book Ride");
       $("#cancelRide").show();
        $("#bookrideBtn").hide();
        $("#paymentBtn").hide();
       $("#estimateRidebtn").show();
   }

   function emailInit(){
      $(".userFoundText").hide();
      $(".usernotFoundText").hide();
      $(".form_first_content_btn").show();
   }

   function check_user_lymousine(){
      $(".form_first_content_btn").hide();
      $(".checking_user_details_waiting").show();
      // setTimeout(function(){
      //    $(".checking_user_details_waiting").hide();
      //    $(".userFoundText").show();
      // }, 2000);      
      //event.preventDefault();
      if($('#user_email').val() != ''){
        var formData = {
          'email': $('#user_email').val() //for get email 
        };
      }else{
        var formData = {
          'mobile': $('#mobile').val() //for get email
        };
      }
      
      console.log(formData);
      $.ajax({
                url: lymoServerURL+"lymousine/api/v1/forcorporateapplication2/",
                type: "post",
                data: JSON.stringify(formData),
                contentType: "application/json",
                success: function(d) {
                    if(d.success == true){
                        userHtmlContent ='<div class="clearfix"></div>';
                        userHtmlContent +='<div class="clearfix">&nbsp;</div>';
                      userHtmlContent += '<i class="fa fa-check"></i> User <strong>'+d.data.email+'</strong> exist in the system.';
                      userHtmlContent +='<div class="clearfix">&nbsp;</div>';
                      userHtmlContent += "<div class='row userBox'>";
                      userHtmlContent += "<div class='userBoxInner'>";
                      userHtmlContent += "<div class='boxUser boxUser1'>";
                      if(d.data.picture && d.data.picture!='null'){
                         userHtmlContent += "<img src='"+lymoServerURL+d.data.picture+"' />";
                      }else{
                          userHtmlContent += "<img src='{% static 'assets/images/default_profile.png.140x140_q85_crop.png' %}' />";
                      }
                      userHtmlContent += "</div>";
                      if(d.data.email) {
                          userHtmlContent += "<div class='boxUser boxUser2' style=\"\n" +
                           +
                              "    text-align: left;\n" +
                              "\">" + d.data.name + "</br>" + d.data.email + "</div>";
                      }
                      if(d.data.mobile) {
                          userHtmlContent += "<div class='boxUser boxUser3'>" + d.data.name + "</br>" + d.data.mobile + "</div>";
                      }
                      userHtmlContent += "</div>";
                      userHtmlContent += "</div>";
                      userHtmlContent +='<div class="clearfix"></div>';
                       userHtmlContent +='<div style="font-size:140%;margin-top:10px"> Click <strong><span style="cursor: pointer;text-decoration:underline" onclick="form_first_content_btn_submit(';
                      userHtmlContent += "'"+d.data.email+"')";
                      userHtmlContent += '">here</span></strong> to book a ride for the user '+d.data.email+'</div>';
                      $(".userFoundText").html(userHtmlContent);
                      $(".finalFormUserCheck").html(d.data.email);
                      $(".checking_user_details_waiting").hide();
                      $(".userFoundText").show();
                      $("#passengerid").val(d.data.id);
                    }else{                      
                      //alert("This user is not Registered with lymousine. Please ask this User to register with Lymousine");
                      $(".checking_user_details_waiting").hide();
                      $(".form_first_content_btn").show();
                      $("#bookaRideform").trigger('reset');
                      $(".userFoundText").hide();

                      if(formData['email'] != ''){
                        var html = "<i class='fa fa-times'></i> User is not registered with Lymousine Portal. <br> Click <span style='cursor:pointer' onclick=\"sendInvitation( 'email', '"+formData['email']+"')\">here</span> to Invite "+formData['email'];
                      }else{
                         var html = "<i class='fa fa-times'></i> User is not registered with Lymousine Portal. <br> Click <span style='cursor:pointer' onclick=\"sendInvitation( 'sms', '"+formData['mobile']+"')\">here</span> to Invite "+formData['mobile'];
                      }
                      $(".usernotFoundText").html(html).show();
                    }
                }
                    
            });
   }



   function estimateRide(){

    $("#estimateRidebtn").html("Estimating Ride ...");
    datetimeFormatted = $("input[name='Ridedate']").val()
    datenew = moment(datetimeFormatted, 'DD MMMM YYYY hh:mm A').format('YYYY-MM-DD')
    timenew = moment(datetimeFormatted, 'DD MMMM YYYY hh:mm A').format('hh:mm:ss')
    console.log(datenew)

     var formData = {
            "country": $("input[name='from_country']").val(),
            "state": $("input[name='from_state']").val(),
            "city": $("input[name='from_city']").val(),
            "database_datetime": moment().format("YYYY-MM-DD hh:mm:ss"),
            "pickup": '"('+$("input[name='from_lat']").val()+','+ $("input[name='from_lon']").val() +')"',
            "dropoff": '"('+$("input[name='to_lat']").val()+','+  $("input[name='to_lon']").val() +')"',
            "vehicle_type": $("#type").val(),
            "date": datenew, 
            "time": timenew,
          } 


          $.ajax({
                url: lymoServerURL_estimate+"estimation_ride_amout",
                type: "post",
                data: (formData),
                //contentType: "application/json",
                success: function(d) {
                    if(d.sucess == true){
                       estimatedCost = d.totalamount;
                       country_id=d.country_id
                       state_id=d.state_id
                       city_id= d.city_id
                       distance=d.distance
                       duration=d.duration
                       total_amount=d.totalamount

                      // $("#rideBookedSuccess").show();
                       $("#rideBookedfail").hide();
                       $(".form_first_content").hide();
                       $(".form_third_content").hide();
                       //$(".form_second_content").hide();                       
                       $("#paymentBtn").show();
                       $("#bookrideBtn").hide();
                       $("#estimateRidebtn").html("Estimate Ride");
                       $("#cancelRide").show();

                       $("#estimatedCost").val(estimatedCost);
        
                      // load_bookedRide()
                       $(".rideEstimatedCostTitle").html("Estimated Cost for the Journey is : $"+ estimatedCost);
                       $("#rideEstimatedCost").show();  
                       $("#estimateRidebtn").hide();  
                       $("#country_id").val(country_id);  
                       $("#state_id").val(state_id);
                       $("#city_id").val(city_id);
                       $("#distance").val(distance);
                       $("#cost").val(estimatedCost);
                       $("#duration").val(duration);                     
     
                    }else{                      
                       $("#rideBookedfail").show();
                       $("#estimateRidebtn").html("Estimate Ride")
                      //  $("#rideBookedSuccess").hide()
                      //   $("bookrideBtn").html("Book Ride ")
                      console.log(d)
                    }
                     
                }
                    
            });

   }

   function load_bookedRide(){

        $.ajax({
                url: "/booked-rides",
                type: "post",
                success: function(d) {
                }
                    
            });

   }



   function sendInvitation(carrier, receiver){

            // Email Invitation
            if(carrier == 'email'){
                var formData = {
                  'email': receiver //for get email
                };
                 html = "Sending Invitation Email to "+receiver+" ..."
              }else{
                var formData = {
                  'mobile_number': $('#mobile').val() //for get email
                };
                 html = "Sending Invitation SMS to Modile no "+receiver+" ..."
              }
              $(".usernotFoundText").html(html);
            InvitationURL = lymoServerURL + 'lymousine/api/v1/appdownloademailsmssend/'
             $.ajax({
                url: InvitationURL,
                type: "post",
                data: JSON.stringify(formData),
                contentType: "application/json",
                success: function(d) {
                   if(d.success==true){
                       html = "<i class='fa fa-check'></i> Invitation successfully  send to "+receiver
                        $(".usernotFoundText").html(html);
                   }else{
                        html = "<i class='fa fa-errors'></i> There is some problem sending Email or Mobile SMS. Please contact Administrator"
                        $(".usernotFoundText").html(html);
                   }
                }
            });

   }

   function proceedToPayment(){
     $(".form_first_content").hide();
     $(".form_second_content").hide();
     $(".form_third_content").show();
     $("#bookrideBtn").show();
     $("#paymentBtn").hide();
   }


   function cancelRide(article_id, ride_id){
    $article_div = $("."+article_id);
    
    $article_div.find('.CancelRideBTN').html('<i class="fa fa-spinner"></i> Estimating Refund Amount ...')

    CancellationURL = lymoServerURL+"lymousine/api/v2/thirdpartyridecancellationcharges/"
    var CurrentDateTime = new moment().format("YYYY-MM-DDTHH:mm:ssZ");
    var formData = {
                  'ride_id': ride_id, //for get email
                  'local_datetime': CurrentDateTime
                };
    $.ajax({
                url: CancellationURL,
                type: "post",
                data: JSON.stringify(formData),
                contentType: "application/json",
                success: function(d) {
			console.log(d);
                  console.log(d['refund_amount']);
                   if(d['success'] != false){
                      $article_div.find(".CancelRideReasonDIV").show();

                       html = "Ride Amount: <strong>$"+d['ride_amount']+"</strong><br/> Amount to be refunded: <strong>$"+ d['refund_amount']+"</strong><br/> Cancellation Charges: <strong>$"+ d['cancellation_charges']+"</strong>";
                         $article_div.find('.cancelRideRefundAmount').show().html(html)
                         $article_div.find('.cancellation_charges').val(d['cancellation_charges']);
                         dropdownHTML =  "";                         
                         $.each(d['cancellation_business_rules'], function(index, value){
                          console.log(value, value['cancel_reason_name']);
                            dropdownHTML += "<option value='"+value['id']+"'>"+value['cancel_reason_name']+"</option>";
                         })
                         $article_div.find('.reason_to_cancel_ride_dropdown').html(dropdownHTML);
                         

                         $article_div.find('.CancelRideBTN').hide().html('<i class="fa fa-ban"></i> Cancel Ride')


                   }else{
			   console.log(d['ride_status']['ride_status_name'])
				   html = "<i class='fa fa-errors'></i> Ride Status is <strong>"+d['ride_status']['ride_status_name']+" </strong>("+d['ride_status']['ride_status_desc']+") hence same cannot be cancelled as Payment was not fullfilled";
                        $article_div.find('.cancelRideRefundAmount').show().html(html)
                        $article_div.find('.CancelRideBTN').html('<i class="fa fa-ban"></i> Cancel Ride')

                   }
                }
            });
    
   }

   function confirmCancelRide(article_id){
    $article_div = $("."+article_id);
    $cancelRideReasonVal = $article_div.find('.cancelRideReason').val();
    $article_div.find('.reason_to_cancel_ride').val($cancelRideReasonVal)
    $article_div.find('.confirmCancelRideBTN').html('<i class="fa fa-spinner fa-spin"></i> Cancelling Ride ...');
    $article_div.find('.cancelRideForm').submit();
   }

   function closeCancelRide(article_id){
    $article_div = $("."+article_id);
    $cancelRideReasonVal = $article_div.find('.cancelRideReason').val();
    $article_div.find(".CancelRideReasonDIV").hide();
    $article_div.find('.cancelRideRefundAmount').hide();
    $article_div.find('.CancelRideBTN').show().html('<i class="fa fa-ban"></i> Cancel Ride')
    $article_div.find('.confirmCancelRideBTN').html('Confirm Cancellation of Ride');
   }

   $(document).ready(function(){     
     $('.menu-types').on('click', 'a', function() {
      $(this).addClass('active').siblings('.active').removeClass('active');
      $(this).parent().find('.type-value').val($(this).data('value'));
      return false;
    });
   });



 </script>
 <script type="text/javascript" src="https://www.malot.fr/bootstrap-datetimepicker/bootstrap-datetimepicker/js/bootstrap-datetimepicker.min.js?t=20130302"></script>
        <script type="text/javascript">
            $(".form_datetime").datetimepicker({
                format: "dd MM yyyy - hh:mm",
                autoclose: true,
                todayBtn: true,
                pickerPosition: "bottom-left",
		startDate: new Date,
            });
        </script> 
  {% endblock scripts %}