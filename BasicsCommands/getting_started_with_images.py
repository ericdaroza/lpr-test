import cv2
img = cv2.imread('lena.jpg', -1)  # O primeiro parâmetro do método '.imread()' é o nome do arquivo
# O segundo parâmetro pode variar entre 1, 0 e -1 no qual representa as seguintes caracteristicas:
'''
 -> Valor do inteiro igual a 1: carrega uma imagem colorida.
 -> Valor do inteiro igual a 0: carrega uma imagem em escala de cinza.
 -> Valor do inteiro igual a -1: "Loads a image as such including alpha channels".
'''

print(img)  # Imprime a matriz da imagem no terminal.

cv2.imshow('image', img)  # Mostra a imagem na tela.
k = cv2.waitKey(0) & 0xFF  # A variavel k determina o tempo de exibição da imagem na tela, onde zero (0) permanece
# por tempo indeterminado, ou por algum valor correspondente a mili segundos.

if k == 27:  # Se for pressionado a tecla 'Esc' no teclado a tela de exibição da imagem fecha, onde 27 é o numero de
    # referencia da tecla.
    cv2.destroyAllWindows()  # O método '.destroyAllWindows()' é utilizado para não correr risco de permanecer
    # o programa rodando em segundo plano.
elif k == ord('s'):  # Se for pressionado a tecla 's' do teclado irá executar esta condicional.
    cv2.imwrite('lena_copy.png', img)  # Cria uma cópia da imagem com as caracteristicas
    # alteradas/salvas na variável img.
    cv2.destroyAllWindows()
