import re
import jieba

def read_and_clean_file(input_file):
    lines = list(open(input_file, "r").readlines())
    lines = [clean_str(line) for line in lines]
    lines = [list(jieba.cut(line)) for line in lines]
    return lines

def clean_str(string):
    string = re.sub(r"[^\u4e00-\u9fff]", " ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip()

def load_positive_negative_data_files(data_file):
    # load data from files
    sentences = read_and_clean_file(data_file)
    return sentences

