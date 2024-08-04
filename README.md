# Groq Pot

## Description
Get recipes from the link of a video. Currate your meals based on calories, appetite and and specific dietary restrictions. With Groq Pot you have the will of your hunger at your fingertips, and endless possibilities for delicious meals.

## API Usage
This application is built with Many techonologies including:
### FastAPI
  - Quick access to a backend with a websocket. Our goal was to stream the chat from the groq chain to the frontend to have a cool UX.
### Groq
  - This is the bread and butter of the application. Groq is quick and works langchain. We used groq as the brain of our application.
### Twelve Labs
  - We used twelve labs sdk to upload videos and generate the embeddings and content and then structured the data into a json format with prompt engineering.
### OpenAI
  - We used OpenAI to generate embeddings for the recipes and instructions json file
### Langchain
  - Langchain was used to create a RAG with context and memory. We want the users to be able to ask questions and alter the instructions based on their preferences. Along with search for more recipes.

NOTE: We chose to work with Python SDKs becuase David and I were familiar with the language. A faster implementation would use the TS SDKs and integrate them straight into Next.js (potentially)



## Motivation
Too many times I have looked for a food recipe on YouTube and fell into the rabit whole of "back in 1917, when my great-grandmother cooked for me, I would watch the cooking show and then go to the kitchen to make the recipe". So much non-sense and fluff GIVE ME THE RECIPE PLEASE. Now all you have to do is insert a YouTube link and wallah you get the recipe and its saved for later use.

## Quickstart

### Clone the repo
```bash
git clone git@github.com:xelacast/ai-tinkerers-hackathon.git
```

### Frontend
#### Requirements
  - Node.js
  - pnpm

CD into directory
  ```bash
  cd frontend
  ```

Install dependencies
  ```bash
  pnpm install
  ```

Run the app
  ```bash
  pnpm dev
  ```

### Backend
#### Requirements
  - Python3.11

  Make a .env file from the example.env file
  API KEYS

    GROQ_API_KEY=""
    TWELVE_LABS_API_KEY=""
    OPENAI_API_KEY=""

CD into the backend directory
```bash
cd ../backend
```

Make a virtual env and Install dependencies
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

  ```bash
  pip install -r requirements.txt
  ```

  ```bash
  cd src
  ```
Run the app
  ```bash
   fastapi dev serve.py
  ```

Endpoints
  - POST /recipe
    - This is the endpoint for twelve labs to generate the recipe and instructions
  - GET /ws
    - This is the endpoint for the websocket to stream the chat from the groq chain

Files
  - db/recipes.json
    - This is the json db that is used to store the recipe and instructions
  - prompts/prompt_schema.json
    - This is the prompt schema that is used to structure the recipe and instructions from twelve labs generated content
  - app/groq_history.py
    - This is the groq rag chain that is used to search for recipes and alter the instructions based on the user's preferences
  - app/serve.py
    - This is the fastapi server that is used to stream the chat from the groq chain
  - app/twelve_labs.py
    - This is the twelve labs sdk that is used to upload videos and generate the embeddings and content and add recipes

## How does it work?
- The user uploads their favorite cooking YouTube link and the app sends this to twelve labs to generate the recipe and instructions and video id on a specific index and inserts the diven data into a json db (local forn now)
- The frontend end opens up a websocket to fastapi to allow us to communicate with the groq RAG chain
- The backend was made with FastAPI to allow for quick streaming

RAG
    - The RAG has access to a vector store of the embeddings of the twelve labs generated content meaning we can search for recipes and ask it to change the instructions based on the user's preferences
    - When videos are uploaded the vector store updates and the rag can instantly search for the new content

## What we could have done better
- Exand our idea to instructional videos and other content types to get the bonus category.
- Recruite/Join teams to have more work power. 24 hours is a small amount of time to build a working prototype.
- Not drink so much caffeine. 💀
- Used TLjockey to cut up videos and create snippets of the actions of cooking and key vocal moments.