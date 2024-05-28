from __future__ import annotations

from io import BytesIO
import struct
from typing import Any, List, Literal, Tuple, TypeVar, Union
from .phira_chart import PhiraAnim, PhiraBpmList, PhiraChart, PhiraChartSettings, PhiraControlObject, PhiraHold, PhiraKeyFrame, PhiraLine, PhiraNote, PhiraObject


SupportBinName = Literal["Byte", "Bool", "Int", "Float", "String", "Color",
                         "Object", "CtrlObject", "Note", "JudgeLine", "ChartSettings", "Chart"] | str
""" "KeyFrame:xxx" for KeyFrame<xxx>, "Anim:xxx" for Anim<xxx>"""


class BinaryReader:

    def __init__(self, io: BytesIO):
        self.io = io
        self._time = 0

    def reset_time(self):
        self._time = 0

    def time(self) -> float:
        self._time += self.uleb()
        return self._time / 1000

    def array(self, T: SupportBinName) -> List[Any]:
        return [BinaryData.read_binary(self, T) for _ in range(self.uleb())]

    def read(self, T: SupportBinName):
        return BinaryData.read_binary(self, T)

    def uleb(self) -> int:
        result = 0
        shift = 0
        while True:
            byte = self.read("Byte")
            result |= (byte & 0x7F) << shift
            if byte & 0x80 == 0:
                break
            shift += 7
        return result


class BinaryWriter:

    def __init__(self, io: BytesIO):
        self.io = io
        self._time = 0

    def reset_time(self):
        self._time = 0

    def time(self, value: float):
        value = round(value * 1000)
        assert value >= self._time
        self.uleb(value - self._time)
        self._time = value

    def array(self, value: List[Any], T: SupportBinName):
        self.uleb(len(value))
        for element in value:
            BinaryData.write_binary(element, self, T)

    def write(self, value: Any, T: SupportBinName):
        BinaryData.write_binary(value, self, T)

    def write_val(self, value: Any, T: SupportBinName):
        BinaryData.write_binary(value, self, T)

    def uleb(self, value: int):
        while True:
            byte = value & 0x7F
            value >>= 7
            if value != 0:
                byte |= 0x80
            self.write_val(byte, "Byte")
            if value == 0:
                break


