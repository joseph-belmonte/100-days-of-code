"""This module contains the Question class."""""


class Question:
    """This class is responsible for creating a question object."""

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


new_q = Question("text", "answer")
