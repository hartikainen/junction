var toggleExperience = function(evt) {
    var experience = $(evt.currentTarget);
    experience.toggleClass("active");
}

$(function() {
    $(".experience").click(toggleExperience);
});
