import scipy
from transformers import VitsModel, AutoTokenizer
import torch


class Voicer:
    def __init__(self,
                 model_name: str="facebook/mms-tts-rus",
                 tokenizer_name: str="facebook/mms-tts-rus"):

        self.model = VitsModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    def predict(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt")

        with torch.no_grad():
            outputs = self.model(**inputs).waveform

        squeezed_outputs = outputs.numpy().squeeze()

        file_name = f"output.wav"

        scipy.io.wavfile.write(file_name, rate=self.model.config.sampling_rate, data=squeezed_outputs)

        return file_name
