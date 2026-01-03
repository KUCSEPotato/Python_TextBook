"""
All examples extracted from the LaTeX draft (Data Type / String sections).
Each block is annotated with comments for readability.

Note:
- Some original examples intentionally produce errors (SyntaxError, IndexError).
  Those are handled safely so this file can run end-to-end.
"""

def header(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def main() -> None:
    # ---------------------------------------------------------------------
    header("1) type() 함수 예제: 변수에 저장된 값의 자료형 확인")

    var1 = "Hello!"
    var2 = 20041015

    print(type(var1))  # Expected: <class 'str'>
    print(type(var2))  # Expected: <class 'int'>

    # ---------------------------------------------------------------------
    header("2) print() 함수 원형(시그니처) 예제")

    # print()는 파이썬 내장 함수이며 아래는 문서에서 설명용으로 제시한 시그니처다.
    # 실제로는 시그니처 자체를 실행하는 것이 아니라, 참고용이다.
    # print(*objects, sep=' ', end='\n')

    print("print(*objects, sep=' ', end='\\n')  # (signature shown as text)")

    # ---------------------------------------------------------------------
    header("3) 문자열 만들기: 큰따옴표(\"\")")

    str1 = "Hello."
    print(str1)

    # ---------------------------------------------------------------------
    header("4) 문자열 만들기: 작은따옴표('')")

    str1 = 'Hello.'
    print(str1)

    # ---------------------------------------------------------------------
    header("5) 문자열 내부에 같은 따옴표를 그대로 쓰면 SyntaxError")

    # 원문 예제는 아래처럼 작성되어 SyntaxError가 발생한다.
    # 이 파일이 멈추지 않도록 문자열로 '그대로' 보여준다.
    bad_code = 'str1 = ""Hello" was spoken"'
    print("This code would raise SyntaxError if executed:")
    print(bad_code)

    # ---------------------------------------------------------------------
    header("6) 다른 종류 따옴표로 해결하기")

    str1 = '"Hello" was spoken'
    str2 = "'Hello' was thought"

    print(str1)
    print(str2)

    # ---------------------------------------------------------------------
    header("7) 이스케이프 문자(\\)로 따옴표를 문자열에 포함시키기")

    str1 = "\"Hello\" was spoken."
    print(str1)

    # ---------------------------------------------------------------------
    header("8) 여러 줄 문자열(삼중 따옴표) 예제: 두 개의 multi-line 문자열 출력")

    str1 = """Until the waters of the East Sea dry up
and Mount Baekdu wears away,
may God watch over and protect our nation."""
    str2 = """Three thousand li of splendid rivers and mountains,
great Korean people,
may our nation endure forever."""

    print(str1)
    print(str2)

    # ---------------------------------------------------------------------
    header("9) 여러 줄 문자열: 코드 가독성 때문에 앞/뒤에 줄바꿈이 포함되는 경우")

    str1 = """
Until the waters of the East Sea dry up
and Mount Baekdu wears away,
may God watch over and protect our nation.
"""
    # 주의: 출력 시 맨 위/맨 아래에 빈 줄이 포함될 수 있음
    print(str1)

    # ---------------------------------------------------------------------
    header("10) 백슬래시(\\)로 의도치 않은 앞/뒤 줄바꿈 제거하기")

    str2 = """\
Three thousand li of splendid rivers and mountains,
great Korean people,
may our nation endure forever.\
"""
    print(str2)

    # ---------------------------------------------------------------------
    header("11) 문자열 연결 연산자 (+)")

    str1 = "Hello"
    str2 = "Everyone"
    print(str1 + str2)  # Expected: HelloEveryone

    # ---------------------------------------------------------------------
    header("12) 문자열 + 숫자 연결 시 TypeError 예제 (안전하게 try/except 처리)")

    str1 = "Hello"
    str2 = "Everyone"
    try:
        print(str1 + str2 + 1)  # TypeError expected
    except TypeError as e:
        print("Caught error:", type(e).__name__, "-", e)

    # ---------------------------------------------------------------------
    header("13) 숫자를 문자열 리터럴로 바꿔서 연결하기")

    str1 = "Hello"
    str2 = "Everyone"
    print(str1 + str2 + "1")  # Expected: HelloEveryone1

    # ---------------------------------------------------------------------
    header("14) (연습문제 원문) str()로 고치기 전 코드 (원래는 TypeError)")

    # 원문 그대로라면 아래는 TypeError가 발생한다.
    # 연습문제 취지를 보존하기 위해 실행은 try/except로 감싼다.
    str1 = "Hello"
    str2 = "Everyone"
    try:
        print(str1 + str2 + 1)
    except TypeError as e:
        print("Caught error:", type(e).__name__, "-", e)

    # ---------------------------------------------------------------------
    header("15) 문자열 반복 연산자 (*)")

    str1 = "Hello"
    print(str1 * 3)   # Expected: HelloHelloHello
    print(4 * str1)   # Expected: HelloHelloHelloHello

    # ---------------------------------------------------------------------
    header("16) 문자 선택 연산자(인덱싱): 양의 정수 인덱스")

    text = "Hello"
    print(text[0])  # H
    print(text[1])  # e
    print(text[4])  # o

    # ---------------------------------------------------------------------
    header("17) 음수 인덱싱: 뒤에서부터 문자 선택")

    text = "Hello"
    print(text[-1])  # o
    print(text[-4])  # e
    print(text[-5])  # H

    # ---------------------------------------------------------------------
    header("18) 슬라이싱 예제 1: [1:4]")

    text = "HelloWorld"
    print(text[1:4])  # ell

    # ---------------------------------------------------------------------
    header("19) 슬라이싱 예제 2: [0:5], [5:10]")

    text = "HelloWorld"
    print(text[0:5])   # Hello
    print(text[5:10])  # World

    # ---------------------------------------------------------------------
    header("20) 슬라이싱: 시작 인덱스 > 종료 인덱스이면 빈 문자열")

    text = "HelloWorld"
    print(text[5:3])  # Expected: "" (empty string)

    # ---------------------------------------------------------------------
    header("21) 슬라이싱: 시작/종료 인덱스 생략하기")

    text = "HelloWorld"
    print(text[5:])   # World
    print(text[:5])   # Hello
    print(text[:])    # HelloWorld
    print(text[:-1])  # HelloWorl

    # ---------------------------------------------------------------------
    header("22) 연습문제 (1) text[0]")

    text = "Python"
    print(text[0])  # P

    # ---------------------------------------------------------------------
    header("23) 연습문제 (2) text[-1]")

    text = "Python"
    print(text[-1])  # n

    # ---------------------------------------------------------------------
    header("24) 연습문제 (3) text[1:4]")

    text = "Python"
    print(text[1:4])  # yth

    # ---------------------------------------------------------------------
    header("25) 연습문제 (4) text[:3], text[3:]")

    text = "Python"
    print(text[:3])  # Pyt
    print(text[3:])  # hon

    # ---------------------------------------------------------------------
    header("26) 연습문제 (5) text[:-1]")

    text = "Python"
    print(text[:-1])  # Pytho

    # ---------------------------------------------------------------------
    header("27) 연습문제 (6) text[2:2] (빈 슬라이싱)")

    text = "Python"
    print(text[2:2])  # "" (empty string)

    # ---------------------------------------------------------------------
    header("28) 연습문제 (7) text[len(text)-1] (마지막 문자)")

    text = "Python"
    print(text[len(text) - 1])  # n

    # ---------------------------------------------------------------------
    header("29) 연습문제 (8) text[len(text)] (IndexError)")

    text = "Python"
    try:
        print(text[len(text)])  # IndexError expected
    except IndexError as e:
        print("Caught error:", type(e).__name__, "-", e)


if __name__ == "__main__":
    main()