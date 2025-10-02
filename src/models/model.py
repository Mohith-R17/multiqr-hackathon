import torch.nn as nn

class QRDetector(nn.Module):
    def __init__(self):
        super(QRDetector, self).__init__()
        self.backbone = nn.Sequential(
            nn.Conv2d(3, 16, 3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, 3, stride=2, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1,1))
        )
        self.fc = nn.Linear(32, 4)  # bbox [x_min, y_min, x_max, y_max]

    def forward(self, x):
        x = self.backbone(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)
