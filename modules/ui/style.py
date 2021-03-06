from __future__ import annotations
from .. typecheck import *

# TODO: Reclaulate css when the layout changes and replace REM_WIDTH_SCALE with the real value from rem_width_scale
# close enough for now but it means that every padding calculation will be slightly off
# better to overestimate and add less padding than more ( calculations don't overlap the side of things)

# REM_WIDTH_SCALE = 13/8 font size 13
# REM_WIDTH_SCALE = 12/7 font size 12
# REM_WIDTH_SCALE = 11/7 font size 11

REM_WIDTH_SCALE = 7.0/12.0

base_css = '''
.dark {
	--panel-color: color(var(--background));
	--segment-color: color(var(--background) blend(black 75%));

	--text-color: var(--foreground);
	--label-color: var(--text-color);

	--primary: var(--text-color);
	--secondary: var(--text-color);
}
.light {
	--panel-color: #ebedef;
	--segment-color: color(#ebedef blend(black 87%));

	--text-color: #333;
	--label-color: var(--text-color);

	--primary: var(--text-color);
	--secondary: var(--text-color);
}
a {
	text-decoration: none;
}
img {
	height: 1.6rem;
}
'''

class css:
	all = base_css
	id = 0

	def __init__(
		self,
		raw: str|None = None,
		width: float|None = None,
		height: float|None = None,
		padding_top: float|None = None,
		padding_bottom: float|None = None,
		padding_left: float|None = None,
		padding_right: float|None = None,
		radius: float|None = None,
		background_color: str|None = None,
		color: str|None = None,
	):

		self.id = css.id
		css.id += 1

		self.class_name = '_{}'.format(self.id)

		css_string = '.{} {{'.format(self.class_name)

		additional_width = 0.0
		additional_height = 0.0

		if not height is None:
			css_string += 'height:{}rem;'.format(height * REM_WIDTH_SCALE)
			additional_height += height
		if not width is None:
			css_string += 'width:{}rem;'.format(width * REM_WIDTH_SCALE)
			additional_width += width
		if not padding_top is None:
			css_string += 'padding-top:{}rem;'.format(padding_top * REM_WIDTH_SCALE)
			additional_height += padding_top
		if not padding_bottom is None:
			css_string += 'padding-bottom:{}rem;'.format(padding_bottom * REM_WIDTH_SCALE)
			additional_height += padding_bottom
		if not padding_left is None:
			css_string += 'padding-left:{}rem;'.format(padding_left * REM_WIDTH_SCALE)
			additional_width += padding_left
		if not padding_right is None:
			css_string += 'padding-right:{}rem;'.format(padding_right * REM_WIDTH_SCALE)
			additional_width += padding_right
		if not background_color is None:
			css_string += 'background-color:{};'.format(background_color)
		if not color is None:
			css_string += 'color:{};'.format(color)
		if not radius is None:
			css_string += 'border-radius:{}rem;'.format(radius * REM_WIDTH_SCALE)
		if not raw is None:
			css_string += raw

		css_string += '}'
		css.all += css_string

		self.padding_height = additional_height
		self.padding_width = additional_width


div_inline_css = css(
	padding_top=-1.0,
	padding_bottom=1.0
)

none_css = css()

icon_css = css(raw='''
	position: relative;
	top:0.5rem;
	line-height:0;
''')
