# Chinese-collocation-complexity

本项目开源了如下论文所涉及的句法复杂度指标计算方法：   
This project releases the codes for computing the syntactic diversity, sophistication and complexity measures from the following articles:

1. 胡韧奋. 基于搭配的句法复杂度指标及其与汉语二语写作质量关系研究. 语言文字应用, 2021(1).   
Renfen Hu. Collocation-based Syntactic Complexity in Chinese Second Language Writing. <em>Applied Linguistics</em>, 2021(1).

2. Renfen Hu, Jifeng Wu, and Xiaofei Lu. Word-combination-based Measures of Phraseological Diversity, Sophistication and Complexity and Their Relationship to L2 Chinese Proficiency and Writing Quality. <em>Under Review</em>.

**环境 (Environments)**

*   **`Python 3.7+`**
*   **[`pyltp`](https://github.com/HIT-SCIR/pyltp)**

**运行 (Run the codes)**

```python
python main.py -i ./samples/ -o result.csv -mp path_to_LTP_models
```
