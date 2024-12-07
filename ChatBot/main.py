import random
import os

# Файл для хранения ответов
RESPONSES_FILE = "responses.txt"


# Загрузка словаря из файла
def load_responses():
    responses = {}
    if os.path.exists(RESPONSES_FILE):
        with open(RESPONSES_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if ":" in line:
                    question, answers = line.split(":", 1)
                    responses[question] = answers.split(",")
    return responses


# Сохранение словаря в файл
def save_responses(responses):
    with open(RESPONSES_FILE, "w", encoding="utf-8") as file:
        for question, answers in responses.items():
            file.write(f"{question}:{','.join(answers)}\n")


# Функция для получения ответа
def chatbot_response(user_input, responses):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return None


# Основная функция
def main():
    print("Привет! Я чат-бот Болтун. Как тебя зовут?")
    name = input("Я: ")
    print(f"Приятно познакомиться, {name}! Напиши мне что-нибдь")
    # Загружаем словарь
    responses = load_responses()

    while True:
        user_input = input(f"{name}: ")
        if user_input.lower() in ["пока", "до свидания", "мне пора"]:
            print("Болтун: Пока! Хорошего дня!")
            break

        # Попытка найти ответ
        response = chatbot_response(user_input, responses)

        if response:
            print(f"Болтун: {response}")
        else:
            print("Болтун: Я не знаю, что ответить. Как мне ответить на это?")
            new_response = input(f"{name}: ")
            if new_response.strip():
                # Добавляем новый вопрос-ответ
                if user_input.lower() not in responses:
                    responses[user_input.lower()] = []
                responses[user_input.lower()].append(new_response)
                save_responses(responses)  # Сохраняем обновленный словарь
                print(f"Болтун: Спасибо, {name}, буду знать!")
            else: print(f"Ещё вопросы, {name}?")


if __name__ == "__main__":
    main()
