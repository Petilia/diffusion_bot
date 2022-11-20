import telebot
import os
import torch
from diffusers import StableDiffusionPipeline
from huggingface_hub.hf_api import HfFolder

MODEL_DATA = os.getenv('MODEL_DATA', 'runwayml/stable-diffusion-v1-5')
LOW_VRAM_MODE = (os.getenv('LOW_VRAM', 'true').lower() == 'true')
USE_AUTH_TOKEN = (os.getenv('USE_AUTH_TOKEN', 'true').lower() == 'true')

hf_token = "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"
tg_token = "5845590654:AAGxeqKoMClAkub3tH9M3bocaZsOSyFQhr0"
HfFolder.save_token(hf_token)

# load the text2img pipeline
revision = "fp16" if LOW_VRAM_MODE else None
torch_dtype = torch.float16 if LOW_VRAM_MODE else None
pipe = StableDiffusionPipeline.from_pretrained(MODEL_DATA, revision=revision, torch_dtype=torch_dtype, use_auth_token=USE_AUTH_TOKEN)
pipe = pipe.to("cuda")

bot=telebot.TeleBot(tg_token)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет")
  print(message.chat.id)

@bot.message_handler(commands=['gen'])
def gen_message(message):
  mesg = bot.send_message(message.chat.id, "Напиши свой запрос для генерации (на английском языке)")
  bot.register_next_step_handler(mesg, generation_image_by_prompt)

def generation_image_by_prompt(message):
    prompt = message.text
    image = pipe(prompt).images[0]

    bot.send_photo(message.from_user.id, image)


bot.infinity_polling()