NEWS_UNIGRAMS_PATH  = "./data/20N_l.rojasb_j.arboleda_unigrams.txt"
NEWS_BIGRAM_PATH    = "../data/20N_l.rojasb_j.arboleda_bigrams.txt"
NEWS_TRIGRAM_PATH   = "../data/20N_l.rojasb_j.arboleda_trigrams.txt"

def load_ngram(path: str) -> dict:
    ngram_dict = {}
    f = open(path, "r")

    ngram = f.readline()
    while(len(ngram) != 0):
        ngram = ngram.split(",")
        ngram_dict[ngram[0]] = {
            "count": ngram[1],
            "prob": ngram[2]
        }
        ngram = f.readline()

    return ngram_dict

print(load_ngram(NEWS_UNIGRAMS_PATH))