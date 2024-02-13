import gradio as gr
import soundfile
from espnet2.bin.tts_inference import Text2Speech
model_name = "espnet/kan-bayashi_ljspeech_vits"
text2speech = Text2Speech.from_pretrained(model_name)
def text_to_speech(input_text):
    speech = text2speech(input_text)["wav"]
    soundfile.write("./tmp/output.wav", speech.numpy(), text2speech.fs, "PCM_16")
        
    
    return "./tmp/output.wav"

input_text = gr.Textbox(lines=3, label="Enter your text here:")
interface = gr.Interface(fn=text_to_speech, inputs=input_text, outputs="audio")
interface.launch()
