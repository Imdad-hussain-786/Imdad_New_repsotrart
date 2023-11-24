from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button


class LoveYouApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Add a background image
        background = Image(source='A.JPEG')  # Replace with the actual filename
        layout.add_widget(background)

        # Create the TextInput for entering the number
        self.number_input = TextInput(hint_text='Enter a number', input_filter='int', multiline=False, size_hint=(1, None), height=40)

        # Create a Label to display the concatenated message
        self.message_label = Label(text='', size_hint=(1, None), height=40)

        # Create a Button to generate the message
        generate_button = Button(text='Generate Message', size_hint=(1, None), height=40)
        generate_button.bind(on_press=self.generate_message)

        # Add the widgets to the layout
        layout.add_widget(self.number_input)
        layout.add_widget(generate_button)
        layout.add_widget(self.message_label)

        return layout

    def generate_message(self, instance):
        # Get the number from the TextInput
        try:
            number = int(self.number_input.text)
            if number <= 0:
                self.message_label.text = "Please enter a number greater than zero."
            else:
                # Concatenate the message
                message = f"Dear Adilla, I love you {number} times"
                self.message_label.text = message
        except ValueError:
            self.message_label.text = "Please enter a valid number."


if __name__ == '__main__':
    # Set the dimensions and orientation for Android
    from kivy.config import Config
    Config.set('graphics', 'width', '720')  # Set the width to 720 pixels
    Config.set('graphics', 'height', '1280')  # Set the height to 1280 pixels
    Config.set('graphics', 'orientation', 'portrait')  # Set the orientation to 'portrait'

    LoveYouApp().run()
