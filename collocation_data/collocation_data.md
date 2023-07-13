# CCA中文搭配知识库

**1. 原始数据**

本目录提供了中文搭配助手(Chinese Collocation Assisant)所依赖的搭配知识库原始数据，包括：

* **textbook_collocation_data.xlsx**: 从二语教材语料库（规模约240万词）中自动抽取的搭配数据，未经过滤。
* **wiki_collocation_data.txt.zip**：从中文维基百科（规模约1.38亿词）中自动抽取的搭配数据，因原始文件较大，此处保留了频次>=2的搭配，并用txt压缩存储，文本以\t分隔各列。

**2. 知识库属性**

搭配知识库所包含的字段包括：

* **ID**: 搭配ID
* **Collocation**: 搭配
* **Type**: 搭配类型，以代码方式呈现，可以通过如下字典映射得到具体名称：
  
  ```
  coll_dict = {'V_O': 'VO', 'V_HV_O': 'VO', 'V_2HV_O': 'VO', 'D_V': 'AP',
               'S_V_HV': 'SP', 'P_X_DN': 'PP', 'V_C': 'PC',
               'S_V': 'SP', 'D_A': 'AP', 'Q_N': 'CN', 'V_D_C': 'PC', 'P_X_U': 'PP',
               'P_X_V': 'PV', 'A_N': 'AN', 'A_X_DE_N': 'AN', 'D_X_A': 'AP', 'P_X_V_HV': 'PV',
               'D_X_V': 'AP', 'V_U_C': 'PC', 'A_DE_N': 'AN', 'V_X_C': 'PC',
               'V_C_U': 'PC', 'D_DI_V': 'AP', 'V_U_X_C': 'PC', 'V_M_C': 'PC', 'V_U_A_C': 'PC',
               'A_X_N': 'AN', 'V_U_D_C': 'PC', 'V_U_M_C': 'PC', 'A_DE_X_N': 'AN',
               'P_X_V_2HV': 'PV', 'S_V_2HV': 'SP', 'V_A_C': 'PC', 'C_X_C': 'CC'}

  coll_names = {'VO': 'Verb-Object (动宾)', 'AP': 'Adverb-Predict (状中)', 'SP': 'Subject-Predicate (主谓)',
                'PC': 'Predict-Complement (述补)', 'PP': 'Preposition-Postposition (介方)', 'PV': 'Preposition-Verb (介谓)',
                'CN': 'Classifier-Noun (量名)', 'AN': 'Adjective-Noun (定中)', 'CC': 'Connectives (关联词)'}
  ```
* **Parent**: 该搭配对应的父级搭配ID，例如“送 上 祝福”的父级搭配为“送 祝福”。
* **Frequency**: 语料库中的频次。
* **Frequency_with_variants**: 如果该搭配有父级搭配(parent)，则该项频次为负；如果该搭配有子搭配，则该项频次是它与其子搭配之和。
* **Mutual_Information**: 互信息，衡量搭配词之间的关联紧密程度，通过如下公式计算：
$$I \left(W_1, W_2, R \right) = log \left( \frac{P(W_1, W_2, R)}{P\left(R \right) \times P\left(W_1|R \right) \times P\left(W_2|R \right)}\right)$$
其中，W<sub>1</sub>和W<sub>2</sub>代表搭配组合中的词语，R代表搭配类型，P为概率。

**3. 更多信息**

各搭配类型的定义及自动抽取方法可参考：

* 胡韧奋,肖航.面向二语教学的汉语搭配知识库构建及其应用研究[J].语言文字应用,2019(01):135-144.

**勘误**：论文中互信息(Mutual Information)公式有排版错误，计算方法以上文公式为准。
