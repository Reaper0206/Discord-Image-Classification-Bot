import discord
from discord.ext import commands
import tensorflow as tf
import numpy as np
import json
import zipfile
import os
from PIL import Image
def extract_zip(zip_path, extract_to="./"):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
t.zip = "t.zip.zip"
EXTRACT_TO = "./my_model/"  

# ZIP dosyasını aç
if not os.path.exists(EXTRACT_TO):
    extract_zip(t.zip, EXTRACT_TO)

# Model yolu
t.zip = EXTRACT_TO

# Bot ayarları
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Model klasörü ve bilgiler
MODEL_PATH = "./my_model/"
MODEL_JSON = MODEL_PATH + "model.json"
MODEL_WEIGHTS = MODEL_PATH + "model.weights.bin"
LABELS_JSON = MODEL_PATH + "metadata.json"

def extract_zip(t.zip, extract_to="./"):
    """ ZIP dosyasını çıkarır """
    with zipfile.ZipFile(t.zip, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# Yapılar ve bilgileri
LANDMARKS = {
    "Taş Köprü": {"konum": "Adana", "tarih": "Roma Dönemi", "giriş": "Ücretsiz", "saatler": "24 Saat Açık"},
    "Sümela Manastırı": {"konum": "Trabzon", "tarih": "4. Yüzyıl", "giriş": "100 TL", "saatler": "09:00 - 19:00"},
    "Peri Bacaları": {"konum": "Kapadokya", "tarih": "Doğal Oluşum", "giriş": "Ücretsiz", "saatler": "24 Saat Açık"},
    "Pamukkale Travertenleri": {"konum": "Denizli", "tarih": "Doğal Oluşum", "giriş": "200 TL", "saatler": "06:30 - 21:00"},
    "Noel Baba Kilisesi": {"konum": "Antalya", "tarih": "5. Yüzyıl", "giriş": "125 TL", "saatler": "08:00 - 18:00"},
    "Nemrut Dağı": {"konum": "Adıyaman", "tarih": "Antik Kommagene Krallığı", "giriş": "50 TL", "saatler": "05:00 - 20:00"},
    "Kız Kulesi": {"konum": "İstanbul", "tarih": "Antik Çağ", "giriş": "150 TL", "saatler": "09:00 - 19:00"},
    "Hattuşaş Antik Kenti": {"konum": "Çorum", "tarih": "Hitit İmparatorluğu", "giriş": "50 TL", "saatler": "08:00 - 17:00"},
    "Göbeklitepe": {"konum": "Şanlıurfa", "tarih": "M.Ö. 9600", "giriş": "75 TL", "saatler": "08:00 - 18:30"},
    "Galata Kulesi": {"konum": "İstanbul", "tarih": "528", "giriş": "175 TL", "saatler": "08:30 - 23:00"},
    "Efes Antik Kenti": {"konum": "İzmir", "tarih": "M.Ö. 10. Yüzyıl", "giriş": "200 TL", "saatler": "08:00 - 19:30"},
    "Cennet Cehennem Mağarası": {"konum": "Mersin", "tarih": "Doğal Mağara", "giriş": "50 TL", "saatler": "09:00 - 17:00"},
    "Ayasofya Camii": {"konum": "İstanbul", "tarih": "537", "giriş": "Ücretsiz", "saatler": "24 Saat Açık"},
    "Aspendos Antik Tiyatrosu": {"konum": "Antalya", "tarih": "M.S. 2. Yüzyıl", "giriş": "100 TL", "saatler": "08:00 - 19:00"},
    "Ani Harabeleri": {"konum": "Kars", "tarih": "M.S. 10. Yüzyıl", "giriş": "50 TL", "saatler": "09:00 - 18:00"},
    "Ağrı Dağı": {"konum": "Ağrı", "tarih": "Doğal Dağ", "giriş": "Ücretsiz", "saatler": "24 Saat Açık"}
}

# Modeli yükle
model = None
labels = []

def load_model():
    global model, labels
    model = tf.keras.models.load_model(t.zip)
    with open(MODEL_JSON, "r") as f:
        labels = json.load(f)["labels"]

# Görseli tanıma
async def predict_image(t.zip):
    img = Image.open(t.zip).resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)[0]
    best_index = np.argmax(predictions)
    return labels[best_index], predictions[best_index]

@bot.event
async def on_ready():
    print(f'Bot {bot.user} olarak giriş yaptı!')
    load_model()

@bot.command()
async def tanı(ctx):
    if not ctx.message.attachments:
        await ctx.send("Lütfen bir resim ekleyin!")
        return
    
    t.zip = "temp.jpg"
    await ctx.message.attachments[0].save(t.zip)
    landmark, confidence = await predict_image(t.zip)
    
    if landmark in LANDMARKS:
        info = LANDMARKS[landmark]
        response = (f"**{landmark}**\n"
                    f"📍 Konum: {info['konum']}\n"
                    f"📜 Tarih: {info['tarih']}\n"
                    f"💰 Giriş Ücreti: {info['giriş']}\n"
                    f"🕰 Açık Saatler: {info['saatler']}\n"
                    f"✅ Güven Skoru: {confidence:.2f}")
    else:
        response = f"Bu yapı tanınamadı! ({confidence:.2f})"
    
    await ctx.send(response)

# Botu başlat
bot.run("YOUR TOKEN")
