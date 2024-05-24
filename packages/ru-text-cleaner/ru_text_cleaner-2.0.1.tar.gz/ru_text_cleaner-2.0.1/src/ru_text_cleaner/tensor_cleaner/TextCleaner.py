import tensorflow

from ._html_cleaner import clean_html
from ._spaces_cleaner import clean_spaces
from ._to_morpheme import text_to_morphems
from ._to_lower import to_lower_text
from ._emoji_cleaner import clean_emoji
from ._clean_stopwords import clean_stopwords
from ._punctuation_cleaner import clean_punctuation


class TextCleaner:
    def __init__(self, spaces=True, punctuation=True, html=True, emoji=True, lower=True,
                 stop_words=True, morpheme=True):

        """
        Метод __init__ инциализирует экземпляр класса TextCleaner

        self.spaces = spaces - Необходимо ли удалять пробелы
        self.punctuation = punctuation - Необходимо ли удалять пунктуацию
        self.html = html - Необходимо ли удалять теги HTML
        self.emoji = emoji - Необходимо ли удалять Emoji
        self.lower = lower - Необходимо ли переводить текст в нижний регистр
        self.stopwords = stop_words - Необходимо ли удалять стоп слова
        self.morpheme = morpheme - Необходимо ли заменять слова на морфемы

        """

        self.spaces = spaces
        self.punctuation = punctuation
        self.html = html
        self.emoji = emoji
        self.lower = lower
        self.stopwords = stop_words
        self.morpheme = morpheme

        self.to_lower = to_lower_text
        self.clean_emoji = clean_emoji
        self.clean_punctuation = clean_punctuation
        self.clean_html = clean_html
        self.clean_space = clean_spaces
        self.clean_stopwords = clean_stopwords
        self.to_morpheme = text_to_morphems

    def clean_text(self, text: tensorflow.string) -> str:

        """ Метод clean_text форматирует текст в зависимости от поставленных флагов"""

        ct = text.numpy().decode()
        print('Ваша строка:', ct)
        if self.lower:
            ct = self.to_lower(ct)
        if self.emoji:
            ct = self.clean_emoji(ct)
        if self.html:
            ct = self.clean_html(ct)
        if self.punctuation:
            ct = self.clean_punctuation(ct)
        if self.stopwords:
            ct = self.clean_stopwords(ct)
        if self.morpheme:
            ct = self.to_morpheme(ct)
        if self.spaces:
            ct = self.clean_space(ct)

        print('Итог:', ct)
        return tensorflow.strings.as_string(ct)

    def clean_texts(self, texts: []) -> []:

        clean_texts = []

        """ Метод clean_texts форматирует массив в зависимости от поставленных флагов"""

        for text in texts:
            ct = text.numpy().decode()
            if self.lower:
                ct = self.to_lower(ct)
            if self.emoji:
                ct = self.clean_emoji(ct)
            if self.html:
                ct = self.clean_html(ct)
            if self.punctuation:
                ct = self.clean_punctuation(ct)
            if self.stopwords:
                ct = self.clean_stopwords(ct)
            if self.morpheme:
                ct = self.to_morpheme(ct)
            if self.spaces:
                ct = self.clean_space(ct)
            clean_texts.append(tensorflow.as_string(ct))

        return clean_texts

    def to_vector(self, text: tensorflow.string) -> []:
        return tensorflow.strings.split(self.clean_text(text))

    def to_vectors(self, text: []) -> []:
        clean_texts = self.clean_texts(text)
        answer = []
        for t in clean_texts:
            answer.append(tensorflow.strings.split(t))
        return answer
