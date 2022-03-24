from aisuru_pp_py import Calculator, ScoreParams

from enum import IntFlag
class Mods(IntFlag):
    NOMOD = 0
    NOFAIL = 1 << 0
    EASY = 1 << 1
    TOUCHSCREEN = 1 << 2
    HIDDEN = 1 << 3
    HARDROCK = 1 << 4
    SUDDENDEATH = 1 << 5
    DOUBLETIME = 1 << 6
    RELAX = 1 << 7
    HALFTIME = 1 << 8
    NIGHTCORE = 1 << 9
    FLASHLIGHT = 1 << 10
    AUTOPLAY = 1 << 11
    SPUNOUT = 1 << 12
    AUTOPILOT = 1 << 13
    PERFECT = 1 << 14
    KEY4 = 1 << 15
    KEY5 = 1 << 16
    KEY6 = 1 << 17
    KEY7 = 1 << 18
    KEY8 = 1 << 19
    FADEIN = 1 << 20
    RANDOM = 1 << 21
    CINEMA = 1 << 22
    TARGET = 1 << 23
    KEY9 = 1 << 24
    KEYCOOP = 1 << 25
    KEY1 = 1 << 26
    KEY3 = 1 << 27
    KEY2 = 1 << 28
    SCOREV2 = 1 << 29
    MIRROR = 1 << 30


def vn_test():
    calculator = Calculator("./mou ii kai.osu")

    rx_params = ScoreParams(mods = int(Mods.DOUBLETIME | Mods.HIDDEN | Mods.RELAX))

    (result,) = calculator.calculate(rx_params)
    return result.pp # type: ignore

def stream_test():
    # using mahmood's honesty 3 mod +rx
    calculator = Calculator("./honesty.osu")

    params = ScoreParams(
        mods = int(Mods.DOUBLETIME | Mods.HIDDEN | Mods.HARDROCK | Mods.RELAX),
        acc = 98.55,
        combo = 2723,
    )

    (result,) = calculator.calculate(params)
    return result.pp  # type: ignore

def underweighted_stream_test():
    # using miyuki's hddtrx
    calculator = Calculator("./once upon a time.osu")

    params = ScoreParams(
        mods = int(Mods.DOUBLETIME | Mods.HIDDEN | Mods.RELAX),
        acc = 99.82,
        combo = 3226,
    )

    (result,) = calculator.calculate(params)
    return result.pp  # type: ignore

def precision_test():
    # using badeu c-type +dthrrx
    calculator = Calculator("./c type.osu")

    params = ScoreParams(
        mods = int(Mods.DOUBLETIME | Mods.HARDROCK | Mods.RELAX),
        acc = 98.4,
        combo = 167,
    )

    (result,) = calculator.calculate(params)
    return result.pp  # type: ignore

def length_check():
    # union, akatsuki zukuyo, arsonist amateur's handbook

    values = []
    for _map in ("union.osu", "akatsuki zukuyo.osu", "arsonist.osu"):
        calculator = Calculator(_map)

        params = ScoreParams(mods = int(Mods.DOUBLETIME | Mods.HIDDEN | Mods.RELAX))
        (result,) = calculator.calculate(params)
        values.append(result.pp)

    return values

def tech_check():
    # carry me away
    calculator = Calculator("carry me away.osu")

    params = ScoreParams(mods = int(Mods.DOUBLETIME | Mods.HIDDEN | Mods.RELAX))
    (result,) = calculator.calculate(params)

    return result.pp  # type: ignore

def three_mod_check():
    # placek's glorious morning, mahmood's amatsuki compilation

    glorious_calc = Calculator("./glorious morning.osu")
    glorious_params = ScoreParams(
        mods = int(Mods.DOUBLETIME | Mods.HIDDEN | Mods.HARDROCK | Mods.RELAX),
        acc = 97.18,
        combo = 603
    )

    amatsuki_calc = Calculator("./amatsuki.osu")
    amatsuki_params = ScoreParams(
        mods = int(Mods.DOUBLETIME | Mods.HIDDEN | Mods.HARDROCK | Mods.RELAX),
        acc = 98.01,
        combo = 3787,
        nMisses = 4,
    )

    (glorious_result,) = glorious_calc.calculate(glorious_params)
    (amatsuki_result,) = amatsuki_calc.calculate(amatsuki_params)

    return glorious_result.pp, amatsuki_result.pp  # type: ignore

def three_mod_stream():
    calculator = Calculator("./sickness.osu")

    params = ScoreParams(
        mods = int(Mods.DOUBLETIME | Mods.HIDDEN | Mods.HARDROCK | Mods.RELAX),
        acc = 99.00,
    )

    (result,) = calculator.calculate(params)
    return result.pp  # type: ignore

def low_ar():
    calculator = Calculator("./kimi no bouken.osu")

    params = ScoreParams(
        mods = int(Mods.EASY | Mods.DOUBLETIME | Mods.RELAX),
        acc = 99.00
    )

    (result,) = calculator.calculate(params)
    return result.pp  # type: ignore
    
def low_ar_fl():
    calculator = Calculator("./eclipse.osu")

    params = ScoreParams(
        mods = int(Mods.EASY | Mods.DOUBLETIME | Mods.FLASHLIGHT | Mods.RELAX),
        acc = 95.94,
    )

    (result,) = calculator.calculate(params)
    return result.pp  # type: ignore

def low_ar2():
    calculator = Calculator("./sudden romance.osu")

    params = ScoreParams(mods = int(Mods.EASY | Mods.RELAX))
    (result,) = calculator.calculate(params)

    return result.pp  # type: ignore

# others to do: mahmood's kimeta yo, snowy calm down juliet & some speed
def main() -> int:
    mou_rx = vn_test()
    honesty_rx = stream_test()
    once_rx = underweighted_stream_test()
    ctype_rx = precision_test()
    union_rx, zukuyo_rx, arsonist_rx = length_check()
    carry_rx = tech_check()

    glorious_rx, amatsuki_rx = three_mod_check()
    sickness_rx = three_mod_stream()
    
    bouken_rx = low_ar()
    eclipse_rx = low_ar_fl()
    sudden_rx = low_ar2()

    print(f"mou ii kai (SS +HDDTRX):\n{mou_rx:.2f}\n")
    print(f"honesty (mahmood's score +HDDTHRRX):\n{honesty_rx:.2f}\n")
    print(f"once upon a time (miyuki's score +HDDTRX):\n{once_rx:.2f}\n")
    print(f"c-type (badeu's score +DTHRRX):\n{ctype_rx:.2f}\n")

    print(f"union (SS +HDDTRX):\n{union_rx:.2f}\n")
    print(f"akatsuki zukuyo (SS +HDDTRX):\n{zukuyo_rx:.2f}\n")
    print(f"arsonist (SS +HDDTRX):\n{arsonist_rx:.2f}\n")

    print(f"carry me away (SS +HDDTRX):\n{carry_rx:.2f}\n")

    print(f"glorious morning (placek's +HDDTHRRX):\n{glorious_rx:.2f}\n")
    print(f"amatsuki compilation (mahmood's +HDDTHRRX):\n{amatsuki_rx:.2f}\n")

    print(f"the shaping sickness (99% +HDDTHRRX):\n{sickness_rx:.2f}\n")

    print(f"kimi no bouken (ezchamp's score +EZDTRX):\n{bouken_rx:.2f}\n")
    print(f"inferno eclipse (akirashine's score +EZDTFLRX):\n{eclipse_rx:.2f}\n")
    print(f"sudden romance (SS +EZRX):\n{sudden_rx:.2f}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())