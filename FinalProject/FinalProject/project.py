import random
import tkinter
from PIL import ImageTk, Image
import time

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/fam.jpg'
CANVAS_WIDTH = 700
CANVAS_HEIGHT = 600


def main():
    keep_going = True
    filename = get_file()
    image = SimpleImage(filename)
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Final Project: Editing Fun!')
    pimg = ImageTk.PhotoImage(image.pil_image)
    canvas.create_image(10, 20, image=pimg, anchor=tkinter.NW)




    while keep_going:
        keep_going = show_menu(image, canvas)
        image = SimpleImage(filename)







def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

def show_menu(image, canvas):
    time.sleep(1/2)
    print('Choose how to edit the image:')
    print('     1. Make more red')
    print('     2. Make more blue')
    print('     3. Make more green')
    print('     4. Make more yellow')
    print('     5. Play with color')
    print('     6. Random color change')
    print('     7. Flip image horizontally')
    print('     8. Flip the image vertically')
    print('     9. Gradual color change (yellow to blue)')
    print('     10. Gradual color change (yellow-pink)')
    print('     99. Move Image ')
    print('     0. Stop editing the image and end')
    selection = int(input('Which is your choice: '))
    if (selection == 0):
        keep_going = False
    else:
        keep_going = True

    edit_picture(selection, image, canvas)
    return keep_going

def edit_picture(selection, image, canvas):
    if (selection == 1):
        more_red(image, canvas)
        #image.show()
    if (selection == 2):
        more_blue(image, canvas)
        #image.show()
    if (selection == 3):
        more_green(image, canvas)
        #image.show()
    if (selection == 4):
        more_yellow(image, canvas)
        #image.show()
    if (selection == 5):
        custom_color(image, canvas)
        #image.show()
    if (selection == 6):
        random_color(image, canvas)
        #image.show()
    if (selection == 7):
        mirror = flip_horizontal(image, canvas)
        #mirror.show()
    if (selection == 8):
        image = flip_vertical(image, canvas)
        #image.show()
    if (selection == 9):
        gradual_change(image, canvas)
    if (selection == 10):
        gradual_change2(image, canvas)
    if (selection == 99):
        move_pic(image, canvas)





def gradual_change(image,canvas):
    for i in range(40):
        for pixel in image:
            blue_value = (20 - i)
            red_value = i

            pixel.red = pixel.red-(red_value*2)
            pixel.green = pixel.green
            pixel.blue = pixel.blue-(blue_value*2)
        pimg = ImageTk.PhotoImage(image.pil_image)
        canvas.create_image(10, 20, image = pimg, anchor=tkinter.NW)
        canvas.update()
    #canvas.create_image(10, 20, image = pimg, anchor=tkinter.NW)


    #input('Hit Enter to continue')

def gradual_change2(image,canvas):
    #img = Image.open('filename.png')
    for i in range(37):
        for pixel in image:
            blue_value = (20 - i)
            red_value = i
           # pixel.red = pixel.red
            pixel.red = pixel.red
            pixel.green = pixel.green-(red_value*1.5)
            pixel.blue = pixel.blue-(blue_value*1.5)
        pimg = ImageTk.PhotoImage(image.pil_image)
        canvas.create_image(10, 20, image = pimg, anchor=tkinter.NW)
        canvas.update()

