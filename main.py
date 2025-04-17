from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.tab import MDTabs
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.image import Image as CoreImage
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.widget import Widget
from kivy.utils import platform
from kivy.utils import platform

if platform in ('android', 'ios'):
    from plyer import filechooser, share
else:
    filechooser = None
    share = None

import qrcode
from PIL import Image as PILImage
import os

Window.size = (360, 640)  # Good resolution for mobile preview


class TabScreen(MDScreen, MDTabsBase):
    pass


class QRApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"

        self.sm = MDScreenManager()
        screen = MDScreen()

        self.tabs = MDTabs()

        self.text_tab = TabScreen(title="Text")
        self.wifi_tab = TabScreen(title="WiFi")
        self.contact_tab = TabScreen(title="Contact")

        self.tabs.add_widget(self.text_tab)
        self.tabs.add_widget(self.wifi_tab)
        self.tabs.add_widget(self.contact_tab)

        self.build_text_tab()
        self.build_wifi_tab()
        self.build_contact_tab()

        screen.add_widget(self.tabs)
        return screen

    def build_text_tab(self):
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)

        self.text_input = MDTextField(
            hint_text="Enter text",
            mode="rectangle"
        )
        layout.add_widget(self.text_input)

        gen_btn = MDRaisedButton(
            text="Generate QR",
            on_release=lambda x: self.generate_qr(self.text_input.text)
        )
        layout.add_widget(gen_btn)

        self.qr_image = Image(source="", size_hint_y=0.7)
        layout.add_widget(self.qr_image)

        btn_row = MDBoxLayout(orientation='horizontal', size_hint_y=0.2, spacing=20)
        save_btn = MDIconButton(icon="content-save", on_release=lambda x: self.save_qr())
        share_btn = MDIconButton(icon="share-variant", on_release=lambda x: self.share_qr())
        btn_row.add_widget(save_btn)
        btn_row.add_widget(share_btn)
        layout.add_widget(btn_row)

        self.text_tab.add_widget(layout)

    def build_wifi_tab(self):
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)

        self.ssid_input = MDTextField(hint_text="WiFi SSID", mode="rectangle")
        self.pass_input = MDTextField(hint_text="Password", mode="rectangle", password=True)
        layout.add_widget(self.ssid_input)
        layout.add_widget(self.pass_input)

        gen_btn = MDRaisedButton(
            text="Generate WiFi QR",
            on_release=lambda x: self.generate_qr(f"WIFI:S:{self.ssid_input.text};T:WPA;P:{self.pass_input.text};;")
        )
        layout.add_widget(gen_btn)

        self.qr_image_wifi = Image(source="", size_hint_y=0.7)
        layout.add_widget(self.qr_image_wifi)

        self.wifi_tab.add_widget(layout)

    def build_contact_tab(self):
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)

        self.name_input = MDTextField(hint_text="Name", mode="rectangle")
        self.phone_input = MDTextField(hint_text="Phone", mode="rectangle")
        self.email_input = MDTextField(hint_text="Email", mode="rectangle")

        layout.add_widget(self.name_input)
        layout.add_widget(self.phone_input)
        layout.add_widget(self.email_input)

        contact_btn = MDRaisedButton(
            text="Generate Contact QR",
            on_release=lambda x: self.generate_qr(
                f"MECARD:N:{self.name_input.text};TEL:{self.phone_input.text};EMAIL:{self.email_input.text};;"
            )
        )
        layout.add_widget(contact_btn)

        self.qr_image_contact = Image(source="", size_hint_y=0.7)
        layout.add_widget(self.qr_image_contact)

        self.contact_tab.add_widget(layout)

    def generate_qr(self, data):
        qr = qrcode.make(data)
        qr.save("generated_qr.png")

        img = PILImage.open("generated_qr.png")
        img = img.resize((512, 512))
        img.save("generated_qr_resized.png")

        current_tab = self.tabs.get_tab_list()[self.tabs.get_tab_index()].title

        if current_tab == "Text":
            self.qr_image.source = "generated_qr_resized.png"
            self.qr_image.reload()
        elif current_tab == "WiFi":
            self.qr_image_wifi.source = "generated_qr_resized.png"
            self.qr_image_wifi.reload()
            if filechooser:
                path = filechooser.save_file(title="Save QR Code", filters=[("PNG", "*.png")])
            else:
                print("Filechooser is not supported on this platform.")
                return
            self.qr_image_contact.source = "generated_qr_resized.png"
            self.qr_image_contact.reload()

            if share:
                share.share(filepath="generated_qr_resized.png")
            else:
                print("Sharing is not supported on this platform.")
        try:
            path = filechooser.save_file(title="Save QR Code", filters=[("PNG", "*.png")])
            if path:
                os.rename("generated_qr_resized.png", path[0])
        except Exception as e:
            print("Error saving:", e)

    def share_qr(self):
        try:
            share.share(filepath="generated_qr_resized.png")
        except Exception as e:
            print("Error sharing:", e)


if __name__ == "__main__":
    QRApp().run()
