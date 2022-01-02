<div align="center">
    <h1>TinyCord 🏮</h1>
    <p> Easy and flexible Discord wrapper built on aiohttp </p>
    <p>Thanks to <a href="https://github.com/Pincer-org/Pincer">Pincer</a> because we did take a lot of ideas and things from it <3  </p>
    <br>
    <img src="./banner.png" />
    <br>
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

@client.lisnten(tinycord.Events.messageUpdate)
async def update_message(before: tinycord.Message, after: tinycord.Message):
    print(f'{before.content} -> {after.content}')
    

client.connect()
```

# Auto Shard Example

```py
import tinycord

client = tinycord.Client(
    "Token", intents=[tinycord.Intents.all()]
)

@client.event
async def on_message(message: tinycord.Message):
    print(message.content)

@client.lisnten(tinycord.Events.messageUpdate)
async def update_message(before: tinycord.Message, after: tinycord.Message):
    print(f'{before.content} -> {after.content}')
    

client.connect_autosharded()
```

# Docs
first let's finish the lib LOL.

# Discord

[![Tinycord Server](https://discord.com/api/guilds/923934645618376704/widget.png?style=banner2)](https://discord.gg/QP3CJythPh)


</div>
</div>

# Note
#### Right Now the lib is in huge development we want to add more things to it like interactions and good event handling

<br>

# Maintainers
xArty#9065

