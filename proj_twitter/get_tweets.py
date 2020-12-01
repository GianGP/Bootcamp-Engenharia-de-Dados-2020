# Importação das bibliotecas necessárias
import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

# Cadastrar chaves de acesso
consumer_key = "apcApwXgBVychsVinzWiCX6sh"
consumer_secret = "9rIgowLIlIzKo37eQ6OC6viwfhZOVl39z5ygGGRGxWm0HhENIP"


access_token = "1333043622036582400-lr6oqdXAqgtHFzPbh1ULupTH9MUCkI"
access_token_secret = "hBhQbob9gIU0ggF5zc1W317nAOghNGbK2Fu2DEfcT8N5x"

# Definir arquivo de saida para os tweets coletados
data_hoje = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
out = open(f"collected_tweets_{data_hoje}.txt", "w")

# Implementar classe para conexão com o Twitter
class MyListener(StreamListener):
    def on_data(self, data):
        itemString = json.dumps(data)
        out.write(itemString + '\n')
        return True
    
    def on_error(self, status):
        print(status)

# Implementar main
if __name__ == "__main__":
    l = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=["Trump"])