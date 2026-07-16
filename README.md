# fun-chat-ai
Python chat project 
<!-- local setup  -->
Fork the Repository
```sh
git@github.com:tomdu3/fun-chat-ai.git
```
Clone the Repo
```sh
git clone git@github.com:ci-sumi/fun-chat-ai.git
cd <project-folder>
```
Intialize   the project with uv
```sh
uv init
```
Update the project configuration
Add the project description to pyproject.toml
```sh
uv sync
```
It automatically create .venv
Add core dependencies
```sh
uv add flask,sqlalchemy,dotenv
```
