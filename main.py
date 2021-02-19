import glob
import argparse
import pandas as pd
from utils_text import *
from syntactic import getSyntacticIndices

''' 

本项目开源了如下论文所涉及的句法复杂度指标计算方法：
This project releases the codes for computing the syntactic complexity measures from the following article:

胡韧奋. 基于搭配的句法复杂度指标及其与汉语二语写作质量关系研究. 语言文字应用, 2021(1).
Hu Renfen. Collocation-based Syntactic Complexity in Chinese Second Language Writing. Applied Linguistics, 2021(1).

python main.py -i ./samples/ -o result.csv -mp path_to_LTP_models

'''

# set the args
parser = argparse.ArgumentParser()
parser.add_argument("-mp", "--modelpath", dest="model_path", type=str, metavar='<str>', required=True,
                    help="The path to the LTP models")
parser.add_argument("-i", "--input", dest="input_path", type=str, metavar='<str>', required=True,
                    help="The path to the input directory")
parser.add_argument("-o", "--output", dest="output_path", type=str, metavar='<str>', required=True,
                    help="The path to the output file")
args = parser.parse_args()

model_path = args.model_path
input_path = args.input_path
output_file = args.output_path

segmentor, postagger, parser = load_ltpmodel(model_path)
input_files = glob.glob(input_path + '*.txt')
index_data = {}

for file in input_files:

    filename = os.path.split(file)[-1].replace('.txt', '')
    text = open(file, 'r').read()
    if len(text) < 20:
        print(filename, 'too short and pass...')
        continue
    text_dict = text_process(text, segmentor, postagger, parser)
    indices = getSyntacticIndices(text_dict)
    index_data[filename] = indices

df = pd.DataFrame.from_dict(index_data, orient='index')
df.to_csv(output_file)
release_ltpmodel(segmentor, postagger, parser)
