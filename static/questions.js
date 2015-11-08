var NUM_QUESTIONS = 3;
var ANSWERS = {
    "q1": ["urban", "nature"],
    "q2": ["adventure", "chill"],
    "q3": ["warm", "cold"]
};

var hideInfoBar = function() {
    $(".info-bar").addClass("hidden");
}

var displayQuestion = function(questionNumber) {
    $(".question").removeClass("active");
    $(".question-" + (questionNumber+1)).addClass("active");
}

var startQuestions = function() {
    var question = 0;
    var answers = [];
    displayQuestion(question);

    var answerQuestion = function(evt) {
        var target = $(evt.currentTarget);
        var answer = target.data("answer");

        answers.push(answer);

        if (question < NUM_QUESTIONS-1) {
            console.log("question" + question);
            ++question;
            if (question > 0) {
                hideInfoBar();
            }
            displayQuestion(question);
        } else {
            queryStr = answers.join("+");
            window.location.replace("/experiences?query=" + queryStr);
        }
    }

    $(".question .option").on("click", answerQuestion);
}

$(function() {
    startQuestions();
});
