from torch import nn
from transformers import BertConfig, BertModel

class ChessBERT(nn.Module):
  def __init__(self, *, vocab_size: int, hidden_size: int, attention_heads: int = 4):
    super().__init__()
    # BERT configuration
    self.config = BertConfig(
      vocab_size=vocab_size,
      hidden_size=hidden_size*attention_heads,
      num_attention_heads=attention_heads,
    )
    self.bert = BertModel(self.config)
    self.fc = nn.Linear(hidden_size*attention_heads, 4 * 8 + 5)

  def forward(self, input_ids, attention_mask = None):
    # Get BERT outputs
    outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
    sequence_output = outputs.last_hidden_state  # Shape: (batch_size, seq_len, hidden_size)
    return self.fc(sequence_output)  # Shape: (batch_size, seq_len, 4 * 8 + 5)