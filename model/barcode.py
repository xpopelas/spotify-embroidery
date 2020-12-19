from typing import List


class SpotifyBarcode:
    bars: List[int]

    def __init__(self):
        self.bars = []

    def to_svg(
            self,
            output_name: str,
            height: int = 270,
            fill: str = 'FFFFFF',  # hex color
            have_logo: bool = True,
            rounded_bars: bool = True,
            background: bool = False,
    ):
        ratio = 4 if have_logo else 3
        width = height * ratio
        x_pos = 20
        bar_width = 6.71

        with open(output_name + '.svg', 'w') as fh:
            fh.write(
                f'<svg width="{width}" height="{height}" viewBox="0 0 {ratio * 100} 100" '
                f'xmlns="http://www.w3.org/2000/svg">\n')
            if background:
                fh.write(f'<rect x="0" y="0" width="{width}" height="{height}" fill="#{fill}"/>\n')
            if have_logo:
                # Logo writing
                fh.write(f'<g transform="translate(20,20)"><path fill="#{fill}" d="M30,0A30,30,0,1,1,0,30,30,30,0,0,'
                         f'1,30,0M43.73,43.2a1.85,1.85,0,0,0-.47-2.43,5,5,0,0,0-.48-.31,30.64,30.64,0,0,0-5.92-2.72,'
                         f'37.07,37.07,0,0,0-11.56-1.84c-1.33.07-2.67.12-4,.23a52.44,52.44,0,0,0-7.08,1.12,3.45,3.45,'
                         f'0,0,0-.54.16,1.83,1.83,0,0,0-1.11,2.08A1.79,1.79,0,0,0,14.37,41a4.29,4.29,0,0,0,.88-.12,'
                         f'48.93,48.93,0,0,1,8.66-1.15,35.33,35.33,0,0,1,6.75.37,28.29,28.29,0,0,1,10.25,3.61,4.77,'
                         f'4.77,0,0,0,.5.27,1.85,1.85,0,0,0,2.33-.74M47.41,35a2.34,2.34,0,0,'
                         f'0-.78-3.19l-.35-.21a35.72,35.72,0,0,0-7.38-3.3,45.39,45.39,0,0,0-15.7-2.13,41.19,41.19,0,'
                         f'0,0-7.39.92c-1,.22-2,.48-2.94.77A2.26,2.26,0,0,0,11.29,30a2.32,2.32,0,0,0,1.44,2.2,2.47,'
                         f'2.47,0,0,0,1.67,0,37,37,0,0,1,10.38-1.46,43,43,0,0,1,7.91.74,35.46,35.46,0,0,1,9.58,'
                         f'3.18c.66.34,1.3.72,1.95,1.08A2.33,2.33,0,0,0,47.41,35m.35-8.49A2.79,2.79,0,0,0,52,'
                         f'24.11c0-.2,0-.4-.08-.6a2.78,2.78,0,0,0-1.4-1.85,35.91,35.91,0,0,0-6.41-2.91,56.19,56.19,0,'
                         f'0,0-16.86-2.89,58.46,58.46,0,0,0-7,.21,48.31,48.31,0,0,0-6.52,'
                         f'1c-.87.2-1.73.42-2.58.7a2.73,2.73,0,0,0-1.85,2.68,2.79,2.79,0,0,0,2,2.61,2.9,2.9,0,0,0,'
                         f'1.6,0c.87-.23,1.75-.47,2.63-.66a45.52,45.52,0,0,1,7.26-.91,57.42,57.42,0,0,1,6.4,0,53.7,'
                         f'53.7,0,0,1,6.11.72,42.63,42.63,0,0,1,8.49,2.35,33.25,33.25,0,0,1,4,2"/></g>\n')
                x_pos += 80

            # Bar creation
            for bar in self.bars:
                s = f'<rect x="{"{:.2f}".format(x_pos)}" y="{"{:.2f}".format(44.5 - bar * 3.5)}" ' + \
                    f'width="{bar_width}" height="{"{:.2f}".format(11 + 7 * bar)}" '
                fh.write(s)

                if rounded_bars:
                    fh.write(f'rx="{"{:.2f}".format(bar_width / 2)}" ry="{"{:.2f}".format(bar_width / 2)}" ')

                fh.write(f'fill="#{fill}"/>\n')
                x_pos += bar_width * 2 - 1

            fh.write('</svg>')
