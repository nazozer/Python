import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Listbox, Button, Entry, Label, END
from PIL import Image, ImageTk

# Web scraping 
def fetch_medal_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Pull country data
            countries = soup.find_all("span", class_="ssrcss-ymac56-CountryName ew4ldjd0")
            countries_list = [country.text.strip() for country in countries]
            
            # Pull medal data
            medal_data = soup.find_all("div", class_="ssrcss-1yl2exm-CellWrapper ef9ipf0")
            
            # Separate gold, silver, bronze and total medal data in order
            gold_list, silver_list, bronze_list, total_list = [], [], [], []
            for i in range(0, len(medal_data), 4):
                gold_list.append(int(medal_data[i].text.strip()))
                silver_list.append(int(medal_data[i + 1].text.strip()))
                bronze_list.append(int(medal_data[i + 2].text.strip()))
                total_list.append(int(medal_data[i + 3].text.strip()))
            
            
            data = {
                "Country": countries_list,
                "Gold": gold_list,
                "Silver": silver_list,
                "Bronze": bronze_list,
                "Total": total_list,
            }
            
            
            df = pd.DataFrame(data)
            
            # Sort the data
            df_sorted = df.sort_values(by="Total", ascending=False)
            
            return df_sorted
        else:
            print(f"Error: Unable to fetch data. HTTP Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def show_general_analytics(df):
    # First 10 country
    df_top10 = df.head(10)

    medal_types = ["Gold", "Silver", "Bronze"]
    colors = {
        "Gold": "#ffc200",
        "Silver": "#9a9a9a",
        "Bronze": "#cd5832",
    }

   
    fig, axes = plt.subplots(2, 2, figsize=(20, 10))  
    axes = axes.flatten()

    # Bronz madalyalar pastası 
    axes[0].pie(
        df_top10["Bronze"],
        labels=df_top10["Country"],
        autopct="%1.1f%%",
        startangle=140,
        colors=[colors["Bronze"]] * len(df_top10),
    )
    axes[0].set_title("Bronze Medals")

    # Altın madalyalar pastası 
    axes[1].pie(
        df_top10["Gold"],
        labels=df_top10["Country"],
        autopct="%1.1f%%",
        startangle=140,
        colors=[colors["Gold"]] * len(df_top10),
    )
    axes[1].set_title("Gold Medals")

    axes[2].pie(
        df_top10["Silver"],
        labels=df_top10["Country"],
        autopct="%1.1f%%",
        startangle=140,
        colors=[colors["Silver"]] * len(df_top10),
    )
    axes[2].set_title("Silver Medals")

   # Line chart-- Total number of medals
    axes[3].plot(df_top10["Country"], df_top10["Total"], label="Total Medals", color="blue", marker='o')
    
    axes[3].set_title("Total Medals Trend")
    axes[3].set_xlabel("Country")
    axes[3].set_ylabel("Number of Medals")
    axes[3].legend()

    plt.tight_layout()
    plt.show()

def show_country_chart(df, country):
    try:
        data = df[df["Country"] == country]
        if data.empty:
            print(f"Country {country} not found in the dataset.")
            return
        
        medals = ["Gold", "Silver", "Bronze"]
        values = [data["Gold"].values[0], data["Silver"].values[0], data["Bronze"].values[0]]
        colors = ["#FFD700", "#C0C0C0", "#cd7f32"]
        
        plt.figure(figsize=(6, 4))
        plt.bar(medals, values, color=colors)
        plt.title(f"Medals for {country}")
        plt.ylabel("Number of Medals")
        plt.show()
    except KeyError:
        print(f"Country {country} not found in the dataset.")

# Tkinter GUI
def create_gui():
    root = Tk()
    root.title("Olympics 2024")
    

    image_path = "C:\\Users\\ASUS\\Desktop\\OlympicStats\\indir.png"
    try:
        title_label1 = Label(root, text="Olympics 2024", font=("Calibri", 20, "bold"), fg="black")
        title_label1.pack(pady=10)

        img_1= Image.open(image_path)
        img_1= img_1.resize((150, 100), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_1)

        img_label = Label(root, image=img_tk)
        img_label.image = img_tk
        img_label.pack(pady=10)

    except FileNotFoundError:
        print(f"Error: File not found at {image_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    url_entry = Entry(root, width=40)
    url_entry.pack(pady=5)

    def fetch_list():
        nonlocal df
        url = url_entry.get()
        df = fetch_medal_data(url)
        
        if df is not None:
            countries_listbox.delete(0, END)
            for country in df["Country"]:
                countries_listbox.insert(END, country)
        else:
            print("NO data... Check the URL or the website structure!")
            
    Button(root, text="Show List", command=fetch_list).pack(pady=10)

    countries_listbox = Listbox(root, width=35, height=15)
    countries_listbox.pack(pady=5)

    df = None

    text_label = Label(root, text="Click on a country to see detailed medals:", font=("Arial", 10), fg="black")
    text_label.pack(pady=10)
    
    def show_chart():
        try:
            selected_country = countries_listbox.get(countries_listbox.curselection())
            show_country_chart(df, selected_country)
        except Exception as e:
            print(f"An error occurred while displaying chart: {e}")

    Button(root, text="Show Chart of selected country", command=show_chart).pack(pady=10)
    
    def show_general():
        if df is not None:
            show_general_analytics(df)
        else:
            print("No data available for general analytics...")

    Button(root, text="Show top 10 performing countries analytics", command=show_general).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
