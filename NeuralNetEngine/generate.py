from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
import logging
from simpletransformers.language_generation import LanguageGenerationModel


class TextGen:
    def textgenerator(self, adv_desc):
        logging.basicConfig(level=logging.INFO)
        transformers_logger = logging.getLogger("transformers")
        transformers_logger.setLevel(logging.WARNING)

        model = LanguageGenerationModel("gpt2", "gpt2", args={"length": 256},use_cuda=False)

        prompts = [
           "{0}".format(adv_desc),
        ]

        for prompt in prompts:
            # Generate text using the model. Verbose set to False to prevent logging generated sequences.
            generated = model.generate(prompt, verbose=False)
            generated = '.'.join(generated[0].split('.')[:-1]) + '.'

        return generated