# fun-chat-ai

A terminal-based AI-powered application for fun conversations.A terminal-based AI-powered application for fun conversations.

## Technologies

- **Languages**
  - `Python` - explain what this is - link to the docs
- **Frameworks and Libraries**
  - `Flask` -->
  - `SqlAlchemy` ->
- **AI Technologies and services**
  - `Deepseek`
  - `Nvidia API`

- **Tools**
  - `Vercel` - explain + link to the docs
  - `uv` -

<!-- TODO:

add these libraries to Technologies details
langchain
langchain-groq
langchain-community
-->

## Local Deployment

1. On your Windows/Linux Machine, go to the bash-based terminal and in your home or some other directory clone the project by executing:

- with SSH protocol

```sh
git clone git@github.com:tomdu3/fun-chat-ai.git
```

- with HTTPS protocol

```sh
git clone https://github.com/tomdu3/fun-chat-ai
```

1. Navigate to the project directory

```sh
cd fun-chat-ai
```

1. Install dependencies
   For this project we are using [uv](https://docs.astral.sh/uv/) to manage Python project environment and dependencies. The following command will install the environment and dependencies:

```sh
uv sync
```

1. Run the application

```sh
uv run python main.py
```

# Flow chart

```mermaid
flowchart TD
A([Start])--> B[Setup DeepSeek Model]
B-->C[Load Data]
C-->D[Define Chatbot function]
D-->E[Evoke Chatbot with question and Context]
E-->F[Get result from Model]
F-->G[Display Result]
G-->H[End]
```

### Use of AI in this Project

Langchain

Agent =Model +Harness
LangChain provides a minimal ,highly configurable harness.The harness is everything around the model loop:the prompt,the tools,and any middleware that shapes the behaviour.
on other hand,its a standalone framework for building agents and third party integrations to simplify AI application development.

Longchain-groq
LanguageChain-Groqu is a connector that allows Langchain applications to use Groq-hosted Large Language models.

Langchain-community

It provides connetctors and integrations.Collection of integrations that connect Langchain applications to external datasource,tools and services.

## References

<https://www.youtube.com/watch?v=rfH6f1U4_kE> Build a Simple Chatbot with DeepSeek
<https://docs.langchain.com/oss/python/langchain/overview>
LangChain overview
<https://github.com/langchain-ai/langchain> The agent engineering platform.

## Copyright
