import cv2

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.5
FONT_COLOR = (255, 0, 0)
LINETYPE = 2


def draw_bounding_box(image, bbox, color=(0, 255, 0), thickness=2, idx=""):
    top_left_x, top_left_y, right_bottom_x, right_bottom_y = bbox
    top_left_x, top_left_y, right_bottom_x, right_bottom_y = (
        int(top_left_x),
        int(top_left_y),
        int(right_bottom_x),
        int(right_bottom_y),
    )
    w = round(right_bottom_x - top_left_x)
    h = round(right_bottom_y - top_left_y)
    image = cv2.line(
        image,
        (top_left_x, top_left_y),
        (top_left_x + w // 4, top_left_y),
        color,
        thickness,
    )

    image = cv2.line(
        image,
        (top_left_x, top_left_y),
        (top_left_x, top_left_y + h // 4),
        color,
        thickness,
    )

    image = cv2.line(
        image,
        (top_left_x + w, top_left_y),
        (top_left_x + w - w // 4, top_left_y),
        color,
        thickness,
    )

    image = cv2.line(
        image,
        (top_left_x + w, top_left_y),
        (top_left_x + w, top_left_y + h // 4),
        color,
        thickness,
    )

    image = cv2.line(
        image,
        (top_left_x, top_left_y + h),
        (top_left_x + w // 4, top_left_y + h),
        color,
        thickness,
    )

    image = cv2.line(
        image,
        (top_left_x, top_left_y + h),
        (top_left_x, top_left_y + h - h // 4),
        color,
        thickness,
    )

    image = cv2.line(
        image,
        (top_left_x + w, top_left_y + h),
        (top_left_x + w - w // 4, top_left_y + h),
        color,
        thickness,
    )

    image = cv2.line(
        image,
        (top_left_x + w, top_left_y + h),
        (top_left_x + w, top_left_y + h - h // 4),
        color,
        thickness,
    )

    cv2.putText(
        image,
        idx[:5],
        (top_left_x, top_left_y - 5),
        FONT,
        FONT_SCALE,
        color,
        LINETYPE,
    )

    return image
