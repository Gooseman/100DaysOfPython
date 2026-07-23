from quiz_master.requester import get_request
from quiz_master.trivia_question_model import TriviaQuestionModel

class QuestionSource:
    BASE_TRIVIA_URL = "https://opentdb.com"
    BASE_QUESTION_URL = f"{BASE_TRIVIA_URL}/api.php?type=boolean"
    TOKEN_URL = f"{BASE_TRIVIA_URL}/api_token.php?command=request"

    NUM_QUESTIONS_PARAM = "amount"
    TOKEN_PARAM = "token"

    def __init__(self):
        self._question_data = []
        self._token = ""

    def get_questions(self, number_of_questions) -> list[TriviaQuestionModel]:
        """
        Fetches a specified number of trivia questions from the Open Trivia Database API.
        """

        if not self._token:
            self._get_session_token()

        if not self._token:
            print("Unable to fetch questions without a valid session token.")
            return []

        code, questions = self._request_questions(number_of_questions)

        # print(f"Response code from question request: {code}")
        # print(f"Number of questions retrieved: {len(questions)}")
        # print(f"Questions data: {questions}")

        if 0 == code:
            self._question_data = self._parse_questions(questions)
        else:
            self._report_question_failure_result(code)
            self._question_data = []

        return self._question_data

    def _get_session_token(self):
        """
            Retrieves a session token from the Open Trivia Database API. The session token is used to ensure
            that the questions fetched are unique and not repeated. If the token retrieval is successful, it
            is stored in the instance variable `_token`. If the retrieval fails, an error message is printed and the
            `_token` remains an empty string.
        """
        token_response = get_request(self.TOKEN_URL)

        if token_response is None:
            print("Failed to retrieve session token.")
            return

        self._token = self._parse_token_response(token_response)

    def _parse_token_response(self, response) -> str:
        """
            Parses the response from the Open Trivia Database API for a session token.  The response is expected to be a
            JSON object with a "response_code" and a "token" field. If the "response_code" is 0, the method returns the 
            "token". Otherwise, it returns an empty string.

            Args:
                response (dict): The JSON response from the Open Trivia Database API.

            Returns:
                str: The session token if the response code is 0, otherwise an empty string.
        """
        if response.get("response_code") == 0:
            return response.get("token", "")

        return ""

    def _request_questions(self, number_of_questions) -> tuple[int, list[dict]]:
        """
            Requests a specified number of trivia questions from the Open Trivia Database API using the session token.

            Args:
                number_of_questions (int): The number of trivia questions to request.

            Returns:
                tuple: A tuple containing the response code and a list of trivia questions if the request is successful,
                otherwise a tuple containing the response code and an empty list.
        """

        questions_response = get_request(self._build_question_url(number_of_questions))

        if questions_response is None:
            print("Failed to retrieve questions.")
            return -1, []

        if questions_response.get("response_code") == 0:
            return 0, questions_response.get("results", [])

        return questions_response.get("response_code"), []

    def _build_question_url(self, number_of_questions) -> str:
        """
            Constructs the URL for requesting trivia questions from the Open Trivia Database API.

            Args:
                number_of_questions (int): The number of trivia questions to request.
            Returns:
                str: The URL for requesting trivia questions.
        """
        num_questions_param = f"{self.NUM_QUESTIONS_PARAM}={number_of_questions}"
        token_param = f"{self.TOKEN_PARAM}={self._token}" if self._token else ""

        return f"{self.BASE_QUESTION_URL}&{num_questions_param}&{token_param}"

    def _parse_questions(self, questions_data) -> list[TriviaQuestionModel]:
        """
            Parses the list of trivia questions received from the Open Trivia Database API and converts them into a list
            of `TriviaQuestionModel` instances.

            Args:
                questions_data (list): A list of trivia question data received from the API.

            Returns:
                list: A list of `TriviaQuestionModel` instances representing the trivia questions.
        """
        return [TriviaQuestionModel(question) for question in questions_data]

    def _report_question_failure_result(self, response_code):
        """
            Reports the result of a failed question request to the Open Trivia Database API.

            Args:
                response_code (int): The response code from the Open Trivia Database API indicating the reason for
                failure.
        """
        if response_code == 1:
            print("There are not enough new questions available in the database.")
        elif response_code == 2:
            print("Invalid parameter in the request.")
        elif response_code == 3:
            print("Token not found.")
        elif response_code == 4:
            print("Token empty. Please reset the token.")
        else:
            print(f"Unknown error occurred with response code: {response_code}")
