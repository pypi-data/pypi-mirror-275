# line-notify-sdk

LINE Notify SDK for Pyrhon

## pip

```bash
$ pip install line-notify-sdk
```

## Usage

```python
from notify import Notify

n = Notify(token="YOUR_NOTIFY_TOKEN")
r = n.send_text("hello")

print(r.json())
# {'status': 200, 'message': 'ok'}
```

![notify](https://github.com/nanato12/line-notify-sdk/assets/49806926/4987186e-8427-452e-95b2-397695523476)

## Methods

| method | description |
| :- | :- |
| send_image_with_url(text, url) | Send image by specifying the image URL |
| send_image_with_local_path(text, path) | Send images by specifying the local image path |
| send_image(text, image) | Send images using BufferedReader or BytesIO |
| send_text(text) | Send text |
| send(files) | Customization request to notify (use this for anything other than images and text) |
| revoke() | Disable access token and remove notification settings |
| get_status() | Check linkage status |
| get_rate_limit() | Get the number of times the API can be called in an hour |

## Documentation

<https://notify-bot.line.me/doc/>

## License

```plain
MIT License

Copyright (c) 2024 nanato12

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
