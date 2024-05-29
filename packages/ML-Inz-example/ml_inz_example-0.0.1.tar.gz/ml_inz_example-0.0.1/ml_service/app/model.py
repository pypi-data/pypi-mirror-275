import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from GPUtil import showUtilization as gpu_usage
from numba import cuda
import os
import gc


def free_gpu_cache():
    print("Initial GPU Usage")
    gpu_usage()

    torch.cuda.empty_cache()

    cuda.select_device(0)
    cuda.close()
    cuda.select_device(0)

    print("GPU Usage after emptying the cache")
    gpu_usage()


device = "cuda" if torch.cuda.is_available() else "cpu"
if device == "cuda":
    free_gpu_cache()

# Загрузка модели
model_id = "nvidia/Llama3-ChatQA-1.5-8B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")


def get_formatted_input(messages, context):
    system = ("System: This is a chat between a user and an artificial intelligence assistant. The assistant gives "
              "helpful, detailed, and polite answers to the user's questions based on the context. The assistant "
              "should also indicate when the answer cannot be found in the context.")
    instruction = "Please give a full and complete answer for the question."

    for item in messages:
        if item['role'] == "user":
            ## only apply this instruction for the first user turn
            item['content'] = instruction + " " + item['content']
            break

    conversation = '\n\n'.join(
        ["User: " + item["content"] if item["role"] == "user" else "Assistant: " + item["content"] for item in
         messages]) + "\n\nAssistant:"
    formatted_input = system + "\n\n" + context + "\n\n" + conversation

    return formatted_input


def generate_response(question: str, document: str) -> str:
    messages = [{"role": "user", "content": question}]
    formatted_input = get_formatted_input(messages, document)
    tokenized_prompt = tokenizer(tokenizer.bos_token + formatted_input, return_tensors="pt").to(model.device)

    terminators = [
        tokenizer.eos_token_id
    ]

    outputs = model.generate(input_ids=tokenized_prompt.input_ids, attention_mask=tokenized_prompt.attention_mask,
                             max_new_tokens=128, eos_token_id=terminators)

    response = outputs[0][tokenized_prompt.input_ids.shape[-1]:]
    return tokenizer.decode(response, skip_special_tokens=True)
