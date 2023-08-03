# ducking-profanity-filter
A profanity filtering api for scoring profanity ratings using [FastAPI](https://fastapi.tiangolo.com/) + [Detoxify](https://github.com/unitaryai/detoxify).

## Profanity / Toxicity Filtering
This repo uses trained models to predict toxic comments based on data provided by 3 Jigsaw challenges: [Toxic comment classification](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge), [Unintended Bias in Toxic comments](https://www.kaggle.com/competitions/jigsaw-unintended-bias-in-toxicity-classification), [Multilingual toxic comment classification](https://www.kaggle.com/competitions/jigsaw-multilingual-toxic-comment-classification).

This repo uses [Detoxify](https://github.com/unitaryai/detoxify) to predict the following classes:

1. Toxic: Comments containing rude, disrespectful, or offensive content.
2. Severe Toxic: Comments containing highly offensive or abusive language.
3. Obscene: Comments containing sexually explicit content.
4. Threat: Comments containing threats to individuals or groups.
5. Insult: Comments that are insulting or disparaging.
6. Identity Hate: Comments containing hate speech targeted at a particular identity (e.g., race, religion, gender, etc.).

The repo uses the `multilingual` model and therefore supports `english`, `french`, `spanish`, `italian`, `portuguese`, `turkish` and `russian` input strings.

## Setup
To run this as a web service you'll need to build and run the docker image using:

1. `docker-compose build`
2. `docker-compose up -d`

The service will then run on localhost:3006

## Endpoints

| Endpoint        | Parameters       | Response                                                                                                                                                                                                                                                     |
|-----------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GET] /toxicity | q (query string) | `{"toxicity":0.0005992225487716496,"severe_toxicity":9.069682960216596e-07,"obscene":1.938134664669633e-05,"identity_attack":9.398855763720348e-05,"insult":0.00015359769167844206,"threat":2.0553250578814186e-05,"sexual_explicit":7.090181497915182e-06}` |


## Running locally
Stop the running docker container and use:
```
uvicorn app.server:app --host 0.0.0.0 --port 3006
```

## Useful commands

### Export requirements from poetry
```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

### Run uvicorn locally
```bash
uvicorn app.server:app --host 0.0.0.0 --port 3006
```