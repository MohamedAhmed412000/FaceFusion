from typing import Optional
import gradio

from facefusion import metadata, wording

ABOUT_BUTTON : Optional[gradio.HTML] = '<img src=https://drive.google.com/uc?export=view&id=1i6f7b3M9MnRe1lRAFZ3rysFmEZEk-Z5_>'
DONATE_BUTTON : Optional[gradio.HTML] = None


def render() -> None:
	global ABOUT_BUTTON
	global DONATE_BUTTON

	ABOUT_BUTTON = gradio.Button(
		value = metadata.get('name') + ' ' + metadata.get('version'),
		variant = 'primary',
		link = metadata.get('url')
	)
	DONATE_BUTTON = gradio.Button(
		value = wording.get('أشترك فى القناة'),
		link = 'https://www.youtube.com/@basetatube/?sub_confirmation=1',
		size = 'sm'
	)
