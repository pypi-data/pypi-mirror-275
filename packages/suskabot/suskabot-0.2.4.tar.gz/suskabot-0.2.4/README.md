# Suskabot
Telegram Bot that really can do it all!

[PyPi package](https://pypi.org/project/suskabot/)


## Current functionality
### YouTube video downloader
  Send a link, get a video!

### Translator
   Fast translations without the need to specify to and from languages!

   Configure "default language to translate to" and "user language"

   Currently supported languages: Russian, English, Ukrainian

### PDF manipulations
  work in progress :)


## Tests
   To run the tests use:
   ```shell
   poetry run pytest -v -s -n auto
   ```


## Usage
### Manual
0) Get the project:
   ```shell
   git clone https://gitlab.com/vinyl_summer/suskabot.git && cd suskabot
   ```
1) Create and activate a new virtual environment
   ```shell
   poetry shell
   ```
2) Install the project requirements
   ```shell
   poetry install
   ```
3) Set the [API_TOKEN](https://t.me/botfather) environment variable using export:
   ```shell
   export TG_BOT_API_TOKEN=<your_token>
   ```
   
   or .env file:
   ```shell
   cat suskabot/config/.env.example >> suskabot/config/.env
   ```
   ```shell
   echo <your_token> >> suskabot/config/.env
   ```
   
   Other environment variables are optional and can be set using your text editor of choice.

   Beware, no configurations from .env.example will be read!

4) Start the app:
   ```shell
   poetry run python -m suskabot
   ```


### Docker 
Build the image yourself:
   ```shell
   git clone https://gitlab.com/vinyl_summer/suskabot.git && cd suskabot
   ```

   ```shell
   docker build -t suskabot .
   ```

   ```shell
   docker run -d --env=TG_BOT_API_TOKEN=<your_token> suskabot
   ```

Or use one from the gitlab registry:
   ```shell
   docker run -d --env=TG_BOT_API_TOKEN=<your_token> registry.gitlab.com/vinyl_summer/suskabot
   ```

### Demo
![](docs/bot_demo.mp4)
