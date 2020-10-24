from PIL import Image, ImageDraw
from math import pi, sin, cos, sqrt
from statistics import pstdev, mean
from time import perf_counter

tic = perf_counter()

PATH = r'C:\Users\Leo Kuchen\Documents\Skola\GA\Rundhet\Test_bilder_paint\rund.png'
VISUALIZE_PATH = r'C:\Users\Leo Kuchen\Documents\Skola\GA\Rundhet\Test_bilder_paint\rund_visualize.png'

image = Image.open(PATH)
SIZE = image.size

im_rgb = image.convert("RGB")

##image_matrix = [] #xy matrix, will contain bools. True means ball, False means no ball. Use this when examining a specific point.
##ball_points = [] #List of all the points on the ball. Use this when you want to get all the points on the ball.

#HAS TO BE MODIFIED BEFORE USING REAL IMAGES
def get_ball(im,width,height):
    image_matrix, ball_points = [], []
    print('finding ball...')
    for x in range(width):
        image_matrix.append([]) #Create a new column
        for y in range(height):
            pixel = im.getpixel((x,y))
            
            #A way of determing if a pixel is ball or non-ball suitable for real photos has to be created here.
            #The four lines below are essentially useless with real photos
            pixel_is_boll = True
            for coulor in pixel:
                if coulor > 127:
                    pixel_is_boll = False
                    
            image_matrix[x].append(pixel_is_boll) #Append Bool to the newly created column
            if pixel_is_boll:
                ball_points.append([x,y])

    return image_matrix, ball_points
            
            
def get_mid(ball_points):
    print('calculating midpoint of ball...')
    mid_x = 0
    mid_y = 0
    for i in ball_points:
        mid_x += i[0]
        mid_y += i[1]
    mid_x /= len(ball_points)
    mid_y /= len(ball_points)
    return [mid_x, mid_y]

def is_edge(point,matrix):
    is_edge = False
    
    #Here we check a square of 9 pixels surrouning a point. If one or more of them is NOT ball then our point is an edge point.
    for x in range(3):
        for y in range(3):
            point_to_check = [point[0]-1+x , point[1]-1+y]
            if not matrix[point_to_check[0]][point_to_check[1]]:
                is_edge = True
                return is_edge
    

def find_raw_edge(ball_points, matrix):
    print('finding edge...')
    edge_pixels = []
    for point in ball_points:
        if is_edge(point, matrix):
            edge_pixels.append(point)
    return edge_pixels

def get_roundness(midpoint,edge):
    print('calculating roundness...')
    magnitudes = []
    for i in edge:
        m = sqrt((i[0]-midpoint[0])**2 + (i[1]-midpoint[1])**2)
        magnitudes.append(m)

    avg = mean(magnitudes)
    dev = pstdev(magnitudes)
    
    return {'average_radius' : avg, 'standard_deviation' : dev, 'roundness' : 1-(dev/avg)}

def visualize(points, image_size, output_path):
    out = Image.new("RGB", (image_size[0],image_size[1]), "white")
    draw = ImageDraw.Draw(out)

    for p in points:
        draw.point((p[0],p[1]), fill="black")

    out.save(output_path)

image_matrix, ball_points = get_ball(im_rgb, SIZE[0], SIZE[1])
#image_matrix: xy matrix, will contain bools. True means ball, False means no ball. Use this when examining a specific point.
#ball_points: #List of all the points on the ball. Use this when you want to get all the points on the ball.

midpoint = get_mid(ball_points)
raw_edge = find_raw_edge(ball_points, image_matrix)
roundness = get_roundness(midpoint,raw_edge)

toc = perf_counter()
print(f'processing time: {toc-tic:0.3} seconds')
print(roundness)

#visualize(raw_edge, SIZE, VISUALIZE_PATH)
