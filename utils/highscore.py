from settings import HIGH_SCORE_FILE


def load_high_score():

    try:

        with open(HIGH_SCORE_FILE, "r") as file:

            return int(file.read())

    except:

        return 0


def save_high_score(high_score):

    with open(HIGH_SCORE_FILE, "w") as file:

        file.write(str(high_score))