import unittest
from QuizEngine4Trivia import QuizEngine
from QuizEngine4Trivia.models import TriviaApiModel, TriviaDataModel, CurrentQuestionModel


class TestTriviaApiModel(unittest.TestCase):
    def test_trivia_api_model_trivia_difficulty_set_wrong_string(self):
        self.assertRaises(ValueError, lambda: TriviaApiModel(trivia_difficulty="wrong string"))

    def test_trivia_api_model_trivia_category_set_wrong_int(self):
        self.assertRaises(ValueError, lambda: TriviaApiModel(trivia_category=254))

    def test_trivia_api_model_trivia_amount_set_negative_int(self):
        self.assertRaises(ValueError, lambda: TriviaApiModel(trivia_amount=-20))

    def test_trivia_api_model_trivia_type_set_wrong_string(self):
        self.assertRaises(ValueError, lambda: TriviaApiModel(trivia_type="wrong string"))

    def test_set_url(self):
        amount = 20
        api = TriviaApiModel(trivia_amount=amount)
        self.assertIn(member="amount", container=api.url_params.keys())
        self.assertEqual(first=amount, second=api.url_params["amount"])


class TestQuizEngine(unittest.TestCase):
    app: QuizEngine | None = None
    question = None

    @classmethod
    def setUpClass(cls):
        cls.app = QuizEngine()

    def test_check_return_of_next_question_is_current_question_model(self):
        self.app.question_number = 0
        self.question = self.app.next_question()
        self.assertIs(
            expr1=type(self.question),
            expr2=CurrentQuestionModel,
            msg="returned question is not a CurrentQuestionModel!"
        )

    def test_check_return_of_next_question_is_not_none(self):
        self.app.question_number = 0
        self.question = self.app.next_question()
        self.assertIsNotNone(obj=self.question, msg="returned question is None!")

    def test_answer_question_false(self):
        self.app.question_number = 0
        self.question = self.app.next_question()
        self.assertFalse(self.app.check_answer(self.app.current_question.incorrect_answers[0]))

    def test_answer_question_true(self):
        self.app.question_number = 0
        self.question = self.app.next_question()
        self.assertTrue(self.app.check_answer(self.app.current_question.correct_answer))

    def test_still_has_questions_true(self):
        length = len(self.app.trivia_data.questions)
        self.app.question_number = 0
        self.assertTrue(self.app.still_has_questions())

    def test_still_has_questions_false(self):
        length = len(self.app.trivia_data.questions)
        self.app.question_number = length
        self.assertFalse(self.app.still_has_questions())

    def test_get_result_return_type(self):
        self.app.question_number = 0
        self.app.next_question()
        self.app.check_answer(self.app.current_question.incorrect_answers[0])
        self.app.next_question()
        self.app.check_answer(self.app.current_question.correct_answer)
        result = self.app.get_result()
        self.assertIs(type(result), list)
        self.assertIs(type(result[0]), tuple)
        self.assertIs(type(result[0][0]), bool)
        self.assertIs(type(result[0][1]), str)
        self.assertIs(type(result[0][2]), str)
