 marker1 = new google.maps.Marker({ //stockholm
          map: map,
          draggable: true,
          animation: google.maps.Animation.DROP,
          position: {lat: 60.1841, lng: 24.8301}
        });
       //google.maps.event.addListenerOnce(marker1,'click', zooming);

	marker2 = new google.maps.Marker({ //aalto
          map: map,
          draggable: true,
          animation: google.maps.Animation.DROP,
          position: {lat: 59.349, lng: 18.067}
        });
        marker2.addListener('click', zooming);

	marker3 = new google.maps.Marker({ //morocco
          map: map,
          draggable: true,
          animation: google.maps.Animation.DROP,
          position: {lat: 33.969, lng: -6.8924}
        });
        marker3.addListener('click', zooming);

	marker4 = new google.maps.Marker({ //algiers
          map: map,
          draggable: true,
          animation: google.maps.Animation.DROP,
          position: {lat: 36.753, lng: 3.041283}
        });
        marker4.addListener('click', zooming);

	marker5 = new google.maps.Marker({// Pakistan
          map: map,
          draggable: true,
          animation: google.maps.Animation.DROP,
          position: {lat: 30.3753, lng: 69.3451}
        });
        marker5.addListener('click', zooming);

	marker7 = new google.maps.Marker({ //Iran
          map: map,
          draggable: true,
          animation: google.maps.Animation.DROP,
          position: {lat: 32.4279, lng: 53.6880}
        });
        marker7.addListener('click', zooming);


	marker8 = new google.maps.Marker({ //university of helsinki
          map: map,
          draggable: true,
          animation: google.maps.Animation.DROP,
          position: {lat: 60.1726, lng: 24.9510}
        });
        marker8.addListener('click', zooming);







////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




this.addingmarkers = function(map)
{

$.ajax({
        url: "../py/form.py/getRegions",
	type: 'POST',
        dataType: "json",
        cache: false,
        success: function(response){
				     if(response.success == false) {window.location='../login.htm';}
				     else {
					   markings = response.cdnlocations;
					   longitudes = response.longitude;
					   latitudes = response.latitude;
					    var i = 0;
  					    var create='';

					    while(i<idRegions.length) {
					   				  create +='<option value="'+nameRegions[i]+'" with="200px">'+nameRegions[i]+'</option>';
					  				  i += 1;
								       }
					    create +='</select>';
 					    $("#listeRegion").empty();	
					    $("#listeRegion").append(create);	
					    //alert(response.idcdn);
					
				       }	
 				     
 	                           }
						
});//end ajax 					



}



////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





this.loadCDNs = function()
{
//var listvalues = sessionStorage.getItem('auth');
//var auth = JSON.parse(listvalues);
var login = sessionStorage.login;//auth["login"];
var passwd = sessionStorage.passwd;//auth["password"];
$.ajax({
        url: "../py/form.py/getCDN",
	data: {user:login, password:passwd},
	type: 'POST',
        dataType: "json",
        cache: false,
        success: function(response){
				     if(response.success == false) {alert("Logging and password are incorrect!");window.location='../login.htm';}
				     else {
					   idCDN = response.idcdn;
					   nameCDN = response.namecdn;
					    var i = 0;
  					    var create='';
					    create +='<table  class="table table-striped">'
					    create +='<tr > <td ><label>CDN name:</label></td><td ><label>Modification:</label> </td><td ><label>Suppression:</label> </td></tr>'
					    while(i<idCDN.length) {
 						create +='<tr > <td ><label>'+nameCDN[i]+'</label></td><td ><a href="#" class="link"><label>Modify</label></a></label> </td><td ><label> <a  href="#" onclick="cdn.deleteCDN('+idCDN[i]+');" class="link"><label>Delete</label> </a> </label> </td></tr>'
					   	i = i + 1	
					    }

				            create +='</table>'
 					    $("#cdn_zone").empty();	
                                            $("#cdn_zone").append(create);	
					    //alert(response.idcdn);
					
				       }	
 				     
 	                           }
						
});//end ajax 					


}



////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



