"""
Examples from Chapter: Introduction to Python
- Statements, expressions, keywords, identifiers
- print(), interpreter behavior
- Naming conventions
- Operators and literals
- Hello World

All examples are annotated for educational clarity.
"""

def header(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main() -> None:
    # ------------------------------------------------------------------
    header("1) 인터프리터 예제: 한 줄 계산 실행")

    # Python 인터프리터에서는 한 줄의 표현식을 입력하면
    # 즉시 결과를 확인할 수 있다.
    print(1 + 2)  # Expected: 3

    # ------------------------------------------------------------------
    header("2) 표현식(Expression) 예제")

    # 아래 코드는 모두 '값을 만들어내는 표현식'이다.
    print(1 + 2)     # 산술 표현식
    print("Hello")   # 문자열 리터럴
    print(3 * 4)     # 곱셈 표현식

    # ------------------------------------------------------------------
    header("3) 키워드(keyword) 목록 확인")

    # Python에서 예약어(키워드) 목록을 확인하는 방법
    import keyword
    print(keyword.kwlist)

    # ------------------------------------------------------------------
    header("4) 식별자와 네이밍 규칙: snake_case vs CamelCase")

    # snake_case: 변수/함수 이름에 주로 사용
    item_list = []
    login_status = True

    print(item_list, login_status)

    # CamelCase: 클래스 이름에 주로 사용
    ItemList = []
    LoginStatus = True

    print(ItemList, LoginStatus)

    # ------------------------------------------------------------------
    header("5) 주석(Comment) 예제")

    # 이 줄은 주석이며 실행되지 않는다.
    print("Hello, Python!")  # 문자열 출력

    # ------------------------------------------------------------------
    header("6) 연산자(operator)와 리터럴(literal)")

    # 리터럴: 값 그 자체 (1, 10 등)
    # 연산자: 값 사이의 연산을 정의 (+, - 등)
    a = 1 + 1
    b = 10 - 10
    c = a + b

    print(a, b, c, sep="/")  # sep 인자를 사용한 출력

    # ------------------------------------------------------------------
    header("7) Hello World 프로그램")

    # 가장 기본적인 Python 프로그램
    print("Hello, World!")

    # ------------------------------------------------------------------
    header("8) 들여쓰기(Indentation)는 문법이다")

    # Python에서는 들여쓰기가 코드 블록을 결정한다.
    # 아래 코드는 조건문 블록 예시를 주석으로만 보여준다.

    example_code = """
if True:
    print("This is inside the block")
print("This is outside the block")
"""
    print(example_code.strip())


if __name__ == "__main__":
    main()