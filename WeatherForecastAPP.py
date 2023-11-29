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

apiKey = "30513af3b8d24f25b8fd33273169bcfc"
url = "http://api.openweathermap.org/data/2.5/weather?"


def getWeatherData(city):
    params = {"q": city, "appid": apiKey, "lang": "tr"}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return None


def main():
    city = myEntry.get()
    weather = getWeatherData(city)

    if not city:
        tkinter.messagebox.showerror("Hata!", "Lütfen bir şehir ismi girin!")
    elif weather is None:
        tkinter.messagebox.showerror("Hata!", "Veri alınamadı. Lütfen tekrar deneyin.")
    else:
        try:
            city_name = weather.get('name', 'Unknown')
            country = weather.get('sys', {}).get('country', 'Unknown')
            temp = int(weather.get('main', {}).get('temp', 0) - 273.15)
            condition = weather.get('weather', [{}])[0].get('description', 'Unknown')

            locationLabel.config(text=f"{city_name}, {country}")
            tempLabel.config(text=f"{temp}°C")
            conditionLabel.config(text=f"{condition}")
        except Exception as e:
            print("Error:", e)
            tkinter.messagebox.showerror("Hata!", "Bir hata oluştu. Lütfen tekrar deneyin.")


myButton = tkinter.Button(text="Sorgula", font=FONT, command=main)
myButton.pack()

locationLabel = tkinter.Label(font=FONT)
locationLabel.pack()

tempLabel = tkinter.Label(font=FONT)
tempLabel.pack()

conditionLabel = tkinter.Label(font=FONT)
conditionLabel.pack()

window.mainloop()
