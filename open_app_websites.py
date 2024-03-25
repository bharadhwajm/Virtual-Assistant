import os
import urllib.request
import webbrowser
import json
import tkinter

def open_app(user_input):
    #! opens apps. command for the apps given in butcher_tasks.json file
    with open('/home/bharadhwaj/personal-code/python/BUTCHER/tasks.json') as apps:
        app = json.load(apps)
        os.system(app["open apps"][user_input])

def open_websites(user_input):
    #! opens websites. links for the websites in butcher_tasks.json file
    with open('/home/bharadhwaj/personal-code/python/BUTCHER/tasks.json') as open_file:
        url = json.load(open_file)
        web_url = urllib.request.urlopen(url["open websites"][user_input])
        webbrowser.open_new(web_url.geturl())

def add_websites():
    #! to add websites to the json file incase isn't currently available
    window = tkinter.Tk()
    window.config(bg="#121212")
    window.title("add website")
    window.geometry("380x150")

    website = tkinter.Label(window, text="Website name",
                            bg="#121212", fg="white")
    website.grid(row=1, column=1, pady=10, padx=10)

    website_entry = tkinter.Entry(window, bg="#121212", fg="white")
    website_entry.grid(row=1, column=2, pady=10, padx=10)

    http = tkinter.Label(
        window, text="Enter the link of the website", bg="#121212", fg="white")
    http.grid(row=2, column=1, pady=10, padx=10)

    http_entry = tkinter.Entry(window, bg="#121212", fg="white")
    http_entry.grid(row=2, column=2, pady=10, padx=10)

    def destroy_window():
        window.destroy()

    cancel_button = tkinter.Button(
        window, text="Cancel", bg="#121212", fg="white", command=destroy_window)
    cancel_button.grid(row=4, column=1, pady=10, padx=10)

    def write_website():
        #! to saves the website's name and the link to the json file
        website_str = str(website_entry.get())
        url_str = str(http_entry.get())

        with open("/home/bharadhwaj/personal-code/python/BUTCHER/tasks.json") as websites:
            url = json.load(websites)
            if website_str not in url["open websites"]:
                with open("tasks.json", 'w') as website_add:
                    url["open websites"][website_str] = url_str
                    json.dump(url, website_add, indent=2)
                    window.destroy()

    done_button = tkinter.Button(
        window, text="Done", bg="#121212", fg="white", command=write_website)
    done_button.grid(row=4, column=2, pady=10, padx=10)

    window.mainloop()
