# AI-tinkerers Hackathon Aug 2024

## Ideas

- [ ] Football coach play recommendation system for young football players

  - Football player can upload tape from their own games or of their competitor
  - Receive currated insights for plays and positioning

- [ ] AI video editor directed at content creators

  - Text to scene or voice to text video editing
  - Pretty ui and easy to use

- [ ] AI coach for extreme sports etc skate and bmx

  - Take videos of your extreme sports sessions and use AI to analyze your form and suggest improvements based on the specific trick you're working on.

- [ ] Coach for lifting and strength training
  - Take videos of your lifting and strength training sessions and use AI to analyze your form and suggest improvements

The Chosen Idea:

- [x] Build recipes from youtube videos with no recipes (This one is the one)
  - Upload a youtube video and get a list of ingredients and steps to make it

# Thought Process

We use twelve labs to create classifications and audio to text embeddings to then give to groq to summarize for ease of use.

## Problems encountered

### Twelve labs

We need a prompt and tags to classify our videos. These prompts and tags will be directed towards recipes. Should we make this specific to a type of cooking first?
The problem I see with a vague range is many many types of cooking styes.
What does cooking all have in common?
