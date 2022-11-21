# Currently unused
# Used in huggingface model hub (upload to repo) for custom inference api / endpoint behaviour
from typing import Any, Dict
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

ADAPTER_NAME = "narrativeqa"

class EndpointHandler():
    def __init__(
        self,
        path: str,
    ):
        self.tokenizer = AutoTokenizer.from_pretrained(path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(path)
        self.model.set_active_adapters(ADAPTER_NAME)

    def __call__(self, data: Dict[str, Any]) -> str:
        """
        data args:
            inputs (:obj: `str` | `PIL.Image` | `np.array`)
            kwargs
        Return:
            output :obj:`list` | `dict`: will be serialized and returned
        """
        inputs = data.pop("inputs", data)
        tokenized_input = self.tokenizer([inputs], return_tensors="pt")
        prediction = self.model.generate(
            tokenized_input.input_ids,
            num_beams=5,
            return_dict_in_generate=True,
            output_scores=True,
            max_length=50,
        )
        output = self.tokenizer.decode(
            prediction["sequences"][0], # single prediction
            skip_special_tokens=True,
            clean_up_tokenization_spaces=True,
        )

        return [output]