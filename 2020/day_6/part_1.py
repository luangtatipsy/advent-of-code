def count_survey_for_anyone(survey):
    cleaned_survey = "".join(survey.split("\n"))

    return len(set(cleaned_survey))


def main(surveys):
    total_count = 0

    for survey in surveys:
        total_count += count_survey_for_anyone(survey)

    return total_count


if __name__ == "__main__":
    with open("input.txt") as f:
        surveys = [
            line.strip() for line in f.read().split("\n\n") if line.strip() != ""
        ]

    total_count = main(surveys)
    print(total_count)

