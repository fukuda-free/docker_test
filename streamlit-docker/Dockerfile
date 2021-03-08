# FROM python:3.7
# EXPOSE 8501
# WORKDIR /app
# COPY requirements.txt ./requirements.txt
# RUN pip3 install -r requirements.txt
# COPY . .
# CMD streamlit run app.py
FROM python:3.7
EXPOSE 8501
WORKDIR /app
RUN pip install spacy-streamlit
COPY . .
CMD streamlit run app.py