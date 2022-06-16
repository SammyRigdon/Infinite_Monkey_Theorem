import glob
from datetime import datetime
from multiprocessing import Pool
from random import choice


# Import text from file to list
def import_text(user_file, mode):
    character_list = []
    document_list = []

    with open(user_file, 'r', encoding='UTF-8') as document:
        for char in document.read():
            character_list.append(char)
    # Word mode
    if mode == 'word':
        new_word = ''
        for char in character_list:
            if char == ' ':
                if new_word != '':
                    document_list.append(new_word)
                    new_word = ''
                document_list.append(char)
            elif char == '\n':
                if new_word != '':
                    document_list.append(new_word)
                    new_word = ''
                document_list.append('\n')
            else:
                new_word += char
    # Character Mode
    elif mode == 'char':
        document_list = character_list

    return document_list


# Typing based on characters
def monkey_type_char(monkey, test_char):
    ascii_chars = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "`",
        "~",
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "-",
        "_",
        "=",
        "+",
        "[",
        "{",
        "]",
        "}",
        ";",
        ":",
        '"',
        "'",
        "<",
        ">",
        "?",
        "\\",
        ".",
        ",",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        "\n",
        " ",
        "\t",
        "\r",
        "\b",
        "\v",
        "€",
        "À",
        "Á",
        "“",
        "é",
        "â",
        "£",
        "",
        "—",
        "’",
        "”",
        "‘",
        "ë",
        "|",
        "î",
        "Æ",
        "ü",
        "à",
        "ê",
        "è",
        "æ",
        "ô",
        "/"]
    start_time = datetime.now()
    print(f'{monkey} initiated the search for "{test_char}" at {start_time}')
    while True:
        typed_char = choice(ascii_chars)
        if typed_char == test_char:
            end_time = datetime.now()
            print(
                f'{monkey} found "{test_char}" at {end_time}, taking a total time of {end_time - start_time}')
            return typed_char


# Typing based on words
def monkey_type_word(monkey, test_word):
    ascii_chars = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "`",
        "~",
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "-",
        "_",
        "=",
        "+",
        "[",
        "{",
        "]",
        "}",
        ";",
        ":",
        '"',
        "'",
        "<",
        ">",
        "?",
        "\\",
        ".",
        ",",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        "\n",
        " ",
        "\t",
        "\r",
        "\b",
        "\v",
        "€",
        "À",
        "Á",
        "“",
        "é",
        "â",
        "£",
        "",
        "—",
        "’",
        "”",
        "‘",
        "ë",
        "|",
        "î",
        "Æ",
        "ü",
        "à",
        "ê",
        "è",
        "æ",
        "ô",
        "/"]
    monkey_word = ''
    longest_found = ''
    starting_date_time = datetime.now()
    print(f'{monkey} initiated search for "{test_word}" at {starting_date_time}')
    while True:
        monkey_word += choice(ascii_chars)
        # Is generated word same length as test word?
        if len(monkey_word) == len(test_word):
            # Is it the correct word
            if monkey_word == test_word:
                ending_date_time = datetime.now()
                print(
                    f'{monkey} found "{monkey_word}" at {ending_date_time} taking a total of '
                    f'{ending_date_time - starting_date_time} to find it')
                return monkey_word
            # Reset string if not
            else:
                monkey_word = ''

        # Is word shorter than test word?
        elif len(monkey_word) < len(test_word):
            # Is it typed correctly so far?
            if monkey_word == test_word[0:len(monkey_word)]:
                if len(monkey_word) > len(longest_found):
                    longest_found = monkey_word
                    print(
                        f'{monkey} found "{monkey_word}" from "{test_word}" at {datetime.now()}')
                continue
            # if not reset string
            else:
                monkey_word = ''

        # Reset if neither above since it must be longer
        else:
            monkey_word = ''


# Compare typed text to original
def compare_texts(user_text):
    with open(user_text, 'r', encoding='UTF-8') as hamlet:
        hamlet_string = hamlet.read()

    with open('Output/_monkeyTyping.txt', 'r', encoding='UTF-8') as monkeyHamlet:
        monkey_hamlet_string = monkeyHamlet.read()

    return hamlet_string == monkey_hamlet_string


# Generate a random list of monkeys equal to the length of text
def get_monkeys(test_list):
    # Master list of monkey names
    monkey_names = [
        "Charles",
        "Bod",
        "Bob",
        "Sebastian",
        "Wazoo",
        "Frankie",
        "Sherlie",
        "Gravyboat",
        "Monarch",
        "Maximilian",
        "Peanut Butter",
        "Milkshake",
        "Muffin",
        "Champion",
        "Patricia",
        "CC",
        "Patches",
        "Xena",
        "Sherbert",
        "Horace",
        "Bradley",
        "Clara",
        "Murphy",
        "Karina",
        "Emerald",
        "Sammy",
        "Sunni",
        "MJ",
        "Larry",
        "Lisa",
        "Brenda",
        "Denda",
        "Orbley",
        "John",
        "Skylar",
        "Tyler",
        "Lindsay",
        "Sarah",
        "Kylie",
        "Ramsey",
        "JJ",
        "Lisa A",
        "Barbara",
        "Lucille",
        "Keewee",
        "Lemon",
        "Blueberry",
        "Clementine",
        "Plum",
        "Juniper",
        "Bojangles"
    ]

    # Randomly assign monkeys based on the number of entries in testList
    monkey_assignments = []
    for _ in test_list:
        random_monkey = choice(monkey_names)
        monkey_assignments.append(random_monkey)

    # Count occurrences of each monkey in characters and add to dict
    monkey_counts = {}
    for monkey in monkey_names:
        monkey_counts[monkey] = monkey_assignments.count(monkey)

    # Count monkeys
    max_typed = max(monkey_counts.values())
    best_monkey = max(monkey_counts, key=monkey_counts.get)
    least_typed = min(monkey_counts.values())
    worst_monkey = min(monkey_counts, key=monkey_counts.get)

    return monkey_assignments, monkey_counts, max_typed, best_monkey, least_typed, worst_monkey


