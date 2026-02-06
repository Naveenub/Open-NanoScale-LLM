import torch
from torch import nn
from transformers.modeling_utils import PreTrainedModel
from .configuration_onb import OpenNanoScaleLLMConfig

class OpenNanoBananaModel(PreTrainedModel):
    config_class = OpenNanoScaleLLMConfig

    def __init__(self, config):
        super().__init__(config)
        self.embed_tokens = nn.Embedding(32000, config.hidden_size)
        self.layers = nn.ModuleList([
            nn.TransformerEncoderLayer(
                d_model=config.hidden_size,
                nhead=config.num_attention_heads,
                batch_first=True
            )
            for _ in range(config.num_hidden_layers)
        ])
        self.norm = nn.LayerNorm(config.hidden_size)

    def forward(self, input_ids):
        x = self.embed_tokens(input_ids)
        for layer in self.layers:
            x = layer(x)
        return self.norm(x)
