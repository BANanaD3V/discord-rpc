# Discord RPC
This is my implementation of discord rpc to show what i'm currently doing. Heavily inspired by [Naomi's variant](https://github.com/nhcarrigan/discord-rpc).
## Installation

Install rpc by clonning this repo and installing dependencies.

```bash
git clone https://github.com/BANanaD3V/discord-rpc
cd discord-rpc
pip install -r requirements.txt
cd src
python main.py
```
PS: dont forget to rename `.env.example` to `.env` and change client id. You also need desktop client on PC to make this work.
    
## Screenshots

![Profile screenshot](img/profile.png)

![Console screenshot](img/console.png)

## Customization options

1. You can customize options in the `config.py` file. This file is using json. The keys is the name of option in selection menu. The value has 2 options: action and icon. Action is shown up in your discord RPC, icon is configured using discord's art asset manager. Feel free to ask questions in my discord - __BANana#0533__.

## License

This project licensed by [MIT](https://choosealicense.com/licenses/mit/) license.

```
The MIT License (MIT)

Copyright (c) 2022 BANana

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## Countributing

Feel free to open PRs and help me with code, but please use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) style.