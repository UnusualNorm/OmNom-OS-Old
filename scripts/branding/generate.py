import os
import gzip
import cairosvg
import subprocess
from PIL import Image
from xpm import pil_save

def convert_png_to_splash(png_file):
    # Load the input PNG image
    image = Image.open(png_file).convert('RGBA')

    # Create a new image with 15 colors
    image = image.quantize(colors=15, method=Image.Quantize.FASTOCTREE)

    # Resize the image to 640x480
    image = image.resize((640, 480), Image.Resampling.BILINEAR)

    # Save the image as a XPM file
    with gzip.open("grub-splash.xpm.gz", 'w') as f:
        f.write(pil_save(image, variable_name=b'grub_splash_xpm'))

    # Rename file to splash.xpm.gz
    os.rename('grub-splash.xpm.gz', 'splash.xpm.gz')


def main():
    # Read the distro and custom os-release files
    # with open('/usr/etc/os-release') as f:
    with open('/etc/os-release') as f:
        os_release = f.readlines()

    with open('os-release') as f:
        custom_os_release = f.readlines()

    # Stitch both release files together
    os_release_dict = {}
    for line in os_release:
        if line.startswith('#'):
            continue
        if '=' not in line:
            continue
        key, value = line.split('=', 1)
        os_release_dict[key] = value.strip().strip('"')

    for line in custom_os_release:
        if line.startswith('#'):
            continue
        if '=' not in line:
            continue
        key, value = line.split('=', 1)
        os_release_dict[key] = value.strip().strip('"')

    # Write back the new os-release file
    # with open('/usr/etc/os-release', 'w') as f:
    for key, value in os_release_dict.items():
        # f.write(f'{key}="{value}"\n')
        print(f'{key}="{value}"')

    # Convert the svgs to the files we need
    cairosvg.svg2png(url='fedora-logo-sprite.svg', write_to='fedora-logo-small.png', output_width=128, output_height=128)
    cairosvg.svg2png(url='fedora-logo-sprite.svg', write_to='system-logo-white.png', output_width=252, output_height=252)
    cairosvg.svg2png(url='fedora-logo-sprite.svg', write_to='bootlogo_128.png', output_width=128, output_height=128)
    cairosvg.svg2png(url='fedora-logo-sprite.svg', write_to='bootlogo_256.png', output_width=256, output_height=256)

    cairosvg.svg2png(url='fedora_logo.svg', write_to='fedora_logo_med.png', output_height=80)
    cairosvg.svg2png(url='fedora-logo.svg', write_to='fedora-logo.png', output_height=164)
    cairosvg.svg2png(url='fedora_whitelogo.svg', write_to='fedora_whitelogo_med.png', output_height=80)

    cairosvg.svg2png(url='poweredby.svg', write_to='poweredby.png', output_width=88, output_height=31)

    subprocess.run(['png2icns', 'fedora.icns', 'fedora-logo-small.png'])

    convert_png_to_splash('fedora_whitelogo_med.png')


if __name__ == '__main__':
    main()