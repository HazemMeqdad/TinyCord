<div align="center">
    <h1>TinyCord 🏮</h1>
    <p> Easy and flexible Discord wrapper built on aiohttp </p>
    <p>Thanks to <a href="https://github.com/Pincer-org/Pincer">Pincer</a> because we did take a lot of ideas and things from it <3  </p>
</div>

<br>

<div align="center">

# Example

<div align="left">

```py
import tinycord

client = tinycord.Client(
    "Token", intents=[tinycord.Intents.all()]
)

@client.event
async def on_message(message: tinycord.Message):
    print(message.content)

client.connect()
```

</div>
</div>

# Note
#### Right Now the lib is in huge development we want to add more things to it like interactions and good event handling


