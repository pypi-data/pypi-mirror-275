from silero_tts.silero_tts import SileroTTS

# Инициализация объекта TTS
tts = SileroTTS(model_id='v4_ru', language='ru', speaker='aidar', sample_rate=48000, device='cpu')

# Синтез речи из текста
text = "Привет, мир!"
tts.tts(text, 'output.wav')

# Синтез речи из текстового файла
# tts.from_file('input.txt', 'output.wav')

# Получение доступных моделей
models = SileroTTS.get_available_models()
print(models)

# Получение доступных голосов для модели
speakers = tts.get_available_speakers()
print(speakers)