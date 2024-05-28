<div align="center">
    <h1>Cursed.py ⚒️</h1>
    <img width="64px" alt="icon" src="./curseforge.png">
</div>

[![PyPI version](https://badge.fury.io/py/cursedpy.svg)](https://badge.fury.io/py/cursedpy)

About:
---
Full asynchronous **Curseforge API** wrapper<br> 
👉 https://docs.curseforge.com<br>
```
All Json Schemas (Python Types) are exactly the same as in docs
Except missing "Return types" which are essentially just this:
```
```python
 {"data": Any}
 {"data": Any, "pagination": Pagination}
```

Usage examples:
---
- [Search mods](https://github.com/DrugsNotIncluded/cursed.py/blob/main/examples/search_mods/README.MD)
- [~~Get curseforge supported games list~~](https://github.com/DrugsNotIncluded/cursed.py/blob/main/examples/games_list/README.md) **TODO**
- [~~Get mods download links~~](https://github.com/DrugsNotIncluded/cursed.py/blob/main/examples/mods_download_links/README.md) **TODO**

Basic usage:
---
```python
# Get all available games for provided API key:
from cursedpy import CFClient
API_KEY = "API_KEY"

async def main():
    try:
        client = CFClient(API_KEY)
        games = await client.games()
        print(games)
    finally:
        client.close()
```

Implemented API:
---
- [x] Games
- [x] Categories
- [x] Mods
- [x] Files
- [x] Fingerprints
- [x] Minecraft

QOL:
---
- [ ] Add helper methods to some types (`Mod.get_download_link()` , for example)
- [ ] Add cache
- [ ] Error handling
- [ ] Document all types parameters
- [ ] Make proper docs page???

Similar projects:
---
https://github.com/Advik-B/CurseForge-API - lacks search method support, example on the main page didn't work for me at all, Lol </br>
https://github.com/Stinky-c/curse-api - cool wrapper, but pydantic is a little bit too much for my taste, thx for multiple http libraries support idea ❤️, although i don't think it will be useful at all **for me**, but this is a library after all..
