import typer
import cv2
import os
from ultralytics import YOLOv10
import torch
from tqdm import tqdm

labels = [
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "airplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "couch",
    "potted plant",
    "bed",
    "dining table",
    "toilet",
    "tv",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]

# make sure to point to the correct weights file
path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(path, "weights/yolov10n.pt")

model = YOLOv10(path)
app = typer.Typer()


def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    full_result = torch.zeros((frame_count, len(labels)), dtype=torch.int8)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    with tqdm(total=frame_count, desc="Processing frames") as pbar:
        frame_index = 0
        while True:
            ret, frame = cap.read()

            if not ret:
                break

            results = model(frame, verbose=False)
            for result in results:
                x_long = result.boxes.cls.long()
                full_result[frame_index, :].scatter_add_(
                    0, x_long, torch.ones_like(x_long, dtype=torch.int8)
                )

            pbar.update(1)
            frame_index += 1

            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()

    torch.save(full_result, f"{video_path}.pt")
    print(f"Results saved to {video_path}.pt")


@app.command()
def vindex(path: str):
    if (
        os.path.exists(path)
        and os.path.isfile(path)
        and path.lower().endswith((".mp4", ".avi", ".mov"))
    ):
        typer.echo(f"Video file is valid: {path}")
        process_video(path)
    else:
        typer.echo("Invalid video file path or format.")


@app.command()
def common(path: str):
    if os.path.exists(path) and os.path.isfile(path) and path.lower().endswith(".pt"):
        results = torch.load(path)
        total = results.sum(dim=0)
        top_5 = torch.topk(total, 5)
        for i in range(5):
            key = top_5.indices[i].item()
            typer.echo(f"{labels[key]}: {top_5.values[i].item()}")
    else:
        typer.echo("Invalid file path or format.")


@app.command()
def where(path: str, object_name: str, avoid_single_frames: bool = False):
    if os.path.exists(path) and os.path.isfile(path) and path.lower().endswith(".pt"):
        results = torch.load(path)
        if object_name not in labels:
            typer.echo(f"Object '{object_name}' not found in labels.")
            return

        object_index = labels.index(object_name)
        indices = torch.nonzero(results[:, object_index]).squeeze()

        if indices.numel() == 0:
            typer.echo(f"{object_name} does not appear in the video.")
        else:
            contiguous_ranges = []
            start = indices[0].item()
            end = start

            for idx in indices[1:]:
                idx = idx.item()
                if idx == end + 1:
                    end = idx
                else:
                    if avoid_single_frames:
                        if start != end:
                            contiguous_ranges.append((start, end))
                    else:
                        contiguous_ranges.append((start, end))
                    start = idx
                    end = start

            contiguous_ranges.append((start, end))

            for start, end in contiguous_ranges:
                typer.echo(f"{object_name} appears between frames {start} and {end}")
    else:
        typer.echo("Invalid file path or format.")


if __name__ == "__main__":
    app()
