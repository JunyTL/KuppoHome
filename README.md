쿳뽀 홈페이지
==========

소개쿳뽀
-------

안녕쿳뽀! 이 프로젝트는 쿳뽀 부대 홈페이지 프로젝트야쿳뽀

쿳뽀 부대의 코딩 쿳뽀들이 열심히 만들어 주고있어쿳뽀

요구사항쿳뽀
---------

쿳뽀 홈페이지 프로젝트는 아래와 같은 요구사항이 필요해쿳뽀

- Python 3.6 +


설치쿳뽀
-------

쿳뽀 홈페이지를 같이 만들고 싶어쿳뽀? 아래 설치 방법을 따라해줘쿳뽀!

1. [git]을 설치해줘쿳뽀!

2. [pip]도 설치해줘쿳뽀!

3. [virtualenv] 랑 [virtualenvwrapper] 을 설치해줘쿳뽀!

    virtualenvwrapper 는 필수는 아니지만 가상환경 관리&진입을 쉽게 할 수 있도록 해줘쿳뽀

4. git 저장소를 클론해줘쿳뽀!

5. 가상환경을 세팅해줘쿳뽀!

    virtualenvwrapper를 사용하는 쿳뽀라면 다음과 같이 해주면 되쿳뽀

        # 현재 프로젝트 디렉토리 최상단에 있다고 가정해쿳뽀
        $ mkvirtualenv -a `pwd` -p $(which python3) kuppo

6. 프로젝트에 필요한 모든 의존성을 설치해쿳뽀!

    $ pip install -r requirements.txt


서버띄우기쿳뽀
-----------

1. 가상환경을 활성화시켜줘 쿳뽀!

    virtualenvwrapper를 사용하는 쿳뽀는 이렇게 하면 되쿳뽀

        $ workon kuppo

2. 서버를 켜줘 쿳뽀!

    그냥 켜도 상관없지만 디버그 모드로 켜고싶다면 `-d` 옵션을 추가하면 되쿳뽀

        $ python run.py

[Python]: http://www.python.org/
[git]: http://www.git-scm.com/
[pip]: http://pip.readthedocs.org/
[virtualenv]: http://pypi.python.org/pypi/virtualenv
[virtualenvwrapper]: http://virtualenvwrapper.readthedocs.org