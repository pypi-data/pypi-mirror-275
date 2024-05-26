from dataclasses import dataclass


@dataclass
class TriviaQuestionModel:
    type: str
    difficulty: str
    category: str
    question: str
    correct_answer: str
    incorrect_answers: list[str]


class TriviaApiModel:
    trivia_dict: dict = {}
    # trivia_encode: str | None  # Not in use
    trivia_difficulty_dict = {
        "Any Difficulty": None,
        'easy': 'easy',
        'medium': 'medium',
        'hard': 'hard'
    }
    trivia_category_dict = {
        "Any Category": None,
        "General Knowledge": 9,
        "Entertainment: Books": 10,
        "Entertainment: Film": 11,
        "Entertainment: Music": 12,
        "Entertainment: Musicals & Theatres": 13,
        "Entertainment: Television": 14,
        "Entertainment: Video Games": 15,
        "Entertainment: Board Games": 16,
        "Science & Nature": 17,
        "Science: Computers": 18,
        "Science: Mathematics": 19,
        "Mythology": 20,
        "Sports": 21,
        "Geography": 22,
        "History": 23,
        "Politics": 24,
        "Art": 25,
        "Celebrities": 26,
        "Animals": 27,
        "Vehicles": 28,
        "Entertainment: Comics": 29,
        "Science: Gadgets": 30,
        "Entertainment: Japanese Anime & Manga": 31,
        "Entertainment: Cartoon & Animations": 32
    }
    trivia_type_dict = {
        "Any type": None,
        "Multiple choices": "multiple",
        "True / False": "boolean",
    }
    trivia_encode_dict = {
        "Default Encoding": None,
        "Legacy URL Encoding": "urlLegacy",
        "URL Encoding (RFC 3986)": "url3986",
        "Base64 Encoding": "base64"
    }

    url: str = "https://opentdb.com/api.php"
    url_params: dict = {}

    def __init__(
            self,
            trivia_amount: int = 10,
            trivia_difficulty: str | None = None,
            trivia_category: int | None = None,
            trivia_type: str | None = None,
            # encode=None # Not in use
    ) -> None:
        """

        :param trivia_amount: int between 0 and 101
        :param trivia_difficulty:
        :param trivia_category:
        """
        locals_vars = locals()
        locals_vars.pop('self')
        # Validate params
        if trivia_difficulty is not None and trivia_difficulty not in self.trivia_difficulty_dict.values():
            raise ValueError(f"trivia_difficulty value is wrong")
        if trivia_category is not None and trivia_category not in self.trivia_category_dict.values():
            raise ValueError(f"trivia_category value is wrong")
        if trivia_amount is not None and (trivia_amount <= 0 or trivia_amount > 100):
            raise ValueError(f"trivia_amount value is wrong")
        if trivia_type not in ["boolean", "multiple"] and trivia_type is not None:
            raise ValueError(f"trivia_type value is wrong")
        key: str
        for key, value in locals_vars.items():
            if value is not None:
                self.url_params.update({key.split('_')[1]: value})


class TriviaDataModel:
    data: list[TriviaQuestionModel] = []

    def from_json(self, question_list):
        for question in question_list:
            self.data.append(TriviaQuestionModel(**question))


class CurrentQuestionModel:
    question: str = ""
    possible_answers: list = []
