
#
# Intersection over Union
# format 'xywh' bounding box [x, y, w, h]
# format 'xyxy' bounding box [x1, y1, x2, y2]
#
def iou(bbox1, bbox2, format='xywh'):
    if format == 'xywh':
        b1_x, b1_y, b1_w, b1_h = bbox1
        b1_w2 = b1_w / 2
        b1_h2 = b1_h / 2
        b1_x1 = b1_x - b1_w2
        b1_y1 = b1_y - b1_h2
        b1_x2 = b1_x + b1_w2
        b1_y2 = b1_y + b1_h2

        b2_x, b2_y, b2_w, b2_h = bbox2
        b2_w2 = b2_w / 2
        b2_h2 = b2_h / 2
        b2_x1 = b2_x - b2_w2
        b2_y1 = b2_y - b2_h2
        b2_x2 = b2_x + b2_w2
        b2_y2 = b2_y + b2_h2
    elif format == 'xyxy':
        # todo
        pass
    else:
        print('Bounding box format not supported.')

    inter_x1 = max(b1_x1, b2_x1)
    inter_y1 = max(b1_y1, b2_y1)
    inter_x2 = min(b1_x2, b2_x2)
    inter_y2 = min(b1_y2, b2_y2)

    inter = max(0, inter_x2 - inter_x1 ) * max(0, inter_y2 - inter_y1) # max is to clamp(min=0)
    union = (b1_x2 - b1_x1) * (b1_y2 - b1_y1) + (b2_x2 - b2_x1) * (b2_y2 - b2_y1) - inter
    return inter / union

