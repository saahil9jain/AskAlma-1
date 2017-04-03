/*
Template: Logistic Pro Modern Multipurpose Services Template
Author: ScriptsBundle
Version: 1.0
Designed and Development by: ScriptsBundle
*/

var $ = jQuery.noConflict();


jQuery(document).ready(function($) {

        // Dropdown Menu

        if ( $().superfish ) { $('#primary-menu ul ul, #primary-menu ul .mega-menu-content').css('display', 'block'); }

        $('#primary-menu .mega-menu-content, #primary-menu ul ul').each( function( index, element ){

            var $menuChildElement = $(element);
            var windowWidth = $(window).width();
            var menuChildOffset = $menuChildElement.offset();
            var menuChildWidth = $menuChildElement.width();
            var menuChildLeft = menuChildOffset.left;

            if(windowWidth - (menuChildWidth + menuChildLeft) < 0) {
                $menuChildElement.addClass('menu-pos-invert');
            }

        });

        if ( $().superfish ) {

            $('#primary-menu > ul, #primary-menu > div > ul,.top-links > ul').superfish({
                popUpSelector: 'ul,.mega-menu-content,.top-link-section',
                delay: 250,
                speed: 350,
                animation: {opacity:'show'},
                animationOut:  {opacity:'hide'},
                cssArrows: false
            });

        }


        $( '#primary-menu ul li:has(ul)' ).addClass('sub-menu');
        $( '.top-links ul li:has(ul) > a' ).append( ' <i class="icon-angle-down"></i>' );
        $( '.top-links > ul' ).addClass( 'clearfix' );

        $("#primary-menu.sub-title > ul > li").hover(function() {
            $(this).prev().css({ backgroundImage : 'none' });
        }, function() {
            $(this).prev().css({ backgroundImage : 'url("images/icons/menu-divider.png")' });
        });

        // Scroll to Top

		$(window).scroll(function() {
			if($(this).scrollTop() > 450) {
                $('#gotoTop').fadeIn();
			} else {
				$('#gotoTop').fadeOut();
			}
		});

		$('#gotoTop').click(function() {
			$('body,html').animate({scrollTop:0},400);
            return false;
		});


       
});