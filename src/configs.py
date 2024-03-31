from vertexai.generative_models import GenerationConfig

creative = GenerationConfig(temperature=0.6)
deterministic = GenerationConfig(temperature=0, top_k=1)