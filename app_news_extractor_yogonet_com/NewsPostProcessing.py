import pandas as pd
from datetime import datetime
class NewsPostProcessing:
    @staticmethod
    def add_metrics(df):
        # Datetime
        df['Datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')        

        # Word count in Title
        df['Word_count_in_title'] = df['Title'].apply(lambda text: len(text.split()))

        # Character count in Title
        df['Character_count_in_title'] = df['Title'].apply(lambda text: len(text.replace(' ','')))

        # List of words that start with a capital letter in Title
        df['List_of_words_that_start_with_a_capital_letter_in_Title'] = df['Title'].apply(
            lambda text: len(list(filter(lambda word: word[0].isupper(),text.split())))
            )
        return df