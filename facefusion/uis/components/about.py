from typing import Optional
import gradio

from facefusion import metadata, wording

ABOUT_BUTTON : Optional[gradio.HTML] = None
DONATE_BUTTON : Optional[gradio.HTML] = None


def render() -> None:
	global ABOUT_BUTTON
	global DONATE_BUTTON

	ABOUT_BUTTON = gradio.HTML(
		value='<img src="file/bLogo.png" />'
	)
	DONATE_BUTTON = gradio.Button(
		value = 'تركيب وجهك على فيديو و تبديل الوجوه في الصور بالذكاء الاصطناعي - أشترك فى القناة',
		link = 'https://www.youtube.com/@basetatube/?sub_confirmation=1',
		size = 'sm'
	)
