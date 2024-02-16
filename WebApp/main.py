import gradio as gr
import soundfile
from IPython.display import Audio


# Using ESPNet Librrary 
ESPNet_model = "espnet/kan-bayashi_ljspeech_vits"
from espnet2.bin.tts_inference import Text2Speech



# Using Transformers Model provided by Facebook 
# Resource Huggingface
facebook_mms_tts_model = "facebook/mms-tts-eng"
from transformers import VitsModel, VitsTokenizer
import torch


def text_to_speech(input_text,model_name):
    if model_name == ESPNet_model:
        espnet_text2speech = Text2Speech.from_pretrained(model_name)
        speech = espnet_text2speech(input_text)["wav"]
        soundfile.write("./tmp/output.wav", speech.numpy(), espnet_text2speech.fs, "PCM_16")
           
        
    if model_name == facebook_mms_tts_model:
        model = VitsModel.from_pretrained(facebook_mms_tts_model)
        tokenizer = VitsTokenizer.from_pretrained(facebook_mms_tts_model)
        inputs = tokenizer(input_text, return_tensors="pt")

        with torch.no_grad():
            output = model(**inputs).waveform

        

        audio = Audio(output.numpy(), rate=model.config.sampling_rate)
        with open('./tmp/output.wav', 'wb') as f:
            f.write(audio.data)
        
    
    return "./tmp/output.wav"








# Define the options for the dropdown
options = ["espnet/kan-bayashi_ljspeech_vits", "facebook/mms-tts-eng"]

# Create a dropdown input
dropdown_input = gr.Dropdown(choices=options, label="Select an option")


# Create the Gradio interface


input_text = gr.Textbox(lines=3, label="Enter your text here:")
interface = gr.Interface(
    fn=text_to_speech, 
    inputs=[input_text,dropdown_input],
    outputs="audio")
interface.launch(share=True)
