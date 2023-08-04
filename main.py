import datetime
from demo_opts import get_device
from luma.core.render import canvas
from PIL import ImageFont
from pathlib import Path


# Fungsi untuk menggambar tampilan jam digital
def make_font(name, size):
    font_path = str(Path(__file__).resolve().parent.joinpath('fonts', name))
    return ImageFont.truetype(font_path, size)

def draw_clock(draw, width, height):
    now = datetime.datetime.now()
    today_time = now.strftime("%H:%M:%S")
    today_date = now.strftime("%a %d %b %y")

    draw.rectangle((0, 0, width-1, height-1), outline="white", fill="black")

    # Font untuk angka jam dan menit
    font_large = make_font("DS-DIGIB.TTF", 40)
    # Font untuk detik
    font_small = make_font("DS-DIGIB.TTF", 20)

    # angka jam
    draw.text((10, 27), today_time[:2], font=font_large, fill="white")
    draw.text((48, 27), ":", font=font_large, fill="white")
    # angka menit
    draw.text((60, 27), today_time[3:5], font=font_large, fill="white")
    # angka detik
    draw.text((105, 42), today_time[6:], font=font_small, fill="white")
    # Tanggal
    draw.text((10, 2), text=today_date, font=font_small, fill="white")

# Fungsi untuk menganimasikan tampilan jam
def show_clock(device):
    # Ambil lebar dan tinggi layar
    width, height = device.width, device.height

    # Loop animasi
    while True:
        with canvas(device) as draw:
            # tampilan jam digital
            draw_clock(draw, device.width, device.height)
            # opsional
            # time.sleep(0.1)

# Fungsi utama
if __name__ == "__main__":
    try:
        # Inisialisasi device
        device = get_device()
        show_clock(device)
        
    except KeyboardInterrupt:
        pass
