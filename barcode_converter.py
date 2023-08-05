def barcode_converter(line: str) -> str:
    def modulo10(num: str) -> int:
        sum = 0
        weight = 2
        for char in reversed(num):
            partial = int(char) * weight
            if partial > 9:
                s = str(partial)
                partial = int(s[0]) + int(s[1])
            sum += partial
            if weight == 2:
                weight = 1
            else:
                weight = 2

        rest10 = sum % 10
        if rest10 == 0:
            modulo10 = 0
        else:
            modulo10 = 10 - rest10
        return modulo10

    def mount_section(field: str) -> str:
        field_dv = "%s%s" % (field, modulo10(field))
        return "%s.%s" % (field_dv[0:5], field_dv[5:])

    return " ".join(
        [
            mount_section(line[0:4] + line[19:24]),
            mount_section(line[24:34]),
            mount_section(line[34:44]),
            line[4],
            line[5:19],
        ]
    )
