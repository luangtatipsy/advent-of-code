def count_survey_for_everyone(survey):
    cleaned_survey = survey.split("\n")
    questions = set("".join(cleaned_survey))
    count = 0

    for question in questions:
        is_everyone_answers = []

        for survey in cleaned_survey:
            is_everyone_answers.append(bool(survey.count(question)))

        if all(is_everyone_answers):
            count += 1

    return count


def main(surveys):
    total_count = 0

    for survey in surveys:
        total_count += count_survey_for_everyone(survey)

    return total_count


if __name__ == "__main__":
    with open("input.txt") as f:
        surveys = [
            line.strip() for line in f.read().split("\n\n") if line.strip() != ""
        ]

    total_count = main(surveys)
    print(total_count)

