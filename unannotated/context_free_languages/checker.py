import itertools as it
from typing import Iterator, Callable
from languages import ps4_q2_crunchy, extra_101
from cfg_tester_parser import get_strings_from_file



def is_in_language(s: str, language: Callable[[str], bool]) -> bool:
    return language(s)


def generate_all_strings(max_length: int) -> Iterator[str]:
    for str_length in range(max_length+1):
        for s in it.product('01', repeat=str_length):
            yield ''.join(s)


def generate_strings_from_language(language: Callable[[str], bool], max_length: int) -> Iterator[str]:
    for s in generate_all_strings(max_length):
        if is_in_language(s, language):
            yield s


def compare_language_to_file(language: Callable[[str], bool], file_name: str, max_length: int, print_answers: bool=False) -> None:
    program_answer = list(generate_strings_from_language(language, max_length))
    file_answer = get_strings_from_file(file_name, max_length)
    if print_answers:
        print(program_answer)
        print(file_answer)
    print(f'Answers equal up to length {max_length}: {program_answer == file_answer}')


if __name__ == '__main__':
    # for max_length in range(0, 8):
        # compare_language_to_file(ps4_q2_crunchy, 'file.html', max_length, True)
    
    for s in generate_strings_from_language(extra_101, 12):
        print(s)