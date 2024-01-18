import torch
import torchvision.transforms

class DoubleConv(torch.nn.Module):
    def __init__(self, in_channels, out_channels, mid_channels = None):
        """
        Double convolution block: two sequential convolutional layers with batch normalization and ReLU activation.

        Args:
            in_channels (int): Number of input channels.
            out_channels (int): Number of output channels.
            mid_channels (int, optional): Number of channels in the intermediate layer. Defaults to None.
        """
        super().__init__()
        if mid_channels is None:
            mid_channels = out_channels
        self.double_conv = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=in_channels, out_channels=mid_channels, kernel_size=3),
            torch.nn.BatchNorm2d(mid_channels),
            torch.nn.ReLU(inplace=True),
            torch.nn.Conv2d(in_channels=mid_channels, out_channels=out_channels, kernel_size=3),
            torch.nn.BatchNorm2d(out_channels),
            torch.nn.ReLU(inplace=True),
            torch.nn.Dropout(p=0.5) # prevent overfitting
        )

    def forward(self, X):
        """
        Forward pass through the double convolution block.

        Args:
            X (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor.
        """
        return self.double_conv(X)


class EncoderBlock(torch.nn.Module):
    def __init__(self, in_channels, out_channels) -> None:
        """
        Encoder block: max-pooling followed by a double convolution block.

        Args:
            in_channels (int): Number of input channels.
            out_channels (int): Number of output channels.
        """
        super().__init__()
        self.encoder = torch.nn.Sequential(
            torch.nn.MaxPool2d(kernel_size=2),
            DoubleConv(in_channels, out_channels=out_channels),
            torch.nn.Dropout(p=0.5)
        )

    def forward(self, X):
        return self.encoder(X)


def center_crop(image, match_x):
    """
    Center-crop an image to match the size of another image.

    Args:
        image (torch.Tensor): Input image tensor.
        match_x (torch.Tensor): Reference tensor for size matching.

    Returns:
        torch.Tensor: Center-cropped image.
    """
    h, w = image.shape[-2], image.shape[-1]
    new_h, new_w = match_x.shape[-2], match_x.shape[-1]

    start_h = max(0, (h - new_h) // 2)
    start_w = max(0, (w - new_w) // 2)

    end_h = start_h + new_h
    end_w = start_w + new_w

    cropped_image = image[... , start_h:end_h, start_w:end_w]

    return cropped_image


class DecoderBlock(torch.nn.Module):
    def __init__(self, in_channels, out_channels) -> None:
        """
        Decoder block: up-sampling followed by concatenation with skip connection and double convolution block.

        Args:
            in_channels (int): Number of input channels.
            out_channels (int): Number of output channels.
        """
        super().__init__()
        self.up = torch.nn.Sequential(
            torch.nn.ConvTranspose2d(in_channels=in_channels, out_channels=in_channels // 2, kernel_size=2, stride=2, padding=0),
            torch.nn.BatchNorm2d(in_channels // 2),
            torch.nn.ReLU(inplace=True),
            torch.nn.Dropout(p=0.5)
        )
        self.double_conv = DoubleConv(in_channels=in_channels, out_channels=out_channels, mid_channels=in_channels//2)

    def forward(self, encoder_features, X):
        """
        Forward pass through the decoder block.

        Args:
            encoder_features (torch.Tensor): Skip connection tensor from encoder.
            X (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor.
        """
        X = self.up(X)
        encoder_features = center_crop(encoder_features, match_x=X)
        X = torch.concat([encoder_features, X], dim=1)
        X = self.double_conv(X)
        return X


class UNet(torch.nn.Module):
    def __init__(self, in_channels, num_classes, intermediary_filters=64, num_layers = 4):
        """
        U-Net model architecture.

        Args:
            in_channels (int): Number of input channels.
            num_classes (int): Number of output classes.
            intermediary_filters (int, optional): Number of filters in the first layer. Defaults to 64.
            num_layers (int, optional): Number of layers in the encoder/decoder. Defaults to 4.
        """
        super().__init__()
        self.in_conv = DoubleConv(in_channels=in_channels, out_channels=intermediary_filters, mid_channels=64)
        self.encoders = torch.nn.ModuleList([EncoderBlock(in_channels=intermediary_filters*2**i, out_channels=2*intermediary_filters*2**i) for i in range(0, num_layers)])
        self.decoders = torch.nn.ModuleList([DecoderBlock(in_channels=2*intermediary_filters*2**i, out_channels=intermediary_filters*2**i) for i in range(0, num_layers)])
        self.out_conv = torch.nn.Conv2d(in_channels=intermediary_filters, out_channels=num_classes, kernel_size=1)

    def forward(self, X):
        """
        Forward pass through the U-Net model.

        Args:
            X (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor.
        """
        X = self.in_conv(X)
        outputs = []
        outputs.append(X)
        for i, encoder in enumerate(self.encoders):
            outputs.append(encoder.forward(outputs[i]))
        X = outputs[-1]
        for i, decoder in enumerate(self.decoders[::-1]):
            X = decoder.forward(outputs[len(self.decoders) - 1 - i], X)
        X = self.out_conv(X)
        return X