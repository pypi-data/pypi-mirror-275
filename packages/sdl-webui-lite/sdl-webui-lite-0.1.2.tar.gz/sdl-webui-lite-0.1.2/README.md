# Self-driving lab Web UI - lite
We don't define Self-driving labs (SDLs). We enable UI for them. 
This is the lite version of Hein Lab [SDL Web UI](https://gitlab.com/heingroup/web_controller)

## Description


Granting SDL flexibility makes it impossible to design a UI, yet it's a necessity for allowing more people to interact with it. 
This web UI aims to ease up the control of any Python-based SDLs by displaying functions and parameters dynamically. 
This lite version allow user to put actions in queue for simply workflow design. 

## Installation
```
pip install sdl-webui-lite
```

## Usage
in your self-driving platform class, use `start_gui(your_sdl)`. Example in [sample_code.py](sample_code.py)
```python
sdl = YourSDL()
from sdl_webui_lite.app import start_gui
start_gui(sdl)
```
## Additional settings
You can change the log file name/path, and the current SDL name, as this will reflect on the webapp page and title.
You can also add other loggers
```python
sdl = YourSDL()
from sdl_webui_lite.app import app, start_gui
app.config["DEBUG"] = False     # show fucntions startwith "_" if True
app.config["LOG_FILENAME"] = "/path/to/log.log"
app.config["TITLE"] = "Your SDL name"
start_gui(sdl, logger="your logger name")
# or
# start_gui(sdl, logger=["your logger name", "another logger"]) 
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors
Ivory Zhang | Hein Lab ([ivoryzhang@chem.ubc.ca]())

## UI snapshot
![page_screenshot.png](sdl_webui_lite/static/page_screenshot.png)
