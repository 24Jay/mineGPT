import re

class SimpleTokenizer:
    def __init__(self, text_file="data/the-verdict.txt"):
        with open(text_file, "r", encoding="utf-8") as f:
            raw_text = f.read()
        result = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
        processed = [item.strip() for item in result if item.strip()]

        self.UNK_TOKEN = "<|unk|>"
        self.END_TOKEN = "<|end|>"

        self.all_tokens = sorted(list(set(processed)))
        self.all_tokens.extend([self.UNK_TOKEN, self.END_TOKEN])
        
        self.word_to_int = {w:i for i, w in enumerate(self.all_tokens)}
        self.int_to_word = {i:w for w, i in self.word_to_int.items()}

    def encode(self, text):
        result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        processed = [item.strip() for item in result if item.strip()]
        return [self.word_to_int[item] if item in self.all_tokens else self.word_to_int["<|unk|>"] for item in processed]

    def decode(self, ids):
        text = " ".join([self.int_to_word[i] for i in ids])
        text = re.sub(r'\s+([,.?"()\'!])', r'\1', text)
        return text
    
    def __len__(self):
        return len(self.all_tokens)