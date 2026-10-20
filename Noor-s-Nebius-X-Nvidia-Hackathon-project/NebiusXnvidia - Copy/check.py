from ai_client import client

# Fetch the exact list of available models from Nebius
models = client.models.list()

print("\n--- YOUR AVAILABLE NEBIUS MODELS ---")
for model in models.data:
    print(model.id)
print("------------------------------------\n")