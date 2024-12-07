# База знаний
rules = {
    "Africa": {
        "if": ["equator", "east"],
        "then": "Это Африка"
    },
    "NorthAmerica": {
        "if": ["umer", "west", "nonequator"],
        "then": "Это Северная Америка"
    },
    "SouthAmerica": {
        "if": ["equator", "west", "tropic"],
        "then": "Это Южная Америка"
    },
    "Eurasia": {
        "if": ["east", "umer", "nonequator"],
        "then": "Это Евразия"
    },
    "Australia": {
        "if": ["east", "nonequator", "tropic"],
        "then": "Это Австралия"
    },
    "Antarctica": {
        "if": ["tropic", "nonequator"],
        "then": "Это Антарктика"
    },
}



# Сбор фактов от пользователя
def get_facts():
    facts = {}
    questions = {
        "east": "Материк находится преимущественно в восточном полушарии? (да/нет): ",
        "equator": "Через материк проходит экватор? (да/нет): ",
        "umer": "На материке преимущественно умеренный климат? (да/нет): ",
    }

    for fact, question in questions.items():
        answer = input(question).strip().lower()
        facts[fact] = answer == "да"

    facts["west"] = not facts["east"]
    facts["nonequator"] = not facts["equator"]
    facts["tropic"] = not facts["umer"]

    return facts


def inputs(rules, facts):
    for rule, data in rules.items():
        conditions = data["if"]
        if all(facts.get(condition, False) for condition in conditions):
            return data["then"]
    return "Материк определить не удалось."


# Главная функция
def main():
    print("Добро пожаловать в экспертную систему!")
    facts = get_facts()
    result = inputs(rules, facts)
    print(result)


if __name__ == "__main__":
    main()
