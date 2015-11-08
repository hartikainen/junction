var redirectToFlights = function(evt) {
    window.location.replace("/flights?" +
                            "origin=123.123+456.456" +
                            "destination=123.123+456.456" +
                            "persons=1" +
                            "departure=2015-11-10" +
                            "arrival=2015-11-21");
}

var closeExperienceInfo = function(evt) {
    var reserve = $(evt.currentTarget);
    console.log(reserve);
    $(".experiences").removeClass("hidden");
    $(".reserve").addClass("hidden")
}

var openExperienceInfo = function(evt) {
    var experience = $(evt.currentTarget);
    console.log(experience);
    $(".experiences").addClass("hidden");
    $(".reserve").removeClass("hidden")
}

$(function() {
    $(".experience-info").click(openExperienceInfo);
    $(".close-info").click(closeExperienceInfo);
    $(".book").click(redirectToFlights);
});
