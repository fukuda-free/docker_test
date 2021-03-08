# import os
# import pkg_resources, imp

# import streamlit as st
# import spacy_streamlit
# import spacy

# # see https://github.com/explosion/spacy-streamlit
# st.title("Spacy Streamlit App")

# spacy_model = ["en_core_web_sm" , "ja_core_news_lg", "ja_core_news_md", "ja_core_news_sm"]

# # 未ダウンロードのモデルファイルがある場合はダウンロード
# for spacy_model in spacy_models:
#     try:
#         imp.find_module(spacy_model)
#     except ImportError:
#         os.system("python -m spacy download {}".format(spacy_model))
#         imp.reload(pkg_resources)


# visualizers = ["parser", "ner", "tokens"] # exclude "textcat", "similarity"
# spacy_streamlit.visualize(spacy_model, "Rusty is the best dog in Charlotte, NC.", visualizers)


import os
import pkg_resources, imp

import spacy_streamlit

models = ["ja_core_news_lg", "ja_core_news_md", "ja_core_news_sm"]

# 未ダウンロードのモデルファイルがある場合はダウンロード
for model in models:
    try:
        imp.find_module(model)
    except ImportError:
        os.system("python -m spacy download {}".format(model))
        imp.reload(pkg_resources)

spacy_streamlit.visualize(models, "")
