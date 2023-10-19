from paddlespeech.cli.tts.infer import TTSExecutor

tts = TTSExecutor()
tts(am="fastspeech2_male", voc="pwgan_male", text="今天天气十分不错。", output="output.wav")
