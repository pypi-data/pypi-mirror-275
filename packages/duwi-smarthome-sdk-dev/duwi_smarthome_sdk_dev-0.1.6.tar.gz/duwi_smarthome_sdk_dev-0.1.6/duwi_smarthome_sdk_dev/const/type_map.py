# device_type
type_map = {
    "SWITCH": {
        "1-002": "On",
        "1-003": "On",
        "1-005": "On",
        "1-006": "On",
        "107-001": "On",
    },
    "LIGHT": {
        "1-001": "On",
        "1-004": "On",
        "3-001": "Dim",
        "3-002": "Temp",
        "3-003": "DimTemp",
        "3-004": "RGBW",
        "3-005": "RGB",
        "3-006": "RGBCW",
    },
    "COVER": {
        "4-001": "Roll",
        "4-002": "Roll",
        "4-003": "Shutter",
        "4-004": "Shutter",
    },
}

media_type_map = {
    "8-001-001": "HuaErSiMusic",
    "8-001-002": "XiangWangMusicS7Mini3S",
    "8-001-003": "XiangWangMusicS8",
    "8-001-004": "ShengBiKeMusic",
    "8-001-005": "BoShengMusic",
    "8-001-006": "SonosMusic",
}

sensor_type_map = {
    "7-001-001": ["Temperature"],
    "7-001-002": ["Temperature"],
    "7-002-001": ["Humidity"],
    "7-003-001": ["Light"],
    "7-004-001": ["Formaldehyde"],
    "7-005-001": ["Pm25"],
    "7-006-001": ["CarbonDioxide"],
    "7-007-001": ["AirQuality"],
    "7-008-001": ["Human"],
    "7-008-002": ["Human"],
    "7-009-001": ["Trigger"],
    "7-009-002": ["Trigger"],
    "7-009-003": ["Trigger"],
    "7-009-004": ["Trigger"],
    "7-009-005": ["Trigger"],
    "7-009-006": ["Trigger"],
    "7-009-007": ["Trigger"],
    "7-009-008": ["Trigger"],
    "7-009-009": ["Trigger"],
    "7-009-010": ["Trigger"],
    "7-010-001": ["CarbonMonoxide"],
    "7-011-001": ["Tvoc"],
    "7-012-001": ["Temperature", "Humidity", "Tvoc", "Formaldehyde", "Pm25", "CarbonDioxide", "Pm10", "AirQuality"],
    "7-012-002": ["CarbonMonoxide"],
    "7-013-001": ["Light", "Human"],
}

group_type_map = {
    "SWITCH": {
        "Breaker": "On",
    },
    "LIGHT": {
        "Light": "Dim",
        "Color": "Temp",
        "LightColor": "DimTemp",
        "RGBW": "RGBW",
        "RGB": "RGB",
    },
    "COVER": {
        "Retractable": "Roll",
        "Roller": "Roll",
    },
}
