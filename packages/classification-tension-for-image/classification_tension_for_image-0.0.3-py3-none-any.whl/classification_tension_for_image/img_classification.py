import torch
import torchvision.transforms as transforms
from PIL import Image
import torch.nn as nn
import torchvision.models as models


class GrayScaleResNet(nn.Module):
    def __init__(self):
        super(GrayScaleResNet, self).__init__()
        self.resnet = models.resnet18(pretrained=False)
        self.resnet.conv1 = nn.Conv2d(
            1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False
        )
        self.num_classes = 7
        num_ftrs = self.resnet.fc.in_features
        self.resnet.fc = nn.Linear(num_ftrs, self.num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.resnet(x)


class ImgClassificationTension:
    def __init__(self, model_path: str, num_candidates: int = 2):
        self.num_classes = 7
        self.num_candidates = num_candidates
        self.model = self.load_model(model_path)
        self.transform = self.setup_transform()

    def setup_transform(self) -> transforms.Compose:
        """
        画像の前処理設定
        """
        transform = transforms.Compose(
            [
                transforms.Resize([224, 224]),
                transforms.Grayscale(num_output_channels=1),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485], std=[0.229]),
            ]
        )
        return transform

    def load_model(self, model_path: str):
        """
        モデルの読み込みと初期化
        """
        model = GrayScaleResNet()
        model_dict = model.state_dict()
        pretrained_dict = torch.load(model_path)
        pretrained_dict = {
            k: v
            for k, v in pretrained_dict.items()
            if k in model_dict and v.size() == model_dict[k].size()
        }
        model_dict.update(pretrained_dict)
        model.load_state_dict(model_dict, strict=False)
        model.eval()
        return model

    def predict(self, image_path):
        """
        画像を予測する関数
        """
        image = Image.open(image_path).convert("L")
        tensor_image = self.transform(image).unsqueeze(0)
        outputs = self.model(tensor_image)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        top_prob, top_classes = torch.topk(probabilities, self.num_candidates)
        top_prob_percent = [round(prob.item() * 100, 2) for prob in top_prob[0]]
        class_names = ["5", "4", "3", "2", "1", "0", "6"]
        predictions = [
            (class_names[class_idx], prob)
            for class_idx, prob in zip(top_classes[0], top_prob_percent)
        ]
        results = []
        for class_name, prob in predictions:
            results.append(f"{class_name}: {prob}%")
        print(results)
        return results


# # 使用例
# model_path = "ResNet152_weights.pth"  # モデルのパス
# img_path = "path/to/image.jpg"  # 画像のパス
# classifier = ImgClassificationTension(model_path)
# predictions = classifier.predict(img_path)
# for prediction in predictions:
#     print(prediction)
