import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    if city == "":
        result_label.config(text="Please enter a city")
        return

    url = f"https://api.weatherapi.com/v1/current.json?key=3aeb49dee1cc47809fd170918260101&q={city}"

    try:
        r = requests.get(url)
        weatherx = r.json()

        city_name = weatherx["location"]["name"]
        time = weatherx["location"]["localtime"]
        temp = weatherx["current"]["temp_c"]

        result_label.config(
            text=f"City: {city_name}\nTime: {time}\nTemperature: {temp} °C"
        )

    except:
        result_label.config(text="Invalid city or API error")

# GUI Window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")

# UI Elements
tk.Label(root, text="Enter City", font=("Arial", 12)).pack(pady=5)

city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Arial", 11), command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()
