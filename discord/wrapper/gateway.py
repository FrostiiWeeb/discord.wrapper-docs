import websockets
import json
import asyncio
import aiohttp
import json
from string import Template


class InvokeError(Exception):
	def __init__(self, message):
		super.__init__(message)

class Gateway:
	
			
	def identify_json(self, token : str, intents : int):
		"""
		The identify payload to authorize the bot.
		
		Attributes
		----------
		
		token : str
			The token of the bot.
		intents : int
			The intents for the bot.
		"""
		
		t = Template('{"op": 2,"d": {"token": "$token","intents": $intents, "properties": {"$os": "linux","$browser": "discord.api","$device": "discord.api"}},"s": null,"t": null}')
		return t.substitute(token=str(token), intents=intents, os="$os", browser="$browser", device="$device")
	
	async def _close(self):
		"""
		The |async| function to close the connection.
		"""
				
		await self.ws.close()
		
	def close(self):
		"""
		The actual function to close the connection.
		"""
		
		asyncio.get_event_loop().run_until_complete(_close())
		
	async def _connect(self, _token : str, _intents : int):
		"""
		Function to connect the bot to discord.
		
		Attributes
		----------
		
		_token : str
			The token of the bot.
		_intents : int
			The intents for the bot.
		"""		
		try:
			self.ws = await aiohttp.ClientSession().ws_connect("wss://gateway.discord.gg/?v=6&encoding=json")			
			heartbeat = '{"op": 1,"d": 251}'
			p = self.identify_json(_token, _intents)
			h = json.loads(heartbeat)
			h_json = json.dumps(h)
			await self.ws.send_str(h_json)
			await self.ws.send_str(p)
		except Exception as e:
			print(e)
		
	def connect(self, token : str, intents : int):
		"""
		The actual function to connect the bot to discord.
		
		Attributes
		----------
		
		token : str
			The token of the bot.
		intents : int
			The intents for the bot.
		"""		
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		asyncio.ensure_future(self._connect(token, intents), loop=loop)
		loop.run_forever()																					