from transformers.configuration_utils import PretrainedConfig

class OpenNanoBananaConfig(PretrainedConfig):
    model_type = "open-nanoscale-llm"

    def __init__(
        self,
        hidden_size=2048,
        num_hidden_layers=22,
        num_attention_heads=32,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.hidden_size = hidden_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
