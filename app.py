#importar a biblioteca Pillow
from PIL import Image

#define o tamanho desejado do pixel
pixel_size = 25

#abre a imagem a ser tratada
image = Image.open('imagem.jpg')

#realiza o tratamento
image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
     )
image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
      )

#imprime a imagem
image.show()