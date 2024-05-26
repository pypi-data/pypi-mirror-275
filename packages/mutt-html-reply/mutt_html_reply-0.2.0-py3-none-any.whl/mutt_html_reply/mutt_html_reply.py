import html
import sys
from bs4 import BeautifulSoup, Doctype
import css_inline

HEADER_FIRST_SORT_LIST_COMPARISON = ['F','D','T','C','S']

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
    bs4_original_msg.html.unwrap() #type: ignore
    bs4_original_msg.body.unwrap() #type: ignore
    bs4_original_msg.head.extract() #type: ignore
    for element in bs4_original_msg.contents:
        if isinstance(element, Doctype):
            element.extract()

    bs4_original_headers = BeautifulSoup(_get_header_html(text_original_headers), 'html.parser')

    # Combine HTML together
    bs4_final = bs4_msg
    bs4_final.body.append(BeautifulSoup('<hr></hr>', 'html.parser')) #type: ignore
    bs4_final.body.append(bs4_original_headers) #type: ignore
    bs4_final.body.append(bs4_original_msg) #type: ignore

    # Write output
    with open(filepath_output, 'w') as file:
        file.write(str(bs4_final))


def _get_header_html(header_list):
    resorted_text = []
    for first in HEADER_FIRST_SORT_LIST_COMPARISON:
        for header in header_list:
            if header[0] == first:
                resorted_text.append(html.escape(header))
    html_headers = "<p>"
    for header in resorted_text:
        html_headers = html_headers + '<br>' + header
    html_headers = html_headers + "</p>\n"
    return html_headers



if __name__ == "__main__":
    main()
