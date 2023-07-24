import wave, audioop,os
from plugs.filename_gen import filename_gen
factor = 6.0

def inc_vol(file):
    with wave.open(file, 'rb') as wav:
        p = wav.getparams()
        name = filename_gen('.wav')
        nfile = f"temp/{name}"
        with wave.open(nfile, 'wb') as audio:
            audio.setparams(p)
            frames = wav.readframes(p.nframes)
            audio.writeframesraw( audioop.mul(frames, p.sampwidth, factor))
        
        return nfile,name