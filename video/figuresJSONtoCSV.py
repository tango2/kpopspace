import json
import os

# Order of keypoints, from the COCO dataset specs
keypoints = [
        'nose',
        'left_eye',
        'right_eye',
        'left_ear',
        'right_ear',
        'left_shoulder',
        'right_shoulder',
        'left_elbow',
        'right_elbow',
        'left_wrist',
        'right_wrist',
        'left_hip',
        'right_hip',
        'left_knee',
        'right_knee',
        'left_ankle',
        'right_ankle'
    ]

# Each line in the CSV output file will have the format:
# frame_timecode, frame_id, figure_index, fig_box_min_x, fig_box_min_y, fig_box_max_x, fig_box_max_y, fig_nose_x, fig_nose_y, fig_left_eye_x, fig_left_eye_y, fig_right_eye_x, fig_right_eye_y, ... and so on through all the body parts

csv_header = ["frame_timecode", "frame_id", "figure_index", "fig_box_min_x", "fig_box_min_y", "fig_box_max_x", "fig_box_max_y"]
for part in keypoints:
    csv_header.append(part + "_x")
    csv_header.append(part + "_y")

for in_file in os.listdir('figuresJSON'):
    if (not in_file.endswith('.json')):
        continue
    print("Processing",in_file)
    csv_file_name = in_file.replace('.json','.csv')

    with open('figuresJSON/' + in_file, 'r') as json_file:
        json_data = json.load(json_file)

        json_list = []
        for frame_data in json_data:
            time_code = list(frame_data.keys())[0]
            frame_info = frame_data[time_code]
            frame_info['timecode'] = time_code 
            json_list.append(frame_info)

        with open('figuresCSV/' + csv_file_name, 'w') as csv_file:
            csv_file.write(",".join(csv_header) + "\n")
            for item_data in json_list:
                frame_id = item_data['frameID']
                timecode = item_data['timecode']

                if (len(item_data['boxes']) == 0):
                    # If a frame has no detections in it,
                    # srite a blank entry (except for frame ID and timecode)
                    parts_list = []
                    for part in keypoints:
                        parts_list += ["N/A", "N/A"]
                    out_list = [timecode, frame_id, "N/A"]
                    out_list += ["N/A", "N/A", "N/A", "N/A"]
                    out_list += parts_list
                    csv_file.write(",".join(out_list) + "\n")
                    continue

                for i in range(0, len(item_data['boxes'])):
                    figure_index = str(i + 1)
                    parts_list = []
                    for part in keypoints:
                        if (part not in item_data['keypoints'][i]):
                            parts_list += ["N/A", "N/A"]
                        else:
                            parts_list += [item_data['keypoints'][i][part][0], item_data['keypoints'][i][part][1]]
                    out_list = [timecode, frame_id, figure_index]
                    out_list += item_data['boxes'][i]
                    out_list += parts_list

                    csv_file.write(",".join(out_list) + "\n")
