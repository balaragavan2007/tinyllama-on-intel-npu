# tinyllama-on-intel-npu
# 🦙 TinyLlama on Intel NPU with OpenVINO

I made **TinyLlama LLM** run on my **Intel Ultra Series 1 NPU** using **OpenVINO**.  
This project shows how to run a lightweight chatbot locally on your laptop’s NPU 🚀.

---

## 📂 Project Features
- Runs **TinyLlama** model on Intel NPU
- Uses **OpenVINO** for optimized inference
- INT4 quantization for faster performance

---

## ⚡ Requirements
Install these before running:
```bash
git clone https://github.com/balaragavan2007/tinyllama-on-intel-npu.git
cd tinyllama-on-intel-npu
pip install -r requirements.txt
```
---

## ⚡ Model Optimization (INT4 Quantization)
- The TinyLlama model was converted to INT4 precision using OpenVINO’s optimum-cli to reduce memory usage and boost performance.
```bash
optimum-cli export openvino --model "TinyLlama/TinyLlama-1.1B-Chat-v1.0" --task "text-generation-with-past" --weight-format fp16 --trust-remote-code ov_tinyllama
```
- The optimized INT4 model will be saved in the folder ./ov_tinyllama

---

## ▶️ Usage
- Run inference with:
```bash
python chat.py
```

---

## 📸 Demo
<img width="2406" height="1578" alt="Screenbox_20250420_190428" src="https://github.com/user-attachments/assets/8f413baa-3677-4547-982a-5f8ce9a303a3" />

---

## 🙌 Credits

- [OpenVINO™](https://github.com/openvinotoolkit/openvino) – for optimized inference on Intel hardware  
- [Optimum Intel](https://github.com/huggingface/optimum-intel) – Hugging Face integration with OpenVINO  
- [Transformers](https://github.com/huggingface/transformers) – Hugging Face library for LLMs  
- [TinyLlama](https://huggingface.co/TinyLlama) – the model used in this project  

