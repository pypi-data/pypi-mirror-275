import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from lang_sam import LangSAM
import torch
import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image
import os
from sklearn.decomposition import PCA
from scipy.ndimage import rotate
import cv2
import os
import numpy as np

def process_video(video_files, video_path, output_path, initial_point=(500, 600)):
    for i in video_files:
        cap = cv2.VideoCapture(os.path.join(video_path, i))    
        print(os.path.join(video_path, i))

        # Take first frame
        ret, old_frame = cap.read()
        old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
        
        # Set the initial tracking point
        p0 = np.array([[list(initial_point)]], dtype=np.float32)
        
        # Initialize the previous point (this will be updated in each frame)
        prev_point = p0[0,0].copy()

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
        out = cv2.VideoWriter(os.path.join(output_path, f'{i.split(".")[0]}.mp4'), fourcc, 30.0, (old_frame.shape[1], old_frame.shape[0]))
        
        while True:
            ret, frame = cap.read()
            
            # Break the loop if the frame can't be read
            if not ret:
                break
        
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            # Calculate optical flow using Farneback method
            flow = cv2.calcOpticalFlowFarneback(old_gray, frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        
            # Update the tracking point
            p0 += flow[int(p0[0,0,1]), int(p0[0,0,0])]
        
            # Draw the tracking point
            a, b = map(int, p0[0,0])
            frame = cv2.circle(frame, (a, b), 5, (0, 0, 255), -1)  # Red color
        
            # Write the frame into the file 'output.mp4'
            out.write(frame)
        
            # Now update the previous frame
            old_gray = frame_gray.copy()

        # Release the VideoCapture and VideoWriter objects and close all windows
        cap.release()
        out.release()
        cv2.destroyAllWindows()

def get_angle(matrix):
    x = np.array(np.where(matrix > 0)).T
    pca = PCA(n_components=2).fit(x)
    angles = np.arctan2(pca.components_[:,1], pca.components_[:,0])
    angles = np.rad2deg(angles)
    angles = np.mod(angles, 180)
    if abs(90 - angles[0]) < 30:
        angle = angles[0]
    else:
        angle = angles[1]
    return 90 - angle

def slope_and_intercept(line):
    x1, y1, x2, y2 = line
    slope = (x2 - x1) / (y2 - y1)
    intercept = x1 - (slope * y1)
    return slope, intercept

def line_getter(slope, intercept, SHAPE):
    new_x1 = int(intercept)
    new_y1 = 0
    new_x2 = int(slope * SHAPE[0] + intercept)
    new_y2 = SHAPE[0]
    return new_x1, new_y1, new_x2, new_y2

def boundry_locator(res,pca_angle):
    SHAPE = res.shape
    PERCENT_INLIERS_HIGH = 0.60
    PERCENT_INLIERS_LOW = 0.50
    depth_filtered_mask = (res > 0) * 1
    depth_filtered_mask_rotated = rotate(depth_filtered_mask * 1, pca_angle, reshape=False)
    img = depth_filtered_mask_rotated
    first_row = 0
    last_row = 0
    for i in range(img.shape[0]):
        col = img[i,:]
        if np.any(col):
            first_row = i
            break
    for i in range(img.shape[0]-1, -1, -1):
        col = img[i,:]
        if np.any(col):
            last_row = i
            break
   
    diff = last_row - first_row
    depth_filtered_mask_rotated = (np.abs(depth_filtered_mask_rotated) > 0.00) * 1
    left_boundary = 0
    for j in range(SHAPE[1]):
        counts = np.bincount(depth_filtered_mask_rotated[:, j])
        if len(counts) < 2:
            continue
        if counts[1] / diff > PERCENT_INLIERS_HIGH:
            left_boundary = j
            break
    for j in range(left_boundary - 1, -1, -1):
        counts = np.bincount(depth_filtered_mask_rotated[:, j])
        if len(counts) < 2:
            continue
        if counts[1] / diff < PERCENT_INLIERS_LOW:
            left_boundary = j + 1
            break


    right_boundary = 0
    for j in range(SHAPE[1] - 1, -1, -1):
        counts = np.bincount(depth_filtered_mask_rotated[:, j])
        if len(counts) < 2:
            continue
        if counts[1] / diff > PERCENT_INLIERS_HIGH:
            right_boundary = j
            break

    for j in range(right_boundary, SHAPE[1]):
        counts = np.bincount(depth_filtered_mask_rotated[:, j])
        if len(counts) < 2:
            continue
        if counts[1] / diff < PERCENT_INLIERS_LOW:
            right_boundary = j - 1
            break
    return left_boundary, right_boundary

def canvas_rotated_boundary(left_boundary,right_boundary,pca_angle, SHAPE):
    

    canvans_left_boundary = np.zeros(SHAPE, dtype=np.uint8)
    canvans_right_boundary = np.zeros(SHAPE, dtype=np.uint8)
   
    canvans_left_boundary[:,left_boundary] = 255
    canvans_right_boundary[:,right_boundary] = 255
    
    canvans_left_boundary = rotate(canvans_left_boundary * 1, -pca_angle, reshape=False)
    canvans_right_boundary = rotate(canvans_right_boundary * 1, -pca_angle, reshape=False)
    

    left_top_point = (0,0)
    left_bottom_point = (0,0)
    for i in range(canvans_left_boundary.shape[0]):
        columns = np.where(canvans_left_boundary[i,:] > 0)[0]
        if columns.size > 0:
            left_top_point = (columns[0], i)
            break
    for i in range(canvans_left_boundary.shape[0] - 1, -1, -1):
        columns = np.where(canvans_left_boundary[i,:] > 0)[0]
        if columns.size > 0:
            left_bottom_point = (columns[0], i)
            break
    line_left = (left_top_point[0], left_top_point[1], left_bottom_point[0], left_bottom_point[1])

    right_top_point = (0,0)
    right_bottom_point = (0,0)
    for i in range(canvans_right_boundary.shape[0]):
        columns = np.where(canvans_right_boundary[i,:] > 0)[0]
        if columns.size > 0:
            right_top_point = (columns[0], i)
            break
    for i in range(canvans_right_boundary.shape[0] - 1, -1, -1):
        columns = np.where(canvans_right_boundary[i,:] > 0)[0]
        if columns.size > 0:
            right_bottom_point = (columns[0], i)
            break
    line_right = (right_top_point[0], right_top_point[1], right_bottom_point[0], right_bottom_point[1])
    
    slope1, intercept1 = slope_and_intercept(line_left)
    slope2, intercept2 = slope_and_intercept(line_right)
    
    new_x1, new_y1 ,new_x2, new_y2 = line_getter(slope1, intercept1, SHAPE)
    new_x3, new_y3 ,new_x4, new_y4 = line_getter(slope2, intercept2,SHAPE)
    
    canvans_left = np.zeros(SHAPE, dtype=np.uint8)
    cv2.line(canvans_left, (new_x1, new_y1), (new_x2, new_y2), (255, 255, 255), 2)
    canvans_right = np.zeros(SHAPE, dtype=np.uint8)
    cv2.line(canvans_right, (new_x3, new_y3), (new_x4, new_y4), (255, 255, 255), 2)
    return canvans_left,canvans_right,slope1,intercept1,slope2,intercept2

def borders_to_segmented_images(seg_img,img):
    enh_image = seg_img
    gray_img = cv2.cvtColor(enh_image, cv2.COLOR_BGR2GRAY)
    mask = gray_img > 0
    mask = mask.astype(np.uint8) * 255
    theta = get_angle(mask)
    lb, rb = boundry_locator(mask, theta)
    canvas_left, canvas_right,slope1,intercept1,slope2,intercept2 = canvas_rotated_boundary(lb, rb, theta, mask.shape)
    single_canvas = cv2.bitwise_or(canvas_left, canvas_right)
    single_canvas_rgb = cv2.cvtColor(single_canvas, cv2.COLOR_GRAY2BGR)
    borders_in_image = cv2.bitwise_or(single_canvas_rgb, img)
    return borders_in_image,slope1,intercept1,slope2,intercept2

def borders_to_original_images(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_img = cv2.threshold(gray_img, 160, 255, cv2.THRESH_BINARY)
    mask = binary_img > 0
    mask = mask.astype(np.uint8) * 255
    theta = get_angle(mask)
    lb, rb = boundry_locator(mask, theta)
    canvas_left, canvas_right,slope1,intercept1,slope2,intercept2 = canvas_rotated_boundary(lb, rb, theta, mask.shape)
    single_canvas = cv2.bitwise_or(canvas_left, canvas_right)
    single_canvas_rgb = cv2.cvtColor(single_canvas, cv2.COLOR_GRAY2BGR)
    borders_in_image = cv2.bitwise_or(single_canvas_rgb, img)
    return borders_in_image,slope1,intercept1,slope2,intercept2

def border_lines_cap(video_files, video_path, output_path, text_prompt="Identify and segment the image to isolate any tree trunks present. If multiple tree trunks are detected, focus on segmenting only the largest one. There will atleast one tree trunk in every image", model=LangSAM()):
    for im in video_files:
        cap = cv2.VideoCapture(os.path.join(video_path, im))
        i = 0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break

            image_rgb = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            masks, boxes, phrases, logits = model.predict(image_rgb, text_prompt)
            masks_np = [mask.squeeze().cpu().numpy() for mask in masks]
            fin_img = None

            if len(masks_np) != 0 and len(masks_np[0][:]) != 0:
                seg_img = image_rgb*np.stack([masks_np[0][:]]*3, axis=-1)
                fin_img,slope1,intercept1,slope2,intercept2 = borders_to_segmented_images(seg_img,frame)
                print("slope left:",slope1, "intercept left:",intercept1,"slope right:",slope2,"intercept right:",intercept2)
                print(i)
            else:
                fin_img,slope1,intercept1,slope2,intercept2 = borders_to_original_images(frame)
                print("slope left:",slope1, "intercept left:",intercept1,"slope right:",slope2,"intercept right:",intercept2)
                print(i)

            if not os.path.exists(os.path.join(output_path,im.split(".")[0])):
                os.makedirs(os.path.join(output_path,im.split(".")[0]))

            cv2.imwrite(os.path.join(output_path,im.split(".")[0],f"frame{i}.jpg"),fin_img)
            i += 1
            plt.imshow(fin_img)
            plt.show()
        cap.release()

def create_video(image_folder, output_file):
    command = f"ffmpeg -r 30 -i {image_folder}/frame%01d.jpg -vcodec mpeg4 -y {output_file}"
    os.system(command)