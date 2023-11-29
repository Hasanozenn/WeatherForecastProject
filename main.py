import tkinter
from tkinter import messagebox
import requests
FONT = ("Arial", 10, "bold")

window = tkinter.Tk()
window.title("Hava Durumu Tahmini")
window.minsize(width=300, height=200)


myLabel = tkinter.Label(text="Yaşadığınız Şehrin İsmini Giriniz", font=FONT)
myLabel.pack()

myEntry = tkinter.Entry()
myEntry.pack()
myEntry.focus()



#inputCity = "Mersin" #str(myEntry.get())
apiKey = "30513af3b8d24f25b8fd33273169bcfc"
url ="http://api.openweathermap.org/data/2.5/weather?"

def getWeatherData(city):
    params = {"q":city, "appid":apiKey, "lang":"tr"}
    response = requests.get(url, params=params).json()
    #print(response)
#getWeatherData("Mersin")

    if response:
        city = response['name']
        country = response['sys']['country']
        temp = int(response['main']['temp'] - 273.15)
        condition = response['weather'][0]['description']
        return (city,country,temp,condition)


def main():
    city = myEntry.get()
    weather = getWeatherData(city)
    if len(city) == 0:
        tkinter.messagebox.showerror("Hata!", "Lütfen geçerli bir şehir ismi yazınız!")
    else:
        try:
            locationLabel.config(text=f"{weather[0]}, {weather[1]}")
            tempLabel.config(text=f"{weather[2]}°C")
            conditionLabel.config(text=f"{weather[3]}")
        except:
            tkinter.messagebox.showerror("Hata!", "Lütfen geçerli bir şehir ismi yazdığınızdan emin olunuz!")







myButton = tkinter.Button(text="Sorgula", font=FONT, command=main)
myButton.pack()


locationLabel = tkinter.Label(font=FONT)
locationLabel.pack()

tempLabel = tkinter.Label(font=FONT)
tempLabel.pack()

conditionLabel = tkinter.Label(font=FONT)
conditionLabel.pack()



window.mainloop()