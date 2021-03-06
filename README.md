<p align="center">
    <img src="https://raw.githubusercontent.com/veraivan/Movies-Scraper/main/.extra/logo.png" width="300" height="300">
</p>
<br>
<p align="center">
    <img src="https://img.shields.io/badge/Version-1.0-green">
    <img src="https://img.shields.io/badge/License-MIT-green"> 
    <br>
    It extracts all the download links from the available servers, skipping the link protectors and advertising from the websites that offer free movie downloads. Getting the real links.
</p>
<hr>

## :grinning: Features!

- Scraping the links using multi-threading.
- Execution of javascript code from python.
- Tag extraction using the lxml library.
- Use of the gibberish-aes and atob javascript library for the decoding of the links.

## :pushpin: Supported sites
 
| Site | URL |  
| :--: | :--:|
| **Hackstore** | <https://hackstore.net> | 
| **Tu Mega Descarga** | <https://www.peliculas1mega.com> |
| **Mega 1080p** | <https://mega1080p.org> |

## :point_right: Installation guide 

Before starting the execution of the script in python, you need to install the dependencies to run the javascript file with node. 
> First you need to install nodejs.

```sh
$ cd Movies-Scraper/.extra/decodeJS

$ npm install
```

### Usage

```sh
$ cd Movies-Scraper

$ pip3 install -r requirements.txt

$ python3 main.py url-content-name-movies 
```
### Example  

For this example we look up the name of a movie on the hackstore site and get the url and run it: 

```sh

$  python3 main.py https://hackstore.net/descargar-tenet-2020/
```
