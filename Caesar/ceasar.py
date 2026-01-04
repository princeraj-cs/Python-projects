import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    """Caesar cipher encryption/decryption function"""
    output_text = ""
    
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    
    return output_text


class CaesarCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher")
        self.root.geometry("650x550")
        self.root.resizable(False, False)
        
        # Color scheme - modern minimal
        self.bg_color = "#1e1e2e"
        self.fg_color = "#cdd6f4"
        self.accent_color = "#89b4fa"
        self.secondary_color = "#f38ba8"
        self.button_encode = "#a6e3a1"
        self.button_decode = "#fab387"
        self.entry_bg = "#313244"
        
        self.root.configure(bg=self.bg_color)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Header
        header_frame = tk.Frame(self.root, bg=self.bg_color)
        header_frame.pack(pady=(20, 10))
        
        title_label = tk.Label(
            header_frame,
            text="🔐 Caesar Cipher",
            font=("Segoe UI", 28, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text="Encrypt & Decrypt Your Messages",
            font=("Segoe UI", 11),
            bg=self.bg_color,
            fg=self.fg_color
        )
        subtitle_label.pack()
        
        # Main content frame
        content_frame = tk.Frame(self.root, bg=self.bg_color)
        content_frame.pack(pady=10, padx=40, fill="both", expand=True)
        
        # Input text area
        input_label = tk.Label(
            content_frame,
            text="Your Message:",
            font=("Segoe UI", 11, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
            anchor="w"
        )
        input_label.pack(fill="x", pady=(10, 5))
        
        self.input_text = tk.Text(
            content_frame,
            height=5,
            font=("Consolas", 11),
            bg=self.entry_bg,
            fg=self.fg_color,
            insertbackground=self.accent_color,
            relief="flat",
            padx=10,
            pady=10,
            wrap="word"
        )
        self.input_text.pack(fill="x", pady=(0, 15))
        
        # Shift amount
        shift_frame = tk.Frame(content_frame, bg=self.bg_color)
        shift_frame.pack(fill="x", pady=(0, 20))
        
        shift_label = tk.Label(
            shift_frame,
            text="Shift Amount:",
            font=("Segoe UI", 11, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        shift_label.pack(side="left", padx=(0, 15))
        
        self.shift_var = tk.StringVar(value="3")
        self.shift_spinbox = tk.Spinbox(
            shift_frame,
            from_=1,
            to=25,
            textvariable=self.shift_var,
            font=("Segoe UI", 11),
            bg=self.entry_bg,
            fg=self.fg_color,
            buttonbackground=self.accent_color,
            relief="flat",
            width=10
        )
        self.shift_spinbox.pack(side="left")
        
        # Button frame
        button_frame = tk.Frame(content_frame, bg=self.bg_color)
        button_frame.pack(pady=(0, 15))
        
        encode_btn = tk.Button(
            button_frame,
            text="🔒 ENCODE",
            font=("Segoe UI", 11, "bold"),
            bg=self.button_encode,
            fg=self.bg_color,
            activebackground="#9ed99a",
            relief="flat",
            padx=30,
            pady=12,
            cursor="hand2",
            command=self.encode_message
        )
        encode_btn.pack(side="left", padx=10)
        
        decode_btn = tk.Button(
            button_frame,
            text="🔓 DECODE",
            font=("Segoe UI", 11, "bold"),
            bg=self.button_decode,
            fg=self.bg_color,
            activebackground="#f5a774",
            relief="flat",
            padx=30,
            pady=12,
            cursor="hand2",
            command=self.decode_message
        )
        decode_btn.pack(side="left", padx=10)
        
        # Output text area
        output_label = tk.Label(
            content_frame,
            text="Result:",
            font=("Segoe UI", 11, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
            anchor="w"
        )
        output_label.pack(fill="x", pady=(10, 5))
        
        output_frame = tk.Frame(content_frame, bg=self.bg_color)
        output_frame.pack(fill="x")
        
        self.output_text = tk.Text(
            output_frame,
            height=5,
            font=("Consolas", 11),
            bg=self.entry_bg,
            fg=self.accent_color,
            relief="flat",
            padx=10,
            pady=10,
            wrap="word",
            state="disabled"
        )
        self.output_text.pack(side="left", fill="x", expand=True)
        
        # Copy button
        copy_btn = tk.Button(
            output_frame,
            text="📋",
            font=("Segoe UI", 14),
            bg=self.accent_color,
            fg=self.bg_color,
            activebackground="#74a3f3",
            relief="flat",
            width=3,
            cursor="hand2",
            command=self.copy_result
        )
        copy_btn.pack(side="left", padx=(10, 0))
        
        # Clear button
        clear_frame = tk.Frame(self.root, bg=self.bg_color)
        clear_frame.pack(pady=(0, 15))
        
        clear_btn = tk.Button(
            clear_frame,
            text="Clear All",
            font=("Segoe UI", 10),
            bg=self.entry_bg,
            fg=self.fg_color,
            activebackground="#45475a",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.clear_all
        )
        clear_btn.pack()
    
    def encode_message(self):
        """Encode the input message"""
        self.process_message("encode")
    
    def decode_message(self):
        """Decode the input message"""
        self.process_message("decode")
    
    def process_message(self, mode):
        """Process the message (encode or decode)"""
        input_message = self.input_text.get("1.0", "end-1c").lower()
        
        if not input_message.strip():
            messagebox.showwarning("Empty Input", "Please enter a message to process.")
            return
        
        try:
            shift = int(self.shift_var.get())
            if shift < 1 or shift > 25:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Shift", "Please enter a shift value between 1 and 25.")
            return
        
        result = caesar(input_message, shift, mode)
        
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result)
        self.output_text.config(state="disabled")
    
    def copy_result(self):
        """Copy the result to clipboard"""
        result = self.output_text.get("1.0", "end-1c")
        if result.strip():
            try:
                pyperclip.copy(result)
                messagebox.showinfo("Copied!", "Result copied to clipboard.")
            except:
                # Fallback if pyperclip is not installed
                self.root.clipboard_clear()
                self.root.clipboard_append(result)
                messagebox.showinfo("Copied!", "Result copied to clipboard.")
        else:
            messagebox.showwarning("No Result", "There is no result to copy.")
    
    def clear_all(self):
        """Clear all text fields"""
        self.input_text.delete("1.0", "end")
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.config(state="disabled")
        self.shift_var.set("3")


def main():
    root = tk.Tk()
    app = CaesarCipherGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()