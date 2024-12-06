# Financial Sentiment Analysis API

Uma API construída com **FastAPI** para análise de textos e retorno de sentimentos, com foco em analise de textos relacionados a finanças.

## Funcionalidades

- **Análise de Sentimentos:** Retorna o sentimento (positivo, negativo ou neutro) com base em textos financeiros fornecidos.
- **Modelos de Machine Learning:** Integração com algoritmos como SVM, Naive Bayes, XGBoost, LightGBM, entre outros.
- **Preprocessamento de Textos:** Limpeza e normalização dos textos antes da análise.

## Tecnologias Utilizadas

As principais tecnologias e bibliotecas usadas no projeto incluem:

- **FastAPI**: Framework backend moderno e de alto desempenho.
- **Pydantic**: Para validação e serialização de dados.
- **Scikit-learn**: Conjunto de ferramentas para aprendizado de máquina e mineração de dados.
- **Joblib**: Para serialização de modelos treinados.
- **NLTK**: Ferramentas para processamento de linguagem natural.

---

## Endpoints

**Acesse a documentação interativa:**

- Swagger UI: [https://rest-api-reply-model-v1.onrender.com/docs](https://rest-api-reply-model-v1.onrender.com/docs)
- ReDoc: [https://rest-api-reply-model-v1.onrender.com/redoc](https://rest-api-reply-model-v1.onrender.com/redoc)

### 1. **`POST /model_prediction/`**

Realiza a análise de sentimentos com base em um texto fornecido e um modelo fornecido.

### 2. **`POST /multi_model_prediction/`**

Realiza a análise de sentimentos com base em um texto fornecido.

- **Modelos Disponíveis**:
  - `Naive Bayes`
  - `SVM`
  - `XGBoost`
  - `LightGBM`
  - `Multilayer Perceptron`
  - `Gradient Boosting`
  - `Random Forest`
  - `AdaBoost`
  - `Decision Tree`

---

## Sobre os modelos

**Acesse a esse repositorio:**

- Financial Market Sentiment Prediction: [https://github.com/erickmaiia/ml-financial-sentiment-analysis](https://github.com/erickmaiia/ml-financial-sentiment-analysis)

## Dependências

As bibliotecas utilizadas estão listadas no arquivo `requirements.txt`.
