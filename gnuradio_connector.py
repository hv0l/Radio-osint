from gnuradio import analog, blocks, gr, osmosdr
import time

class RadioConnector(gr.top_block):
    def __init__(self, frequency, duration, filepath):
        gr.top_block.__init__(self, "Radio Connector")
        
        # Configurazione dei parametri della sorgente
        self.samp_rate = 2e6  
        self.frequency = frequency  
        self.duration = duration  
        self.filepath = filepath  
        
        self.src = osmosdr.source()
        self.src.set_sample_rate(self.samp_rate)
        self.src.set_center_freq(self.frequency, 0)
        
        self.sink = blocks.file_sink(gr.sizeof_gr_complex, self.filepath)
        self.sink.set_unbuffered(True)
        
        self.connect(self.src, self.sink)

def connect_and_record(frequency, duration):
    filepath = "output.raw"  
    connector = RadioConnector(frequency, duration, filepath)
    connector.start() 
    time.sleep(duration)
    connector.stop()
    connector.wait()
    return filepath

