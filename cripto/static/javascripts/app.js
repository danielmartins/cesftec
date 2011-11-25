/* Foundation v2.1.1 http://foundation.zurb.com */
$(document).ready(function() {

	/* Use this js doc for all application specific JS */

	/* PLACEHOLDER FOR FORMS ------------- */
	/* Remove this and jquery.placeholder.min.js if you don't need :) */
	
	$('input, textarea').placeholder();
	
	$("#doCesarEncrytp").click(function(){
	    $('#cesarForm').submit();
	});
	
	$("#doCesarUncrytp").click(function(){
	    var data = { msg: $("#msgEncriptografada").html() };
        $.get("/cesftec/cesar/decrypt/", data, function(data, textStatus, xhr){
            $('#msgDescriptografada').html(data);
            console.log(textStatus);
        });
    });
    
	/* DISABLED BUTTONS ------------- */
	/* Gives elements with a class of 'disabled' a return: false; */
	
	
});
