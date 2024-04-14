import PyPDF2
import re

def extract_keywords_and_definitions(pdf_path, start_page, stop_page, keywords):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Check if the start_page and stop_page are within the range of pages
        if start_page < 0 or start_page >= len(pdf_reader.pages):
            raise ValueError("Invalid start page number")
        
        if stop_page < 0 or stop_page >= len(pdf_reader.pages):
            raise ValueError("Invalid stop page number")
        
        # Initialize text with empty string
        text = ""
        
        # Extract text from each page starting from the specified start_page
        for page_num in range(start_page, stop_page + 1):
            text += pdf_reader.pages[page_num].extract_text()

    # Define a dictionary to store keywords and their context sentences
    keyword_context = {}

    # Extract context sentences for each keyword
    for keyword in keywords:
        # Find all occurrences of the keyword in the text
        keyword_occurrences = [m.start() for m in re.finditer(re.escape(keyword), text, re.IGNORECASE)]
        for keyword_index in keyword_occurrences:
            # Extract the sentence containing the keyword
            sentence_start = text.rfind('.', 0, keyword_index) + 1
            sentence_end = text.find('.', keyword_index) + 1
            keyword_sentence = text[sentence_start: sentence_end]
            # Extract the sentence before the keyword
            before_sentence_end = max(0, text.rfind('.', 0, sentence_start))
            before_sentence_start = text.rfind('.', 0, before_sentence_end) + 1
            before_sentence = text[before_sentence_start: sentence_start]
            # Strip leading and trailing whitespace characters, including periods
            before_sentence = before_sentence.strip('.').strip()
            keyword_sentence = keyword_sentence.strip('.').strip()
            # Store the keyword and its context sentences
            keyword_context[keyword] = {
                "before_sentence": before_sentence,
                "keyword_sentence": keyword_sentence,
                "after_sentence": text[sentence_end: text.find('.', sentence_end) + 1].strip('.').strip()
            }
            # Break after finding the first occurrence of the keyword
            break

    return keyword_context

# Example usage
pdf_path = r"C:\Users\risha\Desktop\projects\Projects\PDFSearch\gov.pdf"
start_page =  524 + 52
stop_page = 531 + 52  # Specify the page number where scanning should stop
keywords = [
    "Democratic National Committee (DNC)",
    "Democratic Party",
    "linkage institutions",
    "national chairperson",
    "national convention",
    "platform",
    "Republican National Committee (RNC)",
    "Republican Party",
    "robocalls",
    "social media",
    "war chest"
]

keyword_context = extract_keywords_and_definitions(pdf_path, start_page, stop_page, keywords)
for keyword, context in keyword_context.items():
    print(f"Keyword: {keyword}")
    print(f"Before Sentence: {context['before_sentence']}")
    print(f"Keyword Sentence: {context['keyword_sentence']}")
    print(f"After Sentence: {context['after_sentence']}\n")
