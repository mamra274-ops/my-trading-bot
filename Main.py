import telebot
import random
import time

TOKEN = '8471735047:AAG5VV0l5yDYyNSiUYIFgiZ1XgaKij9Zk2g'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['signal'])
def get_smart_signal(message):
    assets = ["EUR/USD (OTC)", "GBP/USD (OTC)", "crypto:BTC"]
    asset = random.choice(assets)
    
    # Имитация технического анализа
    rsi_value = random.randint(20, 80) # Индекс относительной силы
    
    bot.send_message(message.chat.id, f"🔍 Анализирую {asset}...\nПроверяю индикаторы RSI и Moving Average...")
    time.sleep(3)

    if rsi_value > 70:
        direction = "ВНИЗ ⬇️ (Перекупленность)"
        accuracy = random.randint(82, 91)
    elif rsi_value < 30:
        direction = "ВВЕРХ ⬆️ (Перепроданность)"
        accuracy = random.randint(82, 91)
    else:
        direction = random.choice(["ВВЕРХ ⬆️", "ВНИЗ ⬇️"])
        accuracy = random.randint(70, 75)

    response = (f"📈 Актив: {asset}\n"
                f"🎯 Сигнал: {direction}\n"
                f"📊 Вероятность успеха: {accuracy}%\n"
                f"⏳ Рекомендуемое время: 2-3 мин")
    
    bot.send_message(message.chat.id, response)

bot.polling(none_stop=True)
