import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io

class WeatherApp:
    def __init__(self, root):
        #window elements
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("450x450")  
        self.root.configure(bg="#2C3E50")
        self.root.resizable(False, False)
        root.iconbitmap("meteorology.ico") 

        self.api_key = "063f52cda08d42a29cc144128243012"                #API key
        self.base_url = "http://api.weatherapi.com/v1/current.json"

        self.setup_ui()

    #deign elements
    def setup_ui(self):           
        #''header element                    
        header_label = tk.Label(self.root,  text="Weather App",  font=("Helvetica", 24, "bold"),  fg="#ECF0F1",  bg="#2C3E50")
        header_label.grid(column=0, row=0, columnspan=2, pady=20)

        # entry frame 
        entry_frame = tk.Frame(self.root, bg="#2C3E50")
        entry_frame.grid(column=0, row=1, columnspan=2, pady=10)

        #events
        def on_enter(event):
            self.city_entry.config(bg="#1ABC9C", fg="#2C3E50")
        def on_leave(event):
            self.city_entry.config(bg="#34495E", fg="#ECF0F1")

        #Enter bar element
        self.city_entry = tk.Entry(entry_frame, width=30, bg="#34495E", fg="#ECF0F1", borderwidth=2, font=("Arial", 14), justify="center")
        self.city_entry.pack(side=tk.LEFT, padx=5)
        self.city_entry.bind("<Enter>", on_enter)
        self.city_entry.bind("<Leave>", on_leave)


        #button element
        search_button = tk.Button(
            entry_frame, 
            text="Search", 
            command=self.get_weather, 
            bg="#1ABC9C", 
            fg="#FFFFFF", 
            activebackground="black", 
            activeforeground="red", 
            borderwidth=0, 
            font=("Arial", 12), 
            padx=10, 
            pady=5
        )
        search_button.pack(side=tk.RIGHT, padx=5)

        # Icon label
        self.icon_label = tk.Label(self.root, bg="#2C3E50")
        self.icon_label.grid(column=0, row=2, columnspan=2, pady=10)

        # Result label
        self.result_label = tk.Label(
            self.root, 
            text="", 
            font=("Arial", 14), 
            fg="#ECF0F1", 
            bg="#34495E", 
            justify="center", 
            padx=10, 
            pady=10, 
            borderwidth=2, 
            relief="solid"
        )
        self.result_label.grid(column=0, row=3, columnspan=2, pady=20)

    #get data from API
    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showwarning("No Input", "Please enter a city name.")
            return

        try:
            response = requests.get(self.base_url, params={"key": self.api_key, "q": city})
            response.raise_for_status()
            data = response.json()

            if data:
                self.display_weather(data)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", "Could not retrieve weather data.")

    #assign data
    def display_weather(self, data):
        city_name = data["location"]["name"]
        country = data["location"]["country"]
        temp = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_kph"]
        pressure = data["current"]["pressure_mb"]
        icon_url = f"http:{data['current']['condition']['icon']}"

        # get and display weather icon
        try:
            response = requests.get(icon_url)
            response.raise_for_status()
            img_data = response.content
            img = Image.open(io.BytesIO(img_data)) 
            photo = ImageTk.PhotoImage(img)
            img = img.resize((80, 80)) 
            self.icon_label.config(image=photo)
            self.icon_label.image = photo  
        except:
            self.icon_label.config(image=None) 

        result_text = f"{city_name}, {country}\n" \
                      f"Temperature: {temp}°C\n" \
                      f"Weather: {weather}\n" \
                      f"Humidity: {humidity}%\n" \
                      f"Wind: {wind} kph\n" \
                      f"Pressure: {pressure} mb"
        self.result_label.config(text=result_text)




#start window
root = tk.Tk()
app = WeatherApp(root)
root.mainloop()
