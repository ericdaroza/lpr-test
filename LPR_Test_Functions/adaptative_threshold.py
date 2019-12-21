import cv2 as cv
import os


def nothing(x):
    pass


'''
    block_size_control tem como objetivo controlar a variavel block_size dentro das funções de cv2.adaptiveThreshold(),
    modificando o tamanho de filtro, com o entuido de ter um melhor controle sobre o processamento da imagem.

    Utilize as teclas de setas da esquerda e direita para variar o valor.

    Ela recebe como parâmetro:

    $ keyboard: a varivel do teclado na qual é lida constantemente.
    $ block_size_var: a varivel que ira corresponder ao block size da função.
'''

def block_size_control(keyboard, block_size_var):
    if (keyboard == 83) and (block_size_var < 255):
        block_size_var += 2
    elif (keyboard == 81) and (block_size_var > 3):
        block_size_var -= 2

    print("blockSize value: {}".format(block_size_var))
    return block_size_var


'''
    c_control tem como objetivo controlar a variavel c dentro das funções de cv2.adaptiveThreshold(),
    modificando o tamanho de filtro, com o entuido de ter um melhor controle sobre o processamento da imagem.

    Utilize as teclas de setas direcionais para cima e para baixo para variar o valor.

    Ela recebe como parâmetro:

    $ keyboard: a varivel do teclado na qual é lida constantemente.
    $ c_var: a varivel que ira corresponder ao c da função.
'''


def c_control(keyboard, c_var):
    if (keyboard == 82) and (c_var < 255):
        c_var += 1
    elif (keyboard == 84) and (c_var > 1):
        c_var -= 1

    print("C value: {}".format(c_var))
    return c_var

'''
    detect_char é uma função para quando for apertado a tecla 'enter' começará a fazer uma leitura na imagem
    em busca de contornos com uma área de pixels entre as variaveis max_area e min_area, desenhando os contornos
    delas na imagem.

    Ela recebe como parametro:

    $ keyboard: a varivel do teclado na qual é lida constantemente.
    $ thresh: uma imagem que tenha sido binarizada por limiarização (threshold).
    $ image: a imagem original que esta sendo utilizada.
    $ channel_num: o número ou nome da tela de amostragem.
'''

def detect_char(keyboard, thresh, image, channel_num):
    if keyboard == 13:

        possible_char = image.copy()
        chars_on_image = image.copy()
        contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        list_of_possible_char = []
        num_chars = 0
        max_area = thresh.size * .075
        min_area = thresh.size * .02
        
        for contour in contours:

            (x, y, w, h) = cv.boundingRect(contour)
            max_h_w_dif = w * 3.8

            if (cv.contourArea(contour) < max_area) and (cv.contourArea(contour) > min_area) and (h > w) and \
                    ((h/w) < max_h_w_dif):


                list_of_possible_char.append(contour)
                cv.rectangle(chars_on_image, (x, y), (x + w, y + h), (0, 255, 0), 1)
                num_chars += 1

        cv.imshow("Possible Chars on Image {}".format(channel_num), chars_on_image)
        print("{} - Number of possible char on image: {}".format(channel_num, num_chars))
        if num_chars == 7:
            list_of_possible_char, bounding_boxes = sorting_contours(list_of_possible_char)
            save_image_of_possible_char(possible_char, bounding_boxes, channel_num)

    return


'''
    Sorting Contours: como o próprio nome indica, ele organiza os contornos em uma array de forma que possa ser lidos
    da esquerda para direita.

    Ele recebe como parâmetro:

    $ list_of_possible_chars: uma lista com os contornos processados no detect_char.
'''

def sorting_contours(list_of_possible_chars):
    if list_of_possible_chars:
        bounding_boxes = [cv.boundingRect(c_) for c_ in list_of_possible_chars]
        (sorted_chars, bounding_boxes) = zip(*sorted(zip(list_of_possible_chars, bounding_boxes), key=lambda b: b[1][0],
                                                     reverse=False))

        return sorted_chars, bounding_boxes

    return

'''
    save_image_of_possible_char: a função lê a lista de possiveis caracteres e salva a imagem de cada um deles para visualizar
    os possiveis caracteres encontrados.

    Recebe como parâmetro:
    $ image: a imagem original da placa.
    $ bounding_boxes: a lista com os contornos dos possiveis caracteres.
    $ channel_num: referencia ao nome ou número da tela de amostragem.
'''

def save_image_of_possible_char(image, bounding_boxes, channel_num):
    num_chars = 0
    possible_char = image.copy()
    if bounding_boxes:
        for contour in bounding_boxes:
            num_chars += 1
            (x, y, w, h) = contour
            cv.imwrite("test_{}_possible_char_{}.png".format(channel_num, num_chars),
                       possible_char[y:(y + h), x:(x + w)])

    return


c = 1 
block_size = 3

while True:

    frame = cv.imread('5.png')

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    th1 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, block_size, c)
    th2 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, block_size, c)

    cv.imshow('th1', th1)
    cv.imshow('th2', th2)

    k = cv.waitKey(0) & 0xFF

    os.system('cls' if os.name == 'nt' else 'clear')


    block_size = block_size_control(k, block_size)
    c = c_control(k, c)

    detect_char(k, th1, frame, 1)
    detect_char(k, th2, frame, 2)
    (height, width) = gray.shape

    print("Image Size: {}\nImage Height: {}\nImage Width: {}".format(gray.size, height, width))
    print("\n\n Keyboard value: {}".format(k))

    if k == 27:
        break

cv.destroyAllWindows()
