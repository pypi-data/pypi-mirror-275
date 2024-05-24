import torch
from torch import nn
from torch.nn import functional as F


class TextCNN(nn.Module):

    def __init__(self, word_dim: int, kernel_sizes=(2, 3, 4), cnn_channels=64, out_features=2, num_hidden_layer=0, drop_out=None):
        """ TextCNN model
        Parameters
        ----------
        word_dim: int, dim of word, in_channels of cnn
        cnn_channels: int, out_channels of cnn
        kernel_sizes: size of each cnn kernel
        out_features: dim of output
        num_hidden_layer:
        drop_out:

        Examples
        --------
        >>> import torch
        >>> from nlpx.models import TextCNN
        >>> X = torch.randn(batch_size, 10, word_dim)
        >>> targets = torch.randint(0, num_classes, (batch_size,))
        >>> model = TextCNN(word_dim, cnn_channels=64, kernel_sizes=(2, 3, 4), out_features=num_classes)
        >>> output = model(X)
        >>> loss, output = model(X, targets)
        """
        super().__init__()
        self.convs = nn.ModuleList([
            nn.Sequential(
                nn.Conv1d(in_channels=word_dim, out_channels=cnn_channels, kernel_size=kernel_size, bias=False),
                nn.ReLU6(inplace=True),  # inplace为True，将会改变输入的数据 ，否则不会改变原输入，只会产生新的输出
                nn.AdaptiveMaxPool1d(1)
            ) for kernel_size in kernel_sizes
        ])

        num_features = cnn_channels * len(kernel_sizes)
        self.fc = nn.ModuleList([
            nn.Sequential(
                nn.Linear(in_features=num_features, out_features=num_features, bias=False),
                nn.LayerNorm(normalized_shape=num_features),
                nn.ReLU6(inplace=True)
            ) for _ in range(num_hidden_layer)
        ])

        if drop_out:
            self.fc.append(nn.Dropout(drop_out))

        self.fc.append(nn.Linear(in_features=num_features, out_features=out_features))

    def forward(self, inputs, labels=None):
        """
        :param inputs: [(batch, sentence, word_dim)]
        :param labels: [long]
        """
        input_embeddings = inputs.transpose(2, 1)
        out = torch.cat([conv(input_embeddings) for conv in self.convs], dim=1)
        out = out.transpose(2, 1)

        for hidden_layer in self.fc:
            out = hidden_layer(out)

        logits = out.squeeze(1)

        if labels is None:
            return logits
        else:
            loss = F.cross_entropy(logits, labels)
            return loss, logits
