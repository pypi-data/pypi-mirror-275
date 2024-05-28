import requests
from QuizEngine4Trivia.models import TriviaDataModel, TriviaQuestionModel, TriviaApiModel, CurrentQuestionModel
from random import shuffle


class QuizEngine:
    api: TriviaApiModel
    trivia_data: TriviaDataModel

    question_number: int = 0
    score: int = 0
    current_question: TriviaQuestionModel

    track_answer: dict = {}

    def __init__(self) -> None:
        """
        QuestionEngine fetch question from trivia api
        """
        self.api = TriviaApiModel()
        self.trivia_data = TriviaDataModel()
        response = requests.get(url=self.api.url, params=self.api.url_params)
        response.raise_for_status()
        self.trivia_data.from_json(response.json()['results'])

    def still_has_questions(self):
        """
        Is there still more question in the deck
        :return boolean:
        """
        return self.question_number < len(self.trivia_data.questions)

    def next_question(self) -> CurrentQuestionModel:
        """
        Return the next question from deck
        :return str: question
        """
        self.current_question = self.trivia_data.questions[self.question_number]
        self.question_number += 1
        question = CurrentQuestionModel()
        question.category = self.current_question.category
        question.question = f"Q.{self.question_number}: {self.current_question.question}:"
        question.possible_answers = list(self.current_question.incorrect_answers)
        question.possible_answers.append(self.current_question.correct_answer)
        shuffle(question.possible_answers)
        return question

    def check_answer(self, user_answer: str) -> bool:
        """
        Checking user answer. Increase score if answer is correct

        :param user_answer: str
        :return boolean: Return True if answer is correct
        """

        if user_answer.lower() == self.current_question.correct_answer.lower():
            self.score += 1
            self.track_answer.update({self.question_number - 1: [True, user_answer]})
            return True
        else:
            self.track_answer.update({self.question_number - 1: [False, user_answer]})
            return False

    def get_result(self) -> list[tuple[bool, str, str]]:
        """
        Get the result of your answers

        :return list[tuple[bool, str, str]]:
        """
        result = []
        for k, v in self.track_answer.items():
            if v[0]:
                result.append((
                    True,
                    f"Q.{k} answer was correct : {self.trivia_data.questions[int(k)].question}",
                    f"{v[1]}"))
            else:
                result.append((
                    False,
                    f"Q.{k} answer was wrong : {self.trivia_data.questions[k].question}",
                    f"your answer {v[1]}\ncorrect answer {self.trivia_data.questions[int(k)].correct_answer}"))
        return result
