# Parser for https://cpiber.github.io/CFG-Tester

from bs4 import BeautifulSoup, Tag


def parse_contents(tag: Tag) -> str:
    contents = str(tag.contents[0])
    if contents == 'ε':
        contents = ''
    return contents


def get_strings_from_file(file_name: str, max_length: int) -> list[str]:
    with open('file.html', 'r') as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    return sorted(
        (string for string in map(parse_contents, soup.find_all('span')) if len(string) <= max_length),
          key=lambda x: (len(x), x))
