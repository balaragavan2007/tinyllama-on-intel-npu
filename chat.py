import openvino_genai as ov_genai

# Load your model (already exported/optimized with OpenVINO)
model_dir = "ov_tinyllama"
pipe = ov_genai.LLMPipeline(model_dir, "NPU")
config = ov_genai.GenerationConfig(max_new_tokens=512)

print("🚀 TinyLlama is running locally on your Intel NPU")
print("Type 'exit' to quit\n")

# Chat history
history = []

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    # Append user message
    history.append(f"User: {user_input}")
    # Build conversation context
    prompt = "\n".join(history) + "\nAssistant:"

    # Generate response
    response = pipe.generate(prompt, config)

    # Clean response
    reply = response.strip()
    history.append(f"Assistant: {reply}")

    print(f"Assistant: {reply}\n")
