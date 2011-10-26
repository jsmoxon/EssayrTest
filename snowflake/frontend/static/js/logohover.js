$(document).ready(function(){
	$("ul.page_nav").hide();
	$("img").hover(function(){
		$("ul.page_nav").slideToggle().delay(3800);
	    });
    });