import re
from collections import Counter

class WordCounter:
    def __init__(self):
        # ストップワードのリスト
        self.stop_words = set([
            'a', 'an', 'the', 'and', 'or', 'but', 'is', 'are', 'was', 'were', 'be', 'been',
            'to', 'of', 'in', 'on', 'with', 'for', 'as', 'by', 'at', 'from', 'that', 'this'
        ])
    
    def count_words(self, text):
        # 正規表現を使って単語を抽出し、小文字に変換
        words = re.findall(r'\b\w+\b', text.lower())
        # ストップワードを除去
        filtered_words = [word for word in words if word not in self.stop_words]
        return Counter(filtered_words)

    def add_stop_words(self, words):
        # ストップワードを追加
        self.stop_words.update(words)
        