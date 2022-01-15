import os

import pandas as pd

VGGFACE_ROOT_DIR = os.path.abspath(
    os.path.join(__file__, "../../../dataset/VGGFace")
)


def download_vggdataset():
    os.makedirs(os.path.join(VGGFACE_ROOT_DIR, "images"), exist_ok=True)
    os.makedirs(os.path.join(VGGFACE_ROOT_DIR, "labels"), exist_ok=True)
    people_names = os.listdir(os.path.join(VGGFACE_ROOT_DIR, "files"))

    cols = [
        "img_id",
        "link",
        "top_left_x",
        "top_left_y",
        "bottom_right_x",
        "bottom_right_y",
        "pose",
        "detection score",
        "curation",
    ]

    for person_name in people_names:
        dest_dir = os.path.join(VGGFACE_ROOT_DIR, "images", person_name)
        os.makedirs(dest_dir, exist_ok=True)

        df = pd.read_csv(
            os.path.join(VGGFACE_ROOT_DIR, "files", person_name),
            sep=" ",
            header=None,
            names=cols,
        )
        rows = df.sample(15).loc[
            :, ~df.columns.isin(["detection score", "curation"])
        ]
        for row in rows.itertuples():
            os.system(f"wget -P {dest_dir} {row.link}")
        rows.to_csv(
            os.path.join(VGGFACE_ROOT_DIR, "labels", person_name), index=False
        )
        break


if __name__ == "__main__":
    pass
