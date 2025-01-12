import pytest
from pages.main_page import MainPage

from data.test_data import FAQ_ANSWERS

class TestFAQ:

    @pytest.mark.parametrize(
        "question_number, expected_answer",
        [(i, FAQ_ANSWERS[i]) for i in range(len(FAQ_ANSWERS))]
    )
    def test_faq_click_question_show_answer(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)

        main_page.go_to_site()
        main_page.click_cookie_accept()

        main_page.click_faq_question(question_number)
        actual_answer = main_page.get_faq_answer_text(question_number)

        assert actual_answer == expected_answer, \
            f"Ответ на вопрос не совпадает с ожидаемым. Ожидалось: {expected_answer}, получено: {actual_answer}"