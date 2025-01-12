import pytest
import allure
from pages.main_page import MainPage
from data.test_data import FAQ_ANSWERS

@allure.feature("Тесты FAQ")
class TestFAQ:

    @allure.story("Проверка отображения ответов на вопросы FAQ")
    @allure.title("Проверка ответа на вопрос")
    @allure.description("""
        Тест проверяет, что при клике на вопрос FAQ отображается правильный ответ.
        Шаги:
        1. Перейти на сайт.
        2. Принять куки.
        3. Кликнуть на вопрос FAQ.
        4. Проверить, что текст ответа совпадает с ожидаемым.
    """)
    @pytest.mark.parametrize(
        "question_number, expected_answer",
        [(i, FAQ_ANSWERS[i]) for i in range(len(FAQ_ANSWERS))]
    )
    def test_faq_click_question_show_answer(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)

        with allure.step("Перейти на сайт"):
            main_page.go_to_site()

        with allure.step("Принять куки"):
            main_page.click_cookie_accept()

        with allure.step(f"Кликнуть на вопрос FAQ №{question_number}"):
            main_page.click_faq_question(question_number)

        with allure.step("Получить текст ответа"):
            actual_answer = main_page.get_faq_answer_text(question_number)

        with allure.step("Проверить, что текст ответа совпадает с ожидаемым"):
            assert actual_answer == expected_answer, \
                f"Ответ на вопрос не совпадает с ожидаемым. Ожидалось: {expected_answer}, получено: {actual_answer}"