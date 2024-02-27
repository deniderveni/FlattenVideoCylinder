import cv2
import numpy as np
import sys

# Function to convert cylindrical rotation to 2D flat plane
def convert_cylindrical_to_2d(video_path, output_path, clockwise=True):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Calculate cw based on specified res, fps, and video duration
    res = width
    time = frame_count / fps
    real_cw = res / (time * fps)
    cw = int(np.ceil(res / (time * fps)))

    # Calculate the fractional difference between real_cw and cw
    overlap_fraction = (cw - real_cw) / cw

    # Initialize the flattened image
    flattened_image = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Take a slice from the center based on the rotational angle
        slice_start = frame.shape[1] // 2 - cw // 2
        slice_end = slice_start + cw
        central_slice = frame[:, slice_start:slice_end, :]

        # Apply transparency to the slice
        central_slice = cv2.addWeighted(central_slice, 0.5, np.zeros_like(central_slice), 0.5, 0)

        # Append the slice to the flattened image based on the "clockwise" argument
        if clockwise:
            if flattened_image is None:
                flattened_image = central_slice
            else:
                flattened_image = np.hstack([flattened_image, central_slice])
        else:
            if flattened_image is None:
                flattened_image = central_slice
            else:
                # Calculate the overlap based on the fractional difference
                overlap_width = int(np.ceil(cw * overlap_fraction))
                flattened_image = np.hstack([central_slice[:, :-overlap_width, :], flattened_image])

    # Release video capture object
    cap.release()

    # Save the flattened image
    cv2.imwrite(output_path, flattened_image)

    print("Conversion complete. Flattened image saved at:", output_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_video_path> <output_image_path> <clockwise (bool)>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    clockwise_arg = sys.argv[3].lower()

    if clockwise_arg == "true":
        clockwise = True
    elif clockwise_arg == "false":
        clockwise = False
    else:
        print("Invalid value for 'clockwise'. Please use 'true' or 'false'.")
        sys.exit(1)

    convert_cylindrical_to_2d(input_path, output_path, clockwise)

