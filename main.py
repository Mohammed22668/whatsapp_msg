import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Function to send WhatsApp messages
def send_whatsapp_messages():
    file_path = file_entry.get()
    if not file_path:
        messagebox.showerror("Error", "Please select an Excel file.")
        return

    try:
        # Load the Excel file
        df = pd.read_excel(file_path)

        # Initialize the WebDriver
        driver = webdriver.Chrome()

        # Open WhatsApp Web
        driver.get('https://web.whatsapp.com')
        print("Please scan the QR code to log in to WhatsApp Web.")

        # Ask the user to confirm they have logged in
        messagebox.showinfo("Confirmation", "Please scan the QR code and log in to WhatsApp Web. Click OK when you are logged in.")
        
        wait = WebDriverWait(driver, 20)  # Wait for elements to appear

        # Function to send WhatsApp message
        def send_message(number, message):
            try:
                # Open a new chat
                chat_url = f'https://web.whatsapp.com/send?phone={number}'
                driver.get(chat_url)

                # Wait for the message box to load
                message_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')))
                
                message_box.send_keys(message)  # Type the message
                message_box.send_keys(Keys.ENTER)  # Send the message
                print(f"Message sent to {number}")

                # Random delay between messages (to avoid detection)
                time.sleep(random.uniform(3, 6))
            except Exception as e:
                print(f"Failed to send message to {number}: {e}")

        # Iterate over the rows in the Excel file
        for index, row in df.iterrows():
            number = str(row['Number'])  # Assuming the column name is 'Number'
            message = row['Message']     # Assuming the column name is 'Message'
            
            # Send the WhatsApp message
            send_message(number, message)

        # Close the browser
        driver.quit()
        messagebox.showinfo("Success", "All messages sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to open file dialog and select Excel file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("Excel files", "*.xls")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

# Create the main GUI window
root = tk.Tk()
root.title("WhatsApp Message Sender")
root.geometry("500x200")
root.resizable(False, False)

# Define style for a professional look
style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=6)
style.configure("TLabel", font=("Arial", 11))
style.configure("TEntry", font=("Arial", 10))

# Create a frame for padding
main_frame = ttk.Frame(root, padding=20)
main_frame.grid(row=0, column=0, sticky="nsew")

# File selection
ttk.Label(main_frame, text="Select Excel File:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
file_entry_var = tk.StringVar()
file_entry = ttk.Entry(main_frame, textvariable=file_entry_var, width=40)
file_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
ttk.Button(main_frame, text="Browse", command=browse_file).grid(row=0, column=2, padx=5, pady=5)

# Send button
send_button = ttk.Button(main_frame, text="Send Messages", command=send_whatsapp_messages)
send_button.grid(row=1, column=1, pady=20, sticky="ew")

# Adjust column weights for responsive layout
main_frame.columnconfigure(1, weight=1)

# Run the GUI event loop
root.mainloop()