# Execute functions based on user decisions
def main():
    # Get all text files
    all_txt_files = glob.glob('Samples/*.txt')

    # Retrieve user input for file
    user_file = ''
    for index, file in enumerate(all_txt_files, 0):
        if file != '_monkeyTyping.txt':
            print(f'{index}: {file}')
    while True:
        user_choice = input(
            "Please type the number of the file you want the monkeys to type: ")
        try:
            user_file = all_txt_files[int(user_choice)]
            break
        except IndexError:
            print(f"{user_choice} is not a possible selection")
            continue

    # Retrieve user input for mode
    while True:
        user_mode_choice = input(
            "0: Character Mode-Each monkey will look for one character at a time(faster)\n"
            "1: Word Mode-Each monkey must type the whole word correctly before getting a new one(slower)\n"
            "2: Exit\n"
            "Please type the number of the typing mode you wish to use, then press enter: ")

        # Char mode
        if user_mode_choice == '0':
            # Get Starting Time
            execution_start_time = datetime.now()

            # Get Text as a list
            print("Getting Text")
            test_list = import_text(user_file, 'char')

            # Get monkeys assignments and typing count
            print("Getting Monkeys")
            monkey_assignments, monkey_counts, most_typed, best_monkey, least_typed, worst_monkey = get_monkeys(
                test_list)

            # start processes
            arguments = list(zip(monkey_assignments, test_list))
            monkeys = Pool()
            results = monkeys.starmap(monkey_type_char, arguments)
            monkeys.close()

            # Type results
            with open('Output/_monkeyTyping.txt', 'w', encoding='UTF-8') as monkeyHamlet:
                monkeyHamlet.writelines(results)

            # Check Results
            if compare_texts(user_file):
                print(
                    f"The monkeys have successfully recreated {user_file}\n\nThe best monkey is {best_monkey} who "
                    f"typed {most_typed} characters\n{worst_monkey} really needs to step up their typing as they typed "
                    f"{least_typed} characters\n\nFull results are below, praise the monkeys accordingly: ")
                for monkey, count in monkey_counts.items():
                    print(f"{monkey}: {count} characters")

            else:
                print(
                    f"The monkeys have failed to recreate {user_file}\n\nBlame {best_monkey} who typed {most_typed} "
                    f"characters of this atrocity\n{worst_monkey} is also to blame, had they typed more than "
                    f"{least_typed} characters maybe it would've be better\n\nFull statistics are below. "
                    f"Shame the appropriately")

                for monkey, count in monkey_counts.items():
                    print(f"{monkey}: {count} characters")

            execution_end_time = datetime.now()
            execution_time = execution_end_time - execution_start_time
            print(
                f"The monkeys took this long to type {user_file}: {execution_time}\n")
            input('Press enter to exit')
            break

        # Word mode
        elif user_mode_choice == '1':
            # Get Starting Time
            execution_start_time = datetime.now()

            # Get Text as a list
            print("Getting Text")
            test_list = import_text(user_file, 'word')

            # Get monkeys assignments and typing count
            print("Getting Monkeys")
            monkey_assignments, monkey_counts, most_typed, best_monkey, least_typed, worst_monkey = get_monkeys(
                test_list)

            # start processes
            arguments = list(zip(monkey_assignments, test_list))
            monkeys = Pool()
            results = monkeys.starmap(monkey_type_word, arguments)
            monkeys.close()

            # Type results
            with open('Output/_monkeyTyping.txt', 'w', encoding='UTF-8') as monkeyTyping:
                monkeyTyping.writelines(results)

            # Check Results
            if compare_texts(user_file):
                print(
                    f"The monkeys have successfully recreated {user_file}\n\nThe best monkey is {best_monkey} who typed"
                    f" {most_typed} words\n{worst_monkey} really needs to step up their typing as they typed "
                    f"{least_typed} words\n\nFull results are below, praise the monkeys accordingly: ")
                for monkey, count in monkey_counts.items():
                    print(f"{monkey}: {count} words")

            else:
                print(
                    f"The monkeys have failed to recreate {user_file}\n\nBlame {best_monkey} who typed {most_typed} "
                    f"words of this atrocity\n{worst_monkey} is also to blame, had they typed more than "
                    f"{least_typed} words maybe it would've be better\n\nFull statistics are below. "
                    f"Shame them appropriately")

                for monkey, count in monkey_counts.items():
                    print(f"{monkey}: {count} characters")

            execution_end_time = datetime.now()
            execution_time = execution_end_time - execution_start_time
            print(
                f"The monkeys took this long to type {user_file}: {execution_time}")
            input('Press enter to exit')
            break

        else:
            break


if __name__ == '__main__':
    main()
