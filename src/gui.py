"""
RateLingo GUI Module
Modern Tkinter interface for RateLingo
"""

from tkinter import *
from tkinter import ttk, messagebox, scrolledtext
from src.core import ServiceRates, WordCounter, PricingCalculator
import src.database as db


class RateLingoGUI:
    """Main GUI application class"""
    
    # Color scheme - Modern purple/violet theme
    COLORS = {
        'primary': '#7C3AED',      # Violet
        'secondary': '#A78BFA',    # Light purple
        'accent': '#F59E0B',       # Amber
        'bg_light': '#F9FAFB',     # Light gray
        'bg_dark': '#1F2937',      # Dark gray
        'text_dark': '#111827',    # Almost black
        'text_light': '#6B7280',   # Gray
        'white': '#FFFFFF',
        'success': '#10B981',      # Green
        'error': '#EF4444',        # Red
        'border': '#E5E7EB'        # Light border
    }
    
    def __init__(self, root):
        self.root = root
        self.root.title("RateLingo - Professional Pricing Calculator")
        self.root.geometry("1000x650")
        self.root.minsize(900, 600)
        
        # Initialize database
        db.create_tables()
        
        # Configure window
        self.root.configure(bg=self.COLORS['bg_light'])
        
        # Initialize variables
        self.selected_service = StringVar()
        self.word_count = IntVar(value=0)
        self.char_count = IntVar(value=0)
        self.total_cost = DoubleVar(value=0.0)
        
        # Build UI
        self.create_header()
        self.create_main_content()
        self.create_footer()
        
        # Bind text change event
        self.text_area.bind('<KeyRelease>', self.on_text_change)
    
    def create_header(self):
        """Create application header"""
        header = Frame(self.root, bg=self.COLORS['primary'], height=80)
        header.pack(fill=X, side=TOP)
        header.pack_propagate(False)
        
        # App title
        title_label = Label(
            header,
            text="RateLingo",
            font=('Segoe UI', 28, 'bold'),
            bg=self.COLORS['primary'],
            fg=self.COLORS['white']
        )
        title_label.pack(side=LEFT, padx=30, pady=15)
        
        # Subtitle
        subtitle = Label(
            header,
            text="Professional Language Service Pricing Calculator",
            font=('Segoe UI', 11),
            bg=self.COLORS['primary'],
            fg=self.COLORS['secondary']
        )
        subtitle.place(x=30, y=50)
        
        # Version badge
        version = Label(
            header,
            text="v1.0",
            font=('Segoe UI', 9),
            bg=self.COLORS['accent'],
            fg=self.COLORS['white'],
            padx=8,
            pady=3
        )
        version.pack(side=RIGHT, padx=30, pady=15)
    
    def create_main_content(self):
        """Create main content area with left and right panels"""
        # Main container
        main_container = Frame(self.root, bg=self.COLORS['bg_light'])
        main_container.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # LEFT PANEL - Text Input Area
        self.create_left_panel(main_container)
        
        # RIGHT PANEL - Service Selection & Calculation
        self.create_right_panel(main_container)
    
    def create_left_panel(self, parent):
        """Create left panel for text input"""
        left_panel = Frame(parent, bg=self.COLORS['white'], relief=FLAT, bd=0)
        left_panel.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))
        
        # Panel header
        header = Frame(left_panel, bg=self.COLORS['white'])
        header.pack(fill=X, padx=20, pady=(20, 10))
        
        Label(
            header,
            text="📝 Your Text",
            font=('Segoe UI', 14, 'bold'),
            bg=self.COLORS['white'],
            fg=self.COLORS['text_dark']
        ).pack(side=LEFT)
        
        # Clear button
        clear_btn = Button(
            header,
            text="Clear",
            font=('Segoe UI', 9),
            bg=self.COLORS['bg_light'],
            fg=self.COLORS['text_light'],
            relief=FLAT,
            cursor='hand2',
            command=self.clear_text
        )
        clear_btn.pack(side=RIGHT)
        
        # Text area frame
        text_frame = Frame(left_panel, bg=self.COLORS['white'])
        text_frame.pack(fill=BOTH, expand=True, padx=20, pady=(0, 20))
        
        # Scrolled text area with placeholder
        self.text_area = scrolledtext.ScrolledText(
            text_frame,
            font=('Consolas', 11),
            wrap=WORD,
            relief=FLAT,
            bg=self.COLORS['bg_light'],
            fg=self.COLORS['text_dark'],
            insertbackground=self.COLORS['primary'],
            selectbackground=self.COLORS['secondary'],
            padx=15,
            pady=15,
            borderwidth=2,
            highlightthickness=1,
            highlightcolor=self.COLORS['primary'],
            highlightbackground=self.COLORS['border']
        )
        self.text_area.pack(fill=BOTH, expand=True)
        
        # Add placeholder
        self.add_placeholder()
        
        # Word/Character count display
        count_frame = Frame(left_panel, bg=self.COLORS['white'])
        count_frame.pack(fill=X, padx=20, pady=(0, 20))
        
        Label(
            count_frame,
            text="Words:",
            font=('Segoe UI', 10),
            bg=self.COLORS['white'],
            fg=self.COLORS['text_light']
        ).pack(side=LEFT)
        
        self.word_count_label = Label(
            count_frame,
            textvariable=self.word_count,
            font=('Segoe UI', 10, 'bold'),
            bg=self.COLORS['white'],
            fg=self.COLORS['primary']
        )
        self.word_count_label.pack(side=LEFT, padx=(5, 20))
        
        Label(
            count_frame,
            text="Characters:",
            font=('Segoe UI', 10),
            bg=self.COLORS['white'],
            fg=self.COLORS['text_light']
        ).pack(side=LEFT)
        
        self.char_count_label = Label(
            count_frame,
            textvariable=self.char_count,
            font=('Segoe UI', 10, 'bold'),
            bg=self.COLORS['white'],
            fg=self.COLORS['primary']
        )
        self.char_count_label.pack(side=LEFT, padx=5)
    
    def create_right_panel(self, parent):
        """Create right panel for service selection and pricing"""
        right_panel = Frame(parent, bg=self.COLORS['white'], relief=FLAT, bd=0, width=380)
        right_panel.pack(side=RIGHT, fill=BOTH, padx=(10, 0))
        right_panel.pack_propagate(False)
        
        # Panel header
        header = Frame(right_panel, bg=self.COLORS['white'])
        header.pack(fill=X, padx=20, pady=(20, 10))
        
        Label(
            header,
            text="💼 Service & Pricing",
            font=('Segoe UI', 14, 'bold'),
            bg=self.COLORS['white'],
            fg=self.COLORS['text_dark']
        ).pack(side=LEFT)
        
        # Service selection
        service_frame = Frame(right_panel, bg=self.COLORS['white'])
        service_frame.pack(fill=X, padx=20, pady=20)
        
        Label(
            service_frame,
            text="Select Service",
            font=('Segoe UI', 11, 'bold'),
            bg=self.COLORS['white'],
            fg=self.COLORS['text_dark']
        ).pack(anchor=W, pady=(0, 8))
        
        # Custom styled combobox
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            'Custom.TCombobox',
            fieldbackground=self.COLORS['bg_light'],
            background=self.COLORS['white'],
            foreground=self.COLORS['text_dark'],
            arrowcolor=self.COLORS['primary'],
            borderwidth=1,
            relief=FLAT
        )
        
        self.service_combo = ttk.Combobox(
            service_frame,
            textvariable=self.selected_service,
            values=[s.capitalize() for s in ServiceRates.get_all_services()],
            state='readonly',
            font=('Segoe UI', 11),
            style='Custom.TCombobox',
            height=10
        )
        self.service_combo.pack(fill=X, ipady=8)
        self.service_combo.set("Select a service...")
        self.service_combo.bind('<<ComboboxSelected>>', self.on_service_change)
        
        # Service description
        self.service_desc = Label(
            service_frame,
            text="",
            font=('Segoe UI', 9),
            bg=self.COLORS['white'],
            fg=self.COLORS['text_light'],
            wraplength=320,
            justify=LEFT
        )
        self.service_desc.pack(anchor=W, pady=(8, 0))
        
        # Rate display
        rate_frame = Frame(right_panel, bg=self.COLORS['bg_light'])
        rate_frame.pack(fill=X, padx=20, pady=20)
        
        rate_inner = Frame(rate_frame, bg=self.COLORS['bg_light'])
        rate_inner.pack(fill=X, padx=15, pady=15)
        
        Label(
            rate_inner,
            text="Rate per Word",
            font=('Segoe UI', 10),
            bg=self.COLORS['bg_light'],
            fg=self.COLORS['text_light']
        ).pack(anchor=W)
        
        self.rate_label = Label(
            rate_inner,
            text="$0.00",
            font=('Segoe UI', 20, 'bold'),
            bg=self.COLORS['bg_light'],
            fg=self.COLORS['primary']
        )
        self.rate_label.pack(anchor=W, pady=(5, 0))
        
        # Calculate button
        calc_frame = Frame(right_panel, bg=self.COLORS['white'])
        calc_frame.pack(fill=X, padx=20, pady=10)
        
        self.calc_button = Button(
            calc_frame,
            text="Calculate Cost",
            font=('Segoe UI', 12, 'bold'),
            bg=self.COLORS['primary'],
            fg=self.COLORS['white'],
            relief=FLAT,
            cursor='hand2',
            command=self.calculate_cost,
            activebackground=self.COLORS['secondary'],
            activeforeground=self.COLORS['white'],
            padx=20,
            pady=15
        )
        self.calc_button.pack(fill=X)
        
        # Results section
        results_frame = Frame(right_panel, bg=self.COLORS['white'])
        results_frame.pack(fill=X, padx=20, pady=20)
        
        Label(
            results_frame,
            text="Total Cost",
            font=('Segoe UI', 11, 'bold'),
            bg=self.COLORS['white'],
            fg=self.COLORS['text_dark']
        ).pack(anchor=W, pady=(0, 8))
        
        # Cost display
        cost_display = Frame(results_frame, bg=self.COLORS['success'], relief=FLAT)
        cost_display.pack(fill=X, ipady=20)
        
        self.cost_label = Label(
            cost_display,
            text="$0.00",
            font=('Segoe UI', 32, 'bold'),
            bg=self.COLORS['success'],
            fg=self.COLORS['white']
        )
        self.cost_label.pack()
        
        # Action buttons
        action_frame = Frame(right_panel, bg=self.COLORS['white'])
        action_frame.pack(fill=X, padx=20, pady=20, side=BOTTOM)
        
        Button(
            action_frame,
            text="Save Quote",
            font=('Segoe UI', 10),
            bg=self.COLORS['bg_light'],
            fg=self.COLORS['text_dark'],
            relief=FLAT,
            cursor='hand2',
            command=self.save_quote,
            padx=15,
            pady=10
        ).pack(side=LEFT, expand=True, fill=X, padx=(0, 5))
        
        Button(
            action_frame,
            text="View History",
            font=('Segoe UI', 10),
            bg=self.COLORS['bg_light'],
            fg=self.COLORS['text_dark'],
            relief=FLAT,
            cursor='hand2',
            command=self.view_history,
            padx=15,
            pady=10
        ).pack(side=RIGHT, expand=True, fill=X, padx=(5, 0))
    
    def create_footer(self):
        """Create application footer"""
        footer = Frame(self.root, bg=self.COLORS['bg_dark'], height=40)
        footer.pack(fill=X, side=BOTTOM)
        footer.pack_propagate(False)
        
        Label(
            footer,
            text="© 2025 RateLingo by Benedict Kofi Amofah",
            font=('Segoe UI', 9),
            bg=self.COLORS['bg_dark'],
            fg=self.COLORS['text_light']
        ).pack(side=LEFT, padx=20)
        
        Label(
            footer,
            text="Made for Twi Language Professionals",
            font=('Segoe UI', 9),
            bg=self.COLORS['bg_dark'],
            fg=self.COLORS['text_light']
        ).pack(side=RIGHT, padx=20)
    
    def add_placeholder(self):
        """Add placeholder text to text area"""
        self.text_area.insert('1.0', 'Paste your text here...')
        self.text_area.config(fg=self.COLORS['text_light'])
        self.text_area.bind('<FocusIn>', self.on_text_focus_in)
        self.text_area.bind('<FocusOut>', self.on_text_focus_out)
    
    def on_text_focus_in(self, event):
        """Remove placeholder on focus"""
        if self.text_area.get('1.0', 'end-1c') == 'Paste your text here...':
            self.text_area.delete('1.0', END)
            self.text_area.config(fg=self.COLORS['text_dark'])
    
    def on_text_focus_out(self, event):
        """Add placeholder if empty"""
        if not self.text_area.get('1.0', 'end-1c').strip():
            self.text_area.insert('1.0', 'Paste your text here...')
            self.text_area.config(fg=self.COLORS['text_light'])
    
    def on_text_change(self, event=None):
        """Update word and character count on text change"""
        text = self.text_area.get('1.0', 'end-1c')
        
        if text == 'Paste your text here...':
            self.word_count.set(0)
            self.char_count.set(0)
        else:
            self.word_count.set(WordCounter.count_words(text))
            self.char_count.set(WordCounter.count_characters(text))
    
    def on_service_change(self, event=None):
        """Update rate display when service changes"""
        service = self.selected_service.get().lower()
        if ServiceRates.is_valid_service(service):
            rate = ServiceRates.get_rate(service)
            desc = ServiceRates.get_description(service)
            self.rate_label.config(text=f"${rate:.2f}")
            self.service_desc.config(text=desc)
    
    def clear_text(self):
        """Clear text area"""
        self.text_area.delete('1.0', END)
        self.add_placeholder()
        self.word_count.set(0)
        self.char_count.set(0)
    
    def calculate_cost(self):
        """Calculate and display total cost"""
        text = self.text_area.get('1.0', 'end-1c')
        service = self.selected_service.get().lower()
        
        # Validation
        if text == 'Paste your text here...' or not text.strip():
            messagebox.showwarning('No Text', 'Please enter some text to calculate.')
            return
        
        if not ServiceRates.is_valid_service(service):
            messagebox.showwarning('No Service', 'Please select a service.')
            return
        
        # Calculate
        result = PricingCalculator.calculate_service_cost(text, service)
        
        if result:
            self.total_cost.set(result['total_cost'])
            self.cost_label.config(text=f"${result['total_cost']:.2f}")
            
            # Show success message
            messagebox.showinfo(
                'Calculation Complete',
                f"Service: {result['service']}\n"
                f"Words: {result['word_count']:,}\n"
                f"Rate: ${result['rate']:.2f}/word\n"
                f"Total: ${result['total_cost']:.2f}"
            )
    
    def save_quote(self):
        """Save current quote to database"""
        text = self.text_area.get('1.0', 'end-1c')
        service = self.selected_service.get().lower()
        
        if text == 'Paste your text here...' or not text.strip():
            messagebox.showwarning('No Text', 'Please enter some text to save.')
            return
        
        if not ServiceRates.is_valid_service(service):
            messagebox.showwarning('No Service', 'Please select a service.')
            return
        
        # Calculate first
        result = PricingCalculator.calculate_service_cost(text, service)
        
        if result:
            # Save to database
            db.save_quote(
                service=result['service'],
                word_count=result['word_count'],
                rate=result['rate'],
                total_cost=result['total_cost'],
                text_sample=text[:200]  # Save first 200 chars
            )
            messagebox.showinfo('Saved', 'Quote saved successfully!')
    
    def view_history(self):
        """Open history window"""
        HistoryWindow(self.root)


