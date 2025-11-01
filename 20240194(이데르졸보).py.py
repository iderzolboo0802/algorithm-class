class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"[{self.book_id}] {self.title} / {self.author} / {self.year}"


class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, book):
        new_node = Node(book)

        if self.head is None:
            self.head = new_node
            return True

        current = self.head
        while current.link:
            # 책 번호 중복 확인
            if current.data.book_id == book.book_id:
                return False
            current = current.link

        if current.data.book_id == book.book_id:
            return False

        current.link = new_node
        return True

    def find_by_title(self, title):
        current = self.head
        while current:
            if current.data.title == title:
                return current.data
            current = current.link
        return None

    def find_pos_by_title(self, title):
        current = self.head
        prev = None
        while current:
            if current.data.title == title:
                return prev, current
            prev = current
            current = current.link
        return None, None

    def delete_by_title(self, title):
        prev, current = self.find_pos_by_title(title)
        if current is None:
            return False

        # 첫 번째 노드 삭제
        if prev is None:
            self.head = current.link
        else:
            prev.link = current.link
        return True

    def display_all(self):
        if self.head is None:
            print("현재 등록된 도서가 없습니다.")
            return

        current = self.head
        while current:
            print(current.data)
            current = current.link


class BookManagement:
    def __init__(self):
        self.book_list = LinkedList()

    def add_book(self):
        try:
            book_id = int(input("책 번호: "))
            title = input("책 제목: ")
            author = input("저자: ")
            year = input("출판 연도: ")
            book = Book(book_id, title, author, year)
            if self.book_list.append(book):
                print("도서가 추가되었습니다.")
            else:
                print("이미 존재하는 책 번호입니다.")
        except ValueError:
            print("입력 형식이 잘못되었습니다. 숫자를 확인하세요.")

    def remove_book(self):
        title = input("삭제할 책 제목: ")
        if self.book_list.delete_by_title(title):
            print("도서가 삭제되었습니다.")
        else:
            print("해당 제목의 도서를 찾을 수 없습니다.")

    def search_book(self):
        title = input("조회할 책 제목: ")
        book = self.book_list.find_by_title(title)
        if book:
            print("조회 결과:")
            print(book)
        else:
            print("해당 제목의 도서를 찾을 수 없습니다.")

    def display_books(self):
        print("=== 전체 도서 목록 ===")
        self.book_list.display_all()

    def run(self):
        while True:
            print("\n===== 도서 관리 프로그램 =====")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로)")
            print("3. 도서 조회 (책 제목으로)")
            print("4. 전체 도서 목록 출력")
            print("5. 프로그램 종료")
            choice = input("메뉴 선택: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                self.display_books()
            elif choice == '5':
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 선택하세요.")


if __name__ == "__main__":
    manager = BookManagement()
    manager.run()
