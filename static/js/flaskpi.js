$(document).ready(function(){
    var desiredMenuItem = 'home' || document.location.hash.replace("#", "");
    $(".nav a[rel=" + desiredMenuItem + "]").parent().addClass("active");
})