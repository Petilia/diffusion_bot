<p align="center"><img src="assets/1.gif"/></p>

## Description ##
Presented Telegram bot for generating pictures by text query. Stable Diffusion is used as the generation model.

## Receiving a tokens ##
You need to write to the bot https://t.me/BotFather, create your own bot and get the API token.  
You need to register at https://huggingface.co/ and get an API token

## Creating .env file ##
You need to create an .env file in the diffusion_bot directory:
```
HF_TOKEN="your_huggingface_api_token"
TG_TOKEN="your_telegram_api_token"
MODEL_DATA=runwayml/stable-diffusion-v1-5
LOW_VRAM_MODE=true
USE_AUTH_TOKEN=true
INFERENCE_DEVICE=cuda
```
You can change INFERENCE_DEVICE to cpu if you do not have gpu

## Building ##
At the root of the repository, run the commands:
```
docker-compose build 
docker-compose up
```
Note that the huggingface cache is mounted in the container. This is necessary if you do not want to wait every time you restart the container to download the model weights. You need to specify where on the host the folder to mount will be located.
```
volumes:
    - /path_to_cache_on_host:/home/docker_current/.cache/huggingface:rw
```