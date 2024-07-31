# WordWeaver: Serverless Text Utility with Django on AWS


**WordWeaver** is a comprehensive text utility application built as a serverless function on AWS Lambda using Python and Django. It offers a suite of powerful text processing tools including *multilingual translation*, *sentiment analysis*, and *text summarization*. Leveraging the `deep-translator`, `TextBlob`, and `Langchain` libraries, the application provides accurate and efficient results. The project is deployed as a Docker container on AWS ECR and integrated with API Gateway for seamless interaction.

This repository serves as the foundation for the application, building upon the core functionalities of the original `Multi-language-Translator` project ([https://github.com/rajendraprasath307/Multi-language-Translator](https://github.com/rajendraprasath307/Multi-language-Translator)). It combines these core features with advanced text analysis capabilities and a user-friendly interface.


## Tech Stack

**Multi-Language Translator**
- *deep-translator:* Python library for translating text in multiple languages, replacing the deprecated googletrans library.
  
**Sentimental Analysis** 
- *TextBlob*: Python library for sentiment analysis, providing polarity and subjectivity scores for input text.

**Text Summarization** 
- *Langchain*: A framework to build LLM pipelines with language models and integrate them into the application.
- *Groq Inference Engine*: Used for powering the Llama-3.1-8B LLM variant, enabling the functionality to perform high quality text summarization.
- *Llama-3.1 (8B)*: A high-performance open-source Large Language Model for text summarization.

**Web Application Development**
- *Django*: Leveraged the Django framework for building the core web application and managing different components.
- *HTML, CSS, JavaScript*: For front-end development to enhance the user interface and provide easy navigation across applications.

**Application Deployment** 
- *Docker*: Containerization tool used for packaging the application with all dependencies for deployment.
- *Mangum*: A Python library used for adapting the Django ASGI application for AWS Lambda.
- *AWS Elastic Container Registry (ECR)*: AWS's native container registry service for storing and managing Docker images.
- *AWS Lambda*: AWS serverless compute service for deploying and running the Dockerized Django application and configuring settings for timeout, memory allocation, and CORS to ensure optimal performance.


## Demo
- Web App Demo
![App Screenshot](https://i.ibb.co/q9bHVBh/ezgif-1-d988809a22.gif)
- Multi Language Translator
![App Screenshot](https://i.ibb.co/zVK43CK/Screenshot-2024-07-31-150143.png)
- Sentiment Analyzer
![App Screenshot](https://i.ibb.co/4StPMys/Screenshot-2024-07-31-150201.png)
- Text Summarizer
![App Screenshot](https://i.ibb.co/vx7Vtfs/Screenshot-2024-07-31-150214.png)
## Run Locally

Clone the project

```bash
  git clone https://github.com/rauhanahmed/WordWeaver
```

Go to the project directory

```bash
  cd WordWeaver
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server (Any of the two approaches)

- ```bash
  # Start the Django development server (will run on post 8000)
  python manage.py runserver 
    ```

- ```bash
  # Start the Uvicorn server (will run on post 7000)
  python main.py runserver 
    ```

After performing the above steps, open any browser, and hit the localhost at the correct port.
## Authors

[Rauhan Ahmed Siddiqui](https://linkedin.com/in/rauhan-ahmed/)


## License

[MIT](https://choosealicense.com/licenses/mit/)

