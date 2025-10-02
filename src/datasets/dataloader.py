from torch.utils.data import Dataset

class QRDataset(Dataset):
    def __init__(self, data_path):
        self.data_path = data_path
        # TODO: implement dataset loading

    def __len__(self):
        return 0  # placeholder

    def __getitem__(self, idx):
        # TODO: return image, bbox
        return None, None
