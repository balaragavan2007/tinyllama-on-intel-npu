from openvino.runtime import Core

ie = Core()
print("Available devices:", ie.available_devices)

model = ie.read_model("public/mobilenet-v2-pytorch/mobilenet-v2.xml")
compiled_model = ie.compile_model(model=model, device_name="NPU")
print("✅ Model compiled successfully on NPU")
