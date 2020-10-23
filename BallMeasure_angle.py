from PIL import Image
from math import pi, sin, cos, sqrt
from statistics import stdev

PATH = r'C:\Users\Leo Kuchen\Documents\Skola\GA\Rundhet\Test_bilder_paint\wonkyboi.png'
B = 819
H = 460

bild = Image.open(PATH)

bild_rgb = bild.convert("RGB")

def get_boll(im,width,height):
    print('finding ball...')
    boll = []
    for b in range(width):
        for h in range(height):
            p = im.getpixel((b,h))
            is_boll = True
            for c in p:
                if c > 127:
                    is_boll = False
            if is_boll:
                boll.append([b,h])
    return boll
            
            
def get_mid(ball_list):
    print('calculating midpoint of ball...')
    mb = 0
    mh = 0
    for i in ball_list:
        mb += i[0]
        mh += i[1]
    mb /= len(ball_list)
    mh /= len(ball_list)
    return [mb, mh]

def find_single_vector(mpoint, b_list, step_size, cosineu, sineu, rstart):
    inside = True
    r=rstart
    while inside:
        p0 = [ int(cosineu*r) , int(sineu*r) ]
        p = [ int(mpoint[0])+p0[0] , int(mpoint[1])+p0[1] ]
        if not p in b_list:
            inside = False
            return [p0, r-step_size]
        r+= step_size
    
        

def get_vectors(ball_list, midpoint):
    vsteps = 360
    print(f'calculating vectors (resolution = {vsteps})...')
    vectors = []
    for v in range(vsteps):
        #print(v)
        u = (v*2*pi)/vsteps
        cosu = cos(u)
        sinu = sin(u)
        r0 = find_single_vector(midpoint, ball_list, 50,cosu,sinu,0)[1]
        r0 = find_single_vector(midpoint, ball_list, 20, cosu,sinu,r0)[1]
        r0 = find_single_vector(midpoint, ball_list, 4,cosu,sinu,r0)[1]
        r0 = find_single_vector(midpoint, ball_list, 1,cosu,sinu,r0)[1]
        #r0 = find_single_vector(midpoint, ball_list, 1,cosu,sinu,r0)[1]
        vectors.append( find_single_vector(midpoint, ball_list, 1,cosu,sinu,r0)[0] )
        #print(v)#f'\nANGLE FINISHED: {v}\n')
        
    return vectors

def get_roundness(vectors):
    print('calculating roundness...')
    magnitudes = []
    avg = 0
    for i in vectors:
        m = sqrt(i[0]**2 + i[1]**2)
        magnitudes.append(m)
        avg += m

    avg /= len(vectors)
    dev = stdev(magnitudes)
    
    return {'average_radius' : avg, 'standard_deviation' : dev, 'roundness' : 1-(dev/avg)}
            
    
blist = get_boll(bild_rgb,B,H)

mid = get_mid(blist)

vec = get_vectors(blist,mid)

roundness = get_roundness(vec)

print(roundness)
