import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
import json, requests

#Getting discord from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
JOKETOKEN = os.getenv("JOKE_TOKEN")

#Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#Opening client
client = commands.Bot(command_prefix='!', intents=intents)

#Jokes
jokes = [
    "Adamın biri gülmüş, bahçeye ekmiş.",
    "Temel kamyonla İstanbul'a gitmiş, kamyonu park etmiş ama İstanbul'u nereye koymuş bilmiyor.",
    "Elektrikçiyle konuşuyorum, çok gerilimli bir adam.",
    "Doktora gittim, bana 'hasta mısın?' dedi. Ben de 'hayır, abiyle geldim' dedim.",
    "Bilgisayar neden üşür? Çünkü çok pencere açar.",
    "Fareler neden bilgisayar kullanamaz? Çünkü fare tuzağı var.",
    "Deniz neden tuzludur? Çünkü karidesler ağlar.",
    "Çekirge neden zıplamış? Çünkü ipi çekmişler.",
    "Otobüs şoförü neden sinirlenmiş? Çünkü direksiyon elinden alınmış.",
    "Makarna neden dans edemez? Çünkü sosu yok.",
    "Karpuz neden doktora gitmiş? Çekirdeği ağrıyormuş.",
    "Bebek neden süt içmiş? Çünkü kahve yasak.",
    "Saat neden geç kalmış? Pili bitmiş.",
    "Tavuk neden ders çalışmaz? Çünkü kafası yumurtada.",
    "Köpek neden bilgisayar başına oturmuş? İnternette kemik aramak için.",
    "Balık neden şarkı söylemez? Çünkü sesi yok.",
    "Müzisyen neden bankaya gitmiş? Nota almak için.",
    "Üzüm neden ağlamış? Salkımı kopmuş.",
    "Kalem neden yorulmuş? Çok yazı yazmış.",
    "Defter neden tatildeymiş? Sayfaları bitmiş.",
    "Elma neden kırmızı olmuş? Utanmış.",
    "Araba neden uyumuş? Benzini bitmiş.",
    "Telefon neden konuşmamış? Konuşma paketi bitmiş.",
    "Ispanak neden spor yapmış? Daha güçlü olmak için.",
    "Kedi neden bilgisayara bakmış? Faresini arıyormuş.",
    "Kahve neden uyuyamamış? Çok kafeinliymiş.",
    "Kitap neden hastalanmış? Fazla sayfa çevrilmiş.",
    "Bal neden tatlıdır? Çünkü arılar şeker gibi.",
    "Lamba neden yanmamış? Elektriği kesilmiş.",
    "Yastık neden üzgünmüş? Üzerine hep kafa konuyormuş.",
    "Gözlük neden kırılmış? Çerçevesi dayanamamış.",
    "Dolap neden şarkı söylüyormuş? İçinde radyo varmış.",
    "Televizyon neden sinirlenmiş? Kanalı değiştirilmiş.",
    "Muz neden kaybolmuş? Kabuk değiştirmiş.",
    "Patates neden dans etmiş? Çıtır olmak istemiş.",
    "Buz neden okula gitmiş? Donmuş bilgilerini çözmek için.",
    "Güneş neden tatil yapmaz? Çünkü hep çalışır.",
    "Ağaç neden bilgisayar kullanmaz? Çünkü kökleri internette değil.",
    "Pencere neden güler? Cam gibi espri yapar.",
    "Kavanoz neden ağlamış? Kapağı sıkılmış.",
    "Pizza neden mutluymuş? Üzerinde bol malzeme varmış.",
    "Fare neden düğüne gitmiş? Peyniri görmek için.",
    "Çorap neden üzülmüş? Eşi kaybolmuş.",
    "Anahtar neden mutluymuş? Kapısını bulmuş.",
    "Kapı neden kollarını açmış? Ziyaretçi gelmiş.",
    "Halı neden yorulmuş? Üzerinde çok gezmişler.",
    "Çamaşır makinesi neden şarkı söylemiş? Suda çok ritim varmış.",
    "Mikser neden sinirlenmiş? Her şeyi karıştırmışlar.",
    "Balon neden patlamış? Ortam gerilmiş.",
    "Sabun neden kaybolmuş? Köpüklerin içinde saklanmış.",
    "Kalorifer neden kızmış? Çok ısıtılmış.",
    "Yağmur neden şarkı söyler? Damla damla notalarla.",
    "Rüzgar neden hızlı koşar? Esmek için.",
    "Göl neden saklanır? Çok derin düşünür.",
    "Dere neden hep güler? Şırıl şırıl mutluluk.",
    "Meyve suyu neden okula gitmiş? Bilgi sıkmak için.",
    "Dondurma neden ağlamış? Erimiş.",
    "Fırın neden sıcakmış? Çünkü hep çalışıyor.",
    "Poşet neden uçmuş? Hafif esinti varmış.",
    "Defter neden gizli saklar? Sayfaları doluymuş.",
    "Karpuz neden kilo vermek istemiş? Çekirdeksiz olmak için.",
    "Kirpi neden yastığa sarılmaz? Çok batarmış.",
    "Salatalık neden üzülmüş? Turşusu çıkmış.",
    "Ekmek neden gülmüş? Kafası kızarmış.",
    "Çay neden konuşmuş? Sohbete katılmış.",
    "Kahve fincanı neden korkmuş? Doldurulacakmış.",
    "Limon neden surat asar? Ekşi hayat.",
    "Yoğurt neden küsmüş? Süzme yapılmış.",
    "Köprü neden hava atmış? Üzerinden çok geçilmiş.",
    "Top neden yorulmuş? Hep tekme yemiş.",
    "Ayakkabı neden konuşmaz? Bağcıkları çözülmüş.",
    "Uçak neden mutluymuş? Hep havalıymış.",
    "Deniz neden espri yapmaz? Dalgınmış.",
    "Ada neden yalnızmış? Kendi başına kalmış.",
    "Tren neden sinirlenmiş? Raydan çıkmış.",
    "Otobüs neden saklanmış? Durakta beklemiş.",
    "Trafik lambası neden utanmış? Kırmızıya dönmüş.",
    "Yıldız neden göz kırpar? Geceyi süslemek için.",
    "Ay neden uyumuş? Gece olmuş.",
    "Bulut neden ağlamış? Yağmur olmak istemiş.",
    "Kar neden yere düşer? Uçmayı bilmez.",
    "Dağ neden sessizmiş? Yüksekten konuşmaz.",
    "Orman neden fısıldar? Yapraklar sır saklar.",
    "Kaktüs neden az su içer? Susuzluğa dayanıklı.",
    "Elma ağacı neden mutlu? Meyvesi bolmuş.",
    "Karpuz neden kırılmış? Düşmüş.",
    "Simit neden sevinmiş? Çayı gelmiş.",
    "Pasta neden mutlu? Doğum günü varmış.",
    "Çikolata neden erimiş? Çok utanmış.",
    "Bardak neden kırılmış? Düşmüş.",
    "Sandalye neden yorulmuş? Hep oturulmuş.",
    "Masa neden gururlu? Üzerinde çok iş yapılmış.",
    "Çekiç neden sert? İşini ciddiye almış.",
    "Makas neden kızmış? Ortamı kesmiş.",
    "Kalemtraş neden mutlu? Kalemle iyi anlaşmış.",
    "Cetvel neden sinirlenmiş? Hep ölçülmüş.",
    "Defter neden şarkı söylemiş? Sayfaları melodikmiş."
]

#events
@client.event
async def on_ready():
    print("Bot is ready for use!")
    print("*********************")    

#commands
@client.command()
async def hello(ctx):
    await ctx.send("Hello I am Muhittin!")

@client.command()
async def goodybye(ctx):
    await ctx.send("I am sorry to hear that, but whatever see ya")

@client.command()
async def whatsup(ctx):
    await ctx.send("I am good, whatsupp to you?")

@client.command()
async def abariii(ctx):
    await ctx.send("ABARİİİİİİİ")

@client.command()
async def joke(ctx):
    joke_t = random.choice(jokes)
    await ctx.send(joke_t)

@client.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command!")

@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("I am not in a voice channel!")

"""
@client.command()
async def joke(ctx):
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    await ctx.send(data["joke"])
@client.command()
async def joke(ctx):
    jokeurl = "https://joke3.p.rapidapi.com/v1/joke"
    headers = {
        "x-rapidapi-key" : "JOKETOKEN",
        "x-rapidapi-host": "joke3.p.rapidapi.com"
        }
    response = requests.get(jokeurl, headers=headers)
    await ctx.send(json.loads(response.text))
"""



client.run(TOKEN)

