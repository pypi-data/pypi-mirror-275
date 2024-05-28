import tkinter as tk

def machine_learning_functions():
    functions = {
        # Previous functions
        "pdf": {
            "description": "Calculate the probability density function (PDF) of a given distribution at a specific point and print the result.",
            "usage": "pdf(x, distribution) where x is the point at which to calculate the PDF and distribution is the specified distribution."
        },
        "hypothesis_test": {
            "description": "Perform a t-test to compare the means of two datasets and print the results.",
            "usage": "hypothesis_test(data1, data2) where data1 and data2 are the datasets to compare."
        },
        "_euclidean_distance": {
            "description": "Compute the Euclidean distance between two vectors.",
            "usage": "_euclidean_distance(x1, x2) where x1 and x2 are the vectors."
        },
        "calculate_covariance_matrix": {
            "description": "Calculate the covariance matrix for a given dataset.",
            "usage": "calculate_covariance_matrix(data) where data is the dataset."
        },
        "cosine_sim": {
            "description": "Calculate the cosine similarity between two vectors.",
            "usage": "cosine_sim(v1, v2) where v1 and v2 are the vectors."
        },

    }
    # Add more functions here



    return functions

functions = machine_learning_functions()

def gethelp():
    def display_description(event):
        widget = event.widget
        index = int(widget.curselection()[0])
        selected_func = widget.get(index)
        description = functions[selected_func]['description']
        usage = functions[selected_func]['usage']
        description_text.config(state=tk.NORMAL)
        description_text.delete('1.0', tk.END)
        description_text.insert(tk.END, f"Description: {description}\n\n")
        description_text.insert(tk.END, f"Usage: {usage}")
        description_text.config(state=tk.DISABLED)

    root = tk.Tk()
    root.title("Function Help")

    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)

    search_frame = tk.Frame(root)
    search_frame.grid(row=0, column=0, sticky="nsew")

    search_label = tk.Label(search_frame, text="Search:")
    search_label.grid(row=0, column=0, padx=5, pady=5)

    search_entry = tk.Entry(search_frame, width=30)
    search_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    def update_listbox(event):
        search_text = search_entry.get().lower()
        results_listbox.delete(0, tk.END)
        for func in functions:
            if search_text in func.lower() or search_text in functions[func]['description'].lower():
                results_listbox.insert(tk.END, func)

    search_entry.bind("<KeyRelease>", update_listbox)

    results_frame = tk.Frame(root)
    results_frame.grid(row=1, column=0, sticky="nsew")

    results_listbox = tk.Listbox(results_frame, height=20, width=30)
    results_listbox.pack(fill=tk.BOTH, expand=True)
    results_listbox.bind('<<ListboxSelect>>', display_description)

    description_frame = tk.Frame(root)
    description_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")

    description_text = tk.Text(description_frame, wrap=tk.WORD)
    description_text.pack(fill=tk.BOTH, expand=True)
    description_text.configure(state=tk.DISABLED)

    root.mainloop()

gethelp()