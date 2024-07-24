# ComfyUI-UniversalTranslator
Translate bidirectionally between any 2 languages.  Useful for "&lt;language> to Chinese" prompting in Kolors, HunyuanDiT and other chinese AI image generation models.  ComfyUI Universal Translation Node
This custom node for ComfyUI provides text translation capabilities using various free translation services.

## Features

-Translate text from any language to any other language

  Google Translate (using deep_translator)

-Optional Auto-detection of source language
-Easy-to-use dropdown menus for language selection

## Installation

Use comfy manager to install via this repo's url.

## Usage

In the ComfyUI interface, look for the "Text Translator" node in the "text" category.
Connect the node to your workflow.
Input the text you want to translate.
Select the source language (or use "auto" for auto-detection).
Choose the target language.
Pick a translation service.
Run your workflow to get the translated text.

## Notes

Some translation services (like Linguee and Pons) support a limited set of language pairs. You may encounter errors if you choose unsupported language combinations for these services.
The free tier of these translation services may have usage limits. For extensive use, you might need to implement API key handling or consider using paid services.

## License
This project is open-source and available under the MIT License.
## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.
## Acknowledgements
This node uses the following libraries:

googletrans
deep-translator

Special thanks to the ComfyUI community and the developers of the translation libraries used in this project.
