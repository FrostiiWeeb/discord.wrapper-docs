# HTTP Requests

```python
from discord import wrapper
import asyncio

bot = wrapper.Bot(token="Your TOKEN", intents=wrapper.Intents().all())

async def fetch_channel(channel_id):
	pirnt(await bot.http.fetch_channel(channel_id))
	
loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_channel(put_your_channel_id))

async def fetch_message(channel_id, message_id):
	print(await bot.http.fetch_message(channel_id, message_id))
	
loop.run_until_complete(fetch_message(put_your_channel_id))

async def send_message(channel_id=None, content=None, *, embed=None):
	print(await bot.http.fetch_message(channel_id, content, embed))
	
loop.run_until_complete(send_message(put_your_args_here))
```
==========

`async def fetch_channel(channel_id)`

Type:
	`function`
	
==========

`async def fetch_message(channel_id, message_id)`

Type:
	`function`
	
==========

`async def send_message(channel_id, content, *, embed)`

Type:
	`function`	
	