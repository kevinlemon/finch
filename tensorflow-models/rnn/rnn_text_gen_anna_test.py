from rnn_text_gen import RNNTextGen
import string


prime_texts = ['the']


if __name__ == '__main__':
    with open('./temp/anna.txt') as f:
        text = f.read()
    model = RNNTextGen(text)
    log = model.fit(prime_texts)
