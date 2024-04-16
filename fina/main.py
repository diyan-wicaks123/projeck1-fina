import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import pytz
import winsound
import math
import pygame

class AlarmClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Alarm Clock")
        self.master.geometry("400x400")
        
        self.alarm_time = tk.StringVar()
        
        # Membuat canvas untuk jam analog
        self.canvas = tk.Canvas(self.master, width=200, height=200)
        self.canvas.pack()
        
        # Label untuk menampilkan waktu Indonesia Barat
        self.time_label = tk.Label(self.master, text="", font=("Helvetica", 16))
        self.time_label.pack()
        
        tk.Label(self.master, text="Set Alarm (HH:MM)").pack()
        self.entry = tk.Entry(self.master, textvariable=self.alarm_time)
        self.entry.pack()
        
        tk.Button(self.master, text="Set Alarm", command=self.set_alarm).pack()
        
        # Memperbarui waktu setiap detik
        self.update_time()
        
    def update_time(self):
        # Mendapatkan waktu saat ini di timezone Asia/Jakarta
        tz = pytz.timezone('Asia/Jakarta')
        current_time = datetime.now(tz)
        
        # Menampilkan waktu Indonesia Barat
        self.time_label.config(text=current_time.strftime("%H:%M:%S %p"))
        
        # Menggambar jarum jam
        self.draw_clock(current_time)
        
        # Memperbarui waktu setiap detik
        self.master.after(1000, self.update_time)
        
    def draw_clock(self, current_time):
        self.canvas.delete("all")
        
        # Menggambar lingkaran jam
        self.canvas.create_oval(10, 10, 190, 190, width=2)
        
        # Menggambar angka jam
        for hour in range(1, 13):
            angle = math.radians(30 * hour - 90)
            x = 100 + 80 * math.cos(angle)
            y = 100 + 80 * math.sin(angle)
            self.canvas.create_text(x, y, text=str(hour), font=("Helvetica", 12))
        
        # Menggambar jarum jam
        hour_angle = math.radians((current_time.hour % 12) * 30 - 90)
        minute_angle = math.radians(current_time.minute * 6 - 90)
        
        hour_x = 100 + 50 * math.cos(hour_angle)
        hour_y = 100 + 50 * math.sin(hour_angle)
        self.canvas.create_line(100, 100, hour_x, hour_y, width=3, fill='blue')
        
        minute_x = 100 + 70 * math.cos(minute_angle)
        minute_y = 100 + 70 * math.sin(minute_angle)
        self.canvas.create_line(100, 100, minute_x, minute_y, width=2, fill='green')
        
    def set_alarm(self):
        alarm_time_str = self.alarm_time.get()
        
        try:
            alarm_hour, alarm_minute = map(int, alarm_time_str.split(':'))
            
            # Mengonversi ke timezone Indonesia Barat
            tz = pytz.timezone('Asia/Jakarta')
            current_time = datetime.now(tz)
            alarm_time = current_time.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
            
            # Memeriksa apakah alarm diatur pada waktu yang sudah berlalu
            if alarm_time < current_time:
                alarm_time += timedelta(days=1)  # Menambahkan satu hari jika alarm sudah berlalu
                
            # Hitung selisih waktu antara alarm dan waktu sekarang
            delta = alarm_time - current_time
            
            # Jalankan alarm setelah selisih waktu tersebut
            self.master.after(int(delta.total_seconds() * 1000), self.ring_alarm)
            
            messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time_str}")
            
        except Exception as e:
            messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")
    
    def ring_alarm(self):
        messagebox.showinfo("Alarm", "Wake up!")
        # Memainkan suara alarm dari file MP3
        pygame.mixer.init()
        pygame.mixer.music.load("alarm_sound.mp3")
        pygame.mixer.music.play()
        

def main():
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