def make_canvas(width, height, title):
    """
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

def custom_color(image, canvas):
    red_value = int(input('Pick a number between 0 and 20 for the red: '))
    blue_value = int(input('Pick a number between 0 and 20 for the blue: '))
    green_value = int(input('Pick a number between 0 and 20 for the green: '))
    for pixel in image:
        pixel.red = pixel.red*(red_value/10)
        pixel.green = pixel.green*(green_value/10)
        pixel.blue = pixel.blue*(blue_value/10)
    pimg = ImageTk.PhotoImage(image.pil_image)
    canvas.create_image(10, 20, image=pimg, anchor=tkinter.NW)
    canvas.update()
    time.sleep(1)



def random_color(image, canvas):
    red_value = random.randint(1,20)
    blue_value = random.randint(1,20)
    green_value = random.randint(1,20)
    for pixel in image:
        pixel.red = pixel.red * (red_value / 10)
        pixel.green = pixel.green * (green_value / 10)
        pixel.blue = pixel.blue * (blue_value / 10)
    pimg = ImageTk.PhotoImage(image.pil_image)
    canvas.create_image(10, 20, image=pimg, anchor=tkinter.NW)
    canvas.update()
    time.sleep(1)

def more_blue(image, canvas):
    for pixel in image:
        pixel.red = pixel.red*0.4
        pixel.green = pixel.green*0.4
        pixel.blue = pixel.blue*1.7
    pimg = ImageTk.PhotoImage(image.pil_image)
    canvas.create_image(10, 20, image=pimg, anchor=tkinter.NW)
    canvas.update()
    return canvas

def more_red(image, canvas):
    for pixel in image:
        pixel.red = pixel.red*1.2
        pixel.green = pixel.green*0.5
        pixel.blue = pixel.blue*0.5
    pimg = ImageTk.PhotoImage(image.pil_image)
    canvas.create_image(10, 20, image=pimg, anchor=tkinter.NW)
    canvas.update()
    return canvas

def more_green(image, canvas):
    for pixel in image:
        pixel.red = pixel.red*0.4
        pixel.green = pixel.green*1.6
        pixel.blue = pixel.blue*0.4
    pimg = ImageTk.PhotoImage(image.pil_image)
    canvas.create_image(10, 20, image=pimg, anchor=tkinter.NW)
    canvas.update()
    return canvas

def more_yellow(image, canvas):
    for pixel in image:
        pixel.red = pixel.red*1.6
        pixel.green = pixel.green*1.6
        pixel.blue = pixel.blue*0.1
    pimg = ImageTk.PhotoImage(image.pil_image)
    canvas.create_image(10, 20, image=pimg, anchor=tkinter.NW)
    canvas.update()
    return canvas

def flip_vertical(image, canvas):
    width = image.width
    height = image.height
    #Create new image to contain the new reflected image
    mirror = SimpleImage.blank(width, height)

    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x,y)
            mirror.set_pixel(x,height - (y+1),pixel)
    pimg = ImageTk.PhotoImage(mirror.pil_image)
    canvas.create_image(10, 20, image=pimg, anchor=tkinter.NW)
    canvas.update()
    time.sleep(1)

    return mirror

def flip_horizontal(image, canvas):
    width = image.width
    height = image.height
    #Create new image to contain the new reflected image
    mirror = SimpleImage.blank(width, height)
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x,y)
            mirror.set_pixel(width - (x+1),y,pixel)
    pimg = ImageTk.PhotoImage(mirror.pil_image)
    canvas.create_image(10, 20, image=pimg, anchor=tkinter.NW)
    canvas.update()
    time.sleep(1)

    return mirror
def move_pic(image, canvas):
    #canvas = make_canvas(700, 600, 'Final Project: Morphing Picture')

    pimg = ImageTk.PhotoImage(image.pil_image)
    img_tk = canvas.create_image(10, 20, image=pimg, anchor=tkinter.NW)
    change_x=3
    change_y =7
    count = 0
    while (count < 7):
        #update world
        canvas.move(img_tk, change_x,change_y)
        if (hit_bottom(canvas, img_tk, pimg)):
            change_y = change_y*-1
            count = count + 1
        if (hit_side(canvas, img_tk, pimg)):
            change_x *= -1
            count = count + 1
        if (hit_top(canvas, img_tk, pimg)):
            change_y *= -1
            count = count + 1
        if (hit_other_side(canvas, img_tk, pimg)):
            change_x *= -1
            count += 1
        canvas.update()
        #pause
        time.sleep(1/70.)
    #canvas.update()
    #canvas.mainloop()
def hit_bottom(canvas, object, pimg):
    return canvas.coords(object)[1] > CANVAS_HEIGHT - pimg.height()
def hit_side(canvas, object, pimg):
    return canvas.coords(object)[0]>CANVAS_WIDTH - pimg.width()
def hit_top(canvas, object, pimg):
    return canvas.coords(object)[1] <= 0
def hit_other_side(canvas, object, pimg):
    return canvas.coords(object)[0] <= 0



if __name__ == '__main__':
    main()