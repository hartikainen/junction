var NUM_QUESTIONS = 3;
var ANSWERS = {
    "q1": ["nature", "urban"],
    "q2": ["adventure", "chill"],
    "q3": ["warm", "cold"]
};

var createTitle = function(answers) {
    return answers[0].capitalize() +
        " or " +
        answers[1].capitalize() +
        "?";
}

var renderQuestion = function(questionNumber) {
    var answers = ANSWERS["q" + (questionNumber+1)];
    var opt1 = $(".question button.option-1");
    var opt2 = $(".question button.option-2");
    var title = createTitle(answers);

    $(".question p").text(title);
    opt1.text(answers[0]);
    opt1.data("answer", answers[0]);
    opt2.text(answers[1]);
    opt2.data("answer", answers[1]);

}

var startQuestions = function() {
    var question = 0;
    var answers = [];
    renderQuestion(question);

    var answerQuestion = function(evt) {
        var target = $(evt.currentTarget);
        var answer = target.data("answer");

        answers.push(answer);

        ++question;
        if (question < NUM_QUESTIONS) {
            renderQuestion(question);
        } else {
            queryStr = answers.join("+");
            window.location.replace("/experiences?query=" + queryStr);
        }
    }

    $(".answer button").on("click", answerQuestion);
}

$(function() {
    startQuestions();
});
