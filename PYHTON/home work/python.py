def grade(score):
    if score >= 80:
        return "A"
    elif score >= 65:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "fill"

print(grade(85))   # ត្រូវបាន A
print(grade(55))   # ត្រូវបាន C
print(grade(30))   # ត្រូវបាន ធ្លាក់