class BinaryData:

    @staticmethod
    def read_binary(reader: BinaryReader, T: SupportBinName) -> Any:
        match T:
            case "Byte":
                return reader.io.read(1)[0]
            case "Bool":
                return reader.io.read(1)[0] == 1
            case "Int":
                return struct.unpack("<i", reader.io.read(4))[0]
            case "Float":
                return struct.unpack("<f", reader.io.read(4))[0]
            case "String":
                return bytes(reader.array("Byte")).decode()
            case "Color":
                return (reader.read("Byte"), reader.read("Byte"), reader.read("Byte"), reader.read("Byte"))
            case "Object":
                return PhiraObject(
                    alpha=reader.read("Anim:Float"),
                    scale=(reader.read("Anim:Float"),
                           reader.read("Anim:Float")),
                    rotation=reader.read("Anim:Float"),
                    translation=(reader.read("Anim:Float"),
                                 reader.read("Anim:Float")),
                )
            case "CtrlObject":
                return PhiraControlObject(
                    alpha=reader.read("Anim:Float"),
                    size=reader.read("Anim:Float"),
                    pos=reader.read("Anim:Float"),
                    y=reader.read("Anim:Float"),
                )
            case "Note":
                object = reader.read("Object")
                kind = ["tap", "hold", "flick", "drag"][reader.read("Byte")]
                if kind == "hold":
                    end_time = reader.read("Float")
                    end_height = reader.read("Float")
                time = reader.time()
                height = reader.read("Float")
                speedB = reader.read("Bool")
                speed = 1.0
                if speedB:
                    speed = reader.read("Float")
                above = reader.read("Bool")
                fake = reader.read("Bool")
                if kind == "hold":
                    return PhiraHold(
                        object=object,
                        kind=kind,
                        time=time,
                        height=height,
                        speed=speed,
                        above=above,
                        fake=fake,
                        end_time=end_time,
                        end_height=end_height,
                    )
                return PhiraNote(
                    object=object,
                    kind=kind,
                    time=time,
                    height=height,
                    speed=speed,
                    above=above,
                    fake=fake,
                )
            case "JudgeLine":
                reader.reset_time()
                object = reader.read("Object")
                kind = ["normal", "texture", "text",
                        "paint"][reader.read("Byte")]
                height = reader.read("Anim:Float")
                notes = reader.array("Note")
                color = reader.read("Color")
                parentB = reader.uleb()
                parent = None
                show_below = reader.read("Bool")
                # TODO: Support
                attach_ui = reader.read("Byte")
                ctrl_obj = reader.read("CtrlObject")
                incline = reader.read("Anim:Float")
                z_index = reader.read("Int")
                if parentB != 0:
                    parent = parentB - 1
                return PhiraLine(
                    object=object,
                    kind=kind,
                    height=height,
                    notes=notes,
                    color=color,
                    parent=parent,
                    show_below=show_below,
                    attach_ui=None,
                    ctrl_obj=ctrl_obj,
                    incline=incline,
                    z_index=z_index,
                )
            case "ChartSettings":
                return PhiraChartSettings(
                    pe_alpha_extension=reader.read("Bool"),
                    hold_partial_cover=reader.read("Bool"),
                )
            case "Chart":
                return PhiraChart(
                    offset=reader.read("Float"),
                    lines=reader.array("JudgeLine"),
                    bpm_list=PhiraBpmList([(0, 120)]),
                    settings=reader.read("ChartSettings"),
                )
        if T.startswith("KeyFrame:"):
            newT = T[len("KeyFrame:"):]
            time = reader.time()
            val = reader.read(newT)
            #! Only StaticTween is implemented
            tween = reader.read("Byte")
            return PhiraKeyFrame(time, val, tween)
        if T.startswith("Anim:"):
            newT = T[len("Anim:"):]

            def read_opt(reader: BinaryReader) -> Union[None, PhiraAnim]:
                x = reader.read("Byte")
                if x == 0:
                    return None
                if x == 1:
                    res = PhiraAnim()
                else:
                    reader.reset_time()
                    PhiraAnim(keyframes=reader.array(f"KeyFrame:{newT}"))
                if res.next:
                    res.next = read_opt(reader)
                return res
            return read_opt(reader)

        raise ValueError(f"Invalid type {T}")

    @staticmethod
    def write_binary(value: Any, writer: BinaryWriter, T: SupportBinName):
        match T:
            case "Byte":
                return writer.io.write(bytes([value]))
            case "Bool":
                return writer.io.write(bytes([1 if value else 0]))
            case "Int":
                return writer.io.write(struct.pack("<i", value))
            case "Float":
                return writer.io.write(struct.pack("<f", value))
            case "String":
                return writer.array(value.encode(), "Byte")
            case "Color":
                value_Color: Tuple[int, int, int, int] = value
                r, g, b, a = value_Color
                writer.write_val(r, "Byte")
                writer.write_val(g, "Byte")
                writer.write_val(b, "Byte")
                writer.write_val(a, "Byte")
                return
            case "Object":
                value_Object: PhiraObject = value
                writer.write(value_Object.alpha, "Anim:Float")
                writer.write(value_Object.scale[0], "Anim:Float")
                writer.write(value_Object.scale[1], "Anim:Float")
                writer.write(value_Object.rotation, "Anim:Float")
                writer.write(value_Object.translation[0], "Anim:Float")
                writer.write(value_Object.translation[1], "Anim:Float")
                return
            case "CtrlObject":
                value_CtrlObject: PhiraControlObject = value
                writer.write(value_CtrlObject.alpha, "Anim:Float")
                writer.write(value_CtrlObject.size, "Anim:Float")
                writer.write(value_CtrlObject.pos, "Anim:Float")
                writer.write(value_CtrlObject.y, "Anim:Float")
            case "Note":
                value_Note: PhiraNote = value
                writer.write(value_Note.object, "Object")
                writer.write(["tap", "hold", "flick", "drag"].index(
                    value_Note.kind), "Byte")
                if isinstance(value_Note, PhiraHold):
                    value_Hold: PhiraHold = value_Note
                    writer.write(value_Hold.end_time, "Float")
                    writer.write(value_Hold.end_height, "Float")
                writer.time(value_Note.time)
                writer.write(value_Note.height, "Float")
                writer.write(value_Note.speed != 1.0, "Bool")
                if value_Note.speed != 1.0:
                    writer.write(value_Note.speed, "Float")
                writer.write(value_Note.above, "Bool")
                writer.write(value_Note.fake, "Bool")
                return
            case "JudgeLine":
                value_JudgeLine: PhiraLine = value
                writer.write(value_JudgeLine.object, "Object")
                writer.write(["normal", "texture", "text",
                              "paint"].index(value_JudgeLine.kind), "Byte")
                writer.write(value_JudgeLine.height, "Anim:Float")
                writer.array(value_JudgeLine.notes, "Note")
                writer.write(value_JudgeLine.color, "Color")
                writer.uleb(value_JudgeLine.parent +
                            1 if value_JudgeLine.parent else 0)
                writer.write(value_JudgeLine.show_below, "Bool")
                writer.write(0, "Byte")
                writer.write(value_JudgeLine.ctrl_obj, "CtrlObject")
                writer.write(value_JudgeLine.incline, "Anim:Float")
                writer.write(value_JudgeLine.z_index, "Int")
            case "ChartSettings":
                value_ChartSettings: PhiraChartSettings = value
                writer.write(value_ChartSettings.pe_alpha_extension, "Bool")
                writer.write(value_ChartSettings.hold_partial_cover, "Bool")
                return
            case "Chart":
                value_Chart: PhiraChart = value
                writer.write(value_Chart.offset, "Float")
                writer.array(value_Chart.lines, "JudgeLine")
                writer.write(value_Chart.settings, "ChartSettings")
                return
        if T.startswith("KeyFrame:"):
            newT = T[len("KeyFrame:"):]
            time, val, tween = value.time, value.value, value.tween
            writer.time(time)
            writer.write(val, newT)
            #! Only StaticTween is implemented
            writer.write(tween, "Byte")
            return
        if T.startswith("Anim:"):
            newT = T[len("Anim:"):]
            cur: PhiraAnim = value
            while True:
                if not cur.keyframes:
                    writer.write_val(1, "Byte")
                else:
                    writer.write_val(2, "Byte")
                    writer.uleb(len(cur.keyframes))
                    writer.reset_time()
                    for kf in cur.keyframes:
                        writer.write(kf, f"KeyFrame:{newT}")
                if cur.next:
                    cur = cur.next
                else:
                    writer.write_val(0, "Byte")
                    break
            return

        raise ValueError(f"Invalid type {T}")


def test():
    test = BytesIO()
    writer = BinaryWriter(test)
    writer.write(True, "Bool")
    writer.write(19260817, "Int")
    writer.write(0.3, "Float")
    writer.write("Hello, World!", "String")
    writer.write((31, 30, 51, 255), "Color")
    print(test.getvalue())
    reader = BinaryReader(BytesIO(test.getvalue()))
    print(reader.read("Bool"))
    print(reader.read("Int"))
    print(reader.read("Float"))
    print(reader.read("String"))
    print(reader.read("Color"))
