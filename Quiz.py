def 주민등록번호_유효성_검사(rrn):
    if len(rrn) != 14 or rrn[6] != '-':
        return False

    숫자들 = [int(숫자) for 숫자 in rrn.replace('-', '')]

    곱셈값들 = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    총합 = 0
    for i in range(12):
        총합 += 숫자들[i] * 곱셈값들[i]

    나머지 = 총합 % 11


    검증숫자 = 11 - 나머지


    검증숫자 = 검증숫자 % 10


    return 검증숫자 == 숫자들[-1]

주민등록번호 = input("주민등록번호를 입력하세요 : ")


if 주민등록번호_유효성_검사(주민등록번호):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")