class HistoryWindow:
    """Window to view saved quotes history"""
    
    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.window.title("Quote History")
        self.window.geometry("800x500")
        self.window.configure(bg=RateLingoGUI.COLORS['bg_light'])
        
        # Header
        header = Frame(self.window, bg=RateLingoGUI.COLORS['primary'], height=60)
        header.pack(fill=X)
        header.pack_propagate(False)
        
        Label(
            header,
            text="📊 Quote History",
            font=('Segoe UI', 16, 'bold'),
            bg=RateLingoGUI.COLORS['primary'],
            fg=RateLingoGUI.COLORS['white']
        ).pack(side=LEFT, padx=20, pady=15)
        
        # Create treeview
        self.create_treeview()
        
        # Load data
        self.load_history()
        
        # Buttons
        btn_frame = Frame(self.window, bg=RateLingoGUI.COLORS['bg_light'])
        btn_frame.pack(fill=X, padx=20, pady=20)
        
        Button(
            btn_frame,
            text="Delete Selected",
            font=('Segoe UI', 10),
            bg=RateLingoGUI.COLORS['error'],
            fg=RateLingoGUI.COLORS['white'],
            relief=FLAT,
            cursor='hand2',
            command=self.delete_selected,
            padx=15,
            pady=10
        ).pack(side=LEFT, padx=(0, 10))
        
        Button(
            btn_frame,
            text="Close",
            font=('Segoe UI', 10),
            bg=RateLingoGUI.COLORS['bg_dark'],
            fg=RateLingoGUI.COLORS['white'],
            relief=FLAT,
            cursor='hand2',
            command=self.window.destroy,
            padx=15,
            pady=10
        ).pack(side=RIGHT)
    
    def create_treeview(self):
        """Create treeview for displaying quotes"""
        frame = Frame(self.window, bg=RateLingoGUI.COLORS['white'])
        frame.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Scrollbar
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Treeview
        self.tree = ttk.Treeview(
            frame,
            columns=('ID', 'Date', 'Service', 'Words', 'Rate', 'Total'),
            show='headings',
            yscrollcommand=scrollbar.set
        )
        
        # Configure columns
        self.tree.heading('ID', text='ID')
        self.tree.heading('Date', text='Date')
        self.tree.heading('Service', text='Service')
        self.tree.heading('Words', text='Words')
        self.tree.heading('Rate', text='Rate')
        self.tree.heading('Total', text='Total Cost')
        
        self.tree.column('ID', width=50)
        self.tree.column('Date', width=150)
        self.tree.column('Service', width=120)
        self.tree.column('Words', width=100)
        self.tree.column('Rate', width=100)
        self.tree.column('Total', width=120)
        
        self.tree.pack(fill=BOTH, expand=True)
        scrollbar.config(command=self.tree.yview)
    
    def load_history(self):
        """Load quote history from database"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Load from database
        quotes = db.get_all_quotes()
        for quote in quotes:
            self.tree.insert('', 'end', values=(
                quote[0],  # ID
                quote[1],  # Date
                quote[2],  # Service
                quote[3],  # Word count
                f"${quote[4]:.2f}",  # Rate
                f"${quote[5]:.2f}"   # Total
            ))
    
    def delete_selected(self):
        """Delete selected quote"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning('No Selection', 'Please select a quote to delete.')
            return
        
        if messagebox.askyesno('Confirm Delete', 'Are you sure you want to delete this quote?'):
            item = self.tree.item(selected[0])
            quote_id = item['values'][0]
            db.delete_quote(quote_id)
            self.load_history()
            messagebox.showinfo('Deleted', 'Quote deleted successfully!')


def main():
    """Entry point for GUI application"""
    root = Tk()
    app = RateLingoGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()