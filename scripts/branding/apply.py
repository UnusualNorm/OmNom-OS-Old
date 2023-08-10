import shutil


def main():
    # Read the distro and custom os-release files
    with open('/usr/lib/os-release') as f:
        os_release = f.readlines()

    with open('/tmp/scripts/branding/os-release') as f:
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
    with open('/usr/lib/os-release', 'w') as f:
        for key, value in os_release_dict.items():
            f.write(f'{key}="{value}"\n')

    # Copy the custom branding files
    shutil.copyfile('/tmp/scripts/branding/fedora-logo-sprite.svg', '/usr/share/pixmaps/fedora-logo-sprite.svg')

    shutil.copyfile('/tmp/scripts/branding/fedora-logo-small.png', '/usr/share/pixmaps/fedora-logo-small.png')
    shutil.copyfile('/tmp/scripts/branding/system-logo-white.png', '/usr/share/pixmaps/system-logo-white.png')

    shutil.copyfile('/tmp/scripts/branding/bootlogo_128.png', '/usr/share/pixmaps/bootloader/bootlogo_128.png')
    shutil.copyfile('/tmp/scripts/branding/bootlogo_256.png', '/usr/share/pixmaps/bootloader/bootlogo_256.png')

    shutil.copyfile('/tmp/scripts/branding/fedora_logo_med.png', '/usr/share/pixmaps/fedora_logo_med.png')
    shutil.copyfile('/tmp/scripts/branding/fedora-logo.png', '/usr/share/pixmaps/fedora-logo.png')
    shutil.copyfile('/tmp/scripts/branding/fedora_whitelogo_med.png', '/usr/share/pixmaps/fedora_whitelogo_med.png')

    shutil.copyfile('/tmp/scripts/branding/poweredby.png', '/usr/share/pixmaps/poweredby.png')

    shutil.copyfile('/tmp/scripts/branding/fedora.icns', '/usr/share/pixmaps/bootloader/fedora.icns')

    # shutil.copyfile('/tmp/scripts/branding/splash.xpm.gz', '/usr/share/pixmaps/bootloader/splash.xpm.gz')

if __name__ == '__main__':
    main()