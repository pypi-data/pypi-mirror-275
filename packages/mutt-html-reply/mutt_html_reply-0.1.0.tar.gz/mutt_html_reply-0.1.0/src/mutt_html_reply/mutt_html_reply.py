import sys
from bs4 import BeautifulSoup
import css_inline

HEADER_FIRST_SORT_LIST_COMPARISON = ['F','D','T','C']

def main():
    """
    Create an Outlook-style HTML reply
    
    mutt-html-reply [html reply] [html original message] [headers to include in quote] [output path]
    """

    # Get filepaths
    filepath_reply = sys.argv[1]
    filepath_original_msg = sys.argv[2]
    filepath_original_headers = sys.argv[3]
    filepath_output = sys.argv[4]

    # Open files and get text
    with open(filepath_reply, 'r') as file:
        html_reply = file.read()
    with open(filepath_original_msg, 'r') as file:
        html_original_msg = file.read()
    with open(filepath_original_headers, 'r') as file:
        text_original_headers = file.read().splitlines()

    # Convert HTML text to BeautifulSoup object and inline all CSS
    bs4_msg = BeautifulSoup(css_inline.inline(html_reply),'html.parser')
    bs4_original_msg = BeautifulSoup(css_inline.inline(html_original_msg), 'html.parser')
    bs4_original_headers = BeautifulSoup(_get_header_html(text_original_headers), 'html.parser')

    # Combine HTML together
    bs4_final = BeautifulSoup()
    bs4_final.append(bs4_msg)
    bs4_final.append(BeautifulSoup('<hr>', 'html.parser'))
    bs4_final.append(bs4_original_headers)
    bs4_final.append(bs4_original_msg)

    # Write output
    with open(filepath_output, 'w') as file:
        file.write(str(bs4_final))


def _get_header_html(text):
    resorted_text = []
    for first in HEADER_FIRST_SORT_LIST_COMPARISON:
        for header in text:
            if header[0] == first:
                resorted_text.append(header)
    html_headers = "<p>\n"
    for header in resorted_text:
        html_headers = html_headers + '<br>' + header
    html_headers = html_headers + "\n</p>\n"
    return html_headers



if __name__ == "__main__":
    main()
