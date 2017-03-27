
 // created  on 06/04/2016
//@author: bagaa miloud 


loading=function(){//start classe


   this.load_myframe=function(  ){//start function
	
	 $("#zone").empty();  

    $("#btn").click(function(  ){
							
							
							
							
	$("#txt_nbre").attr('disabled','disabled');
	var nbre=$("#txt_nbre").val();  
	var create="";
	var x=1;
	 create+='<table with="100% id="mytab" >';
	  create+='<tr>';
   create+='<td ">VMW name: </td>';
    create+='<td "> Type: </td>';
	    create+='<td s"> Flavor:</td>';
		 create+='</tr>';
while(x <= nbre) {
   create+='<tr>';
  	 create+='<td> <input type="text" name="textfield" id="txt'+x+'"/> </td>';
        
	 
   
  	 create+='<td><select style="width:155px;" name ="mytype"  id="mytype" ></select> </td>';
	 
   
  	 create+='<td><select style="width:155px;" name ="myflav"  id="myflav" ></select> </td>';
   create+='</tr>';
   
    x++;
}
create+='<tr><td></td><td></td><td align="right"><input type="button" name="btn-send" value="Send" id="btn1" onclick="loading.sending();"></td> </tr> <tr></tr> <tr>  <td colspan="4"><span> <div id="progressBar"><div></div></div></td></span></tr></table>';
	
	
	
	
	
	
	
	$("#zone").empty();
	
$("#zone").append(create);	




//chargement de type





if (nbre != 0)
{// load table
////////1:loading type////////////////////////////////////////
	var create1='';
 $.ajax({
        url: "php/load_table.php",
	    data: {action:"1"},
	    type: 'POST',
        dataType: "json",
        cache: false,
		 beforeSend : function(){
        progressBar(100, $('#progressBar'));
    },
        success: function(liste)
								{
								
								
								
								create1+='<option value=0  selected >List of type</option>';
								
								$.each(liste,function (i,val)
										{
										
										create1+='<option  value="'+val.id+'" >' + val.type+'</option>';
										}
									  );
									
								
								
								
								$("select[name*='mytype']").empty();
								$("select[name*='mytype']").append(create1);

								
								}
			
});//end ajax 

////2:load flavoor//////////////////////
	
			var create2='';
 $.ajax({
        url: "php/load_table.php",
	    data: {action:"2"},
	    type: 'POST',
        dataType: "json",
        cache: false,
        success: function(liste)
								{
								
								
								
								create2+='<option value=0  selected >List of flavoor</option>';
								
								$.each(liste,function (i,val)
										{
										
										create2+='<option  value="'+val.id+'" >' + val.myflav+'</option>';
										}
									  );
									
								
								
								
								$("select[name*='myflav']").empty();
								$("select[name*='myflav']").append(create2);


								
								}
			
});//end ajax 					

	}//load tables


																							});//.click
  
	
	
}//end function load_myframe	

this.refreshe=function()
{   $("#txt_nbre").val('');
	$("#txt_nbre").removeAttr('disabled');
	$("#zone").empty();
	
	}

this.sending=function()
{//start function
/*
var x=1;
while (x<= $("#txt_nbre").val())
{
 $.ajax({
    url: "../php/addvm.php",	                
	data: {action:"1",VM:$('#txt'+x+')'.val()   },
	type: 'POST',
    dataType: "json",
    cache: false,
	  success: function(liste) {
		 //alert(liste);
		if (liste==1) {alert(' The VMWare with has the name'+$('#txt'+x+')'.val()+ 'is added with succes');} 
		if (liste==0) {alert('there is problem in adding the VMW');}
		
                               }
	});
x++;
}//end while
*/

















}//end sending



 



}//end classe