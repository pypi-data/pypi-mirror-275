import numpy as np
from PIL import Image, ImageDraw

class VfxGenerate:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate_particles(self, num_particles, particle_size):
        # 空の画像を作成
        self.image = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 255))
        self.draw = ImageDraw.Draw(self.image)

        for _ in range(num_particles):
            self._draw_particle(particle_size)

        return self.image

    def _draw_particle(self, particle_size):
        # パーティクルの位置をランダムに決定
        x = np.random.randint(0, self.width)
        y = np.random.randint(0, self.height)
        
        # パーティクルの色と輝きをランダムに決定
        brightness = np.random.randint(150, 256)
        color = (brightness, brightness, brightness, 255)
        
        # パーティクルを描画
        self.draw.ellipse((x - particle_size, y - particle_size, x + particle_size, y + particle_size), fill=color)

    def show_image(self):
        self.image.show()

    def save_image(self, file_path):
        self.image.save(file_path)