import json
import uuid
from pprint import pprint

from np3_convert.parser import Np3Data, parse_np3


def main():
    # path = "CallItLove_Faloo Mi.NP3"
    # path = "PDX_PORTRA_V2.NP3"
    path = "AirGreen_Gunji.NP3"
    np3_data: Np3Data = parse_np3(path)
    convert_to_rrpreset(np3_data)


def convert_to_rrpreset(np3_data: Np3Data):
    rrpreset = {
        "creator": "Anonymous",
        "presets": [
            {
                "preset": {
                    "id": str(uuid.uuid4()),
                    "name": np3_data.name,
                    "adjustments": {
                        "blacks": np3_data.advanced_adjustments.black_level,
                        "brightness": 0,  # why is there no brightness? maybe can find in np3
                        "centré": 0,
                        "chromaticAberrationBlueYellow": 0,
                        "chromaticAberrationRedCyan": 0,
                        "clarity": np3_data.basic_adjustments.clarity,
                        "colorCalibration": {
                            "blueHue": 0,
                            "blueSaturation": 0,
                            "greenHue": 0,
                            "greenSaturation": 0,
                            "redHue": 0,
                            "redSaturation": 0,
                            "shadowsTint": 0,
                        },
                        "colorGrading": {
                            "balance": 0,
                            "blending": 50,
                            "global": {"hue": 0, "luminance": 0, "saturation": 0},
                            "highlights": {
                                "hue": np3_data.color_grading.highlights.hue,
                                "luminance": np3_data.color_grading.highlights.brightness,
                                "saturation": np3_data.color_grading.highlights.chroma,
                            },
                            "midtones": {
                                "hue": np3_data.color_grading.midtone.hue,
                                "luminance": np3_data.color_grading.midtone.brightness,
                                "saturation": np3_data.color_grading.midtone.chroma,
                            },
                            "shadows": {
                                "hue": np3_data.color_grading.shadows.hue,
                                "luminance": np3_data.color_grading.shadows.brightness,
                                "saturation": np3_data.color_grading.shadows.chroma,
                            },
                        },
                        "colorNoiseReduction": 0,
                        "contrast": np3_data.advanced_adjustments.contrast + 50,
                        "curveMode": "point",
                        "curves": {
                            "blue": [{"x": 0, "y": 0}, {"x": 255, "y": 255}],
                            "green": [{"x": 0, "y": 0}, {"x": 255, "y": 255}],
                            "luma": [{"x": 0, "y": 0}, {"x": 255, "y": 255}],
                            "red": [{"x": 0, "y": 0}, {"x": 255, "y": 255}],
                        },
                        "dehaze": 0,
                        "exposure": 1.0,
                        "flareAmount": 0,
                        "glowAmount": 0,
                        "grainAmount": 0,
                        "grainRoughness": 50,
                        "grainSize": 25,
                        "halationAmount": 0,
                        "highlights": np3_data.advanced_adjustments.highlights,
                        "hsl": {
                            "aquas": {
                                "hue": np3_data.color_blender.cyan.hue,
                                "luminance": np3_data.color_blender.cyan.brightness,
                                "saturation": np3_data.color_blender.cyan.chroma + 10,
                            },
                            "blues": {
                                "hue": np3_data.color_blender.blue.hue,
                                "luminance": np3_data.color_blender.blue.brightness,
                                "saturation": np3_data.color_blender.blue.chroma + 10,
                            },
                            "greens": {
                                "hue": np3_data.color_blender.green.hue + 10,
                                "luminance": np3_data.color_blender.green.brightness,
                                "saturation": np3_data.color_blender.green.chroma + 10,
                            },
                            "magentas": {
                                "hue": np3_data.color_blender.magenta.hue,
                                "luminance": np3_data.color_blender.magenta.brightness,
                                "saturation": np3_data.color_blender.magenta.chroma
                                + 10,
                            },
                            "oranges": {
                                "hue": np3_data.color_blender.orange.hue,
                                "luminance": np3_data.color_blender.orange.brightness,
                                "saturation": np3_data.color_blender.orange.chroma + 10,
                            },
                            "purples": {
                                "hue": np3_data.color_blender.purple.hue,
                                "luminance": np3_data.color_blender.purple.brightness,
                                "saturation": np3_data.color_blender.purple.chroma + 10,
                            },
                            "reds": {
                                "hue": np3_data.color_blender.red.hue,
                                "luminance": np3_data.color_blender.red.brightness,
                                "saturation": np3_data.color_blender.red.chroma + 10,
                            },
                            "yellows": {
                                "hue": np3_data.color_blender.yellow.hue,
                                "luminance": np3_data.color_blender.yellow.brightness,
                                "saturation": np3_data.color_blender.yellow.chroma + 10,
                            },
                        },
                        "hue": 0,
                        "lumaNoiseReduction": 0,
                        "lutData": None,
                        "lutIntensity": 100,
                        "lutIsSceneReferred": False,
                        "lutName": None,
                        "lutPath": None,
                        "lutSize": 0,
                        "parametricCurve": {
                            "blue": {
                                "blackLevel": 0,
                                "darks": 0,
                                "highlights": 0,
                                "lights": 0,
                                "shadows": 0,
                                "split1": 25,
                                "split2": 50,
                                "split3": 75,
                                "whiteLevel": 0,
                            },
                            "green": {
                                "blackLevel": 0,
                                "darks": 0,
                                "highlights": 0,
                                "lights": 0,
                                "shadows": 0,
                                "split1": 25,
                                "split2": 50,
                                "split3": 75,
                                "whiteLevel": 0,
                            },
                            "luma": {
                                "blackLevel": 0,
                                "darks": 0,
                                "highlights": 0,
                                "lights": 0,
                                "shadows": 0,
                                "split1": 25,
                                "split2": 50,
                                "split3": 75,
                                "whiteLevel": 0,
                            },
                            "red": {
                                "blackLevel": 0,
                                "darks": 0,
                                "highlights": 0,
                                "lights": 0,
                                "shadows": 0,
                                "split1": 25,
                                "split2": 50,
                                "split3": 75,
                                "whiteLevel": 0,
                            },
                        },
                        "pointCurves": {
                            "blue": [{"x": 0, "y": 0}, {"x": 255, "y": 255}],
                            "green": [{"x": 0, "y": 0}, {"x": 255, "y": 255}],
                            "luma": [{"x": 0, "y": 0}, {"x": 255, "y": 255}],
                            "red": [{"x": 0, "y": 0}, {"x": 255, "y": 255}],
                        },
                        "saturation": np3_data.advanced_adjustments.saturation + 20,
                        "shadows": np3_data.advanced_adjustments.shadows,
                        "sharpness": np3_data.basic_adjustments.sharpening,
                        "sharpnessThreshold": 15,
                        "structure": np3_data.advanced_adjustments.mid_range_sharpening,
                        "temperature": 0,
                        "tint": 0,
                        "toneMapper": "basic",
                        "vibrance": 0,
                        "vignetteAmount": 0,
                        "vignetteFeather": 50,
                        "vignetteMidpoint": 50,
                        "vignetteRoundness": 0,
                        "whites": np3_data.advanced_adjustments.white_level,
                    },
                    "includeMasks": False,
                    "includeCropTransform": False,
                    "presetType": "style",
                }
            }
        ],
    }

    if np3_data.tone_curve:
        rrpreset["presets"][0]["preset"]["adjustments"]["curves"]["luma"] = [
            {"x": point[0], "y": point[1]}
            for point in np3_data.tone_curve.control_points
        ]

    with open(f"{np3_data.name}.rrpreset", "w") as f:
        _ = f.write(json.dumps(rrpreset, indent=4))
