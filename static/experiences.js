var geocoder = null;
var origin = null;
var destination = null;

var selectedExperience = {
    title: null,
    location: null,
};

var processOrigin = function(position) {
    origin = [position.coords.latitude, position.coords.longitude];
    console.log("got origin:", origin);
};

var processDestination = function(result, status) {
    var loc = result[0].geometry.location;
    var lat = loc.lat();
    var lng = loc.lng();
    destination = [loc.lat(), loc.lng()];
    departureDate = getCurrentDate();

    window.location.replace("/flights?" +
                            "origin=" + origin[0] + "+" + origin[1] +
                            "&destination=" + destination[0] + "+" + destination[1] +
                            "&persons=1" +
                            "&departure=" + departureDate +
                            "&arrival=2015-11-21");
};

var redirectToFlights = function(evt) {
    var target = $(evt.currentTarget);
    console.log(target);
    destinationAddress = selectedExperience.location;

    geocoder.geocode({'address': destinationAddress}, processDestination);
}

var closeExperienceInfo = function(evt) {
    var reserve = $(evt.currentTarget);
    console.log(reserve);
    $(".experiences").removeClass("hidden");
    $(".reserve").addClass("hidden");
    $(".close-info").addClass("hidden");
}

var renderExperienceInfo = function(evt) {
    $(".close-info").removeClass("hidden");
    var $element = $(".reserve");

    var originSplit = selectedExperience.location.split(", ");
    $element.find(".origin .city").text("Helsinki");
    $element.find(".origin .country").text("Finland");

    var destinationSplit = selectedExperience.location.split(", ");
    $element.find(".destination .city").text(selectedExperience.title);
    $element.find(".destination .country").text(destinationSplit[1]);

    $element.find(".experiment-info p").html(selectedExperience.price);
}

var openExperienceInfo = function(evt) {
    var button = $(evt.currentTarget);
    var experience = button.parents(".experience");

    selectedExperience.title    = experience.data("title");
    selectedExperience.location = experience.data("location");
    selectedExperience.price    = experience.data("price") + " &euro;";

    renderExperienceInfo();

    $(".experiences").addClass("hidden");
    $(".reserve").removeClass("hidden")
}

$(function() {
    geocoder = new google.maps.Geocoder();

    $(".experience-info").click(openExperienceInfo);
    $(".close-info").click(closeExperienceInfo);
    $(".book").click(redirectToFlights);

    if ("geolocation" in navigator) {
        console.log("Location available");
        navigator.geolocation.getCurrentPosition(processOrigin);
    } else {
        console.log("Location is not available.");
    }

});
