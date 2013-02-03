$(document).ready(function(){
    var desiredMenuItem = document.location.hash.replace("#", "") || 'home';
    $(".nav a[rel=" + desiredMenuItem + "]").parent().addClass("active");
})