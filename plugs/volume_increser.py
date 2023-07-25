
from plugs.filename_gen import filename_gen
factor = 6.0
from pydub import AudioSegment

def inc_vol(file):
    audio = AudioSegment.from_file(file)
    audio += factor
    name = filename_gen('.wav')
    nfile = f"temp/{name}"
    audio.export(nfile, format="wav")
    return nfile,name
