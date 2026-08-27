# reference: https://github.com/wmikuriy/recipe/blob/main/docs/np3-format-specification.md


from dataclasses import dataclass
from pprint import pprint


@dataclass
class BasicAdjustments:
    sharpening: float
    clarity: float


@dataclass
class AdvancedAdjustments:
    mid_range_sharpening: float
    contrast: int
    highlights: int
    shadows: int
    white_level: int
    black_level: int
    saturation: int


@dataclass
class ColorBlenderChannel:
    hue: int
    chroma: int
    brightness: int


@dataclass
class ColorBlender:
    red: ColorBlenderChannel
    orange: ColorBlenderChannel
    yellow: ColorBlenderChannel
    green: ColorBlenderChannel
    cyan: ColorBlenderChannel
    blue: ColorBlenderChannel
    purple: ColorBlenderChannel
    magenta: ColorBlenderChannel


@dataclass
class ColorGrade:
    hue: float
    chroma: int
    brightness: int


@dataclass
class ColorGrading:
    highlights: ColorGrade
    midtone: ColorGrade
    shadows: ColorGrade
    blending: int
    balance: int


@dataclass
class ToneCurve:
    point_count: int
    control_points: list[tuple[float, float]]
    raw_curve: list[int]


@dataclass
class Np3Data:
    name: str
    basic_adjustments: BasicAdjustments
    advanced_adjustments: AdvancedAdjustments
    color_blender: ColorBlender
    color_grading: ColorGrading
    tone_curve: ToneCurve | None = None


def main():
    # TODO: figure out np3 without tone curve
    # path = "PDX_PORTRA_V2.NP3"
    path = "CallItLove_Faloo Mi.NP3"
    data = parse_np3(path)
    pprint(data)


def _read_signed8(data: bytes, offset: int) -> int:
    val = data[offset] - 0x80
    if val == -127:
        return 0
    return val


def _read_scaled4(data: bytes, offset: int) -> float:
    return (data[offset] - 0x80) / 4.0


def _read_hue(data: bytes, offset: int) -> float:
    # ((byte[0] & 0x0F) << 8) | byte[1]
    return ((data[offset] & 0x0F) << 8) | data[offset + 1]


def _get_control_points(data: bytes, point_count: int) -> list[tuple[float, float]]:
    control_points: list[tuple[float, float]] = []
    for i in range(point_count):
        x = data[405 + i * 2]
        y = data[405 + i * 2 + 1]
        control_points.append((x, y))
    return control_points


def _get_raw_curve(data: bytes) -> list[int]:
    raw_curve: list[int] = []
    offset = 460
    for i in range(257):
        value = (data[offset + i * 2] << 8) | data[offset + i * 2 + 1]
        raw_curve.append(value)
    return raw_curve


def _read_name(data: bytes) -> str:
    name_bytes = data[24:64]
    just_name_bytes = name_bytes.split(b"\x00", 1)[0]
    name = just_name_bytes.decode("ascii")
    return name


def parse_np3(file_path: str) -> Np3Data:
    with open(file_path, "rb") as f:
        bytes = f.read()

        tone_curve = None
        if len(bytes) > 404:
            point_count = bytes[404]
            tone_curve = ToneCurve(
                point_count=point_count,
                control_points=_get_control_points(bytes, point_count),
                raw_curve=_get_raw_curve(bytes),
            )

        return Np3Data(
            name=_read_name(bytes),
            basic_adjustments=BasicAdjustments(
                sharpening=_read_scaled4(bytes, 82),
                clarity=_read_scaled4(bytes, 92),
            ),
            advanced_adjustments=AdvancedAdjustments(
                mid_range_sharpening=_read_scaled4(bytes, 242),
                contrast=_read_signed8(bytes, 272),
                highlights=_read_signed8(bytes, 282),
                shadows=_read_signed8(bytes, 292),
                white_level=_read_signed8(bytes, 302),
                black_level=_read_signed8(bytes, 312),
                saturation=_read_signed8(bytes, 322),
            ),
            color_blender=ColorBlender(
                red=ColorBlenderChannel(
                    hue=_read_signed8(bytes, 332),
                    chroma=_read_signed8(bytes, 333),
                    brightness=_read_signed8(bytes, 334),
                ),
                orange=ColorBlenderChannel(
                    hue=_read_signed8(bytes, 335),
                    chroma=_read_signed8(bytes, 336),
                    brightness=_read_signed8(bytes, 337),
                ),
                yellow=ColorBlenderChannel(
                    hue=_read_signed8(bytes, 338),
                    chroma=_read_signed8(bytes, 339),
                    brightness=_read_signed8(bytes, 340),
                ),
                green=ColorBlenderChannel(
                    hue=_read_signed8(bytes, 341),
                    chroma=_read_signed8(bytes, 342),
                    brightness=_read_signed8(bytes, 343),
                ),
                cyan=ColorBlenderChannel(
                    hue=_read_signed8(bytes, 344),
                    chroma=_read_signed8(bytes, 345),
                    brightness=_read_signed8(bytes, 346),
                ),
                blue=ColorBlenderChannel(
                    hue=_read_signed8(bytes, 347),
                    chroma=_read_signed8(bytes, 348),
                    brightness=_read_signed8(bytes, 349),
                ),
                purple=ColorBlenderChannel(
                    hue=_read_signed8(bytes, 350),
                    chroma=_read_signed8(bytes, 351),
                    brightness=_read_signed8(bytes, 352),
                ),
                magenta=ColorBlenderChannel(
                    hue=_read_signed8(bytes, 353),
                    chroma=_read_signed8(bytes, 354),
                    brightness=_read_signed8(bytes, 355),
                ),
            ),
            color_grading=ColorGrading(
                highlights=ColorGrade(
                    hue=_read_hue(bytes, 368),
                    chroma=_read_signed8(bytes, 370),
                    brightness=_read_signed8(bytes, 371),
                ),
                midtone=ColorGrade(
                    hue=_read_hue(bytes, 372),
                    chroma=_read_signed8(bytes, 374),
                    brightness=_read_signed8(bytes, 375),
                ),
                shadows=ColorGrade(
                    hue=_read_hue(bytes, 376),
                    chroma=_read_signed8(bytes, 378),
                    brightness=_read_signed8(bytes, 379),
                ),
                blending=bytes[384],
                balance=_read_signed8(bytes, 386),
            ),
            tone_curve=tone_curve,
        )


if __name__ == "__main__":
    main()
