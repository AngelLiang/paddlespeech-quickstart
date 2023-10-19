import os
from web.utils import get_available_filepath, get_tmp_dir
from web.utils import file2base64
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class TTSService:

    def get_tmp_dir(self):
        curr_dir = os.getcwd()
        TMP_DIR = os.path.join(curr_dir, 'tmp')
        os.makedirs(TMP_DIR, exist_ok=True)
        return TMP_DIR

    def tts(self, text, role='default', filename="output.wav"):
        from paddlespeech.cli.tts.infer import TTSExecutor
        tts = TTSExecutor()

        params = {}
        if role =='male':
            params['am'] ='fastspeech2_male' 
            params['voc'] ='pwgan_male' 
        else:
            pass

        tmp_dir = get_tmp_dir()
        filepath = os.path.join(tmp_dir, filename)
        output = get_available_filepath(filepath) 
        tts(text=text, output=output, **params)
        return file2base64(filepath)

