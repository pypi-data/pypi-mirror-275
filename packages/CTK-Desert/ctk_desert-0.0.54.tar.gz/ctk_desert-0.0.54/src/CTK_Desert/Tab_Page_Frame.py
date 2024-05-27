import os, importlib, copy
import importlib.util
import customtkinter as ctk
from PIL import Image

import win32api

from .Core import userChest as Chest
from .Theme import *
from .utils import hvr_clr_g

from .Settings import Settings
from .AddPage import Workspace

class Frame(ctk.CTkFrame):
    
    def __init__ (self, parent, usr_assets_dir, page_choise, on_theme_change_func=None):
        super().__init__(parent, fg_color=(LIGHT_MODE["background"], DARK_MODE["background"]))
        self.current_dir = os.path.dirname(__file__)
        self.original_icons_dir = f"{self.current_dir}\\images\\Icons\\"
        self.user_icons_dir = os.path.join(usr_assets_dir, "Images\\")
        self.window = parent

        self.menu_relwidth = 0.05
        self.menu_relx = 0
        self.padding = 0.02
        self.menu_opened = False

        self.page_choise = page_choise if page_choise != "" else "Workspace"
        self.on_theme_change_func = on_theme_change_func
        self.last_page = None
        self.tabs = [("Workspace", 0), ("Settings", 0), ] # used to add tabs after importing its class, the 1 or 0 is used to determine if the tab is created at the beginning automatically or do i want to create it manually later 
        
        # Import all the pages from the pages directory
        self.U_Pages_dir = os.path.join(usr_assets_dir, "Pages")
        files = os.listdir(self.U_Pages_dir)                   # get all the files in the directory
        sorted_files = sorted(files, key=lambda x: os.path.getctime(os.path.join(self.U_Pages_dir, x)))            # used to sort the files by creation date so that when they are displayed in the menu the by in order
        module_names = [file[:-3] for file in sorted_files if file.endswith('.py') and file != '__init__.py']   # get all the file names without the .py extension
        for module_name in module_names:
            self.ext_pages_importer(module_name)
        # end of importing the user custom pages

        self.buttons = {}               # used to save all the tab buttons for later configuration
        self.pages_dict = {}            # used to save the initialized frame classes of all the tabs, (ex: home frame, friends frame, etc...)
        self.mainpages_dict = {}
        self.subpages_dict = {}
        
        self.window.update()
        self.window_width = self.window.winfo_width()
        self.window_height = self.window.winfo_height()

        self.window.bind("<Configure>", self.update_state_checker)
        self.size_event = None
        self.updating = False

        self.menu()
        self.page()

        self.pack(expand = True, fill = "both")

        self.pages_dict[self.page_choise].called_when_opened(k=1)   # used to apply some changes to the default page, that can't be applied before the frame is displayed  


    def menu(self):
        self.menu_frame = ctk.CTkFrame(self, fg_color=(hvr_clr_g(LIGHT_MODE["background"], "l"), hvr_clr_g(DARK_MODE["background"], "d")))

        # 1
        self.logo_frame = ctk.CTkFrame(self.menu_frame, fg_color="transparent")
        button = self.tab("Workspace", self.logo_frame, (45,45))
        self.buttons["Workspace"] = button
        self.logo_frame.pack(fill="x", ipady=5, padx=5)

        # 2
        self.tabs_frame = ctk.CTkFrame(self.menu_frame, fg_color="transparent")
        for tab in self.tabs:
            if tab[1] == 1:
                button = self.tab(tab[0], self.tabs_frame)      #create all the tabs
                self.buttons[tab[0]] = button #saving them for later configuration in the color
            else:
                continue
        self.tabs_frame.pack(fill="x", padx=5, pady = 5)    

        self.white_line_spacer(self.menu_frame)                                         # white line
        #3
        self.apps_frame = ctk.CTkFrame(self.menu_frame, fg_color="transparent")

        self.apps_frame.pack(fill="both", expand=True, padx=5, pady = 5)

        self.white_line_spacer(self.menu_frame)                                         # white line
        #4
        self.user_frame = ctk.CTkFrame(self.menu_frame, fg_color="transparent")
        button = self.tab("Settings", self.user_frame)
        self.buttons["Settings"] = button
        self.user_frame.pack(fill="x", padx=5)

        self.menu_frame.place(relx=self.menu_relx, rely=0, anchor="nw", relheight = 1-(25/self.window_height), relwidth = self.menu_relwidth)

    def page(self):
        self.page_frame = ctk.CTkFrame(self, fg_color="transparent")
        Chest._D__Setup_Chest(self.window, self)        #^ Initialize the Chest
        for name in self.tabs:
            self.pages_dict[name[0]] = eval(name[0] + "()")    #calls all the contents of the tabs (but not displaying them) and passing the arguments, while saving them in a dict for later use
            if self.pages_dict[name[0]].scrollable:
                Last_widget = ctk.CTkFrame(self.pages_dict[name[0]].Scrollable_frame, fg_color=self.pages_dict[name[0]].Scrollable_frame._fg_color, bg_color=self.pages_dict[name[0]].Scrollable_frame._fg_color) #created to locate the y position for the edge of the frame
                Last_widget.pack(fill="x", pady=10) 
        #! Replace this with the core implementation, so that any page can request the Uesr pages directory
        # self.pages_dict["Workspace"].pages_path = self.U_Pages_dir


        self.pages_dict[self.page_choise].pack(expand=True, fill="both")                        #display the default page
        directory = self.original_icons_dir if self.page_choise == "Workspace" or self.page_choise == "Settings" else self.user_icons_dir
        self.buttons[self.page_choise].configure(image=ctk.CTkImage(Image.open(f"{directory}{self.page_choise}_l_s.png"), Image.open(f"{directory}{self.page_choise}_d_s.png"), (45,45) if self.page_choise == "Workspace" else (30,30)))


        self.page_frame.place(relx= (self.menu_relx + self.menu_relwidth + (self.padding/2)) , 
                              rely=0, 
                              anchor="nw", 
                              relheight = 1-(25/self.window_height), 
                              relwidth = 1 - (self.menu_relx + self.menu_relwidth + (self.padding/2)) - (self.padding/2)
                              )
        
        self.mainpages_dict = copy.copy(self.pages_dict)
           
    def menu_button_command(self): # currently not used
        if self.menu_opened:
            self.menu_relwidth -= 0.135
            self.menu_frame.place(relx=self.menu_relx, rely=0, anchor="nw", relheight = 1-(40/self.window.winfo_width()), relwidth = self.menu_relwidth)

            self.page_frame.place(relx= (self.menu_relx + self.menu_relwidth + (self.padding/2)) , 
                                rely=0, 
                                anchor="nw", 
                                relheight = 1-(40/self.window.winfo_width()), 
                                relwidth = 1 - (self.menu_relx + self.menu_relwidth + (self.padding/2)) - (self.padding/2)
                                )

            self.update()
            self.menu_opened = False

        else:
            self.menu_relwidth += 0.135
            self.menu_frame.place(relx=self.menu_relx, rely=0, anchor="nw", relheight = 1-(40/self.window.winfo_width()), relwidth = self.menu_relwidth)

            self.page_frame.place(relx= (self.menu_relx + self.menu_relwidth + (self.padding/2)) , 
                                    rely=0, 
                                    anchor="nw", 
                                    relheight = 1-(40/self.window.winfo_width()), 
                                    relwidth = 1 - (self.menu_relx + self.menu_relwidth + (self.padding/2)) - (self.padding/2)
                                    )
            self.update()
            self.menu_opened = True

    def tab(self, tab, parent, btn_size=(30,30)):
        directory = self.original_icons_dir if tab == "Workspace" or tab == "Settings" else self.user_icons_dir
        button = ctk.CTkButton(parent, text="", fg_color="transparent", hover_color=(hvr_clr_g(LIGHT_MODE["background"], "l"), hvr_clr_g(DARK_MODE["background"], "d")), image=ctk.CTkImage(Image.open(f"{directory}{tab.lower()}_l.png"), Image.open(f"{directory}{tab.lower()}_d.png"), btn_size), command = lambda: self.page_switcher(f'{tab}'))
        button.pack(ipadx = 10, pady=10)
        return button

    def page_switcher(self, buttonID):
        if buttonID != self.page_choise and self.pages_dict[buttonID].openable == True:
            if self.pages_dict[self.page_choise].Leaving("global"):
                self.pages_dict[self.page_choise].pack_forget()
                self.pages_dict[self.page_choise].tools_f.place_forget()    #placed inside the file 
                directory = self.original_icons_dir if self.page_choise == "Workspace" or self.page_choise == "Settings" else self.user_icons_dir
                self.buttons[self.page_choise].configure(image=ctk.CTkImage(Image.open(f"{directory}{self.page_choise.lower()}_l.png"), Image.open(f"{directory}{self.page_choise.lower()}_d.png"), (45,45) if self.page_choise == "Workspace" else (30,30)))
                self.last_page = self.page_choise
                # print(self.page_choise, ">>", buttonID)
                self.page_choise = f'{buttonID}'
                directory = self.original_icons_dir if buttonID == "Workspace" or buttonID == "Settings" else self.user_icons_dir
                self.buttons[buttonID].configure(image=ctk.CTkImage(Image.open(f"{directory}{buttonID.lower()}_l_s.png"), Image.open(f"{directory}{buttonID.lower()}_d_s.png"), (45,45) if buttonID == "Workspace" else (30,30)))
                self.pages_dict[buttonID].pack(expand=True, fill="both")
                self.pages_dict[buttonID].called_when_opened(k=1)   # used to apply some changes that can't be applied before the frame is displayed
                if self.pages_dict[buttonID].pickable == 1:
                    self.pages_dict[buttonID].Picking()

    def update_state_checker(self, event):
        if ((event.width != self.window_width or event.height != self.window_height) and (event.widget == self.window)):
            self.size_event = event
            if not self.updating:    
                # print("detected")
                self.updating = True
                self.pack_forget()
                self.check_click_state()

    def check_click_state(self):
        if win32api.GetKeyState(0x01) < 0:
            self.after(50, self.check_click_state)
        else:
            # print("packing and updating")
            self.pack(expand = True, fill = "both")
            self.update_sizes()
            self.updating = False

    def update_sizes(self): 
        self.window_width = self.size_event.width
        self.window_height = self.size_event.height
        self.menu_relwidth = 75/self.window_width
        
        self.menu_frame.place(relx=self.menu_relx, rely=0, anchor="nw", relheight = 1-(25/self.window_height), relwidth = self.menu_relwidth)
        
        self.page_frame.place(relx= (self.menu_relx + self.menu_relwidth + (self.padding/2)) , 
                    rely=0, 
                    anchor="nw", 
                    relheight = 1-(25/self.window_height), 
                    relwidth = 1 - (self.menu_relx + self.menu_relwidth + (self.padding/2)) - (self.padding/2)
                    )
        
        #^ that's the order of updaing any page size
        self.pages_dict[self.page_choise].update_size_BM()      # calls the update function for the displayed page
        self.pages_dict[self.page_choise].called_when_opened()  # called from here so that i don't call it after every single widget update and waste resources
            
    def white_line_spacer(self, parent):
        self.line = ctk.CTkFrame(parent, fg_color=("#b3b3b3","#4c4c4c"), width=2, height=2)
        self.line.pack(fill="x", padx=10)

    def ext_pages_importer(self, module_name):
        module_path = os.path.join(self.U_Pages_dir, f"{module_name}.py")                      # get the full path of the file
        module_spec = importlib.util.spec_from_file_location(module_name, module_path)      # create a module spec, which is used to create a module (a module spec is a file that contains the path of the module)
        module = importlib.util.module_from_spec(module_spec)                               # create a module (a module is a file that contains python code)
        module.__package__ = self.U_Pages_dir.replace("/", ".").replace("\\", ".")
        try:
            module_spec.loader.exec_module(module)                                          # execute the module
            # Now directly import the class
            class_name = module_name  # Assuming the class name is the same as the module name
            globals()[class_name] = getattr(module, class_name)                             # import the class, and save it in the globals() so it can be used later
            self.tabs.append((f"{class_name}", 1))                                          # add the class to the tabs list
        except Exception as e:
            print(f"Failed to import module {module_name}: {e}")

    def new_page_constructor(self, name, switch: bool = True):
    #### importing and executing the file
        self.ext_pages_importer(name)

    #### adding it to the pages_dict and evaluating the class
        self.pages_dict[name] = eval(name + "()")    #calls all the contents of the tabs (but not displaying them) and passing the arguments, while saving them in a dict for later use
        if self.pages_dict[name].scrollable:
            Last_widget = ctk.CTkFrame(self.pages_dict[name].Scrollable_frame, fg_color=(hvr_clr_g(LIGHT_MODE["background"], "l"), hvr_clr_g(DARK_MODE["background"], "d")), bg_color=(hvr_clr_g(LIGHT_MODE["background"], "l"), hvr_clr_g(DARK_MODE["background"], "d"))) #created to locate the y position for the edge of the frame
            Last_widget.pack(fill="x", pady=10) 
        
    #### adding its button to the menu
        self.buttons[name] = self.tab(name, self.tabs_frame)

    #### saving it to the main pages
        self.mainpages_dict[name] = self.pages_dict[name]

        if switch:
        #### Switching to the new page
            self.page_switcher(name)

    def Subpage_Construction(self, Main_page: str, Sub_page): 
        """Constructs the Subpage, so that it is ready to be opened at any moment

        Args:
            Main_page (str): used to get the name of the main page class "case sensitive"
            Sub_page (Class): used to initialize the subpage class with the necessary parameters
        """
        subpage_inited = Sub_page()
        domain = f"{Main_page}.{subpage_inited.__class__.__name__}"
        self.subpages_dict[domain] = subpage_inited
        if self.subpages_dict[domain].scrollable:
            Last_widget = ctk.CTkFrame(self.subpages_dict[domain].Scrollable_frame, fg_color=self.subpages_dict[domain].Scrollable_frame._fg_color, bg_color=self.subpages_dict[domain].Scrollable_frame._fg_color) #created to locate the y position for the edge of the frame
            Last_widget.pack(fill="x", pady=10) 

    def Subpage_init(self, Main_page_name: str, Sub_page_name: str): 
        """Opens the SubPage

        Args:
            Main_page (str): used to get the name of the main page class "case sensitive"
            Sub_page (str): used to get the name of the sub page class "case sensitive"
        """

        MN_split = Main_page_name.split(".")[0] if "." in Main_page_name else Main_page_name

        self.pages_dict[MN_split].pack_forget()
        self.pages_dict[MN_split].tools_f.place_forget()

        self.pages_dict[MN_split] = self.subpages_dict[f"{Main_page_name}.{Sub_page_name}"]
        
        self.pages_dict[MN_split].pack(expand=True, fill="both")
        self.pages_dict[MN_split].called_when_opened(k=1)

        if self.pages_dict[MN_split].pickable == 1:
            self.pages_dict[MN_split].Picking()

    def Subpage_return(self, Main_page_name: str, Sub_page_name: str): 
        """Closes the SubPage

        Args:
            Main_page (str): used to get the name of the main page class "case sensitive"
            Sub_page (str): used to get the name of the sub page class "case sensitive"
        """

        MN_split = Main_page_name.split(".")[0] if "." in Main_page_name else Main_page_name

        if self.pages_dict[MN_split].Leaving("local"):
            self.pages_dict[MN_split].pack_forget()
            self.pages_dict[MN_split].tools_f.place_forget()

            if "." in Main_page_name:
                self.pages_dict[MN_split] = self.subpages_dict[Main_page_name]
            else:
                self.pages_dict[MN_split] = self.mainpages_dict[MN_split]

            self.pages_dict[MN_split].pack(expand=True, fill="both")
            self.pages_dict[MN_split].called_when_opened(k=1)

            if self.pages_dict[MN_split].pickable == 1:
                self.pages_dict[MN_split].Picking()    

                

#### end of the class