from src.ru_text_cleaner import TensorCleaner
from src.ru_text_cleaner import SimpleCleaner
import tensorflow

simple = SimpleCleaner()
tensor = TensorCleaner()

text1 = 'Какая-то    форматирования-нибудь \n\n\t строка-либо то-то'
text2 = tensorflow.as_string('Какая-то    форматирования-нибудь \n\n\t строка-либо то-то')

print(tensor.clean_text(text2).numpy().decode())




