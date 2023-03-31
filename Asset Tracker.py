import time
import yfinance as yf

print("Hazır Varlıkları Görüntülemek için 1' e Basınız: ")
print("Aramak İstediğiniz Spesifik Bir Varlık Varsa 2'e Basınız:")
inp = input()

if inp == "1":
    print("Veriler Çekiliyor Lütfen Bekleyiniz...")
    tsla = "TSLA"
    aapl = "AAPL"
    sbux = "SBUX"
    nflx = "NFLX"
    mcsft = "MSFT"
    meta = "META"
    asels = "ASELS.IS"
    thy = "THYAO.IS"
    koc = "KCHOL.IS"
    akbank = "AKBNK.IS"
    btc = "BTC-USD"
    eth = "ETH-USD"
    avax = "AVAX-USD"
    petrol = "CL=F"
    dollar = "TRY=X"
    euro = "EURTRY=X"
    golden = "GC=F"
    silver = "SI=F"

    tsla_data = yf.Ticker(tsla).info
    aapl_data = yf.Ticker(aapl).info
    nflx_data = yf.Ticker(nflx).info
    btc_data = yf.Ticker(btc).info
    sbux_data = yf.Ticker(sbux).info
    meta_data = yf.Ticker(meta).info
    mcsft_data = yf.Ticker(mcsft).info
    asels_data = yf.Ticker(asels).info
    thy_data = yf.Ticker(thy).info
    koc_data = yf.Ticker(koc).info
    akbank_data = yf.Ticker(akbank).info
    eth_data = yf.Ticker(eth).info
    avax_data = yf.Ticker(avax).info
    petrol_data = yf.Ticker(petrol).info
    dollar_data = yf.Ticker(dollar).info
    euro_data = yf.Ticker(euro).info
    golden_data = yf.Ticker(golden).info
    silver_data = yf.Ticker(silver).info

    print("----------------------------- Merhaba Hoşgeldiniz -----------------------------")
    print("Hisseler")
    print(f" Tesla : {tsla_data['regularMarketPrice']} $")
    print(f" Apple : {aapl_data['regularMarketPrice']} $")
    print(f" Microsoft : {mcsft_data['regularMarketPrice']} $")
    print(f" Netflix : {nflx_data['regularMarketPrice']} $")
    print(f" Meta : {meta_data['regularMarketPrice']} $")
    print(f" Starbucks : {sbux_data['regularMarketPrice']} $")
    print()
    print("Türk Hisseler")
    print(f" ASELSAN : {asels_data['regularMarketPrice']} ₺ ")
    print(f" Türk Hava Yolları : {thy_data['regularMarketPrice']} ₺")
    print(f" Koç Holding : {koc_data['regularMarketPrice']} ₺")
    print(f" Akbank : {akbank_data['regularMarketPrice']} ₺")
    print()
    print()
    print()
    print("Kriptolar")
    print(f" Bitcoin : {btc_data['regularMarketPrice']} $")
    print(f" Etherium : {eth_data['regularMarketPrice']} $")
    print(f" Avax : {avax_data['regularMarketPrice']} $")
    print()
    print("Varlıklar")
    print(f" Dolar : {dollar_data['regularMarketPrice']} ₺")
    print(f" Euro : {euro_data['regularMarketPrice']} ₺")
    print(f" Altın : {golden_data['regularMarketPrice']} $")
    print(f" Gümüş : {silver_data['regularMarketPrice']} $")
    print(f" Ham petrol : {petrol_data['regularMarketPrice']} $")

elif inp == "2":

    print("Türk Varlıklar İçin 1'e Basınız :")
    print("Yabancı Varlıklar İçin 2'e Basınız :")
    turkInput = input()
    if turkInput == "1":
        print("Girmek İstediğiniz Varlığın Kodunu Büyük Harflerle Giriniz")
        turkSymbolInput = input()+".IS"
        turk_data = yf.Ticker(turkSymbolInput).info
        print(turkSymbolInput+ f": {turk_data['regularMarketPrice']} ₺")

    elif turkInput == "2":
        print("Girmek İstediğiniz Varlığın Kodunu Büyük Harflerle Giriniz")
        symbolInput = input()
        symbol_data = yf.Ticker(symbolInput).info
        print(symbolInput+ f": {symbol_data['regularMarketPrice']} $")

time.sleep(60)







