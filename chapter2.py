from PIL import Image, ImageFilter
from pydub import AudioSegment


# ======================
# IMAGE PROCESSING
# ======================

image = Image.open("kucing.jpeg")
image.show()

# Crop tengah (tidak terlalu kecil)
width, height = image.size
crop_area = (
    width * 0.1,
    height * 0.1,
    width * 0.9,
    height * 0.9,
)

cropped_image = image.crop(crop_area)
cropped_image.save("cropped_kucing.jpeg")
cropped_image.show()

# Resize proporsional (tidak distorsi)
resized_image = cropped_image.resize(
    (int(cropped_image.width * 0.5), int(cropped_image.height * 0.5))
)
resized_image.save("resized_kucing.jpeg")
resized_image.show()

# Blur
filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save("blurred_kucing.jpeg")
filtered_image.show()


# ======================
# AUDIO PROCESSING
# ======================

audio = AudioSegment.from_file("audio1.mp4")

# Clip 10 detik pertama
clipped_audio = audio[:10000]
clipped_audio.export("clipped_result.mp4", format="mp4")

# Gabungkan
combined_audio = audio + clipped_audio
combined_audio.export("combined_result.mp4", format="mp4")

# Convert ke WAV
audio.export("result.wav", format="wav")

# Tambah volume
louder_audio = audio + 10
louder_audio.export("louder_result.mp4", format="mp4")

print("SEMUA PROSES SELESAI")
