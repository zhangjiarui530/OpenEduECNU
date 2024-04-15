from transformers import AutoTokenizer
from bigdl.llm.transformers import AutoModelForCausalLM
import torch
import time

start_time = time.time()  # 记录开始时间

model_path = r'C:\model\THUDM\chatglm3-6b'
# model_path = r'C:\model\Qwen\Qwen1.5-4B-Chat'
save_directory = r"C:\OpenEduECNU\model_low_bit"
model = AutoModelForCausalLM.load_low_bit(save_directory, trust_remote_code=True)
model = model.to('xpu')
tokenizer = AutoTokenizer.from_pretrained(model_path,
                                          trust_remote_code=True)


def generate_text_from_model(prompt, max_tokens=4096):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    model_inputs = tokenizer([text], return_tensors="pt").to('xpu')
    # Generate text
    with torch.inference_mode():
        generated_ids = model.generate(model_inputs.input_ids, max_new_tokens=1024)
        generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in
                         zip(model_inputs.input_ids, generated_ids)]
        torch.xpu.synchronize()
        # generated_ids = generated_ids.cpu()
        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response


end_time = time.time()  # 记录结束时间
elapsed_time = end_time - start_time
print(f"执行时间为: {elapsed_time:.4f} 秒")
