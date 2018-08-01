# Coulr

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4c173929259648e19e883f465fb6c64b)](https://www.codacy.com/app/hugo-posnic/Coulr?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Huluti/Coulr&amp;utm_campaign=Badge_Grade)

## Enjoy colors and feel happy

Coulr is a color box to help developers and designers. Currently, it allows to:
  - convert RGB color to its Hexadecimal value and vice versa
  - copy selected color

### Screenshots

![alt tag](coulr/assets/coulr_screenshot.png)

### Version

Coulr is currently in version 1.6.3

## Installation instructions

### Archlinux-based distributions (AUR)

    yaourt -S coulr

### Build from source

Build and install by running:

    sudo python3 setup.py build
    sudo python3 setup.py install

### Developer install

Installing Coulr with develop mode creates binaries that link back to source code. Therefore changes will be reflected immediately with no need to repeatedly install.

    sudo python3 setup.py develop

After that, change the value of the `develop` var in the coulr/main.py file to `True`.
Finaly, launch Coulr:

    coulr

### Tech

Coulr uses open-source projects to work properly:

* [Python 3](https://www.python.org/)

### License

This project is under MIT licence... so do what you want with it :)

### Help me

That would make me very happy you make me feedback on using the software.
Thanks for your interest and see you soon!
