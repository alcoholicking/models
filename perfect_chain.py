from langchain_community.llms import LlamaCpp

from langchain.prompts import PromptTemplate

# A class extended from LlamaCpp that has the same interface as LlamaCpp

# later prepare to build a llama chain

class PerfectLlama(LlamaCpp):
def __init__(self, model_path: str, n_gpu_layers: Optional[int] = 40, n_batch: Optional[int] = 256) -> None:
    """
    Constructor for initializing the object.

    :param model_path: The path to the Llama model.
    :type model_path: str
    :param n_gpu_layers: The number of GPU layers.
    :type n_gpu_layers: Optional[int]
    :param n_batch: The batch size.
    :type n_batch: Optional[int]
    """
    super().__init__(
        model_path=model_path, 
        n_gpu_layers=n_gpu_layers,
        n_batch=n_batch)

def give_prompt(self, prompt: str) -> Any:
    """
    Method to give a prompt and return the result.

    Args:
        prompt (str): The prompt to be given.

    Returns:
        The result of the prompt.
    """
    return self(prompt